import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("request.form")
    print(request.get_json())
    return 'Hello world!'

if __name__ == '__main__':
    app.run(port=4000)
