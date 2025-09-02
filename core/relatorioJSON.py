import os
import json
from datetime import datetime

class StorageManager:
    def __init__(self, path=r"C:\Users\adm.joao.mendes\Documents\Storage Json\acumulador.json"):
        self.path = path
        if not os.path.exists(self.path):
            self._init_storage()

    def _init_storage(self):
        data = {
            "data": datetime.today().strftime("%Y-%m-%d"),
            "relatorios": [],
            "commits": [],
            "tasks": []
        }
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load(self):
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, data):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def add_data(self, relatorios, commits, tasks):
        data = self.load()
        hoje = datetime.today().strftime("%Y-%m-%d")
        if data["data"] != hoje:
            self._init_storage()
            data = self.load()

        data["relatorios"].extend(relatorios)
        data["commits"].extend(commits)
        data["tasks"].extend(tasks)

        self.save(data)

    def reset(self):
        self._init_storage()
