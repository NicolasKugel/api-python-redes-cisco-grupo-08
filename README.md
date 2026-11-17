# TP4 – Redes de Computadoras (3643)

**Universidad Nacional de La Matanza**  
**Grupo 08 – Segundo cuatrimestre de 2026**

## Descripción

Este repositorio contiene los scripts de Python utilizados para interactuar con la API REST del Network Controller de Cisco Packet Tracer.

Se utilizaron los scripts proporcionados por la cátedra y se desarrolló uno adicional para exportar el inventario de la red a un archivo CSV.

## Scripts

| Script | Descripción |
|---|---|
| `01_get-ticket.py` | Obtiene un ticket de autenticación del Network Controller. |
| `02_get-network-device.py` | Consulta y muestra los dispositivos de red descubiertos. |
| `03_get-host.py` | Consulta y muestra los hosts identificados por el controlador. |
| `04_tabulate.py` | Muestra información de dispositivos y hosts mediante tablas. |
| `05_exportar_inventario.py` | Consulta dispositivos y hosts, procesa sus atributos y exporta la información a `inventario.csv`. |

Los scripts 02 y 04 fueron adaptados para contemplar registros de la API que no incluyen el campo `hostname`.

## Requisitos

- Python 3
- Cisco Packet Tracer con Network Controller configurado
- Acceso externo a la API habilitado
- Bibliotecas incluidas en `requirements.txt`

## Instalación

Crear un entorno virtual desde la raíz del proyecto:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Configuración

La API REST del controlador debe estar disponible en:

`http://localhost:58000/api/v1`

Configurar las credenciales del Network Controller mediante las variables de entorno `NC_USERNAME` y `NC_PASSWORD`. Los scripts que necesiten un ticket existente pueden utilizar `NRO_TICKET`. Configurar el valor de las variables en `.env.example` (luego de puede crear un copia de este que se llame .env y listo)

No se incluyen contraseñas ni tickets de autenticación en el repositorio.

## Ejecución del script propio

Desde PowerShell:

```powershell
python .\src\05_exportar_inventario.py
```

El programa obtiene un ticket de autenticación, consulta los endpoints `/network-device` y `/host`, y genera `inventario.csv`.

El archivo contiene las columnas:

- Tipo
- Nombre
- Dirección IP
- Modelo

Durante la validación del TP4 se exportaron correctamente **17 registros**.
