import os
import subprocess
from datetime import datetime
from .config import LOGS_DIR, SCRIPTS_DIR

def ensure_script_log_dir(script_name):
    script_log_dir = os.path.join(LOGS_DIR, script_name)
    os.makedirs(script_log_dir, exist_ok=True)
    return script_log_dir

def run_script(script_name):
    script_path = os.path.join(SCRIPTS_DIR, f"{script_name}.sh")
    if not os.path.exists(script_path):
        print(f"Erro: O script '{script_name}' não existe.")
        return

    script_log_dir = ensure_script_log_dir(script_name)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = os.path.join(script_log_dir, f"log_{timestamp}.txt")

    try:
        with open(log_file_path, 'w') as log_file:
            result = subprocess.run(
                [script_path],
                stdout=log_file,
                stderr=subprocess.STDOUT,
                text=True
            )
        print(f"Script '{script_name}' executado com sucesso. Log salvo em: {log_file_path}")
    except Exception as e:
        print(f"Erro ao executar o script '{script_name}': {e}")

def list_logs(script_name):
    script_log_dir = os.path.join(LOGS_DIR, script_name)
    if not os.path.exists(script_log_dir):
        print(f"Nenhum log encontrado para o script '{script_name}'.")
        return

    logs = sorted(os.listdir(script_log_dir))
    if not logs:
        print(f"Nenhum log encontrado para o script '{script_name}'.")
        return

    print(f"Logs disponíveis para o script '{script_name}':")
    for i, log in enumerate(logs, start=1):
        print(f"{i}. {log}")

def view_log(script_name, log_number):
    script_log_dir = os.path.join(LOGS_DIR, script_name)
    if not os.path.exists(script_log_dir):
        print(f"Nenhum log encontrado para o script '{script_name}'.")
        return

    logs = sorted(os.listdir(script_log_dir))
    if not logs or log_number < 1 or log_number > len(logs):
        print(f"Log número {log_number} não encontrado para o script '{script_name}'.")
        return

    log_file_path = os.path.join(script_log_dir, logs[log_number - 1])
    print(f"Exibindo conteúdo do log '{logs[log_number - 1]}':\n")
    with open(log_file_path, 'r') as log_file:
        print(log_file.read())
