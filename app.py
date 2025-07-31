from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Render!"

# Don't need app.run() when using gunicorn
