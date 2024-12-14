from typing import Optional

from titulos_2024.titulos.models import Clube, Campeonato, Titulo


def cadastrar_titulo(clube: Clube, campeonato: Campeonato):
    titulo = Titulo(clube=clube, campeonato=campeonato)
    titulo.save()
    return titulo


def contar_titulos(campeonato: Optional[str] = None, ano: Optional[int] = None) -> int:
    queryset = Titulo.objects.all()
    if campeonato:
        queryset = queryset.filter(campeonato__nome=campeonato)
    if ano:
        queryset = queryset.filter(campeonato__ano=ano)
    return queryset.count()
