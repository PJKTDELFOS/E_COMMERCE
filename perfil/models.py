from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# from datetime import date

from django.forms import ValidationError
# Create your models here.
import re
from utils.validacpf import valida_cpf

class PerfilUsuario(models.Model):
    usuario=models.OneToOneField(User,max_length=50,on_delete=models.CASCADE)
    idade=models.IntegerField(validators=[
        MaxValueValidator(125),
        MinValueValidator(18)
    ],blank=True,)
    data_nascimento=models.DateField()
    cpf=models.CharField(max_length=12,)
    endereco = models.CharField(max_length=50,)
    numero = models.CharField(max_length=50,)
    complemento=models.CharField(max_length=50,)
    bairro = models.CharField(max_length=50,)
    cep=models.CharField(max_length=9,)
    cidade = models.CharField(max_length=50,)
    estado = models.CharField(default=None,max_length=2,choices=(
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ))

    def __str__(self):
        return self.usuario.username
        '''quando usar o one to one field lembrar de se usar User, 
        no self.xxxx do def str
        retornar o username'''

# para fazer validação de canpos, estudar a logica
    def clean(self):
        error_messages={}
        if not valida_cpf(self.cpf):
            error_messages['cpf']='Dgite um cpf valido'


        if not re.search(r'[^0-9]',self.cep) or len(self.cep)<8:
            error_messages['cep'] = 'Dgite um cep valido'

        if error_messages:
            raise ValidationError(error_messages)



    class Meta:
        verbose_name='Perfil'
        verbose_name_plural='Perfis'






