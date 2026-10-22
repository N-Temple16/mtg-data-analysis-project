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
The data for this analysis comes from MTGJSON (https://www.mtgjson.com/downloads/all-files/), using the AllPrintings.json and AllPrices.json datasets.

To process and prepare the data, a mix of Python and pandas was used to extract card characteristics and price information as well as combine the datasets into a single table for analysis.

The detailed preparation process:
1. Loaded the JSON data and first extracted the characteristics I would be examining from the printing data which includes the aforementioned topics (rarity, mana value, colour, etc.)
2. Following that was extracting the price data and specifically looking at the TCGplayer, retail, normal pricing of cards as well as the most recent price snapshot at the time of this step
3. Formatting both as pandas DataFrames and merging them into one total dataset
4. Quick analysis of the dataset to make sure all values appear as they should as well as some clean up to prepare tables for use in Power BI
5. Generating and exporting the resulting main dataset along with a helper keyword dataset for improved examination to CSV for analysis in Power BI

The final dataset contains one row per printing with a matching price record.

## Key Findings


## Limitations
Of course, as much as this project was aimed to create as accurate of an analysis as possible, there were a few limitations that can not be overlooked:

- ```Price Changes Before/After Snapshot``` - As the price snapshot of cards for the data was taken on September 24, 2026, the analysis is only looking at prices in that current moment in time. Prices could have previously just spiked as a new set was coming out and prices tend to be inflated in the first couple of weeks as well as card prices could be rising or falling by the time you are reading this section currently.
- ```Printing versus Card Design``` - Cards can be reprinted into different sets and therefore have a new record and identity while mechanically being the exact same card. They are still important to look at because each has it's own pricing but similar to the foil/non-foil argument, there is no gameplay difference between cards in this category.
- ```Foil/Non-foil``` - As mentioned previously in this report, while foil/etched foil/non-foil variants all play a part in the price of a card, for this specific analysis I chose to look only at non-foil printings to reduce the influence of premium finishes and to keep the data a bit more cohesive. Different finishes could almost be a separate analysis on it's own.
- ```Not All Prices Listed``` - For a small group of cards in the data I pulled from MTGJSON, they did not have any actively listed prices whether that be because of the age of the card or set the card is from or the scarcity of limited edition printings. This does not cause a huge problem for the dataset but it is a limitation nonetheless.
- ```Extreme Values``` - some characteristics, not limited to just price, can have extreme values that can affect visualizations and summary statistics. For example, cards usually have mana values between 0 and 12 but there are outlliers (ex. a real card that was printed as a joke with a mana value of 1 million) that do have to be taken into account when analyzing the data.
- ```Association versus Causation``` - Though this analysis was created to see which characteristics correlated to expense, one characteristic generally does not dictate price alone. Take the relationship between rarity and price for example. Although the rarity of a card can definitely affect the price of a card, it does not prove that rarity alone causes a card to be expensive.
- ```Scarcity and Collectibility``` - It is hard to capture everything in a dataset. Things like demand for cards in certain gameplay formats, the condition of the card (lightly played, near mint, damaged, etc.) and overall collector interest all affect card pricing and are difficult to keep track of all at once.

## Conclusion
In conclusion,