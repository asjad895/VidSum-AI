from flask import Flask
from VidSumAI.logger import logging
app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    logging.info("Starting")
    return "Testing Application"

if __name__=='__main__':
    app.run(debug=True)

    