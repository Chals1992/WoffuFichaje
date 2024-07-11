from msedge.selenium_tools import Edge, EdgeOptions

options = EdgeOptions()
options.use_chromium = True
options.add_argument("--headless")  # Ejecutar en modo headless
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = Edge(executable_path='/usr/local/bin/edgedriver', options=options)
driver.get('https://www.google.com')

print(driver.title)  # Imprimir el título de la página para verificar que se abrió correctamente

driver.quit()
