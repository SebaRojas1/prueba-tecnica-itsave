<template>
  <div
    class="max-w-3xl mx-auto p-6 mt-16 sm:mt-8 bg-gray-50 rounded-lg shadow-md"
  >
    <h1 class="text-3xl font-bold mb-6 text-gray-800 text-center">
      Lista de Tareas
    </h1>
    <TaskForm @submit="handleAddTask" />
    <div v-if="tasks.length === 0" class="text-center py-8 text-gray-500">
      No hay tareas pendientes. ¡Agrega una nueva tarea!
    </div>
    <ul v-else class="space-y-3">
      <TaskCard
        v-for="task in tasks"
        :key="task.id"
        :task="task"
        @toggle="markCompletedTask"
        @delete="removeTask"
      />
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
import TaskForm from "@/components/TaskForm.vue";
import TaskCard from "@/components/TaskCard.vue";

const tasks = ref([]);

const loadTasks = async () => {
  try {
    const response = await getTasks();
    tasks.value = response.data;
  } catch (error) {
    console.error("Error al cargar tareas:", error);
  }
};

const handleAddTask = async (taskData) => {
  try {
    await addTask(taskData);
    await loadTasks();
  } catch (error) {
    console.error("Error al agregar tarea:", error);
  }
};

const removeTask = async (id) => {
  try {
    await deleteTask(id);
    await loadTasks();
  } catch (error) {
    console.error("Error al eliminar tarea:", error);
  }
};

const markCompletedTask = async (id) => {
  try {
    await markTask(id);
    await loadTasks();
  } catch (error) {
    console.error("Error al marcar tarea:", error);
  }
};

onMounted(() => {
  loadTasks();
});
</script>
