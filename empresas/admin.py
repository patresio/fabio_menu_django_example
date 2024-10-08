from django.contrib import admin

from empresas.models import Area, Componente, Empresa, Equipamento, Proposta


# Register your models here.
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("name",)


class AreaAdmin(admin.ModelAdmin):
    list_display = ("name", "empresa")


class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ("name", "area")


class ComponenteAdmin(admin.ModelAdmin):
    list_display = ("name", "equipamento")


class PropostaAdmin(admin.ModelAdmin):
    list_display = ("name", "componente")


admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Equipamento, EquipamentoAdmin)
admin.site.register(Componente, ComponenteAdmin)
admin.site.register(Proposta, PropostaAdmin)
