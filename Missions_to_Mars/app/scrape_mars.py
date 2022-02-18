#!/usr/bin/env python
# coding: utf-8

# ### NASA Mars News

# 
# * Scrape the [Mars News Site](https://redplanetscience.com/) and 
# collect the latest News Title and Paragraph Text. 
# Assign the text to variables that you can reference later.
# 


from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
#import requests
#import pymongo
import time
from splinter import Browser
import datetime as dt

def scrape_all():

    # Setup splinter and open a browser

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_p = mars_news(browser)

    data = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": hemispheres(browser),
        "last_modified": dt.datetime.now()
    }
    browser.quit()
    return data



def mars_news(browser):
    #browser = Browser('chrome', **executable_path, headless=False)
    print("############## Mars Title ##################")
    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url)

    # use BeatifulSoup to parse the HTML content 
   

    browser.is_element_present_by_css('div.list_text', wait_time=1)
    html = browser.html
    news_soup = bs(html, 'html.parser')
    try:
        slide_elem = news_soup.select_one('div.list_text')
        news_title = slide_elem.find("div", class_="content_title").get_text()
        news_p = slide_elem.find("div", class_="article_teaser_body").get_text()
    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
    # ### JPL Mars Space Images - Featured Image

    # * Visit the url for the Featured Space Image site [here](https://spaceimages-mars.com).
    # 
    print("############ Mars Image ##############")

    # Setup splinter 

    url_img = 'https://spaceimages-mars.com/'
    browser.visit(url_img)
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()
    html = browser.html
    img_soup = bs(html, 'html.parser')
    try:
        # find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    print(img_url)
    return img_url
    
    
def mars_facts():
    # ### Mars Facts
       
    print("########### Mars Facts ##############")
    
    try:
        # scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # dataframe columns
    df.columns = ['Description', 'Mars', 'Earth']

    # set index for teh dataframe
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add table style
    print(df)
    return df.to_html(classes="table table-striped table-hover table-condensed border: 5px solid black")

   
def hemispheres(browser):
    # ### Mars Hemispheres
    #  
    # * Visit the astrogeology site [here](https://marshemispheres.com/) 
    # to obtain high resolution images for each of Mar's hemispheres.
 
 
    print("############# Mars Hemisheres ##############")
    
    url_hemisph = 'https://marshemispheres.com/'
    browser.visit(url_hemisph+'index.html')

    
    hemisphere_image_urls =[]
   
    for i in range(4):
        # Find the images url's
        browser.find_by_css("a.product-item img")[i].click()
        hemi_data = scrape_hemisphere(browser.html)
        hemi_data['img_url'] = url_hemisph + hemi_data['img_url']
        # Append hemisphere object to list
        hemisphere_image_urls.append(hemi_data)
        
        browser.back()

    return hemisphere_image_urls

def scrape_hemisphere(html_text):
    # parse html text
    hemi_soup = bs(html_text, "html.parser")

    # add try/except for error handling
    try:
        title_elem = hemi_soup.find("h2", class_="title").get_text()
        sample_elem = hemi_soup.find("a", text="Sample").get("href")

    except AttributeError:
       
        title_elem = None
        sample_elem = None

    hemispheres = {
        "title": title_elem,
        "img_url": sample_elem
    }

    return hemispheres

     

if __name__ == "__main__":

    # print scraped data
    print(scrape_all())








