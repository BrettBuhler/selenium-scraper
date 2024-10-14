import unittest
from src.scraper import UpworkScraper

class TestUpworkScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = UpworkScraper()

    def test_scrape_jobs(self):
        df = self.scraper.scrape_jobs()
        self.assertGreater(len(df), 0)
        self.assertIn("title", df.columns)
        self.assertIn("description", df.columns)

    def tearDown(self):
        self.scraper.close()

if __name__ == "__main__":
    unittest.main()