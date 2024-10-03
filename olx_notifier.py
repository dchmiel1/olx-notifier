from twilio.rest import Client
from parser import OlxPageParser
from scraper import fetch_offers_page
from storage import Storage

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

def retrieve_new_offers(offers, old_ids):
    new_offers = []
    for offer in offers:
        if offer.id not in old_ids:
            new_offers.append(offer)
    return new_offers

if __name__ == "__main__":
    page_html = fetch_offers_page()
    offers = OlxPageParser(page_html).retrieve_offers()
    storage = Storage()
    ids = storage.read_ids()

    offers = retrieve_new_offers(offers, ids)
    print(len(offers))
    storage.save_offers(offers)