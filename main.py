from flask import Flask, render_template, request, jsonify, Response
import sys
import json
import os
from dotenv import load_dotenv
import requests

load_dotenv('bot/.env.txt')

app = Flask(__name__)



# For testing, this is a fake database of valid auth tokens
# Note to self, take this out before production

keys = ["abc123", "000webhostSUCKS"]
port = os.getenv("PORT")

@app.route("/")
def home():
    if os.getenv("PRODUCTION") == "false":
        return render_template("preview.html")
    else:
        return render_template("index.html")

@app.route("/api/submit", methods=['POST'])
def api():
    try:
        url = request.get_json()["url"]
        auth = request.get_json()["token"]
        if auth not in keys:
            return "Bad Request, invalid token"
        try:
            with open("bot/database.txt", "a") as myfile: # database is stored under the bot
                myfile.write(url + "\n")
            return "OK"
        except:
            return "Internal Server Error (unable to open txt/db file)"
    except:
        return "Bad Request, check your post data"

@app.route("/api")
def api_docs():
    domain = str(os.getenv("DOMAIN"))
    full_domain = str(os.getenv("PROTO")) + "://" + str(os.getenv("DOMAIN"))
    return render_template("api.html", domain=domain, full_domain=full_domain)

@app.route("/api/db")
def api_db():
    f = open("bot/database.txt","r")
    lines = f.readlines()
    return Response(json.dumps(str(lines)), mimetype='application/json')

@app.route("/api/invite/<invite>")
def invite(invite):
    http = requests.get("https://discord.com/api/v9/invites/" + invite + "?with_counts=true&with_expiration=true")
    try:
        name = http.json()["guild"]["name"]
        count = http.json()["approximate_member_count"]
        nsfw = http.json()["guild"]["nsfw"]
        pre_baked_json = {"name": name, "members": count, "isNSFW": nsfw} # add icon for guild/server in a future update
        return Response(json.dumps(pre_baked_json), mimetype='application/json')
    except:
        return Response(json.dumps({"error": "true", "http": http.status_code}), mimetype='application/json'), 400

@app.route("/stats")
def stats():
    f = open("bot/database.txt","r")
    lines = f.readlines()
    number = len(lines)
    return render_template("stats.html", indexed = number)
    
@app.route("/search", methods=['GET'])
def search():
    db = open('bot/database.txt', 'r')
    l = db.readlines()
    
    results = []
    results_raw = []

    try:
        search = request.args.get('q')
    except:
        return "Bad Request"

    for line in l:
        if search in line and line != "":
            pre = line.strip()
            pre1 = pre.strip("https://discord.gg/")
            pre2 = pre1.strip("https://discord.com/invite/")
            results_raw.append(pre2)
            results.append(line.strip())
    return render_template("results.html", results = results, results_raw = results_raw)

if __name__ == "__main__":
    app.run(port=port,host='0.0.0.0')
