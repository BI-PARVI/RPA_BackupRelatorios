import os
import time
from utils.log import log

def limitar_relatorios(pasta: str, limite: int = 8):
    """
    Mantém no máximo 'limite' relatórios em uma pasta.
    Remove os mais antigos caso ultrapasse.
    """
    if not os.path.exists(pasta):
        log(f"[WARN] Pasta não encontrada: {pasta}")
        return

    arquivos = [
        os.path.join(pasta, f) for f in os.listdir(pasta)
        if os.path.isfile(os.path.join(pasta, f))
    ]

    if len(arquivos) <= limite:
        return

    arquivos.sort(key=lambda x: os.path.getmtime(x))


    for arquivo in arquivos[:-limite]:
        try:
            os.remove(arquivo)
            log(f"[OK] Arquivo removido: {arquivo}")
        except Exception as e:
            log(f"[ERRO] Não consegui remover {arquivo}: {e}")
