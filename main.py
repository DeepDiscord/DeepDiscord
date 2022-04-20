from flask import Flask, render_template, request, jsonify, Response
import sys
import json
import os
from dotenv import load_dotenv

load_dotenv('bot/.env.txt')

app = Flask(__name__)

# For testing, this is a fake database of valid auth tokens
# Note to self, take this out before production

keys = ["abc123", "000webhostSUCKS"]
port = os.getenv("PORT")

@app.route("/")
def home():
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

@app.route("/api/db")
def api_db():
    f = open("bot/database.txt","r")
    lines = f.readlines()
    return Response(json.dumps(str(lines)), mimetype='application/json')

@app.route("/stats")
def stats():
    f = open("bot/database.txt","r")
    lines = f.readlines()
    number = len(lines)
    return render_template("stats.html", indexed = number)
    

if __name__ == "__main__":
    app.run(port=port,host='0.0.0.0')
