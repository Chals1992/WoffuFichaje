from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options

# Configurar opciones de Microsoft Edge
options = Options()
options.add_argument('--headless')  # Ejecutar en modo headless, sin interfaz gráfica
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Configurar el servicio de Microsoft Edge
service = EdgeService(executable_path='msedgedriver')

# Inicializar el WebDriver de Microsoft Edge
driver = webdriver.Edge(service=service, options=options)

# Abrir una página web
driver.get("https://www.google.com")

# Verificar el título de la página
assert "Example Domain" in driver.title

# Cerrar el navegador
driver.quit()
