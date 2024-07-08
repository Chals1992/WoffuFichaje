import os
import requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

# Descargar msedgedriver.exe
archivo_msedgedriver = 'msedgedriver.exe'
url_msedgedriver = "https://volkswagengroup-my.sharepoint.com/:u:/r/personal/carles_casajuana1_volkswagen-groupservices_com/Documents/Carles_Seat/edgedriver_win64/msedgedriver.exe?csf=1&web=1&e=qkd8R3"
response = requests.get(url_msedgedriver)
if response.status_code == 200:
    with open(archivo_msedgedriver, 'wb') as file:
        file.write(response.content)
    print("msedgedriver.exe descargado con éxito.")
else:
    print(f"Error al descargar el archivo. Código de estado: {response.status_code}")

options = Options()
options.add_argument("headless")  # Ejecutar en modo headless, sin abrir el navegador
service = Service(executable_path=os.path.abspath(archivo_msedgedriver))
driver = webdriver.Edge(se
