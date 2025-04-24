<template>
  <footer
    class="bg-gradient-to-r from-emerald-400 via-blue-800 to-purple-500 py-8 text-white shadow-lg"
  >
    <div class="container mx-auto px-4">
      <div class="flex flex-col items-center justify-center">
        <div class="mb-4">
          <h3 class="text-2xl font-bold tracking-wide">App Lista de Tareas</h3>
          <div class="mt-2 h-1 w-24 mx-auto bg-white rounded opacity-75"></div>
        </div>
        <p class="text-sm opacity-80 mt-2">Organiza tu día de forma efectiva</p>
        <div class="flex space-x-4 mt-4">
          <a
            href="https://github.com/SebaRojas1"
            class="hover:text-emerald-200 transition-colors duration-300"
          >
            <GithubIcon class="h-6 w-6" />
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { GithubIcon } from "lucide-vue-next";
</script>
