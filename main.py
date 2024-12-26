"Slack webhook for every working day at 11:10 AM"
import time
from datetime import datetime

from utils import check_date
from utils.logger import logger
from utils.settings import settings
from modules.hooking import slack_hooking

def main():
    log_msg = f"Start slack webhook at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    log_msg += f"\nSlack webhook url: {settings.slack_webhook_url}"
    logger.info(log_msg)

    while True:
        now = datetime.now()
        if now.hour == 9:
            if not check_date.is_working_day(now):
                logger.info(f"Today is not a working day: {now.strftime('%Y-%m-%d %H:%M:%S')}")
                time.sleep(60 * 60 * 24)  # 하루 뒤로 이동
                continue
        if not check_date.is_lunch_hour(now):
            logger.info(f"Not lunch hour: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            time.sleep(60 * 60 * 1)  # 1시간 뒤로 이동
            continue
        if not check_date.is_lunch_minute(now):
            logger.info(f"Not lunch minute: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            time.sleep(60)  # 1분 뒤로 이동
            continue
        logger.debug("It's time to send slack webhook")
        slack_hooking.send_lunch_webhook()
        time.sleep(60 * 60 * 20)  # 20시간 뒤로 이동


if __name__ == "__main__":
    main()
