import requests
from utils.settings import settings
from utils.logger import logger


class SlackHooking:
    def __init__(self):
        self.client = requests.Session()
        self.infos = self.prepare_infos()
        self.hansot_menu = "https://thesmartmind.slack.com/files/U03KDQN5JJ0/F086KKU2UR2/_______________________________2024-12-26_11.38.27.png"

    def prepare_infos(self) -> dict:
        url = settings.slack_webhook_url
        payload = {
            "channel": settings.slack_channel,
            "username": settings.slack_username,
            "text": "",
        }
        return {"url": url, "payload": payload}

    def test_slack_webhook(self):
        url = self.infos["url"]
        payload = self.infos["payload"]
        payload["text"] = "Test slack webhook"
        self.client.post(url, json=payload)
        logger.info("Test slack webhook sent")

    def send_lunch_webhook(self):
        # 텍스트 메시지 먼저 보내기
        url = self.infos["url"]
        payload = self.infos["payload"]
        text = f"<#C07TWKY2LSE> 점심시간 조사 시작합니다."
        text += f"\n11시 30분까지 스레드 작성해주세요~"
        payload["text"] = text

        res = self.client.post(url, json=payload)
        if res.status_code == 200:
            logger.info("Lunch slack webhook and file sent successfully")
        else:
            logger.error(f"Failed to upload file: {res.text}")


slack_hooking = SlackHooking()
