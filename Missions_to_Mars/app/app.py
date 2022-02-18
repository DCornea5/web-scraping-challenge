# dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
# import pymongo

# create an instance of Flask
app = Flask(__name__, static_url_path='', static_folder='')

# establish mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# route for landing page
@app.route("/")

def index():
    print("################################")
   
    mars = mongo.db.mars.find_one()

    

    return render_template("index.html", mars = mars)

# create route for scrapping data
@app.route("/scrape")
def scrape():

    # MongoDB connection and update
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update_one({}, {"$set": mars_data}, upsert=True)
    return redirect('/', code=302)


if __name__ == "__main__":
    app.run()