from django.db import models

class FaixaSalarial(models.TextChoices):
    MIL = 1000, ("Até mil reais")
    DOISMIL = 2000, ("Mil até 2 reais")
    TRESMIL = 3000, ("2 mil à 3 mil reais")
    ACIMATRESMIL = 4000, ("Acima de 3 mil reais")

class EscolaridadeMin(models.TextChoices):
    ensinoFundamental = 1, ("Ensino Fundamental")
    ensinoMedio = 2, ("Ensino Medio")
    tecnologo = 3, ("Tecnologo")
    ensinoSuperior = 4,("Ensino Superior")
    posSuperior = 5,("Pós/MBA/Mestrado")
    doutorado = 6, ("Doutorado")