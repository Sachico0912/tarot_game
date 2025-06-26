<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">線上塔羅牌遊戲</h1>
    <button @click="drawCards" class="bg-purple-600 text-white px-4 py-2 rounded">
      抽三張牌 🔮
    </button>

    <div v-if="cards.length" class="mt-6 space-y-4">
      <div v-for="(card, index) in cards" :key="index" class="p-4 border rounded shadow">
        <h2 class="text-xl font-semibold">第 {{ index + 1 }} 張 - {{ card.card.name }}（{{ card.position }}）</h2>
        <!-- 這裡我要再加上圖片 -->
         <!-- <img
          v-if="card.card.image"
          :src="getImageUrl(card.card.image)"
          alt="塔羅牌圖片"
          class="w-32 h-auto my-2"
        /> -->
        <p>{{ card.meaning }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue' //從 Vue 中匯入 ref，用來建立響應式變數。

const cards = ref([]) //建立一個空的陣列 cards，用來存放抽到的塔羅牌資訊。

const drawCards = async () => {
  const res = await fetch('http://127.0.0.1:8000/api/draw_cards/') // 向本地後端發送 GET 請求
  cards.value = await res.json() //解析回傳的 JSON，指派給 cards.value，觸發畫面更新。
}
</script>