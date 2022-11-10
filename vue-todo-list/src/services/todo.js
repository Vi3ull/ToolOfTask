import axios from 'axios'
import instance from './instance'

export default class Api {
  
  static getTodoList(payload) {
    return instance.get('/todos', payload)
  }

  static updateTodoList(payload) {
    return instance.post('/todos', payload)
  }

  static updateTodoListItem(payload) {
    return instance.put(`/todos/${payload.id}`, payload)
  }

  static deleteTodoListItem(payload) {
    return instance.delete(`/todos/${payload.id}`, payload)
  }
}