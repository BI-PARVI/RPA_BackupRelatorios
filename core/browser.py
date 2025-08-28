import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import CAMINHO_CHROME, CAMINHO_PERFIL

class Browser:
    def __init__(self):
        self.driver = None

    def start(self):
        comando = f'"{CAMINHO_CHROME}" --remote-debugging-port=9222 --user-data-dir="{CAMINHO_PERFIL}"'
        subprocess.Popen(comando, shell=True)

        options = Options()
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        prefs = {
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "safebrowsing.disable_download_protection": True
        }
        options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(options=options)
        return self.driver

    def quit(self):
        if self.driver:
            self.driver.quit()
