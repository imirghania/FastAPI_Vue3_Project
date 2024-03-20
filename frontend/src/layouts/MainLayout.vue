<template>
  <div class="flex flex-row h-screen">
    <div class="basis-1/5 h-screen bg-cyan-100">
      <slot name="margin">Margin</slot>
    </div>
    <div class="basis-full p-2">
      <slot name="main">Main</slot>
    </div>
  </div>
</template>
