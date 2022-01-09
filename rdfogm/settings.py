import yaml

from pydantic import BaseSettings
from pydantic.env_settings import SettingsSourceCallable
from typing import Any

def yml_config_setting(settings: BaseSettings) -> dict[str, Any]:
    with open("rdfogm_config.yml") as f:
        return yaml.safe_load(f)

class Settings(BaseSettings):
    environment: str = "development"
    rdf_types: dict = {}
    protocol = "http"
    host = "localhost"
    port = "3030"
    dataset = "test"
    default_graph = "http://www.data4knowledge.dk/default"

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
 