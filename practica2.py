import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

class Practica2SeleniumWebDriver(unittest.TestCase):

    def setUp(self):
        # Inicializamos el driver de Chrome (Selenium 4 maneja los drivers automáticamente)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10) # Espera implícita para dar tiempo a que carguen los elementos
        self.base_url = "https://automationexercise.com"
        
        # Crear carpeta para guardar las capturas de pantalla de evidencia automáticamente
        os.makedirs("evidencias", exist_ok=True)

    def test_ejercicio_2_login_correcto(self):
        driver = self.driver
        driver.get(self.base_url)
        
        # Uso de localizador XPATH
        driver.find_element(By.XPATH, "//a[contains(text(), 'Signup / Login')]").click()
        
        # Uso de localizador CSS SELECTOR y NAME
        driver.find_element(By.CSS_SELECTOR, "[data-qa='login-email']").send_keys("leonidas_test_qa@example.com")
        driver.find_element(By.NAME, "password").send_keys("Test1234")
        driver.find_element(By.CSS_SELECTOR, "[data-qa='login-button']").click()
        time.sleep(2) # Pausa para observar el resultado
        
        # ASSERT 1: Validar que el elemento de bienvenida "Logged in as" esté visible
        logged_in_message = driver.find_element(By.XPATH, "//a[contains(text(), 'Logged in as')]")
        self.assertTrue(logged_in_message.is_displayed(), "Fallo: No se muestra el mensaje 'Logged in as'")
        
        # ASSERT 2: Validar que el botón de "Logout" exista y tenga el enlace correcto
        logout_btn = driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]")
        self.assertEqual(logout_btn.get_attribute("href"), f"{self.base_url}/logout", "Fallo: El href de Logout es incorrecto")
        
        # CAPTURA DE PANTALLA
        driver.save_screenshot("evidencias/ejercicio2_login_correcto.png")

    def test_ejercicio_3_login_incorrecto(self):
        driver = self.driver
        driver.get(self.base_url)
        
        driver.find_element(By.XPATH, "//a[contains(text(), 'Signup / Login')]").click()
        
        # Insertamos credenciales falsas
        driver.find_element(By.CSS_SELECTOR, "[data-qa='login-email']").send_keys("correo_invalido@example.com")
        driver.find_element(By.NAME, "password").send_keys("ClaveFalsa123")
        driver.find_element(By.CSS_SELECTOR, "[data-qa='login-button']").click()
        time.sleep(2)
        
        # Localizamos el mensaje de error
        error_msg = driver.find_element(By.XPATH, "//p[contains(text(), 'Your email or password is incorrect!')]")
        
        # ASSERT 1: Validar que el mensaje de error aparezca en pantalla
        self.assertTrue(error_msg.is_displayed(), "Fallo: El mensaje de error no está visible")
        
        # ASSERT 2: Validar que el texto exacto sea el esperado
        self.assertEqual(error_msg.text, "Your email or password is incorrect!", "Fallo: El texto del error no coincide")
        
        # CAPTURA DE PANTALLA
        driver.save_screenshot("evidencias/ejercicio3_login_incorrecto.png")

    def test_ejercicio_4_busqueda_productos(self):
        driver = self.driver
        driver.get(self.base_url)
        
        driver.find_element(By.XPATH, "//a[contains(text(), 'Products')]").click()
        time.sleep(2) 
        
        # Uso de localizador ID
        driver.find_element(By.ID, "search_product").send_keys("Shirt")
        driver.find_element(By.ID, "submit_search").click()
        time.sleep(2)
        
        # ASSERT 1: Validar que el título sea visible y contenga la palabra 'SEARCHED PRODUCTS'
        searched_title = driver.find_element(By.CSS_SELECTOR, "h2.title.text-center")
        self.assertIn("SEARCHED PRODUCTS", searched_title.text, "Fallo: El título no es el esperado")
        
        # ASSERT 2: Validar que la lista de resultados de búsqueda sea mayor a 0 (que haya productos)
        products = driver.find_elements(By.CSS_SELECTOR, ".productinfo")
        self.assertGreater(len(products), 0, "Fallo: No se encontró ningún producto con ese criterio")
        
        # CAPTURA DE PANTALLA
        driver.save_screenshot("evidencias/ejercicio4_busqueda_productos.png")

    def tearDown(self):
        # Cerramos el navegador al terminar cada prueba
        self.driver.quit()

if __name__ == "__main__":
    # Ejecutamos las pruebas con un nivel de detalle mayor (verbosity=2)
    unittest.main(verbosity=2)