from flask import Flask, render_template, request, jsonify
from assetmap import assetmap

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    code = request.json["code"]
    result = assetmap(code)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
