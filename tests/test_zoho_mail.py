import time
from pages.zoho_mail_page import ZohoMailPage
from config.settings import Settings

def test_tc001_valid_login(driver):
    """TC_001: Valid login - Enter valid email + password -> User logs in successfully"""
    print("Running TC_001: Valid Login...")
    driver.get(Settings.BASE_URL)
    
    zoho_page = ZohoMailPage(driver)
    zoho_page.login(Settings.ADMIN_USERNAME, Settings.ADMIN_PASSWORD)
    
    # Wait for the redirect to complete
    time.sleep(5)
    
    current_url = driver.current_url.lower()
    print(f"Current URL: {driver.current_url}")
    
    # Assert successful login redirect
    assert "mail" in current_url or "zm" in current_url or "accounts.zoho" not in current_url, "TC_001 Failed: Did not reach Zoho Mail dashboard."
    print("✅ TC_001 Passed: Valid login successful.")

def test_tc002_invalid_email(driver):
    """TC_002: Invalid email - Enter wrong email -> Error message shown"""
    print("Running TC_002: Invalid Email...")
    driver.get(Settings.BASE_URL)
    
    zoho_page = ZohoMailPage(driver)
    zoho_page.enter_username("invalid_user_test_999999@caldimengg.in")
    
    error_text = zoho_page.get_error_message()
    print(f"Error displayed: '{error_text}'")
    
    assert "cannot be found" in error_text.lower(), f"TC_002 Failed: Unexpected or missing error message. Got: {error_text}"
    print("✅ TC_002 Passed: Invalid email error displayed correctly.")

def test_tc003_invalid_password(driver):
    """TC_003: Invalid password - Enter correct email + wrong password -> Error message shown"""
    print("Running TC_003: Invalid Password...")
    driver.get(Settings.BASE_URL)
    
    zoho_page = ZohoMailPage(driver)
    zoho_page.enter_username(Settings.ADMIN_USERNAME)
    zoho_page.enter_password("WrongPassword123!")
    
    time.sleep(1.5)
    error_text = zoho_page.get_error_message()
    print(f"Error displayed: '{error_text}'")
    
    assert "incorrect password" in error_text.lower(), f"TC_003 Failed: Unexpected or missing error message. Got: {error_text}"
    print("✅ TC_003 Passed: Incorrect password error displayed correctly.")

def test_tc004_empty_fields(driver):
    """TC_004: Empty fields - Click login without data -> Validation message shown"""
    print("Running TC_004: Empty Fields...")
    driver.get(Settings.BASE_URL)
    
    zoho_page = ZohoMailPage(driver)
    zoho_page.click_next_only()
    
    time.sleep(1)
    error_text = zoho_page.get_error_message()
    print(f"Error displayed: '{error_text}'")
    
    assert "enter your email" in error_text.lower(), f"TC_004 Failed: Unexpected or missing error message. Got: {error_text}"
    print("✅ TC_004 Passed: Empty email validation message displayed correctly.")

def test_tc005_forgot_password(driver):
    """TC_005: Forgot password - Click forgot password -> Reset page opens"""
    print("Running TC_005: Forgot Password...")
    driver.get(Settings.BASE_URL)
    
    zoho_page = ZohoMailPage(driver)
    zoho_page.enter_username(Settings.ADMIN_USERNAME)
    zoho_page.click_forgot_password()
    
    time.sleep(2)
    current_url = driver.current_url.lower()
    print(f"Current URL: {driver.current_url}")
    
    assert "password" in current_url, "TC_005 Failed: Did not reach the password reset page."
    print("✅ TC_005 Passed: Forgot Password redirect successful.")

def test_zoho_send_email(driver):
    """Test Case: Log in to Zoho Mail, compose, and send a test email."""
    print("Navigating to Zoho Mail...")
    driver.get(Settings.BASE_URL)
    
    zoho_page = ZohoMailPage(driver)
    
    print(f"Logging in as {Settings.ADMIN_USERNAME}...")
    zoho_page.login(Settings.ADMIN_USERNAME, Settings.ADMIN_PASSWORD)
    
    # Wait for the dashboard to load fully
    print("Waiting for main mail application to load...")
    time.sleep(15)
    
    recipient = "SURYA.SELVAKUMAR@CALDIMENGG.IN"
    subject = "SAMPLE TEST MAIL"
    body = "Hi Surya,\n\nThis is a sample test email sent automatically via Selenium Python automation.\n\nBest regards,\nAutomation Bot"
    
    print(f"Composing and sending email to {recipient}...")
    zoho_page.compose_and_send_email(recipient, subject, body)
    
    print("✅ Email sent successfully!")
