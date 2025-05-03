import os
import json
import datetime
from .config import SCRIPTS_DIR, META_FILE, load_config
from .history import save_version, get_versions, commit_version

def create_script(name, category, tags):
    if not os.path.exists(SCRIPTS_DIR):
        print(f"Erro: O diretório de scripts '{SCRIPTS_DIR}' não existe. Execute 'shman init' primeiro.")
        return

    script_path = os.path.join(SCRIPTS_DIR, f"{name}.sh")
    if os.path.exists(script_path):
        raise FileExistsError(f"Erro: O script '{name}' já existe.")

    with open(script_path, 'w') as f:
        content = "#!/bin/bash\n"
        f.write(content)
    os.chmod(script_path, 0o755)

    with open(META_FILE, 'r+') as f:
        data = json.load(f)
        data[name] = {
            "name": name,
            "category": category,
            "tags": tags,
            "created_at": datetime.datetime.now().isoformat()
        }
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

    print(f"Script '{name}' criado com sucesso em {script_path}.")

def edit_script(name):
    config = load_config()
    editor = config.get("editor", "mousepad")
    script_path = os.path.join(SCRIPTS_DIR, f"{name}.sh")
    if not os.path.exists(script_path):
        print("Script não encontrado.")
        return

    with open(script_path, 'r') as f:
        original_content = f.read()

    os.system(f"{editor} {script_path}")

    with open(script_path, 'r') as f:
        updated_content = f.read()

def list_versions(name):
    print(f"Buscando versões para o script '{name}'...")
    versions = get_versions(name)
    if not versions:
        print(f"Nenhuma versão encontrada para o script '{name}'.")
        return

    print(f"Encontradas {len(versions)} versões para o script '{name}':")
    for i, version in enumerate(versions, start=1):
        print(f"Versão: {version['version']}, Timestamp: {version['timestamp']}, Mensagem: {version['message']}")

def restore_version(name, version_index):
    versions = get_versions(name)
    if not versions or version_index < 1 or version_index > len(versions):
        print(f"Índice de versão inválido para o script '{name}'.")
        return

    version = versions[version_index - 1]
    script_path = os.path.join(SCRIPTS_DIR, f"{name}.sh")
    with open(script_path, 'w') as f:
        f.write(version["content"])

    print(f"Script '{name}' restaurado para a versão {version_index}.")

def commit_script(name, version, message):
    commit_version(name, version, message)