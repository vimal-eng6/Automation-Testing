import time
from pages.login_page import LoginPage
from pages.sidebar_page import SidebarPage
from config.settings import Settings

def test_admin_sees_all_modules(driver):
    """Test Case: Admin should see IT Support link in the sidebar"""
    # 1. Login as Admin
    login_page = LoginPage(driver)
    login_page.open_url(Settings.BASE_URL.replace("/dashboard", "/login"))
    login_page.login(Settings.ADMIN_USERNAME, Settings.ADMIN_PASSWORD)
    time.sleep(2)
    
    # 2. Check Sidebar
    sidebar = SidebarPage(driver)
    assert sidebar.is_it_support_visible() == True, "Admin should be able to see IT Support"

def test_regular_user_sidebar(driver):
    """Test Case: Regular User SHOULD see the IT Support link in the sidebar"""
    # 1. Login as Regular User
    login_page = LoginPage(driver)
    login_page.open_url(Settings.BASE_URL.replace("/dashboard", "/login"))
    login_page.login(Settings.REGULAR_USERNAME, Settings.REGULAR_PASSWORD)
    time.sleep(2)
    
    # 2. Check Sidebar
    sidebar = SidebarPage(driver)
    assert sidebar.is_it_support_visible() == True, "Regular user should be able to see IT Support"
