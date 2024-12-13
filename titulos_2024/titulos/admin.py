from django.contrib import admin
from titulos_2024.titulos.models import Clube, Federacao, Campeonato, Titulo


class ClubeAdmin(admin.ModelAdmin):
    pass


class FederacaoAdmin(admin.ModelAdmin):
    pass


class CampeonatoAdmin(admin.ModelAdmin):
    pass


class TituloAdmin(admin.ModelAdmin):
    pass


admin.site.register(Clube, ClubeAdmin)
admin.site.register(Federacao, FederacaoAdmin)
admin.site.register(Campeonato, CampeonatoAdmin)
admin.site.register(Titulo, TituloAdmin)
