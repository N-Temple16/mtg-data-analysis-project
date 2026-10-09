from src.prepare_data import prepare_data
from src.analysis import clean_data

def generate_csv(result_df):
    result_df.to_csv("data/mtg_analysis.csv", index=False)

def main():
    print("Processing raw JSON data into clean CSV. This may take a couple of minutes.")
    result_df = prepare_data()

    print("Filtering and organizing data.")
    result_df = clean_data(result_df)
    generate_csv(result_df)

    print("Power BI data is now ready!")

if __name__ == "__main__":
    main()