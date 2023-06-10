import subprocess

# Запуск трьох екземплярів logging-service на різних портах
ports = [8000]

for port in ports:
    command = f"python3 logging_service.py --port {port}"
    subprocess.Popen(command, shell=True)