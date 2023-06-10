import subprocess

# Запуск трьох екземплярів logging-service на різних портах
ports = [8001]

for port in ports:
    command = f"python logging_service.py --port {port}"
    subprocess.Popen(command, shell=True)