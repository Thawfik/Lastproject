from django.db import models

class Categorie(models.Model):
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    prix_unitaire = models.FloatField(null=True)
    quantité_stock = models.IntegerField(null=True)
    Statut = models.CharField(max_length=100)
    Categorie = models.ForeignKey(Categorie , on_delete=models.CASCADE)

class Client(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    residence = models.CharField(max_length=255)

class Panier(models.Model):
    date_creation = models.DateField()
    etat = models.CharField(max_length=100)

class Achat(models.Model):
    quantité_total = models.IntegerField(null=False)
    prix_total = models.FloatField(null=False)
    Statut = models.CharField(max_length=255)
    Client = models.ForeignKey(Client , on_delete=models.CASCADE)
    Panier = models .ForeignKey(Panier , on_delete=models.CASCADE)
    Produit = models.ForeignKey(Produit , on_delete=models.CASCADE , default=1)

class Transaction(models.Model):
    operation = models.CharField(max_length=100)
    montant = models.FloatField(null=False)
    operateur = models.CharField(max_length=255)
    dateoperation = models.DateField()
    Client = models.ForeignKey(Client , on_delete=models.CASCADE)

class Facture(models.Model):
    date = models.DateField()
    mode_paiement = models.CharField(max_length=100)
    etat = models.CharField(max_length=255 )
    notes = models.CharField(max_length=255)
    Panier = models.ForeignKey(Panier , on_delete=models.CASCADE)
