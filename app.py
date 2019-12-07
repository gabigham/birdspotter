from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# import python function that uses model to return prediction

# Create an instance of Flask
app = Flask(__name__)


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # result = look(  default )

    # Return template and data
    return render_template("index.html", result=result)

# Route that will trigger the scrape function
@app.route("/look")
def look():

    # Run the look (model prediction) function
    
    # pass variable to index?  (web scrape passes to db)


    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
