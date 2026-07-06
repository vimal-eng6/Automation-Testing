import time
from pages.login_page import LoginPage
from config.settings import Settings

def test_valid_login(driver):
    """Test Case 1: Valid credentials should successfully log the user in."""
    login_page = LoginPage(driver)
    login_page.open_url(Settings.BASE_URL.replace("/dashboard", "/login")) # Go directly to login page
    
    login_page.login(Settings.ADMIN_USERNAME, Settings.ADMIN_PASSWORD)
    time.sleep(2) # Wait for redirect
    
    # Verify the URL changed to the dashboard
    assert "dashboard" in driver.current_url.lower(), "Login failed, did not reach dashboard."

def test_invalid_username(driver):
    """Test Case 2: Wrong username should show an error message."""
    login_page = LoginPage(driver)
    login_page.open_url(Settings.BASE_URL.replace("/dashboard", "/login"))
    
    login_page.login("WrongUser123", Settings.ADMIN_PASSWORD)
    time.sleep(1) # Wait for error message
    
    # Verify the error message appears
    error_text = login_page.get_error_message()
    assert len(error_text) > 0, "Expected an error message, but none was found."

def test_invalid_password(driver):
    """Test Case 3: Wrong password should show an error message."""
    login_page = LoginPage(driver)
    login_page.open_url(Settings.BASE_URL.replace("/dashboard", "/login"))
    
    login_page.login(Settings.ADMIN_USERNAME, "WrongPass123")
    time.sleep(1)
    
    error_text = login_page.get_error_message()
    assert len(error_text) > 0, "Expected an error message, but none was found."

def test_empty_credentials(driver):
    """Test Case 4: Empty fields should show an error message."""
    login_page = LoginPage(driver)
    login_page.open_url(Settings.BASE_URL.replace("/dashboard", "/login"))
    
    # Send empty strings
    login_page.login("", "")
    time.sleep(1)
    
    # We should still be on the login page
    assert "login" in driver.current_url.lower(), "Empty credentials should not redirect."
