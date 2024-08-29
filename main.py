import data
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    # Localizador del botón pedir un taxi
    ask_taxi_button = (By.CLASS_NAME, 'button round')
    # Localizador del botón comfort
    comfort_button = (By.XPATH, "//div[@class='tcard active']")
    # Localizador del campo numero de telefono
    number_field_module = (By.CLASS_NAME, 'np-text')
    # Localizador del campo para escribir el numero de telefono
    add_phone = (By.ID, 'phone')
    # Localizador del botón siguiente de telefono
    phone_next_button = (By.CLASS_NAME, 'button full')
    # Localizador del campo codigo del telefono
    phone_code_field = (By.ID, 'code')
    # Localizador de confirmar codigo
    code_confirm_button = (By.XPATH, "//button[@class='button full']")
    # Localizador campo método de pago
    payment_field = (By.CLASS_NAME, 'pp-button filled')
    # Localizador para campo agregar tarjeta
    add_card_button = (By.CLASS_NAME, 'pp-row disabled')
    # Localizador para escribir datos de tarjeta
    card_number = (By.ID, 'number')
    # Localizador para codigo de tarjeta
    code_card = (By.ID, 'code')
    # Localizador click en ventana agregar tarjeta para activar el botón agregar
    enable_add_button = (By.CLASS_NAME, 'pp-separator')
    # Localizador para boton tarjeta agregada
    added_card_button = (By.CLASS_NAME, 'button full')
    # localizador botón cerrar ventana
    close_window_button = (By.CLASS_NAME, 'close-button section-close')
    # Localizador para campo mensaje al conductor
    driver_message_field = (By.ID, 'comment')
    # Localizador para casilla de verificación Mantas y panuelos
    Mantas_slider = (By.XPATH, "//span[@class='slider round']")
    # Localizador contador de helado
    ice_cream_counter = (By.CLASS_NAME, 'counter-plus')
    # Localizador enviar solicitud de taxi
    send_taxi_request = (By.CLASS_NAME, 'smart-button-main')
    # Localizador de informacion del conductor
    diver_information = (By.CLASS_NAME, 'order-header-content')

    def __init__(self, driver):
        self.driver = driver

    def set_route(self, from_address, to_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)
        self.driver.find_element(*self.to_field).send_keys(to_address)
    
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')


    def ask_taxi_option(self):
        return self.driver.find_element(*self.ask_taxi_button).click()


    def comfort_rate_button(self):
        return self.driver.find_element(*self.comfort_button).click()


    def is_comfort_button_selected(self):
        return self.driver.find_element(*self.comfort_button).is_selected()


    def add_phone_number_method(self, phone_number):
        self.driver.find_element(*self.number_field_module).click()
        self.driver.find_element(*self.add_phone).send_keys(data.phone_number)
        self.driver.find_element(*self.phone_next_button).click()
        self.driver.find_element(*self.phone_code_field).send_keys(retrieve_phone_code(self.driver))


    def confirm_phone_code(self):
        self.driver.find_element(*self.code_confirm_button).click()


    def is_phone_code_confirmed(self):
        return self.driver.find_element(*self.code_confirm_button).is_selected()


    def add_payment_method(self, card_number, card_code):
        self.driver.find_element(*self.payment_field).click()
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.card_number).send_keys(data.card_number)
        self.driver.find_element(*self.code_card).send_keys(data.card_code)
        self.driver.find_element(*self.enable_add_button).click()
        self.driver.find_element(*self.added_card_button).click()

    def is_enable_add_button_selected(self):
        return self.driver.find_element(*self.enable_add_button).is_selected()

    def driver_message(self, driver_comment):
        self.driver.find_element(*self.driver_message_field).send_keys(data.message_for_driver)

    def request_requirements(self):
        self.driver.find_element(*self.Mantas_slider).click()
        self.driver.find_element(*self.ice_cream_counter).click()
        self.driver.find_element(*self.ice_cream_counter).click()


    def is_manta_selected(self):
        return self.driver.find_element(*self.Mantas_slider).is_selected()


    def end_request(self):
        self.driver.find_element(*self.send_taxi_request).click()


    def is_send_request_button_enabled(self):
        return self.driver.find_element(*self.send_taxi_request).is_selected()

    def wait_for_driver_info(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(self.diver_information))

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        WebDriverWait(self.driver, 3)
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_conf_taxi_request(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        ask_taxi = routes_page.ask_taxi_option()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_located_to_be_selected(ask_taxi))
        routes_page.comfort_rate_button()
        assert routes_page.is_comfort_button_selected(), "El botón de comfort no está seleccionado"

    def test_add_phone_number(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.add_phone_number_method(phone_number)
        retrieve_phone_code(self.driver)
        WebDriverWait(self.driver, 5).until(expected_conditions.text_to_be_present_in_element(UrbanRoutesPage.phone_code_field, data.phone_number))
        routes_page.confirm_phone_code()
        assert routes_page.is_phone_code_confirmed(), 'El boton de confirmar codigo no está seleccionado'

    def test_add_payment_method(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code
        routes_page.add_payment_method(card_number, card_code)
        assert routes_page.is_enable_add_button_selected(), 'El botón agregar tarjeta no est;a seleccioando'

    def test_driver_comment(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        driver_comment = data.message_for_driver
        routes_page.driver_message(driver_comment)
        assert driver_comment == 'Traiga un aperitivo'

    def test_request_requirements(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_requirements()
        assert routes_page.is_manta_selected(), 'La casilla de Manta y pañuelos no está seleccionada'

    def test_end_request(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.end_request()
        routes_page.wait_for_driver_info()
        assert routes_page.is_send_request_button_enabled(), 'El botón pedir taxi no está habilitado'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

