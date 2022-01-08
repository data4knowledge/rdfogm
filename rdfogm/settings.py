import yaml

from pydantic import BaseSettings
from pydantic.env_settings import SettingsSourceCallable
from typing import Any


def yml_config_setting(settings: BaseSettings) -> dict[str, Any]:
    with open("config.yml") as f:
        return yaml.safe_load(f)

class Settings(BaseSettings):
    triple_store_protocol: str = "https"
    triple_store_host: str = "localhost"
    triple_store_port: str = "3030"
    triple_store_dataset: str = "test"
    default_graph: str = "http://www.example.com/default"
    rdf_types: dict = {}

    class Config:
        env_file = ".env"

        @classmethod
        def customise_sources(
            cls,
            init_settings: SettingsSourceCallable,
            env_settings: SettingsSourceCallable,
            file_secret_settings: SettingsSourceCallable,
        ) -> tuple[SettingsSourceCallable, ...]:
            # Add load from yml file, change priority and remove file secret option
            return init_settings, yml_config_setting, env_settings
 