import os
import json

CONFIG_DIR = os.path.expanduser("~/.shman")
SCRIPTS_DIR = os.path.join(CONFIG_DIR, "scripts")
LOGS_DIR = os.path.join(CONFIG_DIR, "logs")
META_FILE = os.path.join(CONFIG_DIR, "metadata.json")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

DEFAULT_CONFIG = {
    "editor": "mousepad"
}

def ensure_directories():
    try:
        os.makedirs(SCRIPTS_DIR, exist_ok=True)
        print(f"Diretório criado ou já existente: {SCRIPTS_DIR}")
        os.makedirs(LOGS_DIR, exist_ok=True)
        print(f"Diretório criado ou já existente: {LOGS_DIR}")
        
        if not os.path.exists(META_FILE):
            with open(META_FILE, 'w') as f:
                json.dump({}, f, indent=4)
            print(f"Arquivo criado: {META_FILE}")
        else:
            print(f"Arquivo já existe: {META_FILE}")
        
        if not os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'w') as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
            print(f"Arquivo criado: {CONFIG_FILE}")
        else:
            print(f"Arquivo já existe: {CONFIG_FILE}")
        
        # Certifica que o arquivo de histórico seja criado
        history_file = os.path.join(LOGS_DIR, "history.json")
        if not os.path.exists(history_file):
            with open(history_file, 'w') as f:
                json.dump({}, f, indent=4)
            print(f"Arquivo criado: {history_file}")
        else:
            print(f"Arquivo já existe: {history_file}")
    except Exception as e:
        print(f"Erro ao criar diretórios ou arquivos: {e}")

def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)