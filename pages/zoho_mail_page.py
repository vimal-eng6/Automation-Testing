from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

class ZohoMailPage(BasePage):
    """
    Page Object Model for the Zoho Mail Login/Sign-in Page and Mail Dashboard.
    """
    # --- Locators ---
    USERNAME_INPUT = (By.ID, "login_id")
    NEXT_BUTTON = (By.ID, "nextbtn")
    PASSWORD_INPUT = (By.ID, "password")
    SIGNIN_BUTTON = (By.ID, "nextbtn")
    ERROR_MESSAGE = (By.CLASS_NAME, "fielderror")
    FORGOT_PASSWORD_LINK = (By.CLASS_NAME, "blueforgotpassword")
    
    # --- Compose Mail Locators ---
    NEW_MAIL_BUTTON = (By.XPATH, "//div[contains(@class, 'zm_compose')]")
    TO_INPUT = (By.XPATH, "//input[@aria-label='To Recipients']")
    SUBJECT_INPUT = (By.XPATH, "//input[@placeholder='Subject']")
    BODY_IFRAME = (By.CLASS_NAME, "ze_area")
    BODY_TEXT = (By.CLASS_NAME, "ze_body")
    SEND_BUTTON = (By.XPATH, "//span[text()='Send']")

    def enter_username(self, username):
        """Action method to input username and click Next"""
        self.input_text(self.USERNAME_INPUT, username)
        self.click_element(self.NEXT_BUTTON)

    def enter_password(self, password):
        """Action method to input password and click Sign In"""
        # Ensure password field is visible before interacting
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.SIGNIN_BUTTON)

    def login(self, username, password):
        """Action method to perform the complete Zoho login process"""
        self.enter_username(username)
        self.enter_password(password)

    def click_next_only(self):
        """Clicks the next/submit button without doing anything else"""
        self.click_element(self.NEXT_BUTTON)

    def get_error_message(self):
        """Finds and returns the text of the validation/error message on the page"""
        # Wait for the error element to be visible
        element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        # Wait until the error message contains non-empty text
        self.wait.until(lambda d: len(element.text.strip()) > 0)
        return element.text.strip()

    def click_forgot_password(self):
        """Clicks the Forgot Password link"""
        # Wait for password screen to be visible
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        self.click_element(self.FORGOT_PASSWORD_LINK)
        time.sleep(2)

    def compose_and_send_email(self, to_email, subject, body_content):
        """Composes a new email and sends it to the specified recipient"""
        # 1. Click New Mail
        self.click_element(self.NEW_MAIL_BUTTON)
        time.sleep(2) # Give a moment for composer to draw
        
        # 2. Input recipient
        to_field = self.find_element(self.TO_INPUT)
        to_field.clear()
        to_field.send_keys(to_email)
        time.sleep(0.5)
        to_field.send_keys(Keys.ENTER)
        time.sleep(0.5)
        
        # 3. Input subject
        self.input_text(self.SUBJECT_INPUT, subject)
        time.sleep(0.5)
        
        # 4. Input body (requires switching to the rich text editor iframe)
        iframe = self.find_element(self.BODY_IFRAME)
        self.driver.switch_to.frame(iframe)
        
        try:
            body_field = self.driver.find_element(*self.BODY_TEXT)
            body_field.clear()
            body_field.send_keys(body_content)
        finally:
            # Crucial: switch back to the main layout
            self.driver.switch_to.default_content()
            
        time.sleep(1)
        
        # 5. Click Send button
        self.click_element(self.SEND_BUTTON)
        print("Send button clicked.")
        time.sleep(3) # Wait for mail to send
