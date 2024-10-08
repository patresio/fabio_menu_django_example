from django.db import models


# Create your models here.
class Empresa(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="areas")

    def __str__(self):
        return self.name


class Equipamento(models.Model):
    name = models.CharField(max_length=100)
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, related_name="equipamentos"
    )

    def __str__(self):
        return self.name


class Componente(models.Model):
    name = models.CharField(max_length=100)
    equipamento = models.ForeignKey(
        Equipamento, on_delete=models.CASCADE, related_name="componentes"
    )

    def __str__(self):
        return self.name


class Proposta(models.Model):
    name = models.CharField(max_length=100)
    componente = models.ForeignKey(
        Componente, on_delete=models.CASCADE, related_name="propostas"
    )

    def __str__(self):
        return self.name
