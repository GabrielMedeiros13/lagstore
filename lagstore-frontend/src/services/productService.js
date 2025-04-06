import apiClient from '../axios.js';

export default {
  getProducts() {
    return apiClient.get('/produtos/');
  },
  getProduct(id) {
    return apiClient.get(`/produtos/${id}/`);
  },
  createProduct(product) {
    return apiClient.post('/produtos/', product);
  },
  updateProduct(id, product) {
    return apiClient.put(`/produtos/${id}/`, product);
  },
  deleteProduct(id) {
    return apiClient.delete(`/produtos/${id}/`);
  }
};
