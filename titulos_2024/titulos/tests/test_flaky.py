import random
import pytest

from titulos_2024.titulos.models import Clube
from titulos_2024.titulos.tests.factories import ClubeFactory


@pytest.fixture
def adversario():
    adversarios = [
        "Palmeiras",
        "Flamengo",
        "Vasco",
        "Fluminense",
        "Corinthians",
        "São Paulo",
        "Pachuca",
        "Bahia",
        "Cruzeiro",
        "Criciúma",
    ]
    return ClubeFactory(nome=random.choice(adversarios))


@pytest.mark.django_db
@pytest.mark.parametrize("count", range(10))
def test_ganhou(botafogo: Clube, adversario: Clube, count):
    assert botafogo.ganhou(adversario), adversario.nome
