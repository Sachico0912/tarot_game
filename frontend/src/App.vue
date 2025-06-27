<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">塔羅牌抽籤</h1>
    
    <button @click="drawCard" class="bg-purple-600 text-white px-4 py-2 rounded">
      抽一張牌 🔮
    </button>

    <div v-if="card" class="mt-6 p-4 border rounded shadow">
      <h2 class="text-xl font-semibold">{{ card.card.name }}（{{ card.position }}）</h2>

      <!-- 顯示圖片 -->
      <img
        v-if="card.card.image"
        :src="getImageUrl(card.card.image)"
        alt="塔羅牌圖片"
        class="w-32 h-auto my-2"
      />
      <br>
      <!-- AI 解釋按鈕 -->
      <button @click="getExplanation" class="mt-4 bg-green-600 text-white px-3 py-1 rounded">
        請AI解釋
      </button>

      <!-- 顯示 Gemini AI 解釋 -->
      <div v-if="aiExplanation" class="mt-4 p-3 bg-yellow-50 border rounded">
        <h3 class="font-bold mb-1">🌟 AI 說：</h3>
        <p>{{ aiExplanation }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const card = ref(null)
const aiExplanation = ref('') // 放 Gemini 回傳的文字

const drawCard = async () => {
  const res = await fetch('http://localhost:8000/api/draw_card/')
  const data = await res.json()
  card.value = data
  aiExplanation.value = '' // 清空舊的解釋
}

const getImageUrl = (path) => {
  return 'http://localhost:8000' + path
}

const getExplanation = async () => {
  if (!card.value) return

  try {
    const res = await fetch('http://localhost:8000/api/explain_card/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: card.value.card.name,
        position: card.value.position
      })
    })

    if (!res.ok) {
      const errorText = await res.text()
      throw new Error(`伺服器錯誤：${res.status} - ${errorText}`)
    }

    const data = await res.json()

    if (data.explanation) {
      aiExplanation.value = data.explanation
    } else if (data.error) {
      aiExplanation.value = `❗AI 回傳錯誤：${data.error}`
    } else {
      aiExplanation.value = '⚠️ 無法取得 AI 解釋，請稍後再試。'
    }

  } catch (err) {
    console.error('AI 解釋失敗：', err)
    aiExplanation.value = '🚫 無法連接 AI 伺服器或發生錯誤'
  }
}
</script>