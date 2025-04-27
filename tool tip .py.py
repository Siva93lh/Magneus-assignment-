
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/tooltip')
def tooltip():
    return render_template('tooltip.html')

if __name__ == "__main__":
    app.run(debug=True)
