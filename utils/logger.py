import logging
from emoji_logger import Logger

from utils.settings import settings

logger = Logger(
    name="slack-lunch-webhook",
    level=settings.logger_level,
    is_save=False
)
