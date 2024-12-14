import pytest


from titulos_2024.titulos.tests.factories import (
    ClubeFactory,
    FederacaoFactory,
)
from titulos_2024.titulos.models import Clube, Federacao


@pytest.fixture
def botafogo() -> Clube:
    return ClubeFactory(nome="Botafogo", cidade="Rio de Janeiro", estado="RJ")


@pytest.fixture
def cbf() -> Federacao:
    return FederacaoFactory(nome="CBF")


@pytest.fixture
def conmebol() -> Federacao:
    return FederacaoFactory(nome="Conmebol")
