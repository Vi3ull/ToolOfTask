<template>
  <b-list-group-item>
    <div class="d-flex justify-content-between align-items-center">
      <b-form-checkbox 
        @click="onDone"
        :checked="item.status === true"
        :disabled="item.status === true"
      >
        {{ item.title }}
      </b-form-checkbox>
      <b-button 
        class="ms-2 p-1 lh-1" 
        variant="outline-danger"
        size="sm"
        @click="onRemove"
      >
        <BootstrapIcon
          icon="x-lg"
          size="md"
        />
      </b-button>
    </div>

  </b-list-group-item>
</template>

<script setup>
  import BootstrapIcon from '@dvuckovic/vue3-bootstrap-icons';

  
  const props = defineProps({
    item: {
      type: Object
    }
  })

  const emit = defineEmits(['onDone', 'onRemove'])

  const onDone = () => {
    emit('onDone')
  }

  const onRemove = () => {
    emit('onRemove')
  }
</script>