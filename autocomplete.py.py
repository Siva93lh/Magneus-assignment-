from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Hardcoded list of tags
tags = ["Python", "Java", "Flask", "Django", "HTML", "CSS", "JavaScript", "React", "Angular", "SQL"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    results = [tag for tag in tags if search.lower() in tag.lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
