import os,sys
from flask import Flask
from src.logger import logging
from src.exception import CustomException


app= Flask(__name__)

@app.route('/', methods=['GET','POST'])

def index():

    try:
        raise Exception("Test of Exception code")
    except Exception as e:
        ML = CustomException(e, sys)
        logging.info(ML.error_message)
        
        logging.info('Starting to test our logging file')

        return "Welcome to my ML project! by Nnamdi Daniel Aghanya"

if __name__ == '__main__':
    app.run(debug=True)#5000