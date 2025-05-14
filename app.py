from flask import Flask, render_template, request, abort, jsonify, redirect, url_for
from datetime import date
import os
import json

app = Flask(__name__)
#json_path = 'C:/Users/MarsuDIOS666/Desktop/MAIN REP/data.json'
#json_path = "C:/Users/bmorales/OneDrive - rmrconsultores.com/Escritorio/Py-Lab-WS-01-CRUD-Blog/data.json"
json_path = "data.json"
current_id = None

@app.route('/', methods=['POST', 'GET'])
def main():
    global current_id
    datos = load_data(json_path)
    action = request.form.get("action")
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

    elif action == "eliminar":
        print(current_id)
        datos = load_data(json_path)
        data_filtrada = [item for item in datos if item["id"] != current_id]
        save_data(json_path, data_filtrada)
        return redirect(url_for('main'))

    else:
        datos = sorted(datos, reverse=True, key=lambda x: x["id"])
        save_data(json_path, datos)
    return render_template('index.html', contenido = datos)


@app.route('/log/<int:id>',methods=['POST','GET'])
def view_log(id):
    global current_id
    action = request.form.get("action")
    print(action)
    if action != "editar":
        datos = load_data(json_path)
        id_url = next((item for item in datos if item.get('id') == id), None)
        current_id = id
        if id_url:
            return render_template('refLog.html', data = id_url)

    else:
        datos = load_data(json_path)
        id_url = next((item for item in datos if item.get('id') == id), None)
        text_title = request.form.get('text_title')
        if text_title == "":
            text_title = id_url['contentTitle']
        text_content = request.form.get('text_content')
        print(text_content)
        if text_content == "":
            text_content = id_url['content']
        if id_url:
            date_time = str(date.today())
            id_url['contentTitle'] = text_title
            id_url['content'] = text_content
            id_url['date'] = date_time
            save_data(json_path, datos)
            return render_template('refLog.html', data = id_url)
    

def load_data(json_path):
    with open(json_path, 'r', encoding="UTF-8") as data:
        datos = json.load(data)
    return datos

def save_data(json_path, data):
    with open(json_path, 'w') as file:
        json.dump(data, file, indent=4)

def get_data(json_path, specific_value):
    data = load_data(json_path)
    specific_value = next((item for item in data if item.get(f'{specific_value}') == specific_value), None)
    return specific_value

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)