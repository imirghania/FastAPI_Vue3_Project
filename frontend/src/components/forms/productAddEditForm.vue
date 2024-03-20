<template>
  <form>
    <!-- name field -->
    <label class="form-control grow">
      <div class="label">
        <span class="label-text">Name</span>
      </div>
      <input
        type="text"
        v-model="name"
        v-bind="nameAttrs"
        placeholder="Type here"
        class="input input-bordered grow"
        ref="nameFieldRef"
        name="name"
      />
      <div class="label" v-if="shouldShowError('name')">
        <span class="label-text-alt text-red-500">{{ errors.name }}</span>
      </div>
    </label>
    <!-- price field -->
    <label class="form-control grow">
      <div class="label">
        <span class="label-text">price</span>
      </div>
      <input
        type="text"
        v-model="price"
        v-bind="priceAttrs"
        placeholder="Type here"
        class="input input-bordered grow"
        name="price"
      />
      <div class="label" v-if="shouldShowError('price')">
        <span class="label-text-alt text-red-500">{{ errors.price }}</span>
      </div>
    </label>
    <!-- quantity field -->
    <label class="form-control grow">
      <div class="label">
        <span class="label-text">quantity</span>
      </div>
      <input
        type="text"
        v-model="quantity"
        v-bind="quantityAttrs"
        placeholder="Type here"
        class="input input-bordered grow"
        name="quantity"
      />
      <div class="label" v-if="shouldShowError('quantity')">
        <span class="label-text-alt text-red-500">{{ errors.quantity }}</span>
      </div>
    </label>
    <!-- description field -->
    <label class="form-control grow">
      <div class="label">
        <span class="label-text">Description</span>
      </div>
      <textarea
        v-model="description"
        v-bind="descriptionAttrs"
        placeholder="Type here"
        class="textarea input-bordered grow h-24"
        name="description"
      />
      <div class="label" v-if="errors.description">
        <span class="label-text-alt text-red-500">{{
          errors.description
        }}</span>
      </div>
    </label>
    <!-- cta -->
    <div class="flex justify-end mt-4">
      <button
        type="submit"
        class="btn btn-accent mr-2"
        @click.prevent="onSubmit()"
      >
        Submit
      </button>
      <button class="btn btn-accent" @click="closeModal()">Cancel</button>
    </div>
  </form>
</template>

<script setup>
import { useForm } from 'vee-validate';
import { useProductStore } from '@/stores/products';
import { computed, onMounted, onUnmounted, watch } from 'vue';
import * as yup from 'yup';
// import { storeToRefs } from 'pinia';

const props = defineProps({
  id: {
    type: Number,
  },
});

const productStore = useProductStore();
const currentProduct = computed(() => productStore.getProductById(props.id));

const formSchema = yup.object({
  name: yup.string().required(),
  description: yup.string(),
  price: yup.number().positive().required(),
  quantity: yup.number().positive().required(),
});

const { errors, handleSubmit, defineField, meta, resetForm } = useForm({
  validationSchema: formSchema,
  initialValues: currentProduct.value,
});

const [name, nameAttrs] = defineField('name');
const [description, descriptionAttrs] = defineField('description');
const [price, priceAttrs] = defineField('price');
const [quantity, quantityAttrs] = defineField('quantity');

watch(currentProduct, () => {
  if (currentProduct.value) {
    resetForm({
      values: {
        name: currentProduct.value.name,
        price: currentProduct.value.price,
        quantity: currentProduct.value.quantity,
        description: currentProduct.value.description,
      },
    });
  }
});

function shouldShowError(field) {
  return meta.value.dirty && !!errors.value[field];
}

const onSubmit = handleSubmit((values) => {
  console.log('[Form] Submitted! ', JSON.stringify(values, null, 2));
});

// close modal emit
const emit = defineEmits(['formCloseModal']);

function closeModal() {
  emit('formCloseModal', false);
}

// close modal on pressing esc
const handleKeyboard = (e) => {
  if (e.key === 'Escape') closeModal();
};

onMounted(() => {
  document.addEventListener('keyup', handleKeyboard);
  const currentProduct = productStore.getProductById(props.id);
});
onUnmounted(() => {
  document.removeEventListener('keyup', handleKeyboard);
});
</script>
