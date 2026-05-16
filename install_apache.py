import subprocess
import sys
import datetime

LOG_FILE = "automation_log.txt"

def log(message, level="INFO"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] [{level}] {message}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def run_command(command, description):
    log(f"Execution: {description}")
    try:
        result = subprocess.run(
            command, shell=True,
            capture_output=True, text=True, timeout=120
        )
        if result.returncode == 0:
            log(f"OK: {description}", "SUCCESS")
            return True
        else:
            log(f"ERREUR: {result.stderr}", "ERROR")
            return False
    except subprocess.TimeoutExpired:
        log(f"TIMEOUT: {description}", "ERROR")
        return False

def install_apache():
    log("=== Debut installation Apache ===")
    steps = [
        ("apt-get update -y", "Mise a jour des paquets"),
        ("apt-get install -y apache2", "Installation Apache2"),
        ("systemctl start apache2", "Demarrage Apache2"),
        ("systemctl enable apache2", "Activation au demarrage"),
    ]
    success = 0
    for cmd, desc in steps:
        if run_command(cmd, desc):
            success += 1
    log(f"=== Termine: {success}/{len(steps)} etapes reussies ===")
    return success == len(steps)

def check_apache():
    log("Verification Apache...")
    result = subprocess.run(
        "systemctl is-active apache2",
        shell=True, capture_output=True, text=True
    )
    status = result.stdout.strip()
    log(f"Statut Apache: {status}", "INFO")
    return status == "active"

if __name__ == "__main__":
    log("Script d'automatisation — Pacome SINWILLY")
    log("Systeme: Linux (Ubuntu/Debian requis)")
    success = install_apache()
    if success:
        check_apache()
        log("Apache installe et operationnel !", "SUCCESS")
    else:
        log("Installation incomplete. Verifier les logs.", "WARNING")