from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import CAMINHO_PERFIL, PASTA_DOWNLOADS

class Browser:
    def __init__(self):
        self.driver = None

    def start(self):
        options = Options()
        # usar perfil já configurado
        # options.add_argument(f'--user-data-dir={CAMINHO_PERFIL}')
        options.add_argument("--disable-blink-features=AutomationControlled")

        prefs = {
            "download.default_directory": PASTA_DOWNLOADS,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "safebrowsing.disable_download_protection": True
        }
        options.add_experimental_option("prefs", prefs)

        # Selenium abre o Chrome direto
        self.driver = webdriver.Chrome(options=options)
        return self.driver

    def quit(self):
        if self.driver:
            self.driver.quit()
