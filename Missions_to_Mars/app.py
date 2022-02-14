# dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
# import pymongo

# create an instance of Flask
app = Flask(__name__, static_url_path='', static_folder='')

# establish mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")

def home():
    print("################################")
    mars_data = mongo.db.collection.find_one()
   
    # print("mars_data is" + str(mars_data))

    return render_template("index.html", mars = mars_data)

#create route for scrapping data
@app.route("/scrape")
def scrape():

    mars_data = scrape_mars.scrape()
      
    mongo.db.collection.update_one({}, {"$set": mars_data}, upsert=True)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=False)