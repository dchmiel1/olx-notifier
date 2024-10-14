import csv
import os


class Storage:
    def __init__(self, storage_file="known_offers.txt"):
        self.filename = storage_file

    def save_offers(self, offers):
        with open(self.filename, "a") as f:
            for offer in offers:
                f.write(str(offer) + "\n")

    def read_offers(self):
        with open(self.filename, "a+") as f:
            offers = f.readlines()
            for offer in offers:
                print(offer)

    def read_ids(self):
        if not os.path.isfile(self.filename):
            return []
        with open(self.filename, "r") as f:
            csvreader = csv.reader(f, delimiter=",", quotechar="|")
            ids = []
            for offer in csvreader:
                ids.append(offer[0])
        return ids
