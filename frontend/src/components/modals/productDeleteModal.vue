<template>
  <dialog
    id="my_modal_1"
    class="modal"
    :open="open"
    ref="modalRef"
    @keyup.esc="turnOffModal()"
  >
    <div class="modal-box px-10">
      <h3 class="font-bold text-lg text-red-500">Delete</h3>
      <p class="py-3">Are you sure that you to delete this product?</p>
      <div class="flex justify-end mt-4">
        <button
          type="submit"
          class="btn btn-error mr-2"
          @click="deleteProduct(productId)"
        >
          Delete
        </button>
        <button class="btn btn-accent" @click="closeModal()">Cancel</button>
      </div>
    </div>
  </dialog>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useProductStore } from '@/stores/products';
import { useRouter } from 'vue-router';
// import { onClickOutside } from '@vueuse/core';

// props
const props = defineProps({
  open: {
    type: Boolean,
  },
  productId: {
    type: Number,
  },
});

// Store
const productStore = useProductStore();

// emits
const emit = defineEmits(['closeDelModal']);

// close the modal
const modalRef = ref(null);
// const formRef = ref(null);

function closeModal() {
  emit('closeDelModal', false);
}

// onClickOutside(modalRef, turnOffModal, {
//   ignore: [formRef],
// });

const handleKeyboard = (e) => {
  if (e.key === 'Escape') closeModal();
};

onMounted(() => {
  document.addEventListener('keyup', handleKeyboard);
});
onUnmounted(() => {
  document.removeEventListener('keyup', handleKeyboard);
});

// Remove Product
const router = useRouter();
const deleteProduct = (productId) => {
  productStore.removeProduct(productId);
  closeModal();
  router.go();
};
</script>
