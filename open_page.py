import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configuración de las opciones del navegador Chrome
options = Options()
options.add_argument("--headless")  # Ejecutar en modo headless (sin ventana)
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Especifica la ruta al archivo chromedriver
chromedriver_path = "/usr/local/bin/chromedriver"

# Configurar el servicio de Chrome con la ruta del chromedriver
service = Service(executable_path=chromedriver_path)

# Espera antes de crear el controlador de Chrome
time.sleep(10)  # Puedes ajustar el tiempo de espera según sea necesario

# Crear una instancia del controlador de Chrome
driver = webdriver.Chrome(service=service, options=options)

# Ejemplo de uso: abrir una página web
driver.get("https://www.example.com")

# Cerrar el navegador al finalizar
driver.quit()
