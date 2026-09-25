import json
import pandas as pd

# Loaded from AllPrintings.json file from mtgjson.com 
"""with open("data/AllPrintings.json", "r", encoding="utf-8") as file:
    printing_data = json.load(file)
"""
# Loaded from AllPrices.json file from mtgjson.com
with open("data/AllPrices.json", "r", encoding="utf-8") as file:
    prices_data = json.load(file)


cards_list = []
prices_list = []

"""for _, set_data in printing_data["data"].items():
    if "cards" in set_data:
        for card in set_data["cards"]:
            cards_list.append({
                "uuid": card["uuid"],
                "name": card["name"],
                "set": card["setCode"],
                "rarity": card["rarity"],
                "mana_value": card["manaValue"],
                "card_text": card.get("text", "N/A"),
                "keywords": card.get("keywords", []),
                "colours": card["colors"]
            })

cards_df = pd.DataFrame(cards_list)"""

#first_uuid = list(prices_data["data"].keys())[2]
printing_details = {}

for id in prices_data["data"].keys():
    uuid_data = prices_data["data"][id]
    if "paper" in uuid_data:
        paper_data = uuid_data["paper"]
        if "tcgplayer" in paper_data:
            tcgplayer_data = paper_data["tcgplayer"]
            if "retail" in tcgplayer_data:
                for printing_type in tcgplayer_data["retail"].keys():
                    if printing_type not in printing_details:
                        printing_details[printing_type] = 0
                    printing_details[printing_type] += 1
        
print(printing_details)
#print(prices_data["data"][first_uuid]["paper"]["tcgplayer"]["retail"].keys())
#print(prices_data["data"][first_uuid]["paper"]["tcgplayer"]["retail"]["normal"])