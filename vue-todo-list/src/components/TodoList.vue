<template>
  <div class="d-flex align-items-center justify-content-between my-4 border-bottom fs-3 pb-2">
    <h2>{{ listTitle }}</h2>
    <b-badge variant="warning">{{ list.length }}</b-badge>
  </div>
  <b-list-group>
    <TodoListItem 
      v-for="item in list" 
      :key="item.id" 
      :item="item"
      @onDone="setDoneTodo(item)" 
      @onRemove="removeTodo(item)" 
    />
  </b-list-group>
</template>

<script setup>
  import TodoListItem from '@c/TodoListItem.vue'

  const props = defineProps({
    listTitle: {
      type: String,
      default: 'List'
    },
    list: {
      type: Array,
      default: []
    }
  })

  const emit = defineEmits(['onDone', 'onRemove'])

  const setDoneTodo = (item) => {
    emit('onDone', item)
  }

  const removeTodo = (item) => {
    emit('onRemove', item)
  }
</script>