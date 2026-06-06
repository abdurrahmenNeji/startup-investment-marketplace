from django.db import models

# Modèle pour "capital_risque"
class CapitalRisque(models.Model):
    id_capital_risque = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    CIN = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    pseudo = models.CharField(max_length=20)
    pwrd = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nom
class Achat(models.Model):
    id_achat = models.AutoField(primary_key=True)
    client = models.ForeignKey(CapitalRisque, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()





