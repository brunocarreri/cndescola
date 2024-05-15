from rest_framework import serializers
from alunos import models

class AlunosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alunos
        fields = '__all__'
