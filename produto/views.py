from idlelib.mainmenu import menudefs

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Produto,Variacao
from pprint import pprint


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
        #TODO REMOVER ABAIXO
        # if self.request.session.get('cart'):
        #     del self.request.session.get['cart']
        #     self.request.session.save()

        http_referer=self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
        )

        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(self.request, 'Produto nao existe')
            return redirect(http_referer)
        variacao = get_object_or_404(Variacao, id=variacao_id)
        variacao_estoque=variacao.estoque
        produto=variacao.produto
        produto_id = produto.id
        produto_nome = produto.nome
        variacao_nome = variacao.nome or ''
        preco_unitario = variacao.preco
        preco_unitario_promocional = variacao.preco_promocional
        quantidade = 1
        slug = produto.slug
        imagem = produto.imagem
        if imagem:
            imagem=imagem.name
        else:
            imagem=''
        #1-checar estoque
        if variacao.estoque<1:
            messages.error(
                self.request,
                'Produto indisponivel'
            )
            return redirect(http_referer)

        if not self.request.session.get('cart'):
            self.request.session['cart']={} #criação do dict
            self.request.session.save()

        cart=self.request.session['cart']

        if variacao_id in cart:
            quantidade_carrinho=cart[variacao_id]['quantidade']# a quantidade elançada dentro do dict aumentar em 1
            # a cada interação
            quantidade_carrinho+=1
            if variacao_estoque <quantidade_carrinho:# 3 verificar se estoque cobre a comprar
                messages.warning(self.request,
                f'Estoque insuficiente para {quantidade_carrinho} unidades do'
                f'{produto_nome}, adicionamos {variacao_estoque} no seu carrinho')
                quantidade_carrinho=variacao_estoque
            cart[variacao_id]['quantidade']=quantidade_carrinho
            cart[variacao_id]['preco_quantitativo'] = (preco_unitario *
                                                       quantidade_carrinho)
            cart[variacao_id]['preco_quantitativo_promocional'] = (preco_unitario_promocional *
                                                       quantidade_carrinho)



        else:#passo 2, lançar as informaçoes que vao no carrinho
           cart[variacao_id]={
            'produto_id' :produto_id ,
            'produto_nome' :produto_nome ,
            'variacao_nome':variacao_nome ,
            'variacao_id'  :variacao_id  ,
            'preco_unitario' :preco_unitario ,
            'preco_unitario_promocional' :preco_unitario_promocional ,
            'preco_quantitativo':preco_unitario,
            'preco_quantitativo_promocional' :preco_unitario_promocional ,
            'quantidade':quantidade ,
            'slug' :slug ,
            'imagem':imagem,
           }

        self.request.session.save()
        pprint(cart)
        messages.success(self.request, f'voce tem no seu '
                                       f'carrinho{cart[variacao_id]['quantidade']}')

        return redirect(http_referer)



class removercarrinho(View):

    def get(self, *args, **kwargs):
        http_referer=self.request.META.get(
            'HTTP_REFERER',
        reverse('produto:lista'))
        variacao_id = self.request.GET.get('vid')
        if not variacao_id:
            return redirect(http_referer)
        if not self.request.session.get('cart'):
            return redirect(http_referer)
        if not variacao_id in self.request.session['cart']:
            return redirect(http_referer)
        cart=self.request.session['cart'][variacao_id]
        messages.success(self.request,f''
                                      f'Produto {cart['produto_nome']}  {cart['variacao_nome']}'
                                      f'   removido do seu carrinho')

        del self.request.session['cart'][variacao_id]
        self.request.session.save()
        return redirect(http_referer)

class carrinho(View):


    def get(self, *args, **kwargs):
        context = {
            'carrinho': self.request.session.get('cart',{})
        }
        return render(self.request,'produto/carrinho.html',context)# pagina da web onde sera renderizado





class ResumoDacompra(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:criar')


        contexto={
            'usuario': self.request.user,
            'carrinho': self.request.session['cart']

        }
        return render(self.request,'produto/resumodacompra.html',contexto)

