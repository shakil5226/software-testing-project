from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_sample_app():
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    try:
        # Navigate to the sample app page
        driver.get("http://uitestingplayground.com/sampleapp")
        print("Opened the sample app page.")

        # Locate the username and password fields
        username_field = driver.find_element(By.XPATH, "//input[@name='UserName']")
        password_field = driver.find_element(By.XPATH, "//input[@name='Password']")

        # Enter valid credentials
        username = "testuser"
        password = "pwd"

        username_field.send_keys(username)
        password_field.send_keys(password)
        print("Entered login credentials.")

        # Submit the form
        login_button = driver.find_element(By.ID, "login")
        login_button.click()

        # Wait for the success message to appear
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "logout"))
        )

        # Verify successful login
        success_message = driver.find_element(By.ID, "loginstatus").text
        assert "Welcome, testuser!" in success_message
        print("Login successful: ", success_message)

        # Log out
        logout_button = driver.find_element(By.ID, "logout")
        logout_button.click()

        # Wait for the logout confirmation
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "loginstatus"), "User logged out."))
        print("Logged out successfully.")

    except Exception as e:
        print("Test failed: ", str(e))

    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    test_sample_app()