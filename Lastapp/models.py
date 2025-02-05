from django.db import models

class Categorie(models.Model):
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.titre

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    prix_unitaire = models.FloatField(null=True)
    Categorie = models.ForeignKey(Categorie , on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Client(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    residence = models.CharField(max_length=255)
    def __str__(self):
        return self.nom

class Panier(models.Model):
    nomPanier = models.CharField(max_length=255 , default="")
    date_creation = models.DateField()
    etat = models.CharField(max_length=100)
    def __str__(self):
        return self.nomPanier

class Achat(models.Model):
    quantité_total = models.IntegerField(null=False)
    prix_total = models.FloatField(null=False)
    Statut = models.BooleanField(null=True)
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
