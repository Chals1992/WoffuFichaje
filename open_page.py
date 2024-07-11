from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

# Configuración de las opciones del navegador Edge
options = Options()
options.add_argument("--headless")  # Ejecutar en modo headless (sin ventana)
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Especifica la ruta al archivo msedgedriver
msedgedriver_path = "/usr/local/bin/msedgedriver"

# Configurar el servicio de Edge con la ruta del msedgedriver
service = Service(executable_path=msedgedriver_path)

# Crear una instancia del controlador de Edge
driver = webdriver.Edge(service=service, options=options)

# Navegar a la página web
driver.get("https://volkswagen-groupservices.woffu.com/v2/personal/dashboard/user")

# Cerrar el navegador al finalizar
driver.quit()
