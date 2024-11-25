from django.urls import path
from .views import ListarProdutos,DetalharProdutos,addcarrinho,removercarrinho,carrinho,ResumoDacompra


app_name='produto'

urlpatterns=[
    path('',ListarProdutos.as_view(),name="lista"),
    path('adicionacarrinho/',addcarrinho.as_view(),name="adicionaraocarrinho"),
    path('removecarrinho/',removercarrinho.as_view(),name="remover"),
    path('resumodacompra/', ResumoDacompra.as_view(), name="resumodacompra"),
    path('carrinho/', carrinho.as_view(), name="carrinho"),
    path('<slug>', DetalharProdutos.as_view(), name="detalhe"),

]