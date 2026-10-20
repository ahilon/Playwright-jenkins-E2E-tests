import os
from dataclasses import dataclass

import playwright_jenkins_e2e.consts as Consts

@dataclass(frozen=True)
class Settings:
    username: str
    password: str
    token: str | None = None

    @classmethod
    def from_env(cls) -> "Settings":
        """
        Create a Settings instance from environment variables.
        returns: Settings instance.
        """
        username = os.getenv(Consts.ENV_USERNAME)
        password = os.getenv(Consts.ENV_PASSWORD)
        token = os.getenv(Consts.ENV_TOKEN, None)

        if username is None or password is None:
            raise ValueError(
                f"Environment variables {Consts.ENV_USERNAME} and {Consts.ENV_PASSWORD} must be set."
            )

        return cls(username=username, password=password, token=token)
