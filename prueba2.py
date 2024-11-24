import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Usa webdriver_manager para obtener la versión correcta de ChromeDriver
service = Service(ChromeDriverManager().install())

# Inicializa el navegador con el servicio
driver = webdriver.Chrome(service=service)

# Abre la página 
driver.get("https://uvirtual.uce.edu.ec/course/view.php?id=9619")

# Obtén las variables de entorno para usuario y contraseña
usuario = os.getenv("username_uvirtual")  # Usa la variable de entorno USERNAME
contrasena = os.getenv("password_uvirtual")  # Usa la variable de entorno PASSWORD

# Verifica si las variables de entorno están configuradas correctamente
if not usuario or not contrasena:
    print("Error: Las variables de entorno 'USERNAME' o 'PASSWORD' no están configuradas.")
else:
    # Encuentra el campo de usuario e ingresa tu usuario
    campo_usuario = driver.find_element(By.ID, "username")  # O usa By.ID, By.CLASS_NAME, etc.
    campo_usuario.send_keys(usuario)

    # Encuentra el campo de contraseña e ingresa tu contraseña
    campo_contrasena = driver.find_element(By.ID, "password")  # Igualmente, usa el selector adecuado
    campo_contrasena.send_keys(contrasena)

    # Encuentra el botón de inicio de sesión y haz clic en él
    boton_login = driver.find_element(By.ID, "loginbtn")  # Reemplaza con el nombre del botón
    boton_login.click()

    time.sleep(10)  # Espera a que la página cargue

    # Puedes esperar que la página cargue o realizar alguna otra acción después de iniciar sesión
    print("Inicio de sesión exitoso.")

    # Descomenta la siguiente línea si deseas cerrar el navegador
    # driver.quit()
