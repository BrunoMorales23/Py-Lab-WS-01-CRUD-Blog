from flask import Flask, render_template, request, abort, jsonify
from datetime import date
import os
import json

app = Flask(__name__)
json_path = 'C:/Users/MarsuDIOS666/Desktop/MAIN REP/data.json'

@app.route('/', methods=['POST', 'GET'])
def main():
    datos = load_data(json_path)
    action = request.form.get("action")
    print(action)
    if action == "aceptar":
        id = len(datos)
        id = int(id) + 1
        text_title = request.form.get('text_title')
        text_content = request.form.get('text_content')
        date_time = str(date.today())
        new_data = {
            "id": id,
            "contentTitle": text_title,
            "content": text_content,
            "date": date_time
        }
        datos.append(new_data)
        datos = sorted(datos, reverse=True, key=lambda x: x["id"])
        save_data(json_path, datos)
    else:
        datos = sorted(datos, reverse=True, key=lambda x: x["id"])
        save_data(json_path, datos)
    return render_template('index.html', contenido = datos)

@app.route('/log/<int:id>',methods=['POST','GET'])
def view_log(id):
    datos = load_data(json_path)
    id_url = next((item for item in datos if item.get('id') == id), None)
    if id_url:
        return render_template('refLog.html', data = id_url)

def load_data(json_path):
    with open(json_path, 'r', encoding="UTF-8") as data:
        datos = json.load(data)
    return datos

def save_data(json_path, data):
    with open(json_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    app.run(debug=True)