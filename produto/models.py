from django.db import models
import os
from PIL import Image
from django.utils.text import slugify
from django.conf import settings
from utils import tool_utils
# Create your models here.


class Produto(models.Model):
    nome=models.CharField(max_length=255,)
    descricao_curta = models.TextField(max_length=255,)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m',blank=True,null=True)
    slug = models.SlugField(unique=True,blank=True,null=True)
    preco_marketing = models.DecimalField(verbose_name='Preço',null=True,blank=True,decimal_places=2,
                                          default=0,max_digits=10)
    preco_marketing_promocional = models.DecimalField(default=0,verbose_name='Preço promo',null=True,blank=True
                                                      ,max_digits=10,decimal_places=2)
    tipo = models.CharField(default='V',max_length=1,choices=(
        ('V','variaveis'),
        ('S','Simples')
    ))


    def get_preco_formatado(self):
        return  tool_utils.formata_preco(self.preco_marketing)
    get_preco_formatado.short_description='Preço'

    def get_preco_promocional_formatado(self):
        return  tool_utils.formata_preco(self.preco_marketing_promocional)
    get_preco_promocional_formatado.short_description='Preço Promo'


    @staticmethod
    def resize_image(img,new_width=800):
        img_full_path=os.path.join(settings.MEDIA_ROOT,img.name)
        img_pil=Image.open(img_full_path)
        original_width,original_height=img_pil.size
        if original_width<=new_width:
            img_pil.close()
            return
        new_height=round((new_width*original_height)/original_width)
        new_img=img_pil.resize((new_width,new_height),Image.Resampling.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50,
        )

    def __str__(self):
        return f'{self.nome}'

    def save(self,*args,**kwargs):

        if not self.slug:
            slug=f'{slugify(self.nome)}-{self.pk}'
            self.slug=slug
        super().save(*args,**kwargs)
        max_size=800
        if self.imagem:
            self.resize_image(self.imagem,max_size)



class Variacao(models.Model):
    produto=models.ForeignKey(Produto,on_delete=models.CASCADE)
    nome=models.CharField(max_length=50,blank=True,null=True)
    preco=models.FloatField()
    preco_promocional=models.FloatField(default=0)
    estoque=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome






    class Meta:
        verbose_name='Variação'
        verbose_name_plural='Variações'


'''
 Variacao:
            nome - char
            produto - FK Produto
            preco - Float
            preco_promocional - Float
            estoque - Int
'''