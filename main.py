from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/submit", methods=['POST'])
def api():
    api = request.json
    print(api)
    return "OK"

if __name__ == "__main__":
    app.run(port=4001,host='0.0.0.0')