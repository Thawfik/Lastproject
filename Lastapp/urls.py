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
    path('ajout_categorie/', views.ajoutCategorie , name="ajoutCategorie"),

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
    path('ajout_panier/', views.ajoutPanier, name="ajoutPanier"),

    #/market/modif_produit : URL menant à la page de modification des Produits
    path('modif_produit/<int:id>/', views.modifierProduit , name="modifierProduit"),

    #/market/supp_produit : URL menant à la page de suppression des produits
    path('supp_produit/<int:id>/', views.supprimerProduit, name="supprimerProduit"),

    #/market/modif_client : URL menant à la page de modification des Clients
    path('modif_client/<int:id>/', views.modifierClient , name="modifierClient"),

    #/market/supp_client : URL menant à la page de suppression des clients
    path('supp_client/<int:id>/', views.supprimerClient , name="supprimerClient"),

     #/market/modif_ctransaction : URL menant à la page de modification des Transactions
    path('modif_transaction/<int:id>/', views.modifierTransaction , name="modifierTransaction"),

    #/market/supp_transaction : URL menant à la page de suppression des transactions
    path('supp_transaction/<int:id>/', views.supprimerTransaction , name="supprimerTransaction"),

     #/market/modif_achat : URL menant à la page de modification des achats
    path('modif_achat/<int:id>/', views.modifierAchat , name="modifierAchat"),

    #/market/supp_achat : URL menant à la page de suppression des achats
    path('supp_achat/<int:id>/', views.supprimerAchat , name="supprimerAchat"),

     #/market/modif_facture : URL menant à la page de modification des Factures
    path('modif_facture/<int:id>/', views.modifierFacture , name="modifierFacture"),

    #/market/supp_client : URL menant à la page de suppression des facutres
    path('supp_facture/<int:id>/', views.supprimerFacture , name="supprimerFacture")




]