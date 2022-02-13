#!/usr/bin/env python
# coding: utf-8

# ### NASA Mars News

# 
# * Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
# 

# In[1]:


import pandas as pd
import requests
import pymongo
import time
from bs4 import BeautifulSoup as soup
from splinter import Browser
from pprint import pprint
from webdriver_manager.chrome import ChromeDriverManager
import requests


# In[2]:

def scrape():

    # Setup splinter and open the website

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://redplanetscience.com/'
    browser.visit(url)


    # In[3]:


    # use BeatifulSoup to parse the HTML content 
    soup = soup(browser.html, 'html.parser')


    # In[4]:


    # print the html parsed data
    print(soup.prettify())


    # In[5]:


    # find and save the latest title in a variable

    news_title = soup.find('div', class_="content_title").text
    news_title


    # In[6]:


    news_p =soup.find('div', class_="article_teaser_body").text
    news_p


    # In[7]:


    # close browser
    browser.quit()


    # ### JPL Mars Space Images - Featured Image

    # * Visit the url for the Featured Space Image site [here](https://spaceimages-mars.com).
    # 
    # * Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
    # 
    # 

    # In[8]:



    from bs4 import BeautifulSoup as soup


    # In[9]:



    # Setup splinter 

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url_img = 'https://spaceimages-mars.com/'
    browser.visit(url_img)
    


    # In[10]:


    # Scrape page into Soup
    html = browser.html
    soup = soup(html, "html.parser")


    # In[11]:


    relative_image_url = soup.find_all('img', class_='headerimage')


    # In[12]:


    for img in relative_image_url:
        if img.has_attr('src'):
            img1=img['src']
            print(img['src'])


    # In[13]:


    featured_image_url = url_img+img1
    featured_image_url


    # In[14]:


    # close browser
    browser.quit()


    # ### Mars Facts

    # 
    # 
    # * Visit the Mars Facts webpage [here](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # 
    # * Use Pandas to convert the data to a HTML table string.

    # In[15]:


    url_facts = 'https://galaxyfacts-mars.com/'


    # In[16]:


    tables = pd.read_html(url_facts)
    tables


    # In[17]:


    type(tables)


    # In[18]:


    list


    # In[19]:


    # create a dataframe for Mars facts
    df = tables[1]
    df


    # In[20]:


    # rename the columns of the dataframe
    df.columns=['Description', 'Value']


    # In[21]:


    df


    # In[22]:


    # convert the dataframe into HTML
    html_table = df.to_html()
    html_table


    # In[ ]:





    # ### Mars Hemispheres
    #  
    # * Visit the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.
    #
    # In[23]:



    from bs4 import BeautifulSoup as soup


    # In[24]:


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)
    url_hemisph = 'https://marshemispheres.com/'
    browser.visit(url_hemisph)


    # In[25]:


    # Scrape page into Soup
    h_html = browser.html
    h_soup = soup(h_html, "html.parser")


    # In[26]:


    h_img_cls = h_soup.find_all('div', class_='item')


    # In[27]:


    h_img_cls[0]


    # In[28]:


    hemisphere_image_urls =[]


    # In[29]:


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


    # In[30]:


    # close browser

    browser.quit()


    # In[ ]:

    mars_scrape_dict={}

    mars_scrape_dict["Latest_News_Title"] = news_title
    mars_scrape_dict["Latest_News_Paragraph"] = news_p
    mars_scrape_dict["Featured_Image"] = featured_image_url
    mars_scrape_dict["Mars_Facts"] = html_table
    mars_scrape_dict["Mars_Hemispheres"] = hemisphere_image_urls
    
    return mars_scrape_dict




