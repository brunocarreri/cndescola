from django.db import models
from uuid import uuid4
from django.core.exceptions import ValidationError

# Create your models here.

def validate_cpf(value):
    if len(value) != 11 or not value.isdigit():
        raise ValidationError('CPF deve conter 11 digitos!.')

class Alunos (models.Model):
    id_aluno = models.UUIDField(primary_key=True, default=uuid4, editable=False)# ira criar uma ID unica do usúario.
    nome = models.CharField(max_length=255)
    cpf_aluno = models.CharField(max_length=11, unique=True, validators=[validate_cpf])
    data_nasc = models.DateField() #ao criar ja se trabalha com o formato de data : dd/mm/aaaa
    curso = models.CharField(max_length=255)
    data_inicio = models.DateField(auto_now_add=True) #ao criar ja se aplica a data atual.
