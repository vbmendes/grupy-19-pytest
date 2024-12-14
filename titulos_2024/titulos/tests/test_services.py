import pytest

from titulos_2024.titulos.models import Clube, Federacao, Campeonato, Titulo
from titulos_2024.titulos.services import cadastrar_titulo


@pytest.mark.django_db
def test_cadastrar_titulo():
    # Preparação
    cbf = Federacao(nome="CBF")
    cbf.save()
    brasileirao2024 = Campeonato(ano=2024, nome="Brasileirão", organizador=cbf)
    brasileirao2024.save()
    botafogo = Clube(nome="Botafogo", cidade="Rio de Janeiro", estado="RJ")
    botafogo.save()

    # Execução
    titulo = cadastrar_titulo(clube=botafogo, campeonato=brasileirao2024)

    # Verificação
    assert titulo.clube == botafogo
    assert titulo.campeonato == brasileirao2024
    assert Titulo.objects.filter(clube=botafogo, campeonato=brasileirao2024).exists()

    # Limpeza
    cbf.delete()
    brasileirao2024.delete()
    botafogo.delete()
    titulo.delete()
