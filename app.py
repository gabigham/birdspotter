from flask import Flask, render_template, redirect
from flask import request
from flask_pymongo import PyMongo
import look_for_birds
import os

# import python function that uses model to return prediction

# Create an instance of Flask
app = Flask(__name__)

IMAGE_FOLDER = os.path.join('static', 'test_images')
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

model = 'fourth_try_full.h5'

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/bs_results")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    result = mongo.db.results.find_one()
      
    answer = result['results'] 
    image = result['image']
    
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], image)
    # Return template and data
    return render_template("index.html", result=answer, image=full_filename)

 # @app.route('/index')
 # def show_index():
 #   full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'test3.jpg')
 #   return render_template("index.html", image = full_filename)


# Route that will trigger the scrape function
@app.route("/look/<image>")
def look(image):

    test_image = 'test/' + image
    # image = 'test6.jpg'

    # look at image and predict
    result = { "results" : look_for_birds.look(model, test_image), "image":image }

    # Run the look (model prediction) function
    mongo.db.results.update({}, result, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
