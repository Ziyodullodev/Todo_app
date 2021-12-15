from django.db import models

# Create your models here.

class Todo(models.Model):
    tanlov = (
        ('yangi','yangi'),
        ('bajarilgan','bajarilgan')
    )
    nom = models.CharField(max_length=15)
    batafsil = models.CharField(max_length=100)
    status = models.CharField(choices=tanlov, max_length=15)
    vaqt = models.TimeField()

    def __str__(self):
        return f"{self.batafsil}"
    

