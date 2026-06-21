from playwright.sync_api import Page

class DashboardPage:

    def __init__(self, page: Page):
        self.page = page

    # Verify dashboard page is displayed
    def verify_dashboard_loaded(self):
        assert "dashboard" in self.page.url, \
        f"Dashboard page not opened. Current URL: {self.page.url}" 