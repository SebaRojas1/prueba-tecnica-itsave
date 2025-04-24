<template>
  <div
    v-if="modelValue"
    class="fixed inset-0 bg-black/30 flex items-center justify-center z-50"
  >
    <div
      class="bg-white p-6 rounded-lg shadow-lg text-center space-y-4 w-[90%] max-w-sm"
    >
      <h2 class="text-lg font-semibold text-gray-800">{{ title }}</h2>
      <p class="text-gray-600">{{ message }}</p>
      <div class="flex justify-center gap-4 mt-4">
        <button
          @click="$emit('confirm')"
          class="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600 transition cursor-pointer"
        >
          {{ confirmText }}
        </button>
        <button
          @click="$emit('update:modelValue', false)"
          class="bg-gray-200 text-gray-700 px-4 py-2 rounded hover:bg-gray-300 transition cursor-pointer"
        >
          {{ cancelText }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  modelValue: Boolean,
  title: {
    type: String,
    default: "¿Estás seguro?",
  },
  message: {
    type: String,
    default: "Esta acción no se puede deshacer.",
  },
  confirmText: {
    type: String,
    default: "Sí, eliminar",
  },
  cancelText: {
    type: String,
    default: "Cancelar",
  },
});

defineEmits(["update:modelValue", "confirm"]);
</script>
