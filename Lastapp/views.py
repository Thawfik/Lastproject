from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect
from Lastapp.models import Produit, Categorie , Client , Transaction , Facture , Panier , Achat
from .forms import ProductForm

def listeProduits(request):
    context = {"listeproduits":Produit.objects.all() }
    return render(request , "Produits/listeProduits.html" , context)

def listeCategorie(request):
    pass

def listeClient(request):
    pass

def listeAchats(request):
    pass

def listeTransaction(request):
    pass

def listeFacture(request):
    pass

def listePanier(request):
    pass

def ajoutProduit(request):
    if request.method == "POST":
        produitform = ProductForm(request.POST)
        if produitform.is_valid():
            nom = produitform.cleaned_data["nameProduct"]
            description = produitform.cleaned_data["describeProduct"]
            prix = produitform.cleaned_data["puProduct"]
            Categorie = produitform.cleaned_data["Categorie"]
            oProduit1 = Produit(nom = nom , description = description ,prix_unitaire = prix   ,Categorie = Categorie)
            oProduit1.save()
            redirect("listeProduits")
    else:
        form = ProductForm()

    return render(request, "ajoutProduit.html", {"product_form": form})

def ajoutCategorie(request):
    pass

def ajoutClient(request):
    pass

def ajoutTransaction(request):
    pass

def ajoutFacture(request):
    pass

def ajoutAchat(request):
    pass

def ajoutPanier(request):
    pass


