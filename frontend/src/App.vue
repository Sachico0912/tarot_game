<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">塔羅牌抽籤</h1>
    <button @click="drawCard" class="bg-purple-600 text-white px-4 py-2 rounded">
      抽一張牌 🔮
    </button>

    <div v-if="card" class="mt-6 p-4 border rounded shadow">
      <h2 class="text-xl font-semibold">{{ card.card.name }}（{{ card.position }}）</h2>
      <!-- 這裡我要再加上圖片 -->
         <img
          v-if="card.card.image"
          :src="getImageUrl(card.card.image)"
          alt="塔羅牌圖片"
          class="w-32 h-auto my-2"
        />
      <p class="mt-2">{{ card.meaning }}</p>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue' //從 Vue 中匯入 ref，用來建立響應式變數。

  const card = ref(null) 

  const drawCard = async () => {
    const res = await fetch('http://localhost:8000/api/draw_card/')
    const data = await res.json()
    card.value = data
  }

  const getImageUrl = (path) => {
    return 'http://localhost:8000' + path
  }

</script>