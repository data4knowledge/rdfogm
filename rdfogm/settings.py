from pydantic import BaseSettings

class Settings(BaseSettings):
    triple_store_protocol: str = "https"
    triple_store_host: str = "localhost"
    triple_store_port: str = "3030"
    triple_store_dataset: str = "test"
    default_graph: str = "http://www.example.com/default"

    class Config:
        env_file = ".env"