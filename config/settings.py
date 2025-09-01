import os, json
from datetime import datetime, date
from dotenv import load_dotenv

load_dotenv()

# ————— CAMINHOS ————— #
CAMINHO_PERFIL = r"C:\chrome-debug"
CAMINHO_CHROME = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
PASTA_DOWNLOADS = r"C:\Users\adm.joao.mendes\Downloads"
PASTA_REPOSITORIO = r"C:\Users\adm.joao.mendes\Documents\BACKUP RELATORIOS BI"

# ————— GITHUB ————— #
REPOSITORIO = os.getenv("REPOSITORIO")
MENSAGEM_COMMIT = f"Backup dos relatorios DATA: {datetime.today().strftime('%d-%m-%Y')}"

# ————— JIRA ————— #
JIRA_URL = os.getenv("JIRA_URL")
JIRA_USER = os.getenv("JIRA_USER")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")
JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")
DATA_HOJE = date.today().strftime("%Y-%m-%d")
JIRA_USERS={
        "joao.mendes":"712020:142fa7a7-5676-4a87-8dc8-18e31a0164c0", 
        "allyf.silva":"712020:ced71a53-5125-4244-b88b-0a484a9c998f", 
        "luiz.vinicius":"712020:ab1f2aff-ad2a-4ff3-9488-1e85d70c0202", 
        "gabriel.freitas":"5d828ef68db4330c3b12851c", 
        "yury.souza":"712020:8f406a09-8c1a-4b89-b104-a2e9dc74fcec", 
        "lucas.silva":"712020:34700eb1-c1ab-49eb-8a51-b9713df07c9a"}


# ————— CATEGORIAS/PASTAS ————— #
RELATORIOS = {
    "adm_auditoria": {
        "link": "http://sqlbi:sql%40bi%21parvi@bi.intranetparvi.com.br/PBIReports/browse/Adm%20Fin%20Cont/Auditoria",
        "pasta": rf"{PASTA_REPOSITORIO}\Adm Fin Cont\Auditoria"
    },
    "adm_cobrancas": {
        "link": "http://bi.intranetparvi.com.br/PBIReports/browse/Adm%20Fin%20Cont/Cobran%C3%A7a",
        "pasta": rf"{PASTA_REPOSITORIO}\Adm Fin Cont\Cobranças"
    },
    "comercial": {
        "link": "http://bi.intranetparvi.com.br/PBIReports/browse/Comercial",
        "pasta": rf"{PASTA_REPOSITORIO}\Comercial"
    },
    "doc": {
        "link": "http://bi.intranetparvi.com.br/PBIReports/browse/DOC",
        "pasta": rf"{PASTA_REPOSITORIO}\DOC"
    },
    "doc_homologacao": {
        "link": "http://bi.intranetparvi.com.br/PBIReports/browse/DOC/Area%20Homologa%C3%A7%C3%A3o",
        "pasta": rf"{PASTA_REPOSITORIO}\DOC\Area Homologação"
    },
    "pos_vendas": {
        "link": "http://bi.intranetparvi.com.br/PBIReports/browse/P%C3%B3s%20Vendas",
        "pasta": rf"{PASTA_REPOSITORIO}\Pós Vendas"
    },
    "pneus": {
        "link": "http://bi.intranetparvi.com.br/PBIReports/browse/Pneus",
        "pasta": rf"{PASTA_REPOSITORIO}\Pneus"
    },
    "bi_empilhadeira": {
        "link": "http://bi.intranetparvi.com.br/PBIReports/browse/BI%20Empilhadeira",
        "pasta": rf"{PASTA_REPOSITORIO}\BI Empilhadeira"
    },
    "mardisa_veiculos": {
        "link": "http://bi.intranetparvi.com.br/PBIReports/browse/BI%20Mardisa/Veiculos",
        "pasta": rf"{PASTA_REPOSITORIO}\BI Mardisa\Veiculos"
    },
    "mardisa_CRM": {
        "link": "http://bi.intranetparvi.com.br/PBIReports/browse/BI%20Mardisa/CRM%20-%20Rac",
        "pasta": rf"{PASTA_REPOSITORIO}\BI Mardisa\CRM - Rac"
    },
    "mardisa_posVendas": {
        "link": "http://bi.intranetparvi.com.br/PBIReports/browse/BI%20Mardisa/P%C3%B3s%20Vendas",
        "pasta": rf"{PASTA_REPOSITORIO}\BI Mardisa\Pós Vendas"
    },
        "fiscal": {
        "link": "http://bi.intranetparvi.com.br/PBIReports/browse/Fiscal",
        "pasta": rf"{PASTA_REPOSITORIO}\Fiscal"
    },
        "DP": {
        "link": "http://bi.intranetparvi.com.br/PBIReports/browse/RH%20-%20DP/DP",
        "pasta": rf"{PASTA_REPOSITORIO}\RH - DP\DP"
    },
        "RH": {
        "link": "http://bi.intranetparvi.com.br/PBIReports/browse/RH%20-%20DP/RH",
        "pasta": rf"{PASTA_REPOSITORIO}\RH - DP\RH"
    },    
        "Contabilidade": {
        "link": "http://bi.intranetparvi.com.br/PBIReports/browse/Contabilidade",
        "pasta": rf"{PASTA_REPOSITORIO}\Contabilidade"
    },
}
