from django.contrib import admin
from django.urls import path , include
from . import views 

urlpatterns = [ 

    #/market/produit : URL menant à la page de la liste des produits
    path('produit/', views.listeProduits , name="listeProduits"),

    #/market/ajout_produit : URL menant à la page d'ajout des produits
    path('ajout_produit/', views.ajoutProduit , name="ajoutProduit"),

    #/market/categorie : URL menant à la page de la liste des categories
    path('categorie/', views.listeCategorie , name="listeCategories"),

    #/market/ajout_categorie : URL menant à la page d'ajout des categories
    path('ajout_produit/', views.ajoutCategorie , name="ajoutCategorie"),

    #/market/client : URL menant à la page de la liste des clients
    path('client/', views.listeClient , name="listeClients"),

    #/market/ajout_produit : URL menant à la page d'ajout des clients
    path('ajout_client/', views.ajoutClient , name="ajoutClient"),

    #/market/achat : URL menant à la page de la liste des achats
    path('achat/', views.listeAchats , name="listeAchats"),

    #/market/ajout_achat : URL menant à la page d'ajout des achats
    path('ajout_achat/', views.ajoutAchat , name="ajoutAchat"),

    #/market/facture : URL menant à la page de la liste des factures
    path('facture/', views.listeFacture , name="listeFactures"),

    #/market/ajout_facture : URL menant à la page d'ajout des factures
    path('ajout_facture/', views.ajoutFacture , name="ajoutFacture"),

    #/market/transaction : URL menant à la page de la liste des Transactions
    path('transaction/', views.listeTransaction , name="listeTransactions"),

    #/market/ajout_transaction : URL menant à la page d'ajout des transactions
    path('ajout_transaction/', views.ajoutTransaction, name="ajoutTransaction"),

     #/market/panier : URL menant à la page de la liste des Paniers
    path('panier/', views.listePanier , name="listePaniers"),

    #/market/ajout_panier : URL menant à la page d'ajout des Paniers
    path('ajout_panier/', views.ajoutPanier, name="ajoutPanier")

]