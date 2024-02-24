import os

import yaml
from pydantic import EmailStr, PostgresDsn
from pydantic_settings import BaseSettings

yaml_settings = dict()

pwd = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(pwd, ".../settings.yaml")) as f:
    yaml_settings.update(yaml.load(f, yaml.FullLoader))


class AppSettings(BaseSettings):
    app_name: str = "FastAPI Demo"


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: PostgresDsn


# TODO: Env vars should override the values from the settings file
env = os.getenv("ENV", "dev")
settings = Settings(**yaml_settings[env])
appsettings = AppSettings()
