import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
import requests

# Definir las opciones del navegador Edge
options = EdgeOptions()
options.use_chromium = True
options.add_argument("headless")

# Descargar el archivo msedgedriver.exe si no existe
archivo_msedgedriver = 'msedgedriver.exe'
if not os.path.isfile(archivo_msedgedriver):
    url_msedgedriver = "https://volkswagengroup-my.sharepoint.com/:u:/r/personal/carles_casajuana1_volkswagen-groupservices_com/Documents/Carles_Seat/edgedriver_win64/msedgedriver.exe?csf=1&web=1&e=qkd8R3"
    print("Descargando msedgedriver.exe...")
    response = requests.get(url_msedgedriver)
    if response.status_code == 200:
        with open(archivo_msedgedriver, 'wb') as file:
            file.write(response.content)
        print("Descarga completada.")
    else:
        print("Error al descargar el archivo. Código de estado:", response.status_code)
        exit(1)

# Crear una instancia del controlador de Edge
service = EdgeService(executable_path=os.path.abspath(archivo_msedgedriver))
driver = webdriver.Edge(service=service, options=options)

# Navegar a la página
