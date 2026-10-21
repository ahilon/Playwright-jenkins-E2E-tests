from playwright.sync_api import Page
import playwright_jenkins_e2e.consts as Consts


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def login(
            self,
            username: str,
            password: str,
            login_page: str = Consts.LOGIN_PAGE
            ) -> None:
        """login to the Jenkins application.
        args:
            username: The username to use for login. Default is Consts.DEFAULT_USERNAME.
            password: The password to use for login. Default is Consts.DEFAULT_PASSWORD.
            login_page: The URL of the login page. Default is Consts.LOGIN_PAGE.
        returns: None"""
        self.page.goto(login_page)
        self.page.get_by_label("Username").fill(username)
        self.page.get_by_label("Password").fill(password)
        self.page.get_by_role("button", name="Sign in").click()
