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
        if not check_date.is_working_day(now):
            logger.info(
                f"Today is not a working day: {now.strftime('%Y-%m-%d %H:%M:%S')}"
            )
            next_working_day = check_date.get_next_working_day(now)
            next_lunch_time = check_date.get_next_lunch_time(next_working_day)
            time_diff = (next_lunch_time - now).total_seconds()
            logger.info(f"Sleeping for {time_diff/60} minutes")
            time.sleep(time_diff)
            continue
        if not check_date.is_lunch_hour(now):
            next_lunch_time = check_date.get_next_lunch_time(now)
            time_diff = (next_lunch_time - now).total_seconds()
            logger.info(f"Sleeping for {time_diff/60} minutes")
            time.sleep(time_diff)
            continue
        if not check_date.is_lunch_minute(now):
            next_lunch_time = check_date.get_next_lunch_time(now)
            time_diff = (next_lunch_time - now).total_seconds()
            logger.info(f"Sleeping for {time_diff/60} minutes")
            time.sleep(time_diff)
            continue
        logger.debug("It's time to send slack webhook")
        slack_hooking.send_lunch_webhook()
        next_working_day = check_date.get_next_working_day(now.replace(hour=13))
        next_lunch_time = check_date.get_next_lunch_time(next_working_day)
        time_diff = (next_lunch_time - now).total_seconds()
        logger.info(f"Sleeping for {time_diff/60} minutes")
        time.sleep(time_diff)


if __name__ == "__main__":
    main()
