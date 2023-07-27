##from random import *
import pygame
from pygame.locals import *
##from contre_ordi import*
pygame.init()

#Chargement des images
def chargement_images():
    nbr_icones=117
    icones=[] #nom des icones chargées
    liste_noms=[] #liste avec icone1, icone2, ...
    for i in range(0,nbr_icones):
        nom = 'Images/Icone (' + str(i+1) + ').jpg'
        #liste_icones.append(nom)
        icones.append(pygame.image.load(nom).convert_alpha())
        liste_noms.append('icone'+str(i))
    return icones,liste_noms

#Création du plateau
def plateau(fenetre):
    icones,liste_noms=chargement_images()
    #création dico : clé = (colonne,ligne) ; valeur = nom icone
    #nom icone commence à 0
    #colonne et ligne commencent à 1
    place_icone={}
    x=0
    y=0
    longueur=100
    hauteur=40
    for i in range(0,27,2):
        #colonne 1
        fenetre.blit(icones[i], (x,y))
        place_icone[(1,i//2+1)]=(liste_noms[i],i)
        #colonne 2
        fenetre.blit(icones[i+1], (x+100,y))
        place_icone[(2,i//2+1)]=(liste_noms[i+1],i+1)
        y=y+40
    x=200
    y=0
    for i in range(28,56,2):
        #colonne 3
        fenetre.blit(icones[i], (x,y))
        place_icone[(3,(i-28)//2+1)]=(liste_noms[i],i)
        #colonne 4
        fenetre.blit(icones[i+1], (x+100,y))
        place_icone[(4,(i-28)//2+1)]=(liste_noms[i+1],i+1)
        y=y+40
    x=400
    y=0
    for i in range(56,78,2):
        #colonne 5
        fenetre.blit(icones[i], (x,y))
        place_icone[(5,(i-56)//2+1)]=(liste_noms[i],i)
        #colonne 6
        fenetre.blit(icones[i+1], (x+100,y))
        place_icone[(6,(i-56)//2+1)]=(liste_noms[i+1],i+1)
        y=y+40
    x=600
    y=0
    for i in range(78,104,2):
        #colonne 7
        fenetre.blit(icones[i], (x,y))
        place_icone[(7,(i-78)//2+1)]=(liste_noms[i],i)
        #colonne 8
        fenetre.blit(icones[i+1], (x+100,y))
        place_icone[(8,(i-78)//2+1)]=(liste_noms[i+1],i+1)
        y=y+40
    fenetre.blit(icones[104], (x,y))
    place_icone[(7,14)]=('icone104',104)
    x=800
    y=0
    for i in range(105,117):
        #colonne 9
        fenetre.blit(icones[i], (x,y))
        place_icone[(9,(i-105)+1)]=(liste_noms[i],i)
        y=y+40
    pygame.image.save(fenetre,'Images/plateau.bmp')
    return icones,place_icone