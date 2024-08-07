from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)
def getDbConnection():
    connection= mysql.connector.connect(
        host="db",  # db refers to the MySQL service in Docker Compose
        user="root",
        password="password",
        database="todo_db"
    )
    return connection

@app.route('/todos', methods=['GET'])
def get_todos():
    connection = getDbConnection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM todos')
    todos= cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(todos)

@app.route('/todos',methods=['POST'])
def create_todos():
    new_todo = request.json 
    connection = getDbConnection()
    cursor= connection.cursor()
    cursor.execute('INSERT INTO todos(title, completed) VALUES(%s,%s)',(new_todo['title'],new_todo['completed']))
    connection.commit()
    cursor.close()
    connection.close()
    return '', 201 

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    updated_todo = request.json
    connection = getDbConnection()
    cursor = connection.cursor()
    cursor.execute('UPDATE todos SET title = %s, completed= %S WHERE id = %s', 
                    update_todo['title'], update_todo['completed'], id )
    connection.commit()
    cursor.close()
    connection.close()
    return '', 204

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo():
    connection = getDbConnection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM todos WHERE id = %s',(id,))
    cursor.commit()
    cursor.close()
    connection.close()
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
