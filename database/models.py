from django.db import models

from django.db import models

class exemple_personnels(models.Model):
    Prenom = models.CharField(max_length=50)
    Nom = models.CharField(max_length=50)
    Postnom = models.CharField(max_length=50, null=True)
    Sexe = models.CharField(max_length=1, null=True)
    Date_de_naissance = models.DateField(null=True)
    Numero_de_telephone = models.CharField(max_length=20, null=True)
    Email = models.EmailField(null=True)
    Statut_id = models.IntegerField()
    Fonction_id = models.IntegerField()
    Affectation_id = models.IntegerField()

    def __str__(self):
        return f"{self.Prenom} {self.Nom}"
