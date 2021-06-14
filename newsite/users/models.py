from vagas.enums import EscolaridadeMin, FaixaSalarial
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Create your models here.

class User(AbstractUser):
    
    email = models.EmailField(('email address'), unique=True)
    
    is_active = models.BooleanField(default=True)

    class TipoPerfil(models.TextChoices):
        EMPRESA = 0 , ("Empresa")
        CANDIDATO = 1, ('Candidato')

    tipo = models.CharField(max_length= 50,
    choices=TipoPerfil.choices,
    default= TipoPerfil.CANDIDATO)

    escolaridade_min = models.CharField(
     max_length= 50,
      choices= EscolaridadeMin.choices)

    faixa_salarial = models.CharField(
      max_length=100, 
      choices = FaixaSalarial.choices) 
      
    staff = bool()
    is_staff = models.BooleanField(default=(not bool(tipo)))
    
    image = models.ImageField(default='placeholder.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.username}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   
    escolaridade_min = models.CharField(
     max_length= 50,
      choices= EscolaridadeMin.choices)

    faixa_salarial = models.CharField(
      max_length=100, 
      choices = FaixaSalarial.choices) 

    class TipoPerfil(models.TextChoices):
        EMPRESA = 0 , ("Empresa")
        CANDIDATO = 1, ('Candidato')

    tipo = models.CharField(max_length= 50,
    choices=TipoPerfil.choices,
    default= TipoPerfil.CANDIDATO)
    
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super(Profile,self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
