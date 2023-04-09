## Flipkart Product Scraper

This is a Python application that scrapes information about a product from Flipkart and inserts it into a SQLite database using the SQLModel library.

### Installation

1.  Clone this repository or download the code as a ZIP file and extract it.
2.  Navigate to the root folder of the project in your terminal.
3.  Run the following command to install the dependencies:

Copy code

`pip install -r requirements.txt`

### Usage

1.  In the `main.py` file, replace the `url` variable with the URL of the product page on Flipkart that you want to scrape.
2.  Run the following command in your terminal to start the application:

cssCopy code

`python main.py`

3.  The scraped product information will be inserted into the `products.db` file in the root folder of the project. If the product already exists in the database, a message will be printed to the console.

### License

This project is licensed under the MIT License - see the LICENSE file for details.
