<template>
  <MainLayout>
    <template #margin>
      <h1 class="text-3xl text-center text-zinc-600 pt-1">Products</h1>
    </template>
    <template #main>
      <div class="overflow-x-auto">
        <table class="table" v-if="productStore.productsCount">
          <!-- head -->
          <thead>
            <tr>
              <th></th>
              <th>Name</th>
              <th>Description</th>
              <th>Quantity</th>
              <th>Price</th>
              <th>Action</th>
            </tr>
          </thead>

          <tbody>
            <tr
              class="hover:bg-base-200"
              v-for="(product, index) in productStore.getProducts"
              :key="product.id"
            >
              <!-- data -->
              <th>{{ index + 1 }}</th>
              <td>{{ product.name }}</td>
              <td>{{ product.description ? product.description : 'N/A' }}</td>
              <td>{{ product.quantity }}</td>
              <td>{{ product.price }}</td>
              <!-- buttons -->
              <td>
                <button
                  class="btn btn-warning btn-xs mr-1"
                  @click="openEditModal(product.id)"
                >
                  Edit
                </button>
                <button
                  class="btn btn-error btn-xs"
                  @click="openDeleteModal(product.id)"
                >
                  Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
        <div v-else>
          <h1>No Products registered.</h1>
        </div>
      </div>
      <!-- modal -->
      <ProductAddEditModal
        :open="isEditModalOpen"
        @close-modal="closeEditModal()"
        :productId="currentProductId"
        title="Edit Product"
      />
      <ProductDeleteModal
        :open="isDeleteModalOpen"
        @close-del-modal="closeDeleteModal()"
        :productId="currentProductId"
      />
    </template>
  </MainLayout>
</template>

<script setup>
import MainLayout from '@/layouts/MainLayout.vue';
import ProductAddEditModal from '@/components/modals/productAddEditModal.vue';
import ProductDeleteModal from '@/components/modals/productDeleteModal.vue';
import { ref, computed } from 'vue';
import { useProductStore } from '@/stores/products';
// import { storeToRefs } from 'pinia';

// const productStore = useProductStore();
const productStore = useProductStore();

// modal
const isEditModalOpen = ref(false);
const isDeleteModalOpen = ref(false);
const currentProductId = ref(-1);

function openEditModal(productId) {
  isEditModalOpen.value = true;
  currentProductId.value = productId;
}

function closeEditModal(off) {
  isEditModalOpen.value = off;
  currentProductId.value = -1;
}

function openDeleteModal(productId) {
  isDeleteModalOpen.value = true;
  currentProductId.value = productId;
}

function closeDeleteModal(off) {
  isDeleteModalOpen.value = off;
}
</script>
