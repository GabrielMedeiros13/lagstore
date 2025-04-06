<template>
  <div class="landing-page">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark container-fluid">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Lagstore</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Produtos</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Sobre</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Contato</a>
            </li>
          </ul>
          <form class="d-flex">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>

    <!-- Carrossel -->
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img class="d-block w-100" src="@/assets/banner1.png" alt="First slide">
        </div>
        <div class="carousel-item">
          <img class="d-block w-100" src="@/assets/banner2.png" alt="Second slide">
        </div>
        <div class="carousel-item">
          <img class="d-block w-100" src="@/assets/banner3.png" alt="Third slide">
        </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>

    <!-- Seção de Produtos -->
    <section class="products">
      <h2>Produtos.</h2>
      <div class="product-grid">
        <div v-for="produto in produtos" :key="produto.id" class="product-item">
          <img :src="produto.image" alt="Product Image" />
          <h3>{{ produto.name }}</h3>
          <p>{{ produto.price }}</p>
        </div>
      </div>
    </section>


    <!-- Seçao cadastre -->

    <section class="cadastre bg-dark">
      <div class="cadastre-grid">
      <h3 class="cadastre-h3">Todos os jogos a todo o momento</h3>
      <button class="button-cadastre">Cadastre-se</button>
      </div>
    </section>
  </div>
</template>

<script>
import productService from '../services/productService';

export default {
  data() {
    return {
      produtos: [],
      slides: [
        { id: 1, caption: 'Slide 1', image: '@/assets/banner1.png' },
        { id: 2, caption: 'Slide 2', image: '@/assets/banner2.png' },
        { id: 3, caption: 'Slide 3', image: '@/assets/banner3.png' }
      ]
    };
  },
  created() {
    productService.getProducts()
      .then(response => {
        console.log('Produtos recebidos:', response.data);
        this.produtos = response.data;
      })
      .catch(error => {
        console.error('Houve um erro ao buscar os dados!', error);
      });
  }
};
</script>

<style scoped>
.landing-page {
  font-family: Arial, sans-serif;
  padding: 20px;
}

.products {
  margin-top: 50px;
}

.product-grid {
  display: flex;
  flex-wrap: wrap;
}

.product-item {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 10px;
  margin: 10px;
  width: calc(33.333% - 20px);
  text-align: center;
}

.product-item h3 {
  margin-top: 10px;
}

.navbar-brand {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-link {
  font-size: 1rem;
}

.navbar-nav .nav-item .nav-link {
  padding: 0.5rem 1rem;
}

.form-control {
  margin-right: 0.5rem;
}

.btn-outline-success {
  margin-left: 0.5rem;
}
.carousel-inner {
  max-height: 500px; /* Define a altura máxima do carrossel */
}

.carousel-item img {
  height: 500px; /* Define a altura das imagens */
  object-fit: fill; /* Ajusta as imagens para cobrir o contêiner */
}

.cadastre {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 40vh; /* Ajuste a altura conforme necessário */
  text-align: center;
  background-color:#F0FFFF
}

.cadastre-grid {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.cadastre-h3 {
  margin: 0;
  color:white;
}

button {
  margin-top: 10px; /* Ajuste o espaçamento conforme necessário */
}

.button-cadastre {
  background-color: #28a745; /* Cor de fundo verde */
  color: #000000; /* Cor do texto preto */
  border: none; /* Sem borda */
  padding: 10px 20px; /* Espaçamento interno */
  font-size: 16px; /* Tamanho da fonte */
  font-weight: bold; /* Texto em negrito */
  border-radius: 5px; /* Bordas arredondadas */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Sombra */
  transition: background-color 0.3s ease, box-shadow 0.3s ease; /* Animação suave */
}

.button-cadastre:hover {
  background-color: #218838; /* Cor de fundo verde escuro ao passar o mouse */
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15); /* Sombra ao passar o mouse */
}

.button-cadastre:active {
  background-color: #1e7e34; /* Cor de fundo verde mais escuro ao clicar */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra ao clicar */
}

.landing-page {
  margin: 0;
  padding: 0;
  width: 100%;
  box-sizing: border-box;
}

.container-fluid {
  padding: 0 !important;
}

.products, .cadastre {
  width: 100%;
  padding: 0 10px; /* Ajuste conforme necessário */
  box-sizing: border-box;
}

.cadastre-grid {
  width: 100%;
}


</style>
