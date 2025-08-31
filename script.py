import os
import subprocess

# Lista de direcciones IP a verificar
ips = ["192.168.1.1", "192.168.1.2", "10.0.0.1", "8.8.8.8"]

# Función para hacer ping a una IP
def check_ping(ip):
    # Ejecuta el comando ping en Ubuntu
    response = os.system("ping -c 1 " + ip)
    
    # Verifica si el ping fue exitoso (0 significa éxito)
    if response == 0:
        print(f"{ip} está en línea")
    else:
        print(f"{ip} no está en línea")

# Verificar cada IP de la lista
for ip in ips:
    check_ping(ip)

