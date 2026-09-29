import pandas as pd

result_df = pd.read_csv("data/mtg_analysis.csv")

pd.set_option("display.max_columns", None)
print(result_df.head(6))

# Analyze Rarity vs Price


# Analyze Mana Value vs Price


# Analyze Colours vs Price


# Analyze Keywords vs Price


# Analyze Card Text (for cards with no keywords) vs Price


# Analyze Set (potential reprints as well) vs Price