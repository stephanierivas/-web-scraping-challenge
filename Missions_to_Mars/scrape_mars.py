from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import time

mars_dict = {}
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    
    html = browser.html
    soup = bs(html, 'html.parser')

    stepone = soup.find('ul', class_='item_list')
    # steptwo = stepone.find('li', class_='slide')
    newstitle = stepone.find('div', class_='content_title').text

    paragraph = stepone.find('div', class_='article_teaser_body').text

    url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(url) 

    html = browser.html
    soup = bs(html, 'html.parser')

        
    featured_image_url= soup.find('img', class_='headerimage fade-in')["src"]
    feat_img = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/" + featured_image_url

        # Store data in a dictionary
    mars_dict = {
        "feat_img": feat_img,
        "newstitle": newstitle,
        "paragraph": paragraph
    }
    return mars_dict
scrape_info()