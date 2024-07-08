import os
import requests
from msedge.selenium_tools import Edge, EdgeOptions

# Función para descargar msedgedriver.exe desde la URL proporcionada
def descargar_msedgedriver(url, archivo_destino):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(archivo_destino, 'wb') as f:
                f.write(response.content)
            print(f"Archivo {archivo_destino} descargado correctamente.")
        else:
            print(f"Error al descargar el archivo. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Error al descargar el archivo: {str(e)}")

# URL de descarga del archivo msedgedriver.exe
url_msedgedriver = "https://volkswagengroup-my.sharepoint.com/:u:/r/personal/carles_casajuana1_volkswagen-groupservices_com/Documents/Carles_Seat/edgedriver_win64/msedgedriver.exe?csf=1&web=1&e=qkd8R3"
archivo_msedgedriver = "msedgedriver.exe"

# Descargar msedgedriver.exe si no existe en el directorio actual
if not os.path.exists(archivo_msedgedriver):
    print(f"Descargando {archivo_msedgedriver}...")
    descargar_msedgedriver(url_msedgedriver, archivo_msedgedriver)

# Configuración de opciones para el navegador Edge
options = EdgeOptions()
options.use_chromium = True

# Inicialización del navegador Edge con la ubicación del ejecutable descargado
driver = Edge(executable_path=os.path.abspath(archivo_msedgedriver), options=options)

# Ejemplo de uso: abrir la URL de Woffu
url_woffu = "https://www.woffu.com/"
driver.get(url_woffu)

# Aquí puedes continuar con las acciones que necesites automatizar en Woffu
# Por ejemplo, llenar formularios, hacer clic en botones, etc.

# Cuando hayas terminado, cierra el navegador
driver.quit()
