from app.models.officer import Officer

from app import response, app, db
from flask import request

def index():
    try:
        officer = Officer.query.all()
        data = formatarray(officer)
        return response.success(data, "success")
    except Exception as e:
        print(e)

def formatarray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))
    return array

def singleObject(data):
    data = {
        'id' : data.id,
        'no_identitas' : data.no_identitas,
        'nama' : data.nama
    }

    return data



