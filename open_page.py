from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

# Configuración del WebDriver de Edge
options = Options()
options.add_argument('--headless')  # Ejecutar Edge en modo headless
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = Service('/usr/local/bin/msedgedriver')  # Ruta donde se descargará msedgedriver

driver = webdriver.Edge(service=service, options=options)
driver.get('https://www.google.com')
print(driver.title)
driver.quit()
