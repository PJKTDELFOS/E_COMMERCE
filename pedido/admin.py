from django.contrib import admin
from . import models



# Register your models here.

class Itensdopedidoadmin(admin.TabularInline):
    model=models.Itempedido
    extra = 1
class Pedidoadmin(admin.ModelAdmin):
    inlines = [Itensdopedidoadmin]

admin.site.register(models.Pedido,Pedidoadmin)
admin.site.register(models.Itempedido)

