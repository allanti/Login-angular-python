from db import mydb
from flask import Flask, make_response, jsonify, request


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/login', methods=['POST'])
def validate_login():
    cur = mydb.cursor()
    userDados = request.json
    sql = f"SELECT * FROM usuarios WHERE email = '{userDados['email']}' AND password = '{userDados['password']}'"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close
    return jsonify(data)


@app.route('/add_user', methods=['POST'])
def add():
    cur = mydb.cursor()
    userDados = request.json
    sql = f"INSERT INTO usuarios (name, email, password) VALUES ('{userDados['name']}','{userDados['email']}', '{userDados['password']}')"
    cur.execute(sql)
    mydb.commit()

    return make_response(
        jsonify(
            mensagem='usuario cadastrado com sucesso.'
        )
    )

app.run()