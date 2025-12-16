from flask import Flask, render_template, request, jsonify
from assetmap import assetmap
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
@app.route("/analyze", methods=["POST"])
def analyze():
    code = request.json["code"]

    tree = assetmap(code, project_root=".")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"assetmap_output_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(tree, f, indent=4)

    return jsonify(tree)


if __name__ == "__main__":
    app.run(debug=True)
