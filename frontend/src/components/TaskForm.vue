<template>
  <form
    @submit.prevent="handleSubmit"
    class="mb-6 bg-white p-4 rounded-lg shadow-sm"
  >
    <div class="flex flex-col md:flex-row gap-3">
      <Input v-model="taskData.title" placeholder="Título" />
      <Input v-model="taskData.description" placeholder="Descripción" />
      <button
        type="submit"
        class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md transition duration-200 ease-in-out flex items-center justify-center cursor-pointer"
      >
        <span>Agregar</span>
      </button>
    </div>
  </form>
</template>

<script setup>
import { ref } from "vue";
import Input from "./Input.vue";

const props = defineProps({
  defaultValues: {
    type: Object,
    default: () => ({ title: "", description: "" }),
  },
});

const emit = defineEmits(["submit"]);

const taskData = ref({
  title: props.defaultValues.title,
  description: props.defaultValues.description,
});

const handleSubmit = () => {
  emit("submit", { ...taskData.value });
  taskData.value = { title: "", description: "" };
};
</script>
