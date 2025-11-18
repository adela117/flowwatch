from pydantic import BaseSettings

class Settings(BaseSettings):
  app_name: str = "Flowwatch"
  environment: str = "development"
  database_url: str = "sqlite+aiosqlite:///./flowwatch.db"

class Config:
  env_file = ".env"

settings = Settings()
