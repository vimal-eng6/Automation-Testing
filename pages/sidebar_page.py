from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SidebarPage(BasePage):
    """
    Page Object Model for the Left Sidebar Navigation (Dashboard, Book Room, etc.).
    """
    # --- Locators ---
    # ⚠️ TODO: Update these locators using Inspect on the sidebar links
    DASHBOARD_LINK = (By.PARTIAL_LINK_TEXT, "Dashboard")
    BOOK_ROOM_LINK = (By.PARTIAL_LINK_TEXT, "Book Room")
    MY_BOOKINGS_LINK = (By.PARTIAL_LINK_TEXT, "My Bookings")
    IT_SUPPORT_LINK = (By.PARTIAL_LINK_TEXT, "IT Support")
    DIRECTORY_LINK = (By.PARTIAL_LINK_TEXT, "Directory")
    ANNOUNCEMENTS_LINK = (By.PARTIAL_LINK_TEXT, "Announcements")
    
    # --- Actions ---
    def click_dashboard(self):
        self.click_element(self.DASHBOARD_LINK)
        
    def click_book_room(self):
        self.click_element(self.BOOK_ROOM_LINK)
        
    def click_it_support(self):
        self.click_element(self.IT_SUPPORT_LINK)

    def is_it_support_visible(self):
        """Check if IT Support link is present on the page"""
        try:
            self.find_element(self.IT_SUPPORT_LINK)
            return True
        except:
            return False
