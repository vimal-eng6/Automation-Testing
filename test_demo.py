from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_google_search():
    print("Starting browser...")
    # Initialize the Chrome driver (Selenium Manager will handle the driver download automatically)
    driver = webdriver.Chrome()
    
    try:
        # Navigate to Google
        print("Navigating to Google...")
        driver.get("https://www.google.com")
        
        # Find the search box
        search_box = driver.find_element(By.NAME, "q")
        
        # Enter search text
        print("Searching for 'Selenium Python Automation'...")
        search_box.send_keys("Selenium Python Automation")
        search_box.submit()
        
        # Wait a moment for results to load
        time.sleep(3)
        
        # Verify title
        if "Selenium" in driver.title:
            print("✅ Test passed successfully! Selenium is working.")
        else:
            print("❌ Test failed or title did not match.")
            
    finally:
        # Close the browser
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    test_google_search()
