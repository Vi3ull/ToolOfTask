from flask import Flask, jsonify, request
from flask_cors import CORS

import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__)
CORS(app)

engine = create_engine('sqlite:///db.sqlite')
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()


from models import *


Base.metadata.create_all(bind=engine)

@app.route('/todos', methods=['GET'])
def getTodoList():
  todos = Todo.query.all()
  serialized = []

  for todo in todos:
    serialized.append({
      'id': todo.id,
      'title': todo.title,
      'description': todo.description,
      'status': todo.status,
    })

  return jsonify(serialized)

@app.route('/todos', methods=['POST'])
def updateTodoList():
  newTodo = Todo(**request.json)
  session.add(newTodo)
  session.commit()
  serialized = {
    'id': newTodo.id,
    'title': newTodo.title,
    'description': newTodo.description,
    'status': newTodo.status,
  }
  return jsonify(serialized)

@app.route('/todos/<int:itemId>', methods=['PUT'])
def updateTodoListItem(itemId):
  item = Todo.query.filter(Todo.id == itemId).first()
  params = request.json
  
  if not item:
    return {'message': 'No todos with this ID'}, 400
  
  for key, value in params.items():
    setattr(item, key, value)

  session.commit()
  serialized = {
    'id': item.id,
    'title': item.title,
    'description': item.description,
    'status': item.status,
  }

  return serialized

@app.route('/todos/<int:itemId>', methods=['DELETE'])
def deleteTodoListItem(itemId):
  item = Todo.query.filter(Todo.id == itemId).first()
  
  if not item:
    return {'message': 'No todos with this ID'}, 400
  
  session.delete(item)
  session.commit()
  return '', 204

@app.teardown_appcontext
def shutdown_session(exception=None):
  session.remove()

if __name__ == '__main__':
  app.run()