from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/submit", methods=['POST'])
def api():
    try:
        url = request.get_json()["url"]
        try:
            with open("bot/database.txt", "a") as myfile: # database is stored under the bot
                myfile.write(url + "\n")
            return "OK"
        except:
            return "Bad Request (unable to open txt/db file)"
    except:
        return "Bad Request"

@app.route("/api/db")
def api_db():
    return "Working on this"

if __name__ == "__main__":
    app.run(port=4001,host='0.0.0.0')
