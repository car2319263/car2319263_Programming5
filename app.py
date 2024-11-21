# Carla Aleman
# CIS265
# Programming 5

from flask import Flask, request, render_template_string
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
# Route to display the login form
@app.route('/login', methods=['GET'])
# Route to handle for submission
@app.route('/login', methods=['POST'])

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