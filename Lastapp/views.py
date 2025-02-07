from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect
from Lastapp.models import Produit, Categorie , Client , Transaction , Facture , Panier , Achat
from .forms import ProductForm , CategorieForm ,ClientForm , TransactionForm , FactureForm , AchatForm , PanierForm

def listeProduits(request):
    context = {"listeproduits":Produit.objects.all() }
    return render(request , "Produits/listeProduits.html" , context)

def listeCategorie(request):
    pass

def listeClient(request):
    context = {"listeclients":Client.objects.all() }
    return render(request , "Clients/listeClients.html" , context)

def listeAchats(request):
    context = {"listeachats":Achat.objects.all() }
    return render(request , "Achats/listeAchats.html" , context)

def listeTransaction(request):
    context = {"listetransactions":Transaction.objects.all() }
    return render(request , "Transactions/listeTransactions.html" , context)

def listeFacture(request):
    context = {"listefactures":Facture.objects.all() }
    return render(request , "Facture/listeFactures.html" , context)

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
            
    else:
        produitform = ProductForm()

    return render(request, "Produits/ajoutProduit.html", {"product_form":produitform})

def ajoutCategorie(request):
    if request.method == "POST":
        categorieform = CategorieForm(request.POST)
        if categorieform.is_valid():
            titre = categorieform.cleaned_data["titreCategorie"]
            description = categorieform.cleaned_data["description"]
            oCategorie1 = Categorie(titre = titre , description = description)
            oCategorie1.save()
        return redirect("listeProduits")
        
            
    else:
        categorieform = CategorieForm()

    return render(request, "Categorie/ajoutCategorie.html", {"categorie_form":categorieform})


def ajoutClient(request):
    if request.method == "POST":
        clientform = ClientForm(request.POST)
        if clientform.is_valid():
            nom = clientform.cleaned_data["nameClient"]
            prenom = clientform.cleaned_data["surnameClient"]
            contact = clientform.cleaned_data["contactClient"]
            residence = clientform.cleaned_data["residenceClient"]
            oClient1 = Client(nom = nom  , prenom = prenom , contact = contact , residence = residence)
            oClient1.save()
            
        return redirect("listeClients")
    else:
        clientform = ClientForm()

    return render (request , "Clients/ajoutClient.html",{"client_form":clientform})

def ajoutTransaction(request):
    if request.method == "POST":
        transactionform = TransactionForm(request.POST)
        if transactionform.is_valid():
            operation = transactionform.cleaned_data["operationTransaction"]
            montant = transactionform.cleaned_data["amountTransaction"]
            date = transactionform.cleaned_data["dateTransaction"]
            Operateur = transactionform.cleaned_data["Operateur"]
            Client = transactionform.cleaned_data["Client"]

            oTransaction1 = Transaction(operation = operation  , montant = montant ,  dateoperation = date , Operateur = Operateur , Client = Client  )
            oTransaction1.save()
        return redirect("listeTransactions")
    else:
        transactionform = TransactionForm()

    return render (request , "Transactions/ajoutTransaction.html",{"transaction_form":transactionform})


def ajoutFacture(request):
    if request.method == "POST":
        factureform = FactureForm(request.POST)
        if factureform.is_valid():
            date = factureform.cleaned_data["dateFacture"]
            etat = factureform.cleaned_data["etatFacture"]
            notes = factureform.cleaned_data["notesFacture"]
            Panier = factureform.cleaned_data["Panier"]
            ModePaiement = factureform.cleaned_data["ModePaiement"]

            oFacture1 = Facture(date = date  , etat = etat , note = notes , Panier = Panier , ModePaiement = ModePaiement)
            oFacture1.save()
    else:
        factureform = FactureForm()

    return render (request , "Facture/ajoutFacture.html",{"facture_form":factureform})

def ajoutAchat(request):
    if request.method == "POST":
        achatform = AchatForm(request.POST)
        if achatform.is_valid():
            quantite = achatform.cleaned_data["quantiteAchat"]
            prix = achatform.cleaned_data["priceAchat"]
            Client = achatform.cleaned_data["Client"]
            Panier = achatform.cleaned_data["Panier"]
            Produit = achatform.cleaned_data["Produit"]

            oAchat1 = Achat(quantite_total = quantite , prix_total = prix , Client = Client , Panier = Panier , Produit = Produit)
            oAchat1.save()
        return redirect("listeAchats")
    else:
        achatform = AchatForm()

    return render (request , "Achats/ajoutAchat.html",{"achat_form":achatform})


def ajoutPanier(request):
    if request.method == "POST":
        panierform = PanierForm(request.POST)
        if panierform.is_valid():
            nom = panierform.cleaned_data["nomPanier"]
            date = panierform.cleaned_data["datePanier"]
            etat = panierform.cleaned_data["etatPanier"]
            oPanier1 = Panier( nomPanier = nom , date_creation = date , etat = etat)
            oPanier1.save()
   
        return redirect("listeFactures")
            
    else:
        panierform = PanierForm()

    return render(request, "Panier/ajoutPanier.html", {"panier_form":panierform})

def modifierProduit(request,id):
    product = Produit.objects.get(id=id)
    if request.method == "POST":
        proform = ProductForm(request.POST , initial=product)
        if proform.is_valid():
            nom = proform.cleaned_data["nameProduct"]
            description = proform.cleaned_data["describeProduct"]
            prix = proform.cleaned_data["puProduct"]
            Categorie = proform.cleaned_data["Categorie"]
        Produit.objects.filter(id=id).update(nom = nom , description = description , prix_unitaire = prix , Categorie = Categorie)

        return redirect("listeProduits")
    else:
        proform = ProductForm()

    return render(request, "Produits/modifierProduit.html", {"product_form":proform})


def supprimerProduit(request , id):
    product = Produit.objects.get(id=id)
    product.delete()
    return redirect("listeProduits")

def modifierClient(request):
    pass

def supprimerClient(request):
    pass

def modifierTransaction(request):
    pass

def supprimerTransaction(request):
    pass

def modifierAchat(request):
    pass

def supprimerAchat(request):
    pass

def modifierFacture(request):
    pass

def supprimerFacture(request):
    pass


