from django.views.generic.list import ListView
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


class criar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('criar')

class update(View):
    def get(self, *args, **kwargs):
        return HttpResponse('atualizar')


class login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('login')

class logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('logout')

