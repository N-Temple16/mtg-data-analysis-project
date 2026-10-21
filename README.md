# Magic: The Gathering Characteristic/Price Analysis Overview
This analysis has been conducted to determine what characteristics are associated with expensive Magic: The Gathering cards. This project used a culmination of Python, pandas, MTGJSON data, and Power BI to investigate this question more in depth.

![Dashboard Screenshot](images/dashboard.png)

## What Characteristics Were Taken into Account?
There are potentially hundreds of characteristics that could be examined to determine the price of a card. From the finish on the card (foil/non-foil), the playablitily in different formats, or the tens of details related to each card such as the artist, release date, promotional only, etc. For this analysis I chose to look at card details as I felt like it was the most reliable way of determining the price of a card. More specifically I chose to look into these characteristics:
- Rarity
- Mana Value
- Keywords / Abilities
- Colour
- Types
- Set

For a more fair examination, I restricted the primary analysis to printings with a non-foil version. This was done to reduce the influence of premium finishes such as foil and etched foil variations, which can command substantially greater prices for otherwise indentical card designs. Premium finishes were treated as a separate potential factor rather than mixed into the primary price analysis.

## Defining an Expensive Card
The term "expensive" is inherently extremely subjective. For one individual, $5 may be considered expensive whereas another individual may frequently purchase cards worth hundreds of dollars without thinking twice. For the purposes of this project, I defined an expensive Magic: The Gathering card as a printing with a TCGplayer normal price of $50 USD or more. The price snapshots used in this analysis were taken on September 24, 2026 for a majority of the printings and earlier dates for cards that are sold more scarcely.

I chose this threshold because $50 represents a meaningful amount of money for a single trading card from the perspective of the analysis. This is in no way intended to represent an official industry definition of an expensive card. Since this threshold is subjective as mentioned previously, I also examined alternative thresholds where appropriate to give a better picture.

## Data Source and Preparation
talk about MTGJSON and the files used, how python and pandas came in, the process of cleaning and preparing the data, and what the final dataset contains

The data for this analysis comes from MTGJSON (https://www.mtgjson.com/downloads/all-files/), using the AllPrintings.json and AllPrices.json datasets.

To process and prepare the data, a mix of Python and pandas was used to extract card characteristics and price information as well as combine the datasets into a single table for analysis.

The detailed preparation process:
1. Loaded the JSON data and first extracted the characteristics I would be examining from the printing data which includes the aforementioned topics (rarity, mana value, colour, etc.)
2. Following that with extracting the price data and specifically looking at the TCGplayer, retail, normal pricing of cards as well as the most recent price snapshot at the time of this step
3. Formatting both as pandas DataFrames and merging them into one total dataset
4. Quick analysis of the dataset to make sure all values appear as they should as well as some clean up to prepare tables for use in Power BI
5. Generating and exporting the resulting main dataset along with a helper keyword dataset for improved examination to CSV for analysis in Power BI

The final dataset contains one row per printing with a matching price record.

## How to Access the Analysis


## Key Findings


## Limitations
prices change from the snapshot, printing vs card design, nonfoil/foil, not all prices listed, extreme values, association vs causation, scarcity and collectibility

## Conclusion
