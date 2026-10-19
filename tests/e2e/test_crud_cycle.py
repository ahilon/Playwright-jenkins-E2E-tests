import pytest

from playwright.sync_api import Page, expect

from playwright_jenkins_e2e.pages.job_page import JobPage


@pytest.mark.e2e
def test_crud_cycle(jenkins_page: Page) -> None:
    """
    Run the CRUD cycle test.
    args:
        page: Page instance to use for the test.
    returns: None
    """
    job_name = "simple_freestyle"
    echo_command = "Build Created"
    page = jenkins_page
    job_page = JobPage(page)
    created = False

    try:
        job_page.create_freestyle(job_name)
        created = True
        job_page.add_echo_build(echo_command)
        job_page.trigger_build(job_name)

        expect(page.get_by_text("Finished: SUCCESS")).to_be_visible()
        expect(page.get_by_text(echo_command)).to_be_visible()
    finally:
        if created:
            job_page.delete_project(job_name)
