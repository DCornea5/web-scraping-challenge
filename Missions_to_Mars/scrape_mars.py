#!/usr/bin/env python
# coding: utf-8

# ### NASA Mars News

# 
# * Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
# 


from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
#import requests
#import pymongo
import time
from splinter import Browser


def scrape():

    # Setup splinter and open the website

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    #browser = Browser('chrome', **executable_path, headless=False)
    print("############## Mars Title ##################")
    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url)

    # use BeatifulSoup to parse the HTML content 
    news_soup = bs(browser.html, 'html.parser')


    # print the html parsed data
    #print(soup.prettify())



    # find and save the latest title in a variable

    news_title = news_soup.find('div', class_="content_title").text
    news_title
    print(news_title)

    print("############### Mars Paragraph ##############")

    news_p =news_soup.find('div', class_="article_teaser_body").text
    news_p
    print(news_p)


    # close browser
    browser.quit()


    # ### JPL Mars Space Images - Featured Image

    # * Visit the url for the Featured Space Image site [here](https://spaceimages-mars.com).
    # 
    # * Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
    # 
    # 
    print("############ Mars Image ##############")

    #from bs4 import BeautifulSoup as bs


    # Setup splinter 

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url_img = 'https://spaceimages-mars.com/'
    browser.visit(url_img)
  
    # Scrape page into Soup
    html = browser.html
    img_soup = bs(html, "html.parser")

    relative_image_url = img_soup.find_all('img', class_='headerimage')


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
    print("########### Mars Facts ##############")
    url_facts = 'https://galaxyfacts-mars.com/'
    browser.visit(url_facts)
  
    table_facts = pd.read_html(url_facts)
    df_facts = table_facts[1]
    df_facts.columns =[" Description", " Value"] 
    df_facts = df_facts.set_index("Description")
    mars_facts = df_facts.to_html()

    # mars_facts = pd.read_html(url_facts)[1]
    # mars_facts.reset_index(inplace=True)
    # mars_facts.columns=['Description', 'Value']
    # mars_facts
    #tables = pd.read_html(url_facts)
    #tables
    #type(tables)
    #list
    # create a dataframe for Mars facts
    #df = tables[1]
    #df
    # rename the columns of the dataframe
    #df.columns=['Description', 'Value']
    #df
    # convert the dataframe into HTML
    #html_table = df.to_html()
    #html_table

    # ### Mars Hemispheres
    #  
    # * Visit the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.
 
   # from bs4 import BeautifulSoup as soup
    print("############# Mars Hemisheres ##############")
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)
    url_hemisph = 'https://marshemispheres.com/'
    browser.visit(url_hemisph)

    h_html = browser.html
    h_soup = bs(h_html, "html.parser")

    h_items = h_soup.find_all('div', class_='item')

    #h_img_cls[0]

    
    

    ###########################################
    # use a for loop to find the images title and url for each hemisphere and create a dictionary of dictionaries  
    # for i in h_img_cls:
    #     title = i.find('h3').text
    #     img_url1 = i.find('a')['href'] 
    #     browser.visit(url_hemisph+img_url1)
    #     img_html = browser.html
    #     h_img_soup=bs(img_html, 'html.parser')
    #     img_url2 = h_img_soup.find('img', class_='wide-image')['src']
    #     img_url3=url_hemisph+img_url2
    #     hemisphere_image_urls.append({"title":title, 'img_url': img_url3 })
    # hemisphere_image_urls

    #######################################
    hemisphere_image_urls =[]
    hemisphere ={}

    for h in h_items:

        
        h_link = h.find('a')
        h_href = h_link['href']
        title = h_link.find('h3').text

        browser.visit(url_hemisph + h_href)

        image_html = browser.html

        image_soup = bs(image_html, 'html.parser')

        download = image_soup.find('div', class_= 'downloads')
        img_url = download.find('a')['href']
        
        print(title)
        print(img_url)

        hemisphere['img_url'] = img_url
        hemisphere['title'] = title
        hemisphere_image_urls.append(hemisphere)
        
        return hemisphere_image_urls

        
        # hemisphere_image_urls = [{'title': 'Cerberus Hemisphere',
        # 'img_url': 'https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'},
        # {'title': 'Schiaparelli Hemisphere',
        # 'img_url': 'https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'},
        # {'title': 'Syrtis Major Hemisphere',
        # 'img_url': 'https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'},
        # {'title': 'Valles Marineris Hemisphere',
        # 'img_url': 'https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'}]
    

    print("############ Mars Dictionary ##################")
    mars_info = {
        "news_title":news_title,
        "news_p":news_p,
        "featured_image_url":featured_image_url,
        "fact_table":mars_facts,
        "hemisphere_images":hemisphere_image_urls
    }

    #mars_scrape_dict={"Latest_News_Title"] = news_title
    #mars_scrape_dict["Latest_News_Paragraph"] = news_p
    #mars_scrape_dict["Featured_Image"] = featured_image_url
    #mars_scrape_dict["Mars_Facts"] = html_table
    #mars_scrape_dict["Mars_Hemispheres"] = hemisphere_image_urls
    browser.quit()
    return mars_info









