from django.db import models

class Kitob(models.Model):
    nom=models.CharField(max_length=200)
    narx=models.FloatField()
    rasm=models.FileField()

    def __str__(self):
        return self.nom
