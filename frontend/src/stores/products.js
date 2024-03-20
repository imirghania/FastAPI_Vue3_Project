import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import { useInitializeStore } from '@/use/useInitializeStore';
import axios from 'axios';

export const useProductStore = defineStore('products', () => {
  const products = ref([]);

  async function fetchProducts() {
    try {
      const response = await axios.get('http://localhost:8000/products');
      products.value = response.data;
      // console.log('From store [products] ', products.value);
    } catch (error) {
      console.log('Fetching products Failed, ', error);
    }
  }

  const { initialized, loading } = useInitializeStore(fetchProducts);

  const getProducts = computed(() => {
    return products.value;
  });

  const productsCount = computed(() => {
    return products.value.length;
  });

  const getProductById = (productId) => {
    return products.value.find((prod) => {
      return prod.id == productId;
    });
  };

  const filterProductOut = (productId) => {
    return products.value.filter((prod) => {
      return prod.id != productId;
    });
  };

  const removeProduct = (productId) => {
    try {
      const { status } = axios.delete(
        `http://localhost:8000/products/${productId}`
      );
      if (status == 202) {
        products.value = filterProductOut(productId);
      }
    } catch (error) {
      console.log('An Error occured during product deletion ', error);
    }
  };

  return {
    products,
    loading,
    initialized,
    getProducts,
    productsCount,
    getProductById,
    removeProduct,
  };
});
