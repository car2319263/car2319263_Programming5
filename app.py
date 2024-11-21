# Carla Aleman
# CIS265
# Programming 5

from flask import Flask, request, render_template_string
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
# Route to display the login form
@app.route('/login', methods=['GET'])
# Function to render HTML form
def login_form():
    # Form design, include username, password, and submit
    form_html = '''
    <form action="/login" method="POST">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password" required>
        <button type="submit">Login</button>
    </form>
    '''
    return render_template_string(form_html)

# Route to handle form submission
@app.route('/login', methods=['POST'])
# Function to render HTML submit form
def login_submit():
    username = request.form['username']
    password = request.form['password']

    # Input validation
    if not all(c.isalnum() or c == '_' for c in username):
        return "Invalid username. Only alphanumeric characters and underscores are allowed."
    if len(password) < 8 or not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
        return "Password must be at least 8 characters long and contain both letters and numbers."

    # Hash the password (not displayed)
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Display success message
    return f'''
            <p>Username: {username}, Password: {password}</p></br></br></br>
            <p>(Hashed password: {hashed_password}) </p>
    '''


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
