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
import { useToast } from "vue-toastification";

const toast = useToast();

const tasks = ref([]);

const loadTasks = async () => {
  try {
    const response = await getTasks();
    tasks.value = response.data;
  } catch (error) {
    console.error("Error al cargar tareas:", error);
    toast.error("Error al cargar tareas");
  }
};

const handleAddTask = async (taskData) => {

  const { title, description } = taskData;

  if (!title || !description) {
    toast.warning("Por favor, completa los campos vacíos.");
    return;
  }

  try {
    await addTask(taskData);
    await loadTasks();
    toast.success("Tarea agregada correctamente");
  } catch (error) {
    console.error("Error al agregar tarea:", error);
    toast.error("Error al agregar tarea");
  }
};

const removeTask = async (id) => {
  try {
    await deleteTask(id);
    await loadTasks();
    toast.success("Tarea eliminada correctamente");
  } catch (error) {
    console.error("Error al eliminar tarea:", error);
    toast.error("Error al eliminar tarea");
  }
};

const markCompletedTask = async (id) => {
  try {
    await markTask(id);
    await loadTasks();
  } catch (error) {
    console.error("Error al marcar tarea:", error);
    toast.error("Error al marcar tarea");
  }
};

onMounted(() => {
  loadTasks();
});
</script>
