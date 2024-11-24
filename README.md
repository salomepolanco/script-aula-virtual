# Automatización del Aula Virtual

Este repositorio contiene un script de automatización utilizando **Selenium** para ingresar automáticamente a un aula virtual de la Universidad Central del Ecuador (UCE), específicamente a la materia de Modelos, y realizar ciertas tareas como hacer clic en la pestaña de "Inicio". El script puede ejecutarse automáticamente cada dos días utilizando el **Programador de tareas de Windows**.

## Requisitos

Antes de ejecutar el script, asegúrate de tener las siguientes dependencias y herramientas instaladas en tu sistema:

- **Python 3.10+**
- **Selenium**
- **ChromeDriver** (para controlar Google Chrome)
- **webdriver-manager**
- **Programador de Tareas de Windows** (si quieres automatizar la ejecución)

### Instalación de Dependencias

1. **Instalar Python 3.10+**:
   - Descarga e instala Python desde [python.org](https://www.python.org/downloads/).

2. **Instalar las dependencias del proyecto**:
   Clona el repositorio o descarga los archivos del proyecto.

   Luego, instala las dependencias necesarias usando `pip`:

   ```bash
   pip install selenium webdriver-manager

3. **Instalar ChromeDriver: El script utiliza ChromeDriver para automatizar Google Chrome. Usa el siguiente comando para instalarlo automáticamente**:
   ```bash
   pip install webdriver-manager

## Instalación de Dependencias
El script necesita algunas variables de entorno para funcionar correctamente. Puedes configurar las siguientes variables en tu sistema operativo o directamente en el archivo prueba.py:

username_uvirtual: Tu nombre de usuario para ingresar al aula virtual.
password_uvirtual: Tu contraseña para el aula virtual.


## Automatización con el Programador de Tareas de Windows
Si deseas ejecutar este script automáticamente cada dos días, puedes configurar el Programador de tareas de Windows:

Abre el Programador de tareas de Windows.

Crea una nueva tarea programada:

Nombre: Automatización Aula Virtual.

Frecuencia: Cada 2 días.

Acción: Ejecutar el script prueba3.py utilizando el comando python.

En la acción de la tarea, agrega lo siguiente:

Programa/script: python

Argumentos: La ruta completa de tu archivo prueba3.py, por ejemplo:

C:\Users\tu_usuario\Documents\ScriptAulaVirtual\prueba3.py

El script se ejecutará automáticamente según la programación que hayas establecido. :D
