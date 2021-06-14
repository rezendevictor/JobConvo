from django.db import models
from django.utils import timezone
from .enums import FaixaSalarial,EscolaridadeMin
from django.conf import settings
from django.urls import reverse

class PostVaga(models.Model):
    title = models.CharField(max_length=100)
    faixa_salarial = models.CharField(
      max_length=100, 
      choices = FaixaSalarial.choices)
    requisitos = models.TextField()
    escolaridade_min = models.CharField(
     max_length= 50,
      choices= EscolaridadeMin.choices)
      
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE)

    def __str__(self):
      return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    



