import yaml
import os

from pydantic import BaseSettings
from pydantic.env_settings import SettingsSourceCallable
from typing import Any
from pathlib import Path

BASE_DIR =  Path(os.getcwd())
CONFIG_FILE = Path.joinpath(BASE_DIR,"rdfogm_config.yml") 

def yml_config_setting(settings: BaseSettings) -> dict[str, Any]:
    print(CONFIG_FILE, flush=True )
    print(os.path.abspath(os.curdir), flush=True )
    with open(CONFIG_FILE) as f:
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
 