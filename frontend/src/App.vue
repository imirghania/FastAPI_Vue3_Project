<template>
  <div class="container mx-auto px-4">
    <NavBar />
    <RouterView />
  </div>
</template>

<script setup>
import NavBar from '@/components/NavBarComponent.vue';
</script>

<style lang="scss" scoped></style>
