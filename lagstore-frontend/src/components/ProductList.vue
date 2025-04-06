<template>
  <div>
    <h1>Produtos</h1>
    <ul>
      <li v-for="produto in produtos" :key="produto.id">{{ produto.name }} - {{ produto.price }}</li>
    </ul>
  </div>
</template>

<script>
import productService from '../services/productService';

export default {
  data() {
    return {
      produtos: []
    };
  },
  created() {
    productService.getProducts()
      .then(response => {
        this.produtos = response.data;
      })
      .catch(error => {
        console.error('Houve um erro ao buscar os dados!', error);
      });
  }
};
</script>
