import time
from datetime import datetime, timedelta
from pages.login_page import LoginPage
from pages.sidebar_page import SidebarPage
from pages.book_room_page import BookRoomPage
from config.settings import Settings

def test_successful_room_booking(driver):
    """Test Case: Book a room successfully."""
    # 1. Login
    login_page = LoginPage(driver)
    login_page.open_url(Settings.BASE_URL.replace("/dashboard", "/login"))
    login_page.login(Settings.REGULAR_USERNAME, Settings.REGULAR_PASSWORD)
    time.sleep(2)
    
    # 2. Navigate to Book Room
    sidebar = SidebarPage(driver)
    sidebar.click_book_room()
    time.sleep(2) # Wait for page to load
    
    # 3. Fill out the booking form
    book_page = BookRoomPage(driver)
    book_page.select_first_room()
    
    # Calculate a date 7 days in the future to avoid conflicts
    future_start = datetime.now() + timedelta(days=7)
    future_end = future_start + timedelta(hours=1)
    
    # Set the start and end times (Format: YYYY-MM-DDTHH:MM)
    book_page.set_start_time(future_start.strftime("%Y-%m-%dT%H:%M"))
    book_page.set_end_time(future_end.strftime("%Y-%m-%dT%H:%M"))
    
    # Add CC emails
    book_page.set_notify_emails("test_automation@company.com")
    
    book_page.submit_booking()
    time.sleep(1) # Wait for server response
    
    # 4. Verify success message
    try:
        success_msg = book_page.get_success_message()
        assert "successfully" in success_msg.lower(), "Booking was not successful."
    except Exception:
        # If success message doesn't appear, let's catch the error message!
        error_msg = book_page.get_error_message()
        assert False, f"Booking failed on the website with error: {error_msg}"
