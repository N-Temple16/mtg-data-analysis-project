import pandas as pd

result_df = pd.read_csv("data/mtg_analysis.csv")
result_df = result_df[result_df["rarity"] != "special"]

#pd.set_option("display.max_columns", None)
#print(result_df.head(6))

#print("Cards $5 and above", len(result_df[result_df["price"] >= 5]))
#print("Cards $10 and above", len(result_df[result_df["price"] >= 10]))
#print("Cards $20 and above", len(result_df[result_df["price"] >= 20]))
#print("Cards $50 and above", len(result_df[result_df["price"] >= 50]))
#print("Cards $100 and above", len(result_df[result_df["price"] >= 100]))
#print("Cards $500 and above", len(result_df[result_df["price"] >= 500]))

expensive_cards = result_df[result_df["price"] >= 50]

# Analyze Rarity vs Price
total = result_df.groupby("rarity")["price"].count()
expensive = expensive_cards.groupby("rarity")["price"].count()
percentage = (expensive / total) * 100

all_cards = result_df.groupby("rarity")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
#print(all_cards)
#print()


higher_tier_cards = expensive_cards.groupby("rarity")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
#print(higher_tier_cards)
#print()


expense_percentage = pd.DataFrame({
    "total": total,
    "$50+": expensive,
    "% $50+": percentage,
})
#print(expense_percentage)
#print()

#expensive_commons = expensive_cards[expensive_cards["rarity"] == "common"]
#print(expensive_commons[["name", "set", "price"]])


# Analyze Mana Value vs Price
all_mana_values = result_df.groupby("mana_value")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
#print(all_mana_values)
#print()


higher_tier_mana_values = expensive_cards.groupby("mana_value")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
#print(higher_tier_mana_values)
#print()


# Analyze Colours vs Price
all_colours = result_df.groupby("colours")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
#print(all_colours)
#print()


higher_tier_colours = expensive_cards.groupby("colours")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
#print(higher_tier_colours)
#print()


# Analyze Keywords vs Price
all_keywords = result_df.groupby("keywords")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
print(all_keywords)
print()


higher_tier_keywords = expensive_cards.groupby("keywords")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
print(higher_tier_keywords)
#print()


# Analyze Card Text (for cards with no keywords) vs Price


# Analyze Set (potential reprints as well) vs Price