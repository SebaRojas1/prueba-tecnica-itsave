<template>
  <form @submit.prevent="handleSubmit" class="mb-4">
    <input
      v-model="taskData.title"
      type="text"
      placeholder="Título"
      class="border p-2 mr-2"
      required
    />
    <input
      v-model="taskData.description"
      type="text"
      placeholder="Descripción"
      class="border p-2 mr-2"
      required
    />
    <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">
      Agregar Tarea
    </button>
  </form>
</template>

<script setup>
import { ref } from "vue";

const props = defineProps({
  defaultValues: {
    type: Object,
    default: () => ({ title: "", description: "" }),
  },
});

const emit = defineEmits(["submit"]);

const taskData = ref({ ...props.defaultValues });

const handleSubmit = () => {
  if (!taskData.value.title || !taskData.value.description) return;
  emit("submit", { ...taskData.value });
  taskData.value = { title: "", description: "" };
};
</script>
