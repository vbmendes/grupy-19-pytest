from django.db import models


class Clube(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    def ganhou(self, adversario):
        if self.nome == "Botafogo" and adversario.nome not in [
            "Pachuca",
            "Bahia",
            "Cruzeiro",
            "Criciúma",
        ]:
            return True
        return False


class Federacao(models.Model):
    nome = models.CharField(max_length=100)


class Campeonato(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    abrangencia = models.CharField(max_length=100)
    organizador = models.ForeignKey(Federacao, on_delete=models.CASCADE)


class Titulo(models.Model):
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
