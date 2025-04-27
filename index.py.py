
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                mobile_no TEXT,
                email TEXT,
                gender TEXT,
                birth_date TEXT,
                country TEXT,
                city TEXT)""")
    conn.commit()
    conn.close()

init_db()

# Home page - View and Search Employees
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    query = "SELECT * FROM employee"
    params = ()
    if request.method == 'POST':
        name = request.form.get('name')
        mobile_no = request.form.get('mobile_no')
        email = request.form.get('email')
        query += " WHERE 1=1"
        if name:
            query += " AND (first_name LIKE ? OR last_name LIKE ?)"
            params += (f'%{name}%', f'%{name}%')
        if mobile_no:
            query += " AND mobile_no LIKE ?"
            params += (f'%{mobile_no}%',)
        if email:
            query += " AND email LIKE ?"
            params += (f'%{email}%',)
    c.execute(query, params)
    employees = c.fetchall()
    conn.close()
    return render_template('index.html', employees=employees)

# Add new Employee
@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        data = (
            request.form['first_name'],
            request.form['last_name'],
            request.form['mobile_no'],
            request.form['email'],
            request.form['gender'],
            request.form['birth_date'],
            request.form['country'],
            request.form['city']
        )
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute('INSERT INTO employee (first_name, last_name, mobile_no, email, gender, birth_date, country, city) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', data)
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_employee.html')

# Edit Employee
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    if request.method == 'POST':
        data = (
            request.form['first_name'],
            request.form['last_name'],
            request.form['mobile_no'],
            request.form['email'],
            request.form['gender'],
            request.form['birth_date'],
            request.form['country'],
            request.form['city'],
            id
        )
        c.execute('UPDATE employee SET first_name=?, last_name=?, mobile_no=?, email=?, gender=?, birth_date=?, country=?, city=? WHERE id=?', data)
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    c.execute('SELECT * FROM employee WHERE id=?', (id,))
    employee = c.fetchone()
    conn.close()
    return render_template('edit_employee.html', employee=employee)

# Delete Employee
@app.route('/delete/<int:id>')
def delete_employee(id):
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    c.execute('DELETE FROM employee WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
