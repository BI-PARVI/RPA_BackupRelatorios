from config.settings import RELATORIOS, PASTA_REPOSITORIO, REPOSITORIO, MENSAGEM_COMMIT
from core.browser import Browser
from core.relatorio import RelatorioManager
from core.github_manager import GitHubManager
from utils.log import log

class Main:
    def __init__(self):
        self.browser = Browser()

    def run(self):
        driver = self.browser.start()
        rel_manager = RelatorioManager(driver)

        for nome_pasta, dados in RELATORIOS.items():
            log(f"\nIniciando backup de {nome_pasta}...")
            rel_manager.baixar_relatorios_em_massa(dados["link"], dados["pasta"])

        log("\n[OK] Backup Realizado com Sucesso!")
        self.browser.quit()

        GitHubManager(PASTA_REPOSITORIO, REPOSITORIO, MENSAGEM_COMMIT).atualizar()

if __name__ == "__main__":
    Main().run()
