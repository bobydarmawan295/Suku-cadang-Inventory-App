from app import app
from app.controller import OfficerController

@app.route('/')
def index():
    return "Hello Flask"

@app.route('/officer', methods=['GET'])
def officer():
    return OfficerController.index()
