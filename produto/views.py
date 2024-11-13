from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Produto,Variacao


# Create your views here.


class ListarProdutos(ListView):
    model=Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10


class DetalharProdutos(DetailView):
    model = Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'



class addcarrinho(View):

    def get(self, *args, **kwargs):
        http_referer=self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
        )
        # produto_id = self.request.GET.get('pid')
        # if  produto_id:
        #     produto = get_object_or_404(Produto, id=produto_id)
        #     return HttpResponse(f' {produto.nome}')
        variacao_id = self.request.GET.get('vid')
        if not variacao_id:
            messages.error(self.request, 'Produto nao existe')
            return redirect(http_referer)
        variacao = get_object_or_404(Variacao, id=variacao_id)
        if not self.request.session.get('carrinho'):
            self.request.session['carrinho']={}
            self.request.session.save()

        cart=self.request.session['carrinho']

        if variacao_id in cart:
            #TODO:Variação existe no carrinho
            pass
        else:
            #TODO:Variação não existe no carrinho
            pass


        return HttpResponse(f'{variacao.produto} {variacao.nome}')












class removercarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('removercarrinho')

class carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('carrinho')

class finalizarcompra(View):
    def get(self, *args, **kwargs):
        return HttpResponse('finalizarcompra')

