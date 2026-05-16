# Automation Réseau — Pacôme SINWILLY

Automatisation du déploiement d'un serveur Apache avec Python, Docker et Ansible.

## Architecture

```
06-automation/
├── install_apache.py   # Script Python d'installation
├── Dockerfile          # Image Docker Ubuntu + Apache
├── docker-compose.yml  # Orchestration
├── playbook.yml        # Playbook Ansible
└── README.md
```

## Utilisation

### Avec Docker
```bash
docker-compose up -d
# Accès : http://localhost:8080
```

### Avec Ansible
```bash
ansible-playbook -i hosts playbook.yml
```

### Script Python seul (Linux)
```bash
python3 install_apache.py
```

## Technologies
- Python 3 · subprocess
- Docker · Docker Compose
- Ansible
- Ubuntu 22.04

## Auteur
Pacôme SINWILLY — [GitHub](https://github.com/Pacomesinwilly)