from src.prepare_data import prepare_data
#from src.analysis import ...

def generate_csv(result_df):
    result_df.to_csv("data/mtg_analysis.csv", index=False)

def main():
    print("Process raw JSON data into clean CSV")

    result_df = prepare_data()
    generate_csv(result_df)

    #print("Trend analysis and extracting characteristics")
    #...

    print("Power BI data is now ready")

if __name__ == "__main__":
    main()