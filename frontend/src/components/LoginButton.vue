<template>
  <button
  @click="handleLogin"
  class=""
  >登入</button>
</template>

<script setup>
function handleLogin() {
  // 這裡寫登入邏輯，例如導向登入頁面
  window.location.href = '/login'
}
</script>
