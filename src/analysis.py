import ast
import sys
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")

result_df = pd.read_csv("data/mtg_analysis.csv")
result_df["keywords"] = result_df["keywords"].apply(ast.literal_eval)
result_df = result_df[result_df["rarity"] != "special"]

pd.set_option("display.max_columns", None)
#print(result_df.head(6))

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

# Started with 85,841 records
# common - 26620
# uncommon - 22515
# rare - 30079
# mythic - 6627

# 3,272 cards worth over $20
# common - 207 - 0.78% of total commons
# uncommon - 366 - 1.63% of total uncommons
# rare - 1709 - 5.68% of total rares
# mythic - 990 - 14.94% of total mythics

# 1117 cards worth over $50
# common - 52 - 0.20% of total commons
# uncommon - 177 - 0.79% of total uncommons
# rare - 638 - 2.12% of total rares
# mythic - 250 - 3.77% of total mythics


# Analyze Mana Value vs Price
all_mana_values = result_df.groupby("mana_value")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
print(all_mana_values)
print()


higher_tier_mana_values = expensive_cards.groupby("mana_value")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
print(higher_tier_mana_values)
print()

# Mana Values of all cards range from 0 to 1,000,000 
# (0.5, 1,000,000, and other mana values in between are gimmicks from un-sets)


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
keywords_df = result_df.explode("keywords")
expensive_keywords = keywords_df[keywords_df["price"] >= 50]

total_keywords = keywords_df.groupby("keywords")["price"].count()
exp_keywords = expensive_keywords.groupby("keywords")["price"].count()
exp_keywords = exp_keywords.reindex(total_keywords.index, fill_value=0)
perc = (exp_keywords / total_keywords) * 100

all_keywords = keywords_df.groupby("keywords")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
#print(all_keywords.sort_values(by="count", ascending=False))
#print()


higher_tier_keywords = expensive_keywords.groupby("keywords")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
#print(higher_tier_keywords.sort_values(by="count", ascending=False))
#print()


keyword_percentage = pd.DataFrame({
    "total": total_keywords,
    "$50+": exp_keywords,
    "% $50+": perc,
})
#print(keyword_percentage.sort_values(by="% $50+", ascending=False))
#print()


# Analyze Card Text (for cards with no keywords) vs Price
no_keyword_cards = keywords_df[
    (keywords_df["keywords"].isna()) & 
    (keywords_df["card_text"] != "N/A")
]
expensive_no_keywords = no_keyword_cards[no_keyword_cards["price"] >= 50]


all_no_keywords = no_keyword_cards.groupby("card_text")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
#print(all_no_keywords.sort_values(by="count", ascending=False))
#print()


higher_tier_no_keywords = expensive_no_keywords.groupby("card_text")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
#print(higher_tier_no_keywords.sort_values(by="count", ascending=False))
#print()


# Analyze Set (potential reprints as well) vs Price
all_sets = result_df.groupby("set_code")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
#print(all_sets.sort_values(by="count", ascending=False))
#print()


higher_tier_sets = expensive_cards.groupby("set_code")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
#print(higher_tier_sets.sort_values(by="count", ascending=False))
#print()
