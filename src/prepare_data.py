import json
import pandas as pd

# Loaded from AllPrintings.json file from mtgjson.com 
with open("data/AllPrintings.json", "r", encoding="utf-8") as file:
    printing_data = json.load(file)

# Loaded from AllPrices.json file from mtgjson.com
with open("data/AllPrices.json", "r", encoding="utf-8") as file:
    prices_data = json.load(file)

cards_list = []
prices_list = []


for _, set_data in printing_data["data"].items():
    if "cards" in set_data:
        for card in set_data["cards"]:
            if "nonfoil" in card["finishes"]:
                cards_list.append({
                    "uuid": card["uuid"],
                    "name": card["name"],
                    "set_code": card["setCode"],
                    "set_name": set_data["name"],
                    "rarity": card["rarity"],
                    "mana_value": card["manaValue"],
                    "card_text": card.get("text", "N/A"),
                    "keywords": card.get("keywords", []),
                    "colours": card["colors"],
                    "finishes": card["finishes"]
                })

cards_df = pd.DataFrame(cards_list)


for id in prices_data["data"].keys():
    uuid_data = prices_data["data"][id]
    if "paper" in uuid_data:
        paper_data = uuid_data["paper"]
        if "tcgplayer" in paper_data:
            tcgplayer_data = paper_data["tcgplayer"]
            if "retail" in tcgplayer_data:
                if "normal" in tcgplayer_data["retail"]:
                    normal_prices = tcgplayer_data["retail"]["normal"]
                    latest_date = max(normal_prices.keys())
                    prices_list.append({
                        "uuid": id,
                        "price": normal_prices[latest_date],
                        "price_date": latest_date
                    })

prices_df = pd.DataFrame(prices_list)

result_df = pd.merge(cards_df, prices_df, on="uuid", how="inner")

#missing_uuids = set(prices_df["uuid"]) - set(cards_df["uuid"])
#pd.set_option("display.max_columns", None)
#print(result_df.head(6))

result_df.to_csv("data/mtg_analysis.csv", index=False)

