# Urban Routes Automated Testing project

## Descripción del Proyecto

Este proyecto tiene como objetivo automatizar las pruebas de la aplicación web **Urban Routes**, un servicio para solicitar taxis en línea. Las pruebas están diseñadas utilizando Python y Selenium WebDriver, y cubren funcionalidades críticas de la aplicación, como la selección de rutas, solicitud de taxis, autenticación por número de teléfono, y adición de métodos de pago. Este enfoque garantiza que los usuarios puedan utilizar la aplicación de manera efectiva y segura.

## Estructura del proyecto:

UrbanRoutes/
├── data.py                # Contiene los datos utilizados en las pruebas
├── helpers.py             # Funciones auxiliares
├── UrbanRoutesPage.py      # Localizadores y métodos para interactuar con la página web
└── main.py                # Pruebas automatizadas

## Explicación de los Archivos

    data.py: Contiene valores como urban_routes_url, address_from, address_to, phone_number, card_number, etc. que se usan en los tests.

    helpers.py: Proporciona métodos auxiliares, como retrieve_phone_code, que permite obtener códigos de verificación desde los logs de la red.

    UrbanRoutesPage.py: Este archivo define los elementos de la página y las acciones que se pueden realizar en ellos. Por ejemplo, permite seleccionar el punto de origen, destino, agregar un método de pago, etc.

    main.py: Contiene la clase TestUrbanRoutes, que agrupa las pruebas. Las pruebas incluyen escenarios como:
        Configuración de rutas
        Selección de taxi (opción de confort)
        Agregar número de teléfono y confirmarlo
        Agregar un método de pago
        Agregar un mensaje para el conductor
        Seleccionar requisitos adicionales (como mantas y helados)

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
- Google Chrome
- ChromeDriver

## Ejecución de las Pruebas

- pytest tests/main.py

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor, realiza un fork del repositorio y abre un pull request con tus cambios.
Autor

Este proyecto fue desarrollado por Stephany Torres S.
