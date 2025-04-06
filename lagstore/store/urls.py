from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.views import CategoriaViewSet, ProdutoViewSet, CarrinhoViewSet, ItemCarrinhoViewSet, PedidoViewSet, ItemPedidoViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'carrinhos', CarrinhoViewSet)
router.register(r'itens-carrinho', ItemCarrinhoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'itens-pedido', ItemPedidoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
