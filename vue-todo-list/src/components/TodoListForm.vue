<template>
  <b-form 
    class="d-flex flex-grow-1"
    @submit.prevent="onAddTodo"
  >
    <b-input-group>
      <b-form-input
        placeholder="Add a new todo..."
        v-model="title"
        ref="inputRef"
        required
      />
      <b-input-group-append>
        <b-button 
          type="submit"
          variant="primary"
        >
          Add
        </b-button>
      </b-input-group-append>
    </b-input-group>
  </b-form>
</template>

<script setup>
  import { ref } from 'vue'

  const emit = defineEmits(['onAddTodo'])

  const inputRef = ref(null)
  const title = ref('')

  const onAddTodo = () => {
    emit('onAddTodo', { title: title.value, input: inputRef.value.input  })
    title.value = ''
  }

</script>