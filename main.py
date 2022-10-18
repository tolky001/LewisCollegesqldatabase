from flask import Flask, render_template
from SQLConnector import querySQL

app = Flask(__name__)


@app.route("/checkmyqueries")
def check_my_queries():
    query = 'SELECT AVG(sat_score) FROM Student AS S INNER JOIN Phonebook AS P ON S.personid = P.personid GROUP BY phone LIKE "_%480_%";'
    result = querySQL(query)

    if result:
        return render_template("displayData.html", query=query, result=result)
    else:
        return "<h2>Query Returned nothing...</h2>"

@app.route("/")
def homePage():
    links = []
    for rule in app.url_map.iter_rules():
        links.append(str(rule))
    links.remove("/")
    links.remove("/static/<path:filename>")
    return render_template("home.html", urlList=links)


app.run("0.0.0.0")
