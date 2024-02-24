import os

import yaml
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings

yaml_settings = {}

pwd = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(pwd, ".../settings.yaml")) as f:
    yaml_settings.update(yaml.safe_load(f))


class AppSettings(BaseSettings):
    """
    Represents the application settings.
    """

    app_name: str = "FastAPI Demo"


class Settings(BaseSettings):
    """
    Represents the settings for the application.
    """

    SQLALCHEMY_DATABASE_URI: PostgresDsn


# TODO: Env vars should override the values from the settings file
env = os.getenv("ENV", "dev")
settings = Settings(**yaml_settings[env])
appsettings = AppSettings()
