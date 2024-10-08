from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Empresa(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save()


class Area(models.Model):
    name = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="areas")
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save()


class Equipamento(models.Model):
    name = models.CharField(max_length=100)
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, related_name="equipamentos"
    )
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save()


class Componente(models.Model):
    name = models.CharField(max_length=100)
    equipamento = models.ForeignKey(
        Equipamento, on_delete=models.CASCADE, related_name="componentes"
    )
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save()


class Proposta(models.Model):
    name = models.CharField(max_length=100)
    componente = models.ForeignKey(
        Componente, on_delete=models.CASCADE, related_name="propostas"
    )
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save()
