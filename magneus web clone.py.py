
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/links')
def links():
    return render_template('links.html')

@app.route('/css_properties')
def css_properties():
    return render_template('css_properties.html')

if __name__ == '__main__':
    app.run(debug=True)
