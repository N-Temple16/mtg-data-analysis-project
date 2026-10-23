# How to Access the Analysis
1. Clone this repository 
2. Install Python from the official Python website if not already on your machine
3. Download AllPrintings.json and AllPrices.json from MTGJSON (https://www.mtgjson.com/downloads/all-files/) and place them in the project's ```data/``` directory (it is recommended to download the compressed files if possible and then extract them to the directory afterwards)
4. Run the data preparation pipeline using: ```python main.py```


## Viewing the Results
### Power BI Dashboard
To exlpore the interactive report, open the file located at ```powerbi/mtg_analysis.pbix``` in Power BI. If not already, generate the analytical CSV file from the instructions above. If Power BI cannot locate the CSV file, update the report's data source path to point to your local ```data/mtg_analysis.csv``` file, then refresh the report.

### Analytical Dataset
If you are just interested in the cleaned dataset without the dashboard and visuals, follow the instructions up to and including creating the ```data/mtg_analysis.csv``` file using ```python main.py```. From here you are free to use a data analysis tool of your choosing (Excel, Python, Power BI, etc.) to explore the generated CSV file.