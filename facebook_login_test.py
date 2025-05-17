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

@allure.title("Facebook Login Test")
@allure.description("Verify login functionality")
def test_facebook_login(driver):
    with allure.step("1. Open Facebook"):
        driver.get("https://www.facebook.com")
        assert "Facebook" in driver.title

    with allure.step("2. Enter Email"):
        email = driver.find_element(By.ID, "email")
        email.send_keys("your_test_email@example.com")  # Replace with test email

    with allure.step("3. Enter Password"):
        password = driver.find_element(By.ID, "pass")
        password.send_keys("your_test_password")  # Replace with test password

    with allure.step("4. Click Login"):
        login_button = driver.find_element(By.NAME, "login")
        login_button.click()

    with allure.step("5. Verify Login"):
        try:
            assert "Find Friends" in driver.page_source  # Post-login element
            allure.attach(driver.get_screenshot_as_png(), name="Login-Success", attachment_type=allure.attachment_type.PNG)
        except AssertionError:
            allure.attach(driver.get_screenshot_as_png(), name="Login-Failed", attachment_type=allure.attachment_type.PNG)
            raise