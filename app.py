from http.client import HTTPException

from flask import Flask, redirect
from pydantic import BaseModel

import reg

app = Flask(__name__)

from flask import request
class New_User(BaseModel):
    name: str
    email: str
    role: str
    country: str
    nationality: str
    mobile: str
    password: str

@app.route('/login')
def login():
    return '''
        <form method="post">
            <p>User Name: <input type="text" name="username"></p>
            <p>password : <input type="password" name="password"></p>
            <p>Submit   : <input type="submit" value="Login"></p>
        </form>
    '''


@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    user = reg.login(username, password)

    if user.role == "admin":
        return redirect('/admin')
    elif user.role == "student":
        return redirect('/student')
    elif user.role == "staff":
        return redirect('/staff')
    elif user.role == "editor":
        return redirect('/editor')
    else:
        return "Roles not found"


@app.route('/admin')
def admin_dashboard():
    # return {"message": "Welcome to the admin dashboard!"}
    return '''
        <h1>Welcome to the Admin page</h1>
    '''


@app.route("/student", )
def student_dashboard():
    return '''
            <h1>Welcome to the Student page</h1>
        '''


@app.route("/staff", )
def staff_dashboard():
    return '''
            <h1>Welcome to the Staff page</h1>
        '''


@app.route("/editor", )
def editor_dashboard():
    return '''
            <h1>Welcome to the Editor page</h1>
        '''


@app.route('/register')
def register():
    return '''
        <form method="post">
            <p>Name: <input type="text" required pattern="[a-zA-Z]+" name="name"></p>
            <p>Email: <input type="email" required pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$" name="email"></p>
            <p>Role: <input type="text" required name="role"></p>
            <p>Country: <input type="text" required name="country"></p>
            <p>Nationality: <input type="text" name="nationality"></p>
            <p>Mobile: <input type="int" name="mobile" required pattern="[0-9]{10}"></p>
            <p> Password: <input type="password" id="password" name="password" required></p>
            <p>Submit: <input type="submit" value="register"></p>
        </form>            
    '''


@app.route('/register', methods=['POST'])
def register_post():
    name = request.form['name']
    email = request.form['email']
    role = request.form['role']
    country = request.form['country']
    nationality = request.form['nationality']
    mobile = request.form['mobile']
    password = request.form['password']
    reg.reg_user(name, email, role, country, nationality, mobile, password)
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
