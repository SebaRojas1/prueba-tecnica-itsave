<template>
  <li
    class="bg-white rounded-lg shadow-sm p-4 border-l-4 transition-all duration-200"
    :class="{
      'border-green-500': task.is_completed,
      'border-amber-500': !task.is_completed,
    }"
  >
    <div class="flex justify-between items-center">
      <div class="flex-1">
        <div class="flex items-center gap-2">
          <h3
            class="font-bold text-lg transition-opacity duration-200"
            :class="{
              'line-through text-gray-500 opacity-60': task.is_completed,
              'text-gray-800 opacity-100': !task.is_completed,
            }"
          >
            {{ task.title }}
          </h3>

          <span
            class="text-xs font-medium px-2 py-1 rounded-full"
            :class="{
              'bg-green-100 text-green-800': task.is_completed,
              'bg-amber-100 text-amber-800': !task.is_completed,
            }"
          >
            {{ task.is_completed ? "Completada" : "Pendiente" }}
          </span>
        </div>

        <p
          class="mt-1 transition-opacity duration-200"
          :class="{
            'line-through text-gray-400 opacity-60': task.is_completed,
            'text-gray-600 opacity-100': !task.is_completed,
          }"
        >
          {{ task.description }}
        </p>
      </div>

      <div class="flex gap-2">
        <button
          @click="toggleTask"
          class="p-2 rounded-md transition-colors duration-200 flex items-center justify-center"
          :class="
            task.is_completed
              ? 'bg-green-100 text-green-700 hover:bg-green-200'
              : 'bg-amber-100 text-amber-700 hover:bg-amber-200'
          "
          title="Marcar como completada"
        >
          <component
            :is="task.is_completed ? CheckSquare : Square"
            class="w-5 h-5"
          />
        </button>
        <button
          @click="showModal = true"
          class="bg-red-100 text-red-700 hover:bg-red-200 p-2 rounded-md transition-colors duration-200 flex items-center justify-center"
          title="Eliminar"
        >
          <TrashIcon class="w-4 h-4" />
        </button>
      </div>
    </div>

    <ConfirmModal v-model="showModal" @confirm="confirmDelete" />
  </li>
</template>

<script setup>
import { ref } from "vue";
import { TrashIcon, CheckSquare, Square } from "lucide-vue-next";
import ConfirmModal from "./ConfirmModal.vue";

const props = defineProps({
  task: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(["toggle", "delete"]);

const showModal = ref(false);

const toggleTask = () => {
  emit("toggle", props.task.id);
};

const confirmDelete = () => {
  emit("delete", props.task.id);
  showModal.value = false;
};
</script>
