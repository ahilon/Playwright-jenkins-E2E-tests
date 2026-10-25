from playwright.sync_api import Page

import playwright_jenkins_e2e.consts as Consts


class JobPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def create_freestyle(self, freestyle_name: str):
        """
        Create a new freestyle project.
        args:
            freestyle_name: The name of the freestyle project to create.
        returns: None
        """
        self.page.get_by_role("link", name="New Item").click()
        self.page.get_by_role("textbox", name="Enter an item name").fill(freestyle_name)
        self.page.get_by_text("Freestyle projectClassic,").click()
        self.page.get_by_role("radio", name="Freestyle project Classic,").check()
        self.page.get_by_role("button", name="OK").click()

    def add_echo_build(self, command: str) -> None:
        """
        Add an echo build step.
        args:
            command: The command to execute.
        returns: None
        """
        self.page.get_by_role("button", name="Add build step").click()
        self.page.get_by_role("button", name="Execute shell").click()
        self.page.locator("section").filter(
            has_text="Build Steps Automate your"
        ).get_by_role("textbox").fill(f'echo "{command}"')
        self.page.get_by_role("button", name="Save").click()

    def trigger_build(self, freestyle_name: str) -> None:
        """
        Trigger a build for the specified freestyle project.
        args:
            freestyle_name: The name of the freestyle project for which to trigger a build.
        returns: None
        """
        self.page.get_by_role("link", name="Build Now").click()
        self.page.locator("#jenkins-build-history").get_by_role("link").first.wait_for()
        self.page.goto(f"{Consts.JOB_PAGE}/{freestyle_name}/lastBuild/console")

    def delete_project(self, project_name: str) -> None:
        """
        Delete the specified project.
        args:
            project_name: The name of the project to delete.
        returns: None
        """
        self.page.get_by_role("link", name="Jenkins", exact=True).click()
        self.page.get_by_role("link", name=project_name, exact=True).click()
        self.page.get_by_role("link", name="Delete Project", exact=True).click()
        self.page.get_by_role("button", name="Yes", exact=True).click()
