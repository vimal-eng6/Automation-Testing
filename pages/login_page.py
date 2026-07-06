from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    """
    Page Object Model for the Login Page.
    This file stores the 'locators' (how to find elements) and the 'actions' (what to do with them).
    """
    # --- Locators ---
    USERNAME_INPUT = (By.ID, "login-username")  
    PASSWORD_INPUT = (By.ID, "login-password")  
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']") 
    
    # ⚠️ TODO: Update this locator to match the red error text that appears when a login fails
    ERROR_MESSAGE = (By.CLASS_NAME, "alert--error") 
    
    # --- Actions ---
    def login(self, username, password):
        """Action method to perform the login process"""
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
        
    def get_error_message(self):
        """Finds and returns the text of the error message on the page"""
        element = self.find_element(self.ERROR_MESSAGE)
        return element.text
