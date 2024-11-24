
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Usa webdriver_manager para obtener la versión correcta de ChromeDriver
service = Service(ChromeDriverManager().install())

# Inicializa el navegador con el servicio
driver = webdriver.Chrome(service=service)

# Abre Google
driver.get("https://uvirtual.uce.edu.ec/my/")


print("Selenium está funcionando correctamente.")
driver.quit()
