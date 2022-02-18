
web-scraping-challenge - Web Scraping Homework - Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)  

Repository web-scraping-challenge

Directory for the web scraping Missions_to_Mars

Initial scraping completed by using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

Jupyter Notebook file mission_to_mars.ipynb

NASA Mars News
Scrape the Mars News Site and collect the latest News Title and Paragraph Text.
JPL Mars Space Images - Featured Image
Visit the url for the Featured Space Image site here.
Mars Facts
Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
Mars Hemispheres
Visit the astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
Step 2 - MongoDB and Flask Application
Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

Convert mission_to_mars.ipynb Jupyter notebook into a Python script called scrape_mars.py with a function called scrape

Create a route called /scrape and import scrape_mars.py script and call scrape function.

Store the return value in Mongo as a Python dictionary.
Create a root route / that will query Mongo database and pass the mars data into an HTML template to display the data.

Create a template HTML file called index.html with Mars data