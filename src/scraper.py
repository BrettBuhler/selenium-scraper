from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def scrape():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.get("https://www.upwork.com/nx/search/jobs/?hourly_rate=40-&q=make.com&sort=recency&t=0")
    print(driver.title)
    
    driver.quit()

if __name__ == "__main__":
    scrape()