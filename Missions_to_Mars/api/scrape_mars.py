import pandas as pd
import time
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # Open the browser
    browser = open_brower()

    # Collect the latest News Title and Paragraph Text
    soup = get_html_content(browser, "https://redplanetscience.com/")

    title = soup.find("div", class_="content_title").get_text()
    paragraph = soup.find("div", class_="article_teaser_body").get_text()
    
    # Find the current Featured Mars Image
    space_images_mars_url = "https://spaceimages-mars.com"
    soup = get_html_content(browser, space_images_mars_url)

    featured_image_url = f'{space_images_mars_url}/{soup.find("img", class_="headerimage")["src"]}'

    # Scrape facts about Mars
    facts_df = pd.read_html("https://galaxyfacts-mars.com")[0]
    facts_df = facts_df.loc[1:]
    facts_df.rename(columns={0: 'Mars - Earth Comparison', 1: 'Mars', 2: 'Earth'}, inplace=True)

    # Convert to html table with bootstrap style
    facts_table = facts_df.to_html(index=False)
    facts_table = facts_table.replace('dataframe', 'table table-hover table-striped')
    facts_table = facts_table.replace('<th>', '<th scope="col">')
    facts_table = facts_table.replace('\n', '')
    facts_table = facts_table.replace(' border="1"', '')
    facts_table = facts_table.replace(' style="text-align: right;"', '')

    # Obtain high resolution images for each of Mar's hemispheres
    mars_hemispheres_url = "https://marshemispheres.com/"
    soup = get_html_content(browser, mars_hemispheres_url)

    # List of links
    elements = soup.select(".description a")
    links = [ f"{mars_hemispheres_url}{element['href']}" for element in elements]

    hemisphere_image_urls = []
    for link in links:
        soup = get_html_content(browser, link)
        
        hemisphere_image_urls.append({
            "title": soup.find("h2", class_="title").get_text(),
            "img_url": mars_hemispheres_url + soup.find("img", class_="wide-image")["src"]
        })

    # Quit the browser
    browser.quit()

    scraped_data = {
        'title': title,
        'paragraph': paragraph,
        'featured_image_url': featured_image_url,
        'facts_table': facts_table,
        'hemisphere_image_urls': hemisphere_image_urls
    }

    return scraped_data

def open_brower():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser
    
def get_html_content(browser, url):
    # Visti url
    browser.visit(url)

    # wait to load page
    time.sleep(1)

    # Parse html content
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    return soup