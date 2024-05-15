from rest_framework import viewsets
from alunos.api import serializers
from alunos import models

class AlunosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AlunosSerializer
    queryset = models.Alunos.objects.all()
