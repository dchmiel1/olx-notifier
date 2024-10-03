from twilio.rest import Client
from parser import OlxPageParser
from scraper import fetch_offers_page

# in this part you have to replace account_sid
# auth_token, twilio_number, recipient_number with your actual credential

account_sid = "ACa5f316db44cd623625218d50111b9e85"
auth_token = "d654ebff5a91021b065f68d255df1c7e"
twilio_number = "+13343103088"
recipient_number = "+48602460473"

# # Create Twilio client
# client = Client(account_sid, auth_token)

# # Send SMS
# # in body part you have to write your message
# message = client.messages.create(
#     body='This is a new message',
#     from_=twilio_number,
#     to=recipient_number
# )

# print(f"Message sent with SID: {message.sid}")


if __name__ == "__main__":
    page_html = fetch_offers_page()
    parser = OlxPageParser(page_html)
    offers = parser.retrieve_offers()
