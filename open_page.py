from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configuración de las opciones del navegador Chrome
options = Options()
options.headless = True  # Ejecutar en modo headless (sin ventana)
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Especifica la ruta al archivo chromedriver
chromedriver_path = "/usr/local/bin/chromedriver"

# Configurar el servicio de Chrome con la ruta del chromedriver
service = Service(executable_path=chromedriver_path)

# Crear una instancia del controlador de Chrome
driver = webdriver.Chrome(service=service, options=options)

# Navegar a la página web
driver.get("https://volkswagen-groupservices.woffu.com/v2/personal/dashboard/user")

# Cerrar el navegador al finalizar
driver.quit()
