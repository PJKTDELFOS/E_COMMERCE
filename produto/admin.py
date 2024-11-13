from django.contrib import admin
from . import models

# Register your models here.

class Variacaoinline(admin.TabularInline):
    model=models.Variacao
    extra=1


class Produtoadmin(admin.ModelAdmin):
    list_display = ('id','nome','descricao_curta','get_preco_formatado','get_preco_promocional_formatado')
    list_display_links = ('id','nome')
    inlines = [Variacaoinline]

admin.site.register(models.Produto,Produtoadmin)
admin.site.register(models.Variacao)

