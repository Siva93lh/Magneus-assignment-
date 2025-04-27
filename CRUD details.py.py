
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
employee_data = []

@app.route('/')
def home():
    return redirect(url_for('employee_list'))

@app.route('/employee/create', methods=['GET', 'POST'])
def create_employee():
    if request.method == 'POST':
        employee = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'mobile': request.form['mobile'],
            'dob': request.form['dob'],
            'gender': request.form['gender'],
            'address': request.form['address'],
        }
        employee_data.append(employee)
        return redirect(url_for('employee_list'))
    return render_template('create_employee.html')

@app.route('/employee')
def employee_list():
    return render_template('list_employee.html', employees=employee_data)

@app.route('/employee/edit/<int:index>', methods=['GET', 'POST'])
def edit_employee(index):
    employee = employee_data[index]
    if request.method == 'POST':
        employee_data[index] = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'mobile': request.form['mobile'],
            'dob': request.form['dob'],
            'gender': request.form['gender'],
            'address': request.form['address'],
        }
        return redirect(url_for('employee_list'))
    return render_template('edit_employee.html', employee=employee)

@app.route('/employee/delete/<int:index>')
def delete_employee(index):
    employee_data.pop(index)
    return redirect(url_for('employee_list'))

if __name__ == "__main__":
    app.run(debug=True)
