from flask import Flask
app = Flask(__name__)

# In terminal: flask run --host=127.0.0.1 --port=4000

@app.route('/')
def home():
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True)
