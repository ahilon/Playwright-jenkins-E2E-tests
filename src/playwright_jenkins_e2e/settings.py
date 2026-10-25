import os
from dataclasses import dataclass

from dotenv import load_dotenv

import playwright_jenkins_e2e.consts as Consts


@dataclass(frozen=True)
class Settings:
    username: str
    password: str
    url: str
    token: str | None = None

    @classmethod
    def from_env(cls) -> "Settings":
        """
        Create a Settings instance from environment variables.
        returns: Settings instance.
        """
        # load the environment variables from the .env file
        load_dotenv()
        username = os.getenv(Consts.ENV_USERNAME)
        password = os.getenv(Consts.ENV_PASSWORD)
        token = os.getenv(Consts.ENV_TOKEN, None)
        url = os.getenv(Consts.ENV_URL)

        if username is None or password is None:
            raise ValueError(
                f"Environment variables {Consts.ENV_USERNAME} and {Consts.ENV_PASSWORD} must be set."
            )
        if url is None:
            raise ValueError(f"Environment variable {Consts.ENV_URL} must be set.")

        return cls(username=username, password=password, url=url, token=token)
