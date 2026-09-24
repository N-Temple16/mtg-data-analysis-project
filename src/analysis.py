import json
import pandas as pd

with open("data/AllPrintings.json", "r", encoding="utf-8") as file:
    printing_data = json.load(file)
    #sample = file.read(1000)

#with open("data/AllPrices.json", "r", encoding="utf-8") as file:
    #prices_data = json.load(file)

LTR_card_data = printing_data["data"]["LTR"]["cards"]

card_list = []

for card in LTR_card_data:
    card_dict = {
        "uuid": card["uuid"],
        "name": card["name"],
        "set": card["setCode"],
        "rarity": card["rarity"],
        "mana_value": card["manaValue"],
        "card_text": card.get("text", "N/A"),
        "keywords": card.get("keywords", []),
        "colours": card["colors"]
    }
    card_list.append(card_dict)

cards_df = pd.DataFrame(card_list)

print(cards_df["rarity"].value_counts())