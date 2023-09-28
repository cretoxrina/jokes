from flask import Flask
from markupsafe import escape
import csv
import json
from flask import request
app = Flask(name)

@app.route("/")
def liner():
    name = request.args.get('genre')
    file = open('imdb-movie-data.csv', 'r')
    csvreader = csv.reader(file)
    rows = []
    for col in csvreader:
        dic_keys = ['Rank', 'Title', 'Genre', 'Description', 'Director', 'Actors', 'Year', 'Runtime (Minutes)',
                    'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']
        for i in col[2].split(","):
            if i.lower() == name:
                dictionary = dict(zip(dic_keys,col))
                rows.append(dictionary)

    file.close()

    final = json.dumps(rows)
    return final


@app.route("/<name>")
def hello(name):
    file = open('imdb-movie-data.csv', 'r')
    csvreader = csv.reader(file)

    rows = []
    for col in csvreader:
        dic_keys = ['Rank', 'Title', 'Genre', 'Description', 'Director', 'Actors', 'Year', 'Runtime (Minutes)',
                    'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']
        for i in col[2].split(","):
            if i.lower() == name:
                dictionary = dict(zip(dic_keys,col))
                rows.append(dictionary)

    file.close()

    final = json.dumps(rows)
    return final