import pytest

from titulos_2024.titulos.tests.factories import (
    ClubeFactory,
    CampeonatoFactory,
    FederacaoFactory,
)
from titulos_2024.titulos.models import Clube, Federacao, Campeonato, Titulo
from titulos_2024.titulos.services import cadastrar_titulo


@pytest.fixture
def cbf() -> Federacao:
    return FederacaoFactory(nome="CBF")


@pytest.fixture
def brasileirao2024(cbf: Federacao) -> Campeonato:
    return CampeonatoFactory(ano=2024, nome="Brasileirão", organizador=cbf)


@pytest.fixture
def botafogo() -> Clube:
    return ClubeFactory(nome="Botafogo", cidade="Rio de Janeiro", estado="RJ")


@pytest.fixture
def conmebol() -> Federacao:
    return FederacaoFactory(nome="Conmebol")


@pytest.fixture
def libertadores2024(conmebol: Federacao) -> Campeonato:
    return CampeonatoFactory(ano=2024, nome="Libertadores", organizador=conmebol)


@pytest.mark.django_db
@pytest.mark.parametrize("fixture_campeonato", ["brasileirao2024", "libertadores2024"])
def test_cadastrar_titulo_brasileiro(
    botafogo: Clube, fixture_campeonato: str, request: pytest.FixtureRequest
):
    campeonato = request.getfixturevalue(fixture_campeonato)
    # Execução
    titulo = cadastrar_titulo(clube=botafogo, campeonato=campeonato)

    # Verificação
    assert titulo.clube == botafogo
    assert titulo.campeonato == campeonato
    assert Titulo.objects.filter(clube=botafogo, campeonato=campeonato).exists()
