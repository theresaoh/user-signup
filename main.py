from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def display_form():
   return render_template('base.html')

@app.route('/welcome', methods = ['POST', 'GET'])
def welcome():
    #retrieving form data
    username = request.form["Username"]
    password = request.form["Password"]
    verify_password = request.form["Verify-Password"]
    email = request.form["Email"]
    #declaring empty error variables
    username_error = ""
    password_error = ""
    password_match_error = ""
    email_error = ""

    #setting different error messages for various invalid or incomplete field entries
    if username == "":
        username_error = "Please enter a username"
    if password == "":
        password_error = "Please enter a password"
    if len(password) < 3 or len(password) > 20 or " " in password:
        password_error = "Please enter a valid password (passwords must be between 3-20 characters)"
    if verify_password == "":
        password_match_error = "Please enter a valid password (passwords must be between 3-20 characters)"
    if verify_password != password:
        password_match_error = "Passwords do not match"
    if email != "":
        if "@" not in email or "." not in email or len(email) < 3 or len(email) > 20 or " " in email:
            email_error = "Please enter a valid email address"

    #if there are no errors, welcome the new user
    if password_error == "" and username_error == "" and password_match_error == "" and email_error == "":
        return render_template('welcome.html', username=username)
    #if there are any errors, render the form again with the proper error message displayed
    else:
        return render_template('base.html', username=username, email=email, username_error=username_error, password_error=password_error, password_match_error=password_match_error, email_error=email_error)

if __name__ == '__main__':
   app.run(debug = True)