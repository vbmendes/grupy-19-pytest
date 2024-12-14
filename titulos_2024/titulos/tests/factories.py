import factory
from factory.django import DjangoModelFactory

from titulos_2024.titulos.models import Campeonato, Clube, Federacao, Titulo


class CampeonatoFactory(DjangoModelFactory[Campeonato]):

    nome = factory.Faker("word")
    ano = factory.Faker("year")
    abrangencia = factory.Faker(
        "random_element", elements=["nacional", "continental", "mundial"]
    )
    organizador = factory.SubFactory(
        "titulos_2024.titulos.tests.factories.FederacaoFactory"
    )

    class Meta:
        model = Campeonato
        django_get_or_create = ["nome"]


class ClubeFactory(DjangoModelFactory[Clube]):
    nome = factory.Faker("word")
    cidade = factory.Faker("city")
    estado = factory.Faker("state_abbr")

    class Meta:
        model = Clube
        django_get_or_create = ["nome"]


class FederacaoFactory(DjangoModelFactory[Federacao]):
    nome = factory.Faker("word")

    class Meta:
        model = Federacao
        django_get_or_create = ["nome"]


class TituloFactory(DjangoModelFactory[Titulo]):
    clube = factory.SubFactory("titulos_2024.titulos.tests.factories.ClubeFactory")
    campeonato = factory.SubFactory(
        "titulos_2024.titulos.tests.factories.CampeonatoFactory"
    )

    class Meta:
        model = Titulo
