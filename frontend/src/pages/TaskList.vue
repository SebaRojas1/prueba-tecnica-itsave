<template>
  <div>
    <h1 class="text-2xl font-bold mb-4">Lista de Tareas</h1>

    <form @submit.prevent="handleAddTask" class="mb-4">
      <input
        v-model="newTask.title"
        type="text"
        placeholder="Título"
        class="border p-2 mr-2"
        required
      />
      <input
        v-model="newTask.description"
        type="text"
        placeholder="Descripción"
        class="border p-2 mr-2"
        required
      />
      <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">
        Agregar Tarea
      </button>
    </form>

    <ul>
      <li
        v-for="task in tasks"
        :key="task.id"
        class="flex justify-between items-center border-b py-2"
      >
        <div>
          <strong>{{ task.title }}</strong> - {{ task.description }} -
          <span
            :class="{
              'text-green-600': task.is_completed,
              'text-red-500': !task.is_completed,
            }"
          >
            {{ task.is_completed ? "Completada" : "Incompleta" }}
          </span>
        </div>
        <div class="flex gap-2">
          <button
            @click="markCompletedTask(task.id)"
            class="bg-yellow-500 text-white px-2 py-1 rounded"
          >
            {{ task.is_completed ? "Desmarcar" : "Marcar" }}
          </button>
          <button
            @click="removeTask(task.id)"
            class="bg-red-600 text-white px-2 py-1 rounded"
          >
            Eliminar
          </button>
        </div>
      </li>
    </ul>
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

const tasks = ref([]);
const newTask = ref({
  title: "",
  description: "",
});

const loadTasks = async () => {
  const response = await getTasks();
  tasks.value = response.data;
};

const handleAddTask = async () => {
  if (!newTask.value.title || !newTask.value.description) return;
  await addTask(newTask.value);
  newTask.value = { title: "", description: "" };
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
