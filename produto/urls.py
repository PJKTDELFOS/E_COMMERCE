from django.urls import path
from .views import ListarProdutos,DetalharProdutos,addcarrinho,removercarrinho,carrinho,finalizarcompra


app_name='produto'

urlpatterns=[
    path('',ListarProdutos.as_view(),name="lista"),
    path('adicionacarrinho/',addcarrinho.as_view(),name="adicionaraocarrinho"),
    path('removecarrinho/',removercarrinho.as_view(),name="remover"),
    path('carrinho/', carrinho.as_view(), name="carrinho"),
    path('finalizar/', finalizarcompra.as_view(), name="finalizarcompra"),
    path('<slug>', DetalharProdutos.as_view(), name="detalhe"),

]