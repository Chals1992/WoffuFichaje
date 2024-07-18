from selenium import webdriver

options = webdriver.EdgeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Edge(options=options)

driver.get("https://www.example.com")
print(driver.title)

driver.quit()
