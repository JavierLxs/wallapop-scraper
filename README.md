# wallapop-scraper
This project contains scripts to scrape titles and URLs from wallapop.com for ads meeting a given criteria.
It uses Python library `Selenium` to extract and process data.
Ideally we would create a DAG in Apache Airflow so that this script automatically looks for search results daily.

## Features
- Scrapes data based on user-defined parameters (e.g. category, location, price, search terms, etc.).
- Outputs data as a list of tuples (title,url).
- Sends the list of results per e-mail as clickable links.

## File Descriptions
- `script.py`: Contains some examples of URLs of different searches we may want to perform. Uses `kleinanzeigen_heute()` to collect the data and sends the output as an e-mail message.
- `function.py`: Contains the function `wallapop_search()` that collects ads for the given search parameters.
- `search_template_cars.txt`: Contains a template with the components of a typical URL for a search in the Cars category of wallapop.com. A similar template could be created for any other type of search (Real State, Computers, etc.); we would then simply manually perform a search on the website with all the possible filters, copy-paste the URL on a text file and split the components of the address.
- `requirements.txt`: Lists the Python libraries needed for the project.

## Requirements
- redmail==0.6.0
- selenium==4.26.1
- Install dependencies using `pip install -r requirements.txt`.

## Usage
1. Clone the repository:
   ```
   git clone https://github.com/JavierLxs/wallapop-scraper
   cd wallapop-scraper
   ```
2. Configure the `script.py` file with your search parameters and e-mail credentials. To define your search URLs you can use any of the provided search templates or create your own.
3. Run the script:
   ```
   python script.py
   ```
