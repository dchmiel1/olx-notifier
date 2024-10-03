from twilio.rest import Client
from requests import get

account_sid = "ACa5f316db44cd623625218d50111b9e85"
auth_token = "d654ebff5a91021b065f68d255df1c7e"
twilio_number = "+13343103088"
recipient_number = "+48602460473"
# ScrapyCloud.123@


class SMSClient:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, msg):
        message = self.client.messages.create(
            body=msg,
            from_=twilio_number,
            to=recipient_number,
        )
        print(f"Message sent with SID: {message.sid} - {msg}")

    def notify_about_new_offers(self, offers):
        if len(offers) == 0:
            return
        msg = "\n"

        for i, offer in enumerate(offers):
            msg += f"{str(i+1)}. {offer.name}, {offer.loc}, {offer.img}\n"
        self.send_sms(msg)
