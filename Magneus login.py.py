from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secretkey'  # needed for flashing messages

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email == "training@jalaacademy.com" and password == "jobprogram":
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Credentials. Please try again.', 'danger')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return "<h1>Welcome to the Dashboard!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
