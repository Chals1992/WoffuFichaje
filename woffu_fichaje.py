# Importar las clases necesarias desde msedge.selenium_tools
from msedge.selenium_tools import Edge, EdgeOptions

# Crear las opciones para el navegador Edge
options = EdgeOptions()
options.use_chromium = True  # Utilizar el motor Chromium
options.add_argument("start-maximized")  # Opción para maximizar la ventana del navegador

# Especificar la ruta al ejecutable de msedgedriver
driver_path = 'C:\\Users\\W1VFOUS\\OneDrive - Volkswagen AG\\Carles_Seat\\edgedriver_win64\\msedgedriver.exe'

# Inicializar el WebDriver para Microsoft Edge
driver = Edge(executable_path=driver_path, options=options)

# A partir de este punto, puedes utilizar 'driver' para interactuar con el navegador Edge
