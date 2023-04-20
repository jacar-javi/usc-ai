from pydantic import BaseSettings

class Settings(BaseSettings):
    qdrant_host: str = "localhost"
    qdrant_port: int = 6333
    openai_api_key: str

    class Config:
        env_file = ".env"


settings = Settings()