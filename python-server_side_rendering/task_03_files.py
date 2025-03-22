#!/usr/bin/python3

from flask import Flask, render_template
from flask import json
from flask import request
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/items")
def items():
    try:
        with open("items.json", "r") as file:
            data = json.load(file)
            items = data.get("items", [])

        return render_template("items.html", items=items)

    except FileNotFoundError:
        return "Items file not found", 404

    except json.JSONDecodeError:
        return "Error decoding JSON", 500


@app.route("/products")
def products():
    # Get from request
    source = request.args.get("source")
    product_id = request.args.get("id")

    data = []

    if source == "json":

        with open("products.json", 'r') as file:
            reader = json.load(file)
            data = reader

    elif source == "csv":

        with open("products.csv", newline="") as file:
            reader = csv.DictReader(file)
            data = list(reader)

    else:
        return "Wrong source", 400

    # Append a dictionnary with only one element to fit with HTML prerequisites
    if product_id:
        filtered = []
        item_found = False
        for item in data:
            if str(item.get("id")) == product_id:
                item_found = True
                filtered.append(item)

        if item_found is True:
            return render_template("product_display.html", products=filtered)
        else:
            return "Product not found", 404

    return render_template("product_display.html", products=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
