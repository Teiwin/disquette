from django.db import models

# Create your models here.
class Disquette(models.Model):
    disquette = models.CharField(max_length=500)
    langue = models.ForeignKey('Langue', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.disquette


class Langue(models.Model):
    nom = models.CharField(max_length=50)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.nom
