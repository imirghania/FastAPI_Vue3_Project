<template>
  <dialog
    id="my_modal_1"
    class="modal"
    :open="open"
    ref="modalRef"
    @keyup.esc="turnOffModal()"
  >
    <div class="modal-box px-10">
      <h3 class="font-bold text-lg">{{ title }}</h3>
      <ProductAddEditForm @form-close-modal="turnOffModal()" :id="productId" />
    </div>
  </dialog>
</template>

<script setup>
import { ref, watch } from 'vue';
// import { onClickOutside } from '@vueuse/core';
import ProductAddEditForm from '@/components/forms/productAddEditForm.vue';
import { useProductStore } from '@/stores/products';

// props
const props = defineProps({
  open: {
    type: Boolean,
  },
  productId: {
    type: Number,
  },
  title: {
    type: String,
  },
});

// emits
const emit = defineEmits(['closeModal']);

// close the modal
const modalRef = ref(null);
// const formRef = ref(null);

function turnOffModal() {
  emit('closeModal', false);
}

// onClickOutside(modalRef, turnOffModal, {
//   ignore: [formRef],
// });
</script>
