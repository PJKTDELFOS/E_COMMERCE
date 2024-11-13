from django.views.generic.list import ListView
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


class pagar(View):
    def get(self,*args,**kwargs):
        return HttpResponse('pagar')


class fecharpedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('fecharpedido')


class detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('detalhar ')



