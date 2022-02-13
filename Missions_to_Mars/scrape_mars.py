# import dependencies
import pandas as pd
import requests
import pymongo
import time
from bs4 import BeautifulSoup as soup
from splinter import Browser
from pprint import pprint
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from selenium import webdriver


def init_browser():
    #executable_path = {'executable_path': 'chromedriver'}
    #browser = Browser('Chrome', **executable_path, headless=False)

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)



def scrape():
    browser=init_browser()
    #mars_data={}

    ###  NASA Mars News   
    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url)
    time.sleep(4)
    news_html=browser.html
    soup=soup(news_html,'html.parser')

    ### Latest News

    news_title = soup.find('div', class_="content_title").text
    news_p =soup.find('div', class_="article_teaser_body").text
    
    ### JPL Mars Space Images - Featured Image

    url_img = 'https://spaceimages-mars.com/'
    browser.visit(url_img)
    time.sleep(4)
    html = browser.html
    soup = soup(html, "html.parser")
    relative_image_url = soup.find_all('img', class_='headerimage')
    for img in relative_image_url:
        if img.has_attr('src'):
            img1=img['src']
            
    featured_image_url = url_img+img1
   
   ### Mars Facts
    url_facts = 'https://galaxyfacts-mars.com/'

    tables = pd.read_html(url_facts)
    mars_fact_table=tables[1]
    mars_fact=mars_fact.rename(columns={0:"Description",1:"Value"},errors="raise")
    mars_fact.set_index("Description",inplace=True)
    mars_fact
    
    fact_table=mars_fact.to_html()
    fact_table.replace('\n','')

    ### Mars Hemispheres
    
    # hemisphere_image_urls = [
    #     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    #     {"title": "Cerberus Hemisphere", "img_url": "..."},
    #     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    #     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
    # ]
    # ```

    # https://marshemispheres.com/
    # 
    # https://marshemispheres.com/cerberus.html  
    # https://marshemispheres.com/schiaparelli.html  
    # https://marshemispheres.com/syrtis.html      
    # https://marshemispheres.com/valles.html  

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)
    url_hemisph = 'https://marshemispheres.com/'
    browser.visit(url_hemisph)


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
        

    mars_info = {
        "mars_news": {
            "news_title": news_title,
            "news_p": news_p,
            },
        "mars_img": featured_image_url,
        "mars_fact": mars_fact,
        "mars_hemisphere": hemisphere_image_urls
    }

    # close browser

    browser.quit()

    return mars_info
   