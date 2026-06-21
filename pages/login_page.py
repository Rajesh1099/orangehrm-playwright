from playwright.sync_api import Page, expect

# Login Page class
class LoginPage:

    def __init__(self, page: Page):

        self.page = page

        #locators
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button",name="Login")
        self.user_dropdown = page.locator(".oxd-userdropdown-tab")
        self.logout_link = page.get_by_role("menuitem", name="Logout")

    # Open login page
    def navigate(self):

        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Perform login
    def login(self, username, password):

        self.username.fill(username)

        self.password.fill(password)

        with self.page.expect_navigation():
            self.login_button.click()

    #LogOut
    def logout(self):
        self.user_dropdown.click()
        self.logout_link.click()    

    def verify_logout_successful(self):
        expect(self.login_button).to_be_visible()
        assert "login" in self.page.url.lower(), \
        f"Logout failed. Current URL: {self.page.url}"     