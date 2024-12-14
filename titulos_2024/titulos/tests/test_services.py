import pytest

from titulos_2024.titulos.models import Clube, Federacao, Campeonato, Titulo
from titulos_2024.titulos.services import cadastrar_titulo


@pytest.fixture
def cbf() -> Federacao:
    cbf = Federacao(nome="CBF")
    cbf.save()
    yield cbf
    cbf.delete()


@pytest.fixture
def brasileirao2024(cbf: Federacao) -> Campeonato:
    brasileirao2024 = Campeonato(ano=2024, nome="Brasileirão", organizador=cbf)
    brasileirao2024.save()
    yield brasileirao2024
    brasileirao2024.delete()


@pytest.fixture
def botafogo() -> Clube:
    botafogo = Clube(nome="Botafogo", cidade="Rio de Janeiro", estado="RJ")
    botafogo.save()
    yield botafogo
    botafogo.delete()


@pytest.fixture
def conmebol() -> Federacao:
    conmebol = Federacao(nome="Conmebol")
    conmebol.save()
    yield conmebol
    conmebol.delete()


@pytest.fixture
def libertadores2024(conmebol: Federacao) -> Campeonato:
    libertadores2024 = Campeonato(ano=2024, nome="Libertadores", organizador=conmebol)
    libertadores2024.save()
    yield libertadores2024
    libertadores2024.delete()


@pytest.mark.django_db
def test_cadastrar_titulo_brasileiro(brasileirao2024: Campeonato, botafogo: Clube):
    # Execução
    titulo = cadastrar_titulo(clube=botafogo, campeonato=brasileirao2024)

    # Verificação
    assert titulo.clube == botafogo
    assert titulo.campeonato == brasileirao2024
    assert Titulo.objects.filter(clube=botafogo, campeonato=brasileirao2024).exists()


@pytest.mark.django_db
def test_cadastrar_titulo_libertadores(libertadores2024: Campeonato, botafogo: Clube):
    # Execução
    titulo = cadastrar_titulo(clube=botafogo, campeonato=libertadores2024)

    # Verificação
    assert titulo.clube == botafogo
    assert titulo.campeonato == libertadores2024
    assert Titulo.objects.filter(clube=botafogo, campeonato=libertadores2024).exists()
