<template>
  <b-progress 
  height="6px" 
  class="fixed-top rounded-0"
  :value="loadingPercentage"
  max="100" 
  v-if="isLoading"
  >
  </b-progress>

  <header class="bg-light shadow rounded-bottom rounded-3 py-3">
    <div class="container d-flex align-items-center justify-content-between ">
      <h1 class="text-dark fs-4 fw-bold me-4 mb-0">ToDo List</h1>
      <TodoListForm 
        @onAddTodo="addTodo" 
      />
    </div>
  </header>
  <main class="container my-5 flex-grow-1">
    <b-alert
      v-model="dismissCountDown"
      dismissible
      variant="danger"
      @dismissed="dismissCountDown=0"
      @dismiss-count-down="countDownChanged"
    >
      <p>We're sorry, we're not able to retrieve this information at the moment, please try back later</p>
      <b-progress
        variant="warning"
        :max="dismissSecs"
        :value="dismissCountDown"
        height="4px"
      ></b-progress>
    </b-alert>
    <TodoList 
      :list="todoList" 
      :listTitle="'ToDo'" 
      @onDone="setDoneTodo" 
      @onRemove="deleteTodo" 
    />
  </main>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import TodoList from '@c/TodoList.vue'

  import API from './services/todo'

  const todoList = ref([])

  const isLoading = ref(true)
  const loadingPercentage = ref(0)

  const dismissSecs = 5
  const dismissCountDown = ref(0)
  
  const countDownChanged = (countDown) => {
    dismissCountDown.value = countDown
  }

  const showAlert = () => {
    dismissCountDown.value = dismissSecs
  }

  const config = {
    onUploadProgress: event => {
      loadingPercentage.value = Math.round(
        (event.loaded * 100) / event.total
      );
      isLoading.value = false
    }
  }

  const addTodo = ({ title }) => {
    const newTodo = {
      id: todoList.value[todoList.value.length - 1].id + 1, 
      title, 
      description: '',
      status: false 
    }

    todoList.value = [...todoList.value, newTodo]

    API
      .updateTodoList(newTodo)
      .then(response => response.data)
      .catch(error => {
        console.log(error)
        showAlert()
      })
  }

  const setDoneTodo = (item) => {
    todoList.value = todoList.value.map(el => {
      if (el.id === item.id ) 
        el.status = !el.status 
      return el
    })

    API
      .updateTodoListItem({ 
        ...item,
        status: 1 
      })
      .then(response => response.data)
      .catch(error => {
        console.log(error)
        showAlert()
      })
  }

  const deleteTodo = (item) => {
    todoList.value = todoList.value.filter(el => el.id != item.id)

    API
      .deleteTodoListItem({ id: item.id })
      .then(response => response.data)
      .catch(error => {
        console.log(error)
        showAlert()
      })
  }

  onMounted(() => {
    API
      .getTodoList()
      .then(response => { todoList.value = response.data })
      .catch(error => {
        console.log(error)
        showAlert()
      })
      .finally(() => (isLoading.value = false))
  })
</script>