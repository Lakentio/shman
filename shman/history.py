import os
import json
import datetime
from .config import LOGS_DIR

HISTORY_FILE = os.path.join(LOGS_DIR, "history.json")

def ensure_history_file():
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'w') as f:
            json.dump({}, f, indent=4)

def save_version(script_name, content):
    ensure_history_file()
    with open(HISTORY_FILE, 'r+') as f:
        history = json.load(f)
        if script_name not in history:
            history[script_name] = []
        history[script_name].append({
            "timestamp": datetime.datetime.now().isoformat(),
            "content": content
        })
        f.seek(0)
        json.dump(history, f, indent=4)
        f.truncate()

def get_versions(script_name):
    ensure_history_file()
    with open(HISTORY_FILE, 'r') as f:
        try:
            history = json.load(f)
        except json.JSONDecodeError:
            print(f"Erro: O arquivo de histórico '{HISTORY_FILE}' está corrompido.")
            return []
        
        script_versions = history.get(str(script_name), [])
        if not script_versions:
            print(f"Nenhuma versão encontrada para o script '{script_name}'.")
        return script_versions

def commit_version(script_name, version, message):
    ensure_history_file()
    script_path = os.path.join(LOGS_DIR, "../scripts", f"{script_name}.sh")
    if not os.path.exists(script_path):
        print(f"Erro: O script '{script_name}' não existe.")
        return

    with open(script_path, 'r') as f:
        content = f.read()

    with open(HISTORY_FILE, 'r+') as f:
        history = json.load(f)
        if script_name not in history:
            history[script_name] = []
        history[script_name].append({
            "version": version,
            "timestamp": datetime.datetime.now().isoformat(),
            "message": message,
            "content": content
        })
        f.seek(0)
        json.dump(history, f, indent=4)
        f.truncate()

    print(f"Versão {version} do script '{script_name}' salva com sucesso.")
