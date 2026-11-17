
import csv
import requests
from config import BASE_URL, USUARIO, PASSWORD

# 1. Obtener ticket de autenticacion.
respuesta = requests.post(
    f"{BASE_URL}/ticket",
    json={"username": USUARIO, "password": PASSWORD},
    timeout=15
)
respuesta.raise_for_status()

ticket = respuesta.json()["response"]["serviceTicket"]
headers = {"X-Auth-Token": ticket}

# 2. Consultar dispositivos y hosts.
dispositivos_resp = requests.get(
    f"{BASE_URL}/network-device",
    headers=headers,
    timeout=15
)
dispositivos_resp.raise_for_status()

hosts_resp = requests.get(
    f"{BASE_URL}/host",
    headers=headers,
    timeout=15
)
hosts_resp.raise_for_status()

dispositivos = dispositivos_resp.json()["response"]
hosts = hosts_resp.json()["response"]

# 3. Preparar los registros del inventario.
inventario = []

for equipo in dispositivos:
    inventario.append({
        "Tipo": "Dispositivo",
        "Nombre": equipo.get("hostname") or "Sin hostname",
        "Direccion IP": equipo.get("managementIpAddress") or "N/D",
        "Modelo": equipo.get("platformId") or "N/D"
    })

for host in hosts:
    inventario.append({
        "Tipo": "Host",
        "Nombre": host.get("hostName") or "Sin nombre",
        "Direccion IP": host.get("hostIp") or "N/D",
        "Modelo": host.get("hostType") or "N/D"
    })

# 4. Exportar la informacion a CSV.
with open("inventario.csv", "w", newline="", encoding="utf-8-sig") as archivo:
    columnas = ["Tipo", "Nombre", "Direccion IP", "Modelo"]

    writer = csv.DictWriter(archivo, fieldnames=columnas)
    writer.writeheader()
    writer.writerows(inventario)

print("Inventario exportado correctamente.")
print(f"Dispositivos encontrados: {len(dispositivos)}")
print(f"Hosts encontrados: {len(hosts)}")
print(f"Total de registros exportados: {len(inventario)}")
print("Archivo generado: inventario.csv")
