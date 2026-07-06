import pytest
from selenium import webdriver
from config.settings import Settings

@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture that initializes the webdriver before each test
    and cleanly tears it down afterwards.
    """
    print("\nSetting up browser...")
    if Settings.BROWSER == "chrome":
        driver_instance = webdriver.Chrome()
    elif Settings.BROWSER == "firefox":
        driver_instance = webdriver.Firefox()
    elif Settings.BROWSER == "edge":
        driver_instance = webdriver.Edge()
    else:
        raise ValueError(f"Browser {Settings.BROWSER} is not supported.")
        
    driver_instance.maximize_window()
    
    # Pass the driver to the test function
    yield driver_instance
    
    # Teardown after test completes
    print("\nClosing browser...")
    driver_instance.quit()
