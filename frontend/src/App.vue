<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">線上塔羅牌抽籤</h1>
    <button @click="drawCards" class="bg-purple-600 text-white px-4 py-2 rounded">
      抽三張牌 🔮
    </button>

    <div v-if="cards.length" class="mt-6 space-y-4">
      <div v-for="(card, index) in cards" :key="index" class="p-4 border rounded shadow">
        <h2 class="text-xl font-semibold">第 {{ index + 1 }} 張 - {{ card.card.name }}（{{ card.position }}）</h2>
        <p>{{ card.meaning }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const cards = ref([])

const drawCards = async () => {
  const res = await fetch('http://127.0.0.1:8000/api/draw/')
  cards.value = await res.json()
}
</script>