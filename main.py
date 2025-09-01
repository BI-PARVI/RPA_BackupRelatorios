from config.settings import RELATORIOS, PASTA_REPOSITORIO, REPOSITORIO, MENSAGEM_COMMIT
from core.browser import Browser
from core.relatorio import RelatorioManager
from core.github_manager import GitHubManager
from core.relatorio_PDF import ReportManager
from utils.limiteBackup import limitar_relatorios
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
            limitar_relatorios(dados["pasta"], limite=8)

        log("\n[OK] Backup Realizado com Sucesso!")

        ##Alteração nova
        
        git_manager = GitHubManager(PASTA_REPOSITORIO, REPOSITORIO, MENSAGEM_COMMIT)
        git_manager.atualizar()

        # Gera o relatório diário automaticamente
        ReportManager().gerar_relatorio(
            rel_manager.relatorios_baixados,
            git_manager.commits,
            rel_manager.tasks_criadas
        )
        self.browser.quit()

if __name__ == "__main__":
    Main().run()
