<template>
  <li
    class="bg-white rounded-lg shadow-sm p-4 border-l-4"
    :class="{
      'border-green-500': task.is_completed,
      'border-amber-500': !task.is_completed,
    }"
  >
    <div class="flex justify-between items-center">
      <div class="flex-1">
        <div class="flex items-center gap-2">
          <h3
            class="font-bold text-lg"
          >
            {{ task.title }}
          </h3>
        </div>

        <p
          class="mt-1"
        >
          {{ task.description }}
        </p>
      </div>

      <div class="flex gap-2">
        <button
          @click="toggleTask"
          class="px-4 py-2 rounded-md font-semibold"
          :class="
            task.is_completed
              ? 'bg-green-100 text-green-700 hover:bg-green-200'
              : 'bg-amber-100 text-amber-700 hover:bg-amber-200'
          "
        >
          {{ task.is_completed ? "Desmarcar" : "Marcar" }}
        </button>

        <button
          @click="deleteTask"
          class="bg-red-100 text-red-700 hover:bg-red-200 px-4 py-2 rounded-md font-semibold"
        >
          Eliminar
        </button>
      </div>
    </div>
  </li>
</template>

<script setup>
const props = defineProps({
  task: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(["toggle", "delete"]);

const toggleTask = () => {
  emit("toggle", props.task.id);
};

const deleteTask = () => {
  emit("delete", props.task.id);
};
</script>
