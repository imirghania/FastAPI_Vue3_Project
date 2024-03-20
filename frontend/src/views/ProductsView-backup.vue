<template>
  <MainLayout>
    <template #margin>
      <h1 class="text-3xl text-center text-zinc-600 pt-1">Products</h1>
    </template>
    <template #main>
      <div class="overflow-x-auto">
        <table class="table" v-if="products.length != 0">
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
              v-for="(product, index) in products"
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
                  @click="isModalOpen = true"
                >
                  Edit
                </button>
                <button class="btn btn-error btn-xs">Delete</button>
                <!-- modal -->
                <ProductAddEditModal
                  :open="isModalOpen"
                  @close-modal="closeModal()"
                  :product="product"
                />
              </td>
            </tr>
          </tbody>
        </table>
        <div v-else>
          <h1>No Products registered.</h1>
        </div>
      </div>
    </template>
  </MainLayout>
</template>

<script setup>
import MainLayout from '@/layouts/MainLayout.vue';
import ProductAddEditModal from '@/components/modals/productAddEditModal.vue';
import axios from 'axios';
import { ref, onMounted } from 'vue';

// onMount
const products = ref([]);
onMounted(async () => {
  const { data } = await axios.get('http://localhost:8000/products');
  products.value = data;
});

// modal
const isModalOpen = ref(false);
function closeModal(off) {
  isModalOpen.value = off;
}
</script>
