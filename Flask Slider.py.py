
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def slider():
    return render_template("slider.html")

@app.route("/update_slider", methods=["POST"])
def update_slider():
    value = request.json.get("value", 0)
    return jsonify({"slider_value": value})

if __name__ == "__main__":
    app.run(debug=True)
