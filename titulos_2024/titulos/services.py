from titulos_2024.titulos.models import Clube, Campeonato, Titulo


def cadastrar_titulo(clube: Clube, campeonato: Campeonato):
    titulo = Titulo(clube=clube, campeonato=campeonato)
    titulo.save()
    return titulo
