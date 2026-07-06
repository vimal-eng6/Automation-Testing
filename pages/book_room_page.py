from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class BookRoomPage(BasePage):
    """Page Object for the Book Room module."""
    
    # Locators (Extracted directly from your React source code!)
    ROOM_CARD = (By.CLASS_NAME, "room-visual-card")
    START_TIME = (By.ID, "book-start")
    END_TIME = (By.ID, "book-end")
    NOTIFY_EMAILS = (By.ID, "cc-emails")
    KT_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
    KT_TOPIC = (By.ID, "kt-topic")
    KT_NOTES = (By.ID, "kt-notes")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert--success")
    ERROR_MESSAGE = (By.CLASS_NAME, "alert--error")

    def select_first_room(self):
        self.click_element(self.ROOM_CARD)

    def set_start_time(self, time_string):
        self._set_datetime_js(self.START_TIME, time_string)

    def set_end_time(self, time_string):
        self._set_datetime_js(self.END_TIME, time_string)

    def _set_datetime_js(self, locator, time_string):
        """Sets datetime-local value using JS to bypass browser formatting rules and trigger React state."""
        element = self.find_element(locator)
        self.driver.execute_script('''
            let elem = arguments[0];
            let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
            if (nativeSetter) {
                nativeSetter.call(elem, arguments[1]);
                elem.dispatchEvent(new Event('input', { bubbles: true }));
                elem.dispatchEvent(new Event('change', { bubbles: true }));
            }
        ''', element, time_string)

    def set_notify_emails(self, emails):
        self.input_text(self.NOTIFY_EMAILS, emails)
        
    def check_kt_session(self):
        self.click_element(self.KT_CHECKBOX)
        
    def set_kt_topic(self, topic):
        self.input_text(self.KT_TOPIC, topic)
        
    def set_kt_notes(self, notes):
        self.input_text(self.KT_NOTES, notes)

    def submit_booking(self):
        self.click_element(self.SUBMIT_BUTTON)
        
    def get_success_message(self):
        element = self.find_element(self.SUCCESS_MESSAGE)
        return element.text

    def get_error_message(self):
        element = self.find_element(self.ERROR_MESSAGE)
        return element.text
