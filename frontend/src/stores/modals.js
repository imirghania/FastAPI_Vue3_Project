import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useModalStore = defineStore('modals', () => {
  const productEditModal = ref({ isOpen: false });

  function toggleProductEditModal() {
    productEditModal.value.isOpen = !productEditModal.value.isOpen;
  }

  return { productEditModal, toggleProductEditModal };
});
