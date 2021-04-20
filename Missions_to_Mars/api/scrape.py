from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def scrape(url):
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    listings = {}
    listings["headline"] = soup.find("div", class_="content_title").get_text()
    listings["article"] = soup.find("div", class_="article_teaser_body").get_text()
    
    # Quit the browser
    browser.quit()
    
    return listings