from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from selenium import webdriver
import time

#NO LO HE PROBADO PERO YA ESTAN LOS TESTS

class LoginTest(TestCase):
    def setUp(self):
        # Inicializar el navegador (por ejemplo, Chrome)
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Capturar un screenshot y guardarlo en un archivo
        self.driver.save_screenshot('screenshot.png')
        # Cerrar el navegador
        self.driver.quit()

    def test_login(self):
        # Abrir el archivo HTML local (asegúrate de proporcionar la ruta completa)
        self.driver.get('file:///C:/Users/luiss/Desktop/proyecto-final-desarrollo-colab-proyecto-inicial/web/templates/login.html')

        # Esperar unos segundos para que la página se cargue completamente
        time.sleep(2)

        # Encontrar los elementos del formulario por su nombre y enviar datos de prueba
        username_input = self.driver.find_element_by_name('username')
        password_input = self.driver.find_element_by_name('password')

        # Ingresa datos de prueba
        username_input.send_keys('nombre_de_usuario')
        password_input.send_keys('contraseña_secreta')

        # Envía el formulario
        login_button = self.driver.find_element_by_css_selector('input[type="submit"]')
        login_button.click()

        # Esperar unos segundos para ver los resultados (puedes agregar más tiempo si es necesario)
        time.sleep(5)

        # Realiza tus aserciones de prueba aquí, por ejemplo:
        # assert 'Bienvenido' in self.driver.page_source

# Si estás ejecutando estas pruebas desde la línea de comandos, podrías usar:
# python manage.py test nombre_de_tu_app.tests.test_nombre_de_tu_clase_de_prueba

