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

# Mana Values of all cards range from 0 to 1,000,000 
# (0.5, 1,000,000, and some cards from other mana values in between are gimmicks from un-sets)
# From both the entire card set as well as just the expensive cards, mana values 0 to 4 have the most printings for the most part
# It can be more seen in the expensive card set but the average price per mana value steadily decreases as the mana value goes up
# Expensive mana values only range from 0 to 12


# Analyze Colours vs Price
result_df["colours"] = result_df["colours"].apply(
    lambda colours: str(sorted(ast.literal_eval(colours)))
)

all_colours = result_df.groupby("colours")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
#print(all_colours.sort_values(by=["mean", "median"], ascending=False))
#print()


higher_tier_colours = expensive_cards.groupby("colours")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
#print(higher_tier_colours.sort_values(by=["mean", "median"], ascending=False))
#print()

# In both the whole data set and the expensive cards only, colourless cards have the highest count and next comes monocoloured cards
# however the monocoloured cards have different orders in each table
# Looking at the mean (average) price for expensive card colours, colourless cards still lead the category followed by all the monocoloured cards
# with a mix of [G, U], [B, R, U] and [U, W] in between. The least expensive colour pairing in this category is [B, G, U, W]


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
#print(all_keywords.sort_values(by=["mean", "median"], ascending=False))
#print()


higher_tier_keywords = expensive_keywords.groupby("keywords")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
#print(higher_tier_keywords.sort_values(by=["mean", "median"], ascending=False))
#print()


keyword_percentage = pd.DataFrame({
    "total": total_keywords,
    "$50+": exp_keywords,
    "% $50+": perc,
})
#print(keyword_percentage.sort_values(by="% $50+", ascending=False))
#print()

# A similarity between the counts of both the whole data set and the expensive cards is that they each start with Flying, Enchant and Trample
# Looking at mean (average) prices, for the whole data set the top 3 keywords are from cards that have only ever been printed a single time
# The average price of expensive cards come from mostly common keywords but cards printed with assumingly high scarcity


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
#print(all_no_keywords.sort_values(by="mean", ascending=False))
#print()


higher_tier_no_keywords = expensive_no_keywords.groupby("card_text")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
#print(higher_tier_no_keywords.sort_values(by="mean", ascending=False))
#print()

# Both the whole data set and the expensive cards have the same top 3 cards when looking at the average price
# They also have the same count being (4, 1, 1) respectively which shows the rarity/scarcity of the top cards


# Analyze Set (potential reprints as well) vs Price
all_sets = result_df.groupby("set_code")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
print(all_sets.sort_values(by="mean", ascending=False))
print()


higher_tier_sets = expensive_cards.groupby("set_code")["price"].agg(
    count="count", 
    median="median", 
    mean="mean", 
    max="max",
)
print(higher_tier_sets.sort_values(by="mean", ascending=False))
#print()


# Looking at the count of cards in each set within the whole data set, PLST (The List) and SLD (Secret Lair Drop) are the top 2 and are both technically not sets
# This is then followed by 3 commander focused sets with CMM (Commander Masters), CLB (Commander Legends: Battle for Baldur's Gate) and MSC (Marvel Super Heroes Commander)
# Comparing that to the expensive data set, the top sets are either the first magic sets printed like LEA (Limited Edition Alpha), LEB (Limited Edition Beta)
# 2ED (Unlimited Edition), SLD (Secret Lair Drop) again as the printings alawys come with rarity since they are primarily printed only once
# Or 30A 30th Anniversary Edition) which is an anniversary set with reprints of a lot of very expensive older cards

# Then looking at the average price of sets, both with the whole data set and the expensive set, the leaders are promotional sets with very very scarce printings
# In some cases sets only contain 1-5 cards that are only printed once or a handfull of times which brings the price up dramatically
# These 3 sets appear in the top 3 in both data sets, each in a different order: PGRU (Guru), PPRO (Pro Tour Promos) and PF25 (MagicFest 2025)