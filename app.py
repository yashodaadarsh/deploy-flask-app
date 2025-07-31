from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Render!"

@app.route('/about')
def about():
    return "This is the about page."
# The app is ready to be deployed on Render
# Gunicorn will be used as the WSGI server in production
# Don't need app.run() when using gunicorn
