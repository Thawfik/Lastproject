from django import forms
from Lastapp.models import Categorie , Produit , Client , Panier , Operateur , ModePaiement

class ProductForm(forms.Form):
    nameProduct = forms.CharField(label="Nom produit" , max_length=255)
    describeProduct = forms.CharField(label="description ", max_length=255)
    puProduct = forms.IntegerField(label="Prix unitaire" ,max_value=10000 , required=True)
    Categorie = forms.ModelChoiceField(label="Categorie ",queryset=Categorie.objects.all())

class ClientForm(forms.Form):
    nameClient = forms.CharField(label="Nom client " , max_length=255)
    surnameClient = forms.CharField(label="Prenom  ", max_length=255)
    contactClient = forms.CharField(label="Contact ", max_length=255)
    residenceClient = forms.CharField(label="Residience " , max_length=255)

class AchatForm(forms.Form):
    quantiteAchat = forms.IntegerField(label="Quantité " , max_value=50 , required=True)
    priceAchat = forms.FloatField(label="Prix total", max_value=100000 , required=True)
    statutAchat = forms.CharField(label="Statut " , max_length=255)
    Client = forms.ModelChoiceField(queryset=Client.objects.all ())
    Panier = forms.ModelChoiceField(queryset=Panier.objects.all())
    Produit = forms.ModelMultipleChoiceField(queryset=Produit.objects.all() , widget = forms.CheckboxSelectMultiple)

class TransactionForm(forms.Form):
    operationTransaction = forms.CharField(label="Operation", max_length=255)
    amountTransaction = forms.FloatField(label="Montant " , max_value=200000)
    dateTransaction = forms.DateField(label="Date " , required=True)
    Operateur = forms.ModelChoiceField(label="Operateur",queryset=Operateur.objects.all())
    Client = forms.ModelChoiceField(label="Client concerné " ,queryset=Client.objects.all ())

class FactureForm(forms.Form):
    dateFacture = forms.DateField(label="Date " , required=True)
    etatFacture = forms.CharField(label="Etat  " , max_length=255)
    notesFacture = forms.CharField(label="Notes" , max_length=255)
    Panier = forms.ModelChoiceField(queryset=Panier.objects.all())
    ModePaiement = forms.ModelChoiceField(label="Paiement" , queryset=ModePaiement.objects.all())

class CategorieForm(forms.Form):
    titreCategorie = forms.CharField(label="Titre ",max_length=255)
    description = forms.CharField(label=" description", max_length=255)

class PanierForm(forms.Form):
    nomPanier = forms.CharField(label="Nom du Panier ", max_length=255)
    datePanier = forms.DateField(label="Date " , required=True)
    etatPanier = forms.CharField(label="Etat du panier", required=True)
