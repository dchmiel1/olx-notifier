import schedule

from parser import OlxPageParser
from scraper import fetch_offers_page
from sms import SMSClient
from storage import Storage
from time import sleep


def retrieve_new_offers(offers, old_ids):
    new_offers = []
    for offer in offers:
        if offer.id not in old_ids:
            new_offers.append(offer)
    return new_offers


def check_for_updates():
    page_html = fetch_offers_page()
    offers = OlxPageParser(page_html).retrieve_offers()
    storage = Storage()
    sms_client = SMSClient()
    ids = storage.read_ids()

    offers = retrieve_new_offers(offers, ids)
    print("New offers: ", len(offers))
    sms_client.notify_about_new_offers(offers)
    storage.save_offers(offers)


if __name__ == "__main__":
    check_for_updates()
    schedule.every(10).minutes.do(check_for_updates)

    while True:
        schedule.run_pending()
        n = schedule.idle_seconds()
        sleep(n)
