from typing import Final

PORT = "8080"
LOCAL_HOST: Final[str] = f"http://localhost:{PORT}"
LOGIN_PAGE: Final[str] = f"{LOCAL_HOST}/login"
JOB_PAGE: Final[str] = f"{LOCAL_HOST}/job"
DEFAULT_USERNAME: Final[str] = "testuser"
DEFAULT_PASSWORD: Final[str] = "testpass123"