import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import quote
from config.settings import (
    JIRA_URL, JIRA_USER, JIRA_TOKEN, JIRA_PROJECT_KEY, JIRA_USERS, DATA_HOJE
)
from utils.log import log

class JiraManager:
    def __init__(self):
        self.base_url = JIRA_URL
        self.auth = HTTPBasicAuth(JIRA_USER, JIRA_TOKEN)
        self.headers = {"Accept": "application/json", "Content-Type": "application/json"}

    def _search_issues(self, jql: str, max_results: int = 50):
        url = f"{self.base_url}/search?jql={quote(jql)}&maxResults={max_results}"
        r = requests.get(url, headers=self.headers, auth=self.auth)
        r.raise_for_status()
        return r.json().get("issues", [])

    def issue_exists_with_exact_summary(self, summary: str) -> bool:
        jql = f'project = "{JIRA_PROJECT_KEY}" AND summary ~ "\\"{summary}\\""'
        issues = self._search_issues(jql)
        for issue in issues:
            if issue.get("fields", {}).get("summary", "") == summary:
                return True
        return False

    def criar_task(self, titulo: str, assignee_username: str | None = None):
        """Cria task apenas se não existir com o MESMO summary."""
        if self.issue_exists_with_exact_summary(titulo):
            log(f"[WARN] Task já existe no Jira com o mesmo título. Pulando criação: {titulo}")
            return None

        assignee_id = JIRA_USERS.get(assignee_username or "", None)


        if assignee_username and not assignee_id:
            log(f"[WARN] Usuário desconhecido: {assignee_username}. Task não será criada.")
            return None

        payload = {
            "fields": {
                "project": {"key": JIRA_PROJECT_KEY},
                "summary": titulo,
                "issuetype": {"name": "Task"},
                "labels": ["BACKUP"],
                "duedate": DATA_HOJE,
                "customfield_10020": 114,            
                "customfield_10037": DATA_HOJE 
            }
        }
        if assignee_id:
            payload["fields"]["assignee"] = {"id": assignee_id}

        r = requests.post(
            f"{self.base_url}/issue",
            json=payload,
            headers=self.headers,
            auth=self.auth
        )
        if r.status_code == 201:
            key = r.json().get("key")
            log(f"[OK] Task criada no Jira: {key}")
            return key
        log(f"[ERROR] Erro ao criar task no Jira: {r.status_code} - {r.text}")
        return None
    
    
    def descricao_task(self, summary: str) -> str | None:
        """Busca a descrição da issue no Jira a partir do summary."""
        jql = f'project = "{JIRA_PROJECT_KEY}" AND summary ~ "\\"{summary}\\""'
        issues = self._search_issues(jql)
        for issue in issues:
            if issue.get("fields", {}).get("summary", "") == summary:
                return issue.get("fields", {}).get("description", None)
        return None
