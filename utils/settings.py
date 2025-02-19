from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    slack_webhook_url: str = Field(default="", env="SLACK_WEBHOOK_URL")
    slack_username: str = Field(default="lunch-bot", env="SLACK_USER_NAME")
    slack_channel: str = Field(default="맛점", env="SLACK_CHANNEL")
    logger_level: str = Field(default="INFO", env="LOGGER_LEVEL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
