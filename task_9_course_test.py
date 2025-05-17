import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import allure

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@allure.title("Login & Book Appoinment Test")
@allure.description("Verify Web Functionality")

def test_login(driver):
    with allure.step("1. Open the website"):
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        assert "CURA Healthcare Service" in driver.title
    with allure.step("2. Click on Make Appointment"):
        make_appointment = driver.find_element(By.ID, "btn-make-appointment")
        make_appointment.click()