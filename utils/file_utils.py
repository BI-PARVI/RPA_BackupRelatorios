import os
import re
import glob
import time

def limpar_nome(nome: str) -> str:
    """Remove caracteres inválidos para nome de arquivo/pasta no Windows."""
    return re.sub(r'[\\/*?:"<>|]', "_", nome).strip()

def esperar_download_concluir(pasta_downloads: str, timeout: int = 120) -> bool:
    """Espera acabar arquivos .crdownload."""
    inicio = time.time()
    while time.time() - inicio < timeout:
        if not glob.glob(os.path.join(pasta_downloads, "*.crdownload")):
            return True
        time.sleep(2)
    raise TimeoutError("Download não concluiu no tempo limite")

def garantir_pasta(path: str) -> None:
    os.makedirs(path, exist_ok=True)
