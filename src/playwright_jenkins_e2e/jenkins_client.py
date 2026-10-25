from urllib.parse import quote

import httpx

import playwright_jenkins_e2e.consts as Consts


class JenkinsClient:
    def __init__(self, base_url: str, username: str, api_token: str):
        self._http = httpx.Client(
            base_url=base_url.rstrip("/"),
            auth=(username, api_token),
            timeout=Consts.JENKINS_TIMEOUT,
            follow_redirects=True,
        )

    def create_job(self, name: str, config_xml: str) -> None:
        response = self._http.post(
            "/createItem",
            params={"name": name},
            content=config_xml,
            headers={"Content-Type": "application/xml"},
        )
        response.raise_for_status()

    def delete_job(self, name: str) -> None:
        path = quote(name, safe="")
        response = self._http.post(f"/job/{path}/doDelete")
        response.raise_for_status()

    def close(self) -> None:
        self._http.close()

    def get_job(self, name: str) -> httpx.Response:
        return self._http.get(f"/job/{quote(name, safe='')}/api/json")
