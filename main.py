from src.prepare_data import prepare_data
from src.analysis import clean_data


def generate_csv(result_df):
    result_df.to_csv("data/mtg_analysis.csv", index=False)

def generate_keyword_csv(result_df):
    keywords_df = result_df.explode("keywords")
    keywords_df.to_csv("data/mtg_keywords_analysis.csv", index=False)


def main():
    print("Processing raw JSON data into clean CSV. This may take a couple of minutes.")
    result_df = prepare_data()

    print("Filtering and organizing data.")
    result_df = result_df[result_df["rarity"] != "special"]
    result_df = clean_data(result_df)

    generate_csv(result_df)
    generate_keyword_csv(result_df)

    print("CSV data is now ready for Power BI!")

if __name__ == "__main__":
    main()