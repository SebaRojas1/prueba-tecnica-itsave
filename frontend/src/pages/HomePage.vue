<template>
  <div
    class="max-w-3xl mx-auto p-6 mt-16 sm:mt-8 bg-gray-50 rounded-lg shadow-md"
  >
    <h1 class="text-3xl font-bold mb-6 text-gray-800 text-center">
      Lista de Tareas
    </h1>
    <div class="text-center">
      <TaskForm @submit="handleAddTask" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import {
  getTasks,
  addTask,
  deleteTask,
  markTask,
} from "@/services/taskService";
import TaskForm from "@/components/TaskForm.vue";

const tasks = ref([]);
const newTask = ref({
  title: "",
  description: "",
});

const loadTasks = async () => {
  const response = await getTasks();
  tasks.value = response.data;
};

const handleAddTask = async (newTask) => {
  if (!newTask.title || !newTask.description) return;
  await addTask(newTask);
  newTask = { title: "", description: "" };
  await loadTasks();
};

const removeTask = async (id) => {
  await deleteTask(id);
  await loadTasks();
};

const markCompletedTask = async (id) => {
  await markTask(id);
  await loadTasks();
};

onMounted(() => {
  loadTasks();
});
</script>
