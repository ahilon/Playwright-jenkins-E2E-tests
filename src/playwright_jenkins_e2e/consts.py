from typing import Final

PORT = "8080"
LOCAL_HOST: Final[str] = f"http://localhost:{PORT}"
LOGIN_PAGE: Final[str] = f"{LOCAL_HOST}/login"
JOB_PAGE: Final[str] = f"{LOCAL_HOST}/job"
ENV_USERNAME: Final[str] = "JENKINS_USER"
ENV_PASSWORD: Final[str] = "JENKINS_PASSWORD"
ENV_TOKEN: Final[str] = "JENKINS_TOKEN"