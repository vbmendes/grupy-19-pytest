import pytest

from titulos_2024.titulos.tests.factories import (
    CampeonatoFactory,
    TituloFactory,
)
from titulos_2024.titulos.models import Clube, Federacao, Titulo
from titulos_2024.titulos.services import contar_titulos


@pytest.fixture
def preparar_titulos_brasileiros(
    botafogo: Clube,
    cbf: Federacao,
):
    return [
        TituloFactory(
            clube=botafogo,
            campeonato=CampeonatoFactory(nome="Brasileirão", ano=ano, organizador=cbf),
        )
        for ano in (1968, 1995, 2024)
    ]


@pytest.fixture
def preparar_titulos_2024(
    botafogo: Clube,
    cbf: Federacao,
    conmebol: Federacao,
):
    return [
        TituloFactory(
            clube=botafogo,
            campeonato=CampeonatoFactory(nome="Brasileirão", ano=2024, organizador=cbf),
        ),
        TituloFactory(
            clube=botafogo,
            campeonato=CampeonatoFactory(
                nome="Libertadores", ano=2024, organizador=conmebol
            ),
        ),
    ]


@pytest.mark.django_db
@pytest.mark.usefixtures("preparar_titulos_brasileiros")
def test_count_titulos_brasileiros():
    quantidade_titulos = contar_titulos(campeonato="Brasileirão")

    assert quantidade_titulos == 3


@pytest.mark.django_db
@pytest.mark.usefixtures("preparar_titulos_2024")
def test_count_titulos_2024():
    quantidade_titulos = contar_titulos(ano=2024)

    assert quantidade_titulos == 2
