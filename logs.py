from flask import Flask
from src.logger import logging

app= Flask(__name__)

@app.route('/', methods=['GET','POST'])

def index():
    logging.info('Starting to test our logging file')

    return "Welcome to my ML project! by Nnamdi Daniel Aghanya"

if __name__ == '__main__':
    app.run(debug=True)#5000