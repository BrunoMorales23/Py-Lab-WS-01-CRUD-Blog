from flask import Flask, render_template, request
import json

app = Flask(__name__)
json_path = 'C:/Users/MarsuDIOS666/Desktop/MAIN REP/data.json'

@app.route('/', methods=['POST', 'GET'])
def main():
    datos = load_data(json_path)
    action = request.form.get("action")
    print(action)
    if action == "aceptar":
        text_title = request.form.get('text_title')
        text_content = request.form.get('text_content')
        new_data = {
            "contentTitle": text_title,
            "content": text_content
        }
        datos.append(new_data)
        save_data(json_path, datos)

    return render_template('index.html', contenido = datos)

def load_data(json_path):
    with open(json_path, 'r', encoding="UTF-8") as data:
        datos = json.load(data)
    return datos

def save_data(json_path, data):
    with open(json_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    app.run(debug=True)