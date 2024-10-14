from flask import Flask
from scraper import scrape

app = Flask(__name__)

@app.route('/')
def run_scraper():
    scrape()
    return "Scraper ran successfully!"

if __name__ == "__main__":
    app.run(debug=True)