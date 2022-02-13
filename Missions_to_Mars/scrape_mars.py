#!/usr/bin/env python
# coding: utf-8

# ### NASA Mars News

# 
# * Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
# 


import pandas as pd
import requests
import pymongo
import time
from bs4 import BeautifulSoup as soup
from splinter import Browser
from pprint import pprint
from webdriver_manager.chrome import ChromeDriverManager

def scrape():

    # Setup splinter and open the website

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    #browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # use BeatifulSoup to parse the HTML content 
    soup = soup(browser.html, 'html.parser')


    # print the html parsed data
    print(soup.prettify())



    # find and save the latest title in a variable

    news_title = soup.find('div', class_="content_title").text
    news_title


    news_p =soup.find('div', class_="article_teaser_body").text
    news_p


    # close browser
    browser.quit()


    # ### JPL Mars Space Images - Featured Image

    # * Visit the url for the Featured Space Image site [here](https://spaceimages-mars.com).
    # 
    # * Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
    # 
    # 


    from bs4 import BeautifulSoup as soup


    # Setup splinter 

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url_img = 'https://spaceimages-mars.com/'
    browser.visit(url_img)
  
    # Scrape page into Soup
    html = browser.html
    soup = soup(html, "html.parser")

    relative_image_url = soup.find_all('img', class_='headerimage')


    for img in relative_image_url:
        if img.has_attr('src'):
            img1=img['src']
            print(img['src'])



    featured_image_url = url_img+img1
    featured_image_url


    # close browser
    browser.quit()


    # ### Mars Facts
    # * Visit the Mars Facts webpage [here](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # 
    # * Use Pandas to convert the data to a HTML table string.

    url_facts = 'https://galaxyfacts-mars.com/'


    tables = pd.read_html(url_facts)
    tables



    type(tables)



    list

    # create a dataframe for Mars facts
    df = tables[1]
    df

    # rename the columns of the dataframe
    df.columns=['Description', 'Value']

    df

    # convert the dataframe into HTML
    html_table = df.to_html()
    html_table

    # ### Mars Hemispheres
    #  
    # * Visit the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.
 
   # from bs4 import BeautifulSoup as soup

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)
    url_hemisph = 'https://marshemispheres.com/'
    browser.visit(url_hemisph)


    # Scrape page into Soup
    h_html = browser.html
    h_soup = soup(h_html, "html.parser")


    h_img_cls = h_soup.find_all('div', class_='item')

    h_img_cls[0]


    hemisphere_image_urls =[]


    # use a for loop to find the images title and url for each hemisphere and create a dictionary of dictionaries  
    for i in h_img_cls:
        title = i.find('h3').text
        img_url1 = i.find('a')['href'] 
        browser.visit(url_hemisph+img_url1)
        img_html = browser.html
        h_img_soup=soup(img_html, 'html.parser')
        img_url2 = h_img_soup.find('img', class_='wide-image')['src']
        img_url3=url_hemisph+img_url2
        hemisphere_image_urls.append({"title":title, 'img_url': img_url3 })
    hemisphere_image_urls

    mars_data = {
        "news_title":news_title,
        "news_p":news_p,
        "featured_image_url":featured_image_url,
        "fact_table":html_table,
        "hemisphere_images":hemisphere_image_urls
    }

    #mars_scrape_dict={"Latest_News_Title"] = news_title
    #mars_scrape_dict["Latest_News_Paragraph"] = news_p
    #mars_scrape_dict["Featured_Image"] = featured_image_url
    #mars_scrape_dict["Mars_Facts"] = html_table
    #mars_scrape_dict["Mars_Hemispheres"] = hemisphere_image_urls
    browser.quit()

    return mars_data



