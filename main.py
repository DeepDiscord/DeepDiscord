from flask import Flask, render_template, request, jsonify
import sys
import os
from dotenv import load_dotenv

load_dotenv('bot/.env.txt')

app = Flask(__name__)

# For testing, this is a fake database of valid auth tokens
# Note to self, take this out before production

keys = ["abc123", "000webhostSUCKS"]

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
    return "Working on this"

if __name__ == "__main__":
    app.run(port=4001,host='0.0.0.0')
