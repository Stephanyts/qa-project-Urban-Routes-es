# Urban Routes Automated Testing project

## Descripción del Proyecto

Este proyecto tiene como objetivo automatizar las pruebas de la aplicación web **Urban Routes**, un servicio para solicitar taxis en línea. Las pruebas están diseñadas utilizando Python y Selenium WebDriver, y cubren funcionalidades críticas de la aplicación, como la selección de rutas, solicitud de taxis, autenticación por número de teléfono, y adición de métodos de pago. Este enfoque garantiza que los usuarios puedan utilizar la aplicación de manera efectiva y segura.

## Tecnologías y Técnicas Utilizadas

- **Python**: Lenguaje de programación utilizado para escribir los scripts de prueba.
- **Selenium WebDriver**: Herramienta de automatización para la interacción con la interfaz de usuario de la aplicación web.
- **Google Chrome**: Navegador utilizado para ejecutar las pruebas.
- **ChromeDriver**: Driver específico para controlar Google Chrome mediante Selenium.
- **pytest**: Framework de pruebas para ejecutar y organizar los casos de prueba.

## Clonar el repositorio:
- git clone https://github.com/tu_usuario/UrbanRoutesTest.git
- cd UrbanRoutesTest

## Crear un entorno virtual:
- python -m venv env
- source env/bin/activate  # En Windows usa `env\Scripts\activate`

## Instalar las dependencias:
- pip install selenium pytest

## Asegúrate de tener un archivo requirements.txt que contenga:
- selenium==4.x.x
- pytest==x.x.x

## Configuración el archivo data.py con la información requerida:

- urban_routes_url = 'https://example.com'
- address_from = 'Calle Falsa 123'
- address_to = 'Avenida Siempreviva 456'
- phone_number = '123456789'
- card_number = '4111111111111111'
- card_code = '123'
- message_for_driver = 'Traiga un aperitivo'

## Ejecución de las Pruebas

- pytest tests/main.py
