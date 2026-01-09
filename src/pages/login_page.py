from .base_page import BasePage

class LoginPage(BasePage):
    LOGIN_URL = "https://www.saucedemo.com/"

    def goto_login(self):
        self.goto(self.LOGIN_URL)

    def login(self, username: str, password: str):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def get_error_message(self):
        # SauceDemo error message is in a div[data-test="error-message-container"]
        return self.page.locator('[data-test="error"]').inner_text()

    def is_login_button_enabled(self):
        return self.page.get_by_role("button", name="Login").is_enabled()

    def is_password_masked(self):
        input_type = self.page.get_by_placeholder("Password").get_attribute("type")
        return input_type == "password"