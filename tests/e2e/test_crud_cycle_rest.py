import pytest
import uuid

import httpx

from playwright_jenkins_e2e.jenkins_client import JenkinsClient

FREESTYLE_XML = """<?xml version='1.1' encoding='UTF-8'?>
<project>
  <description>Created via REST</description>
  <builders>
    <hudson.tasks.Shell><command>echo "Build Created"</command></hudson.tasks.Shell>
  </builders>
</project>"""

@pytest.mark.e2e
def test_crud_cycle_rest(jenkins_client: JenkinsClient) -> None:
    job_name = f"rest_job_{uuid.uuid4().hex[:8]}"
    jenkins_client.create_job(job_name, FREESTYLE_XML)
    try:
        response = jenkins_client.get_job(job_name)
        assert response.status_code == httpx.codes.OK
        assert response.json()["name"] == job_name
        assert response.json()["description"] == "Created via REST"
    finally:
        jenkins_client.delete_job(job_name)

    assert jenkins_client.get_job(job_name).status_code == httpx.codes.NOT_FOUND