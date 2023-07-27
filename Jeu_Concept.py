"""
    jeu Concept à 2 joueurs humains

"""

#---------------1ère partie - Création page "Accueil"--------------------#
#Importation des bibliothèques
from random import *
from contre_ordi import*
from conception_plateau import*
import pygame
from pygame.locals import *
pygame.init()

#Choix des courleurs en RGB et de la police pour les textes
BLUE = (49, 140, 231)
VIOLET = (150,131,236)
GREEN = (0, 128, 0)
ORANGE = (230,56,40)
font = pygame.font.SysFont('Comic Sans MS,Arial', 20)
font2 = pygame.font.SysFont('Verdana,Arial', 12)


#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((850,750))

#Titre de la fenêtre
pygame.display.set_caption("Jeu Concept")

#chargement du fond
fond = Color(242,255,255)
fenetre.fill(fond)

#fonction permettant d'afficher la page "accueil" et retourne le not à trouver
def debut_jeu():
    #affichage des consignes pour l'écran du JOUEUR 1
    consigne_joueur1 = font.render('Le Joueur 1 doit faire deviner le mot ci-dessous',True,BLUE)
    fenetre.blit(consigne_joueur1, (50,50))
    pygame.display.flip()

    # zone mot, choix aléatoire de l'entier i dans liste_mots
    i= randint(0,len(liste_mots)-1)
    mot= liste_mots[i]
    mot_joueur1 = font.render(mot,True,VIOLET)  #creation zone du mot
    fenetre.blit(mot_joueur1,(50,560)) #affichage de la zone
    pygame.display.flip() #actualisation de l'affichage
    return mot #retourne le mot à trouver par le joueur 2

#Affichage de la page d'accueil et attendre 2000 ms
mot= debut_jeu()  #récupérer le nom à chercher en appelant la bonne fonction
pygame.time.wait(2000)   #attendre 2000 ms

##       Faire une vérification de votre travail      ######
## Mettre toute la suite du programme en commentaires ######



#-------------2ème partie - Création de l'interface  de jeu -------------------#
#Chargement et affichage du plateau -> voir outils généraux (partie 2)
fenetre.fill(fond)
icones,place_icone=plateau(fenetre)
image_niveau = 'Images/plateau.bmp' #Importer le fond
image = pygame.image.load(image_niveau).convert_alpha()
fenetre.blit(image,(0,0))
pygame.display.flip()

#Création de la zone de texte "consigne" -> voir outils généraux (partie 3)
consigne = font.render("Joueur 1 : Cliquer sur l'icone du concept principal puis sur 4 icones au maximum",True,BLUE)   #saisie texte
fenetre.blit(consigne,(50,560))  #affichage texte
pygame.display.flip()  #actualisation affichage


#Création de la zone de texte "concept principal" -> voir outils généraux (partie 3)
concept_principal = font2.render('Concept Principal',True,VIOLET)   #saisie texte
fenetre.blit(concept_principal,(50,590))  #affichage texte
pygame.display.flip()  #actualisation affichage

#Création de la zone de texte "Votre réponse" -> voir outils généraux (partie 4)
texte_reponse = font.render('Votre réponse : ', True, ORANGE)  #saisie texte

#Récupération de la réponse
reponse_joueur2 = ""  #initialisation de la réponse du JOUEUR 2
zone_reponse_joueur2 = font.render(reponse_joueur2, True, ORANGE) #saisie texte

#Création du bouton "valider" -> voir outils généraux (partie 4)
bouton = pygame.draw.rect(fenetre,BLUE,(700,620,100,40))   #tracer le rectangle
bouton_text = font.render('Valider',True,ORANGE)      #saisie texte "Valider"
fenetre.blit(bouton_text,(725,628))  #affichage texte
pygame.display.flip()  #actualisation affichage


####       Faire une vérification de votre travail      ######
#### Mettre toute la suite du programme en commentaires ######


#------------------ 3ème partie : Boucle principale du jeu ---------------------#

#initialisation des varaibles
nbr_icones_select=0
stop_icone=False
liste_icones=[]

#boucle principale -> voir outils généraux (partie 5)
continuer = True
while continuer == True:
    for event in pygame.event.get():
        # Pour quitter
        if event.type == pygame.QUIT:
            continuer = False
            break
        #gestion des événements à la souris -> voir outils généraux (partie 6)
        if event.type == MOUSEBUTTONDOWN :
            if event.button == 1:
                #Sélection des 5 icones max
                if nbr_icones_select<5 and stop_icone==False:
                    nbr_icones_select=nbr_icones_select+1

                    #récupération des coordonnées du clic de la souris
                    clic_x = event.pos[0]
                    clic_y = event.pos[1]
                    #affichage du texte "Votre réponse" si moins de 5 icônes sélectionnées
                    #et appuie sur le bouton "Valider"
                    if (700<=clic_x<=800 and 620<=clic_y<=660) and stop_icone==False:
                        fenetre.blit(texte_reponse, (100,670))
                        pygame.display.flip()
                        stop_icone=True
                        break
                    else :
                        #déterminer le numéro de la colonne et de la ligne sur le plateau
                        colonne=clic_x//100+1
                        ligne=clic_y//40+1
                        #retrouver le numéro de l'icone choisi
                        icone_select=place_icone[(colonne,ligne)]
                        n=icone_select[1]  #n=numéro de l'icone (voir feuille)
                        #constitution de la liste des icones sélectionnées
                        liste_icones.append(n)

                        #affichage de l'icone du concept principal à sa place (50,620)
                        if nbr_icones_select==1:
                            fenetre.blit(icones[n],(50,620))
                            pygame.display.flip() #actualisation affichage
                        #affichage des autres icones qui sont dans la liste "icones" au rang "n"
                        #à la position (230,620) -> voir schéma feuille
                        else :
                            fenetre.blit(icones[n],(230+(nbr_icones_select-2)*100,630))
                            pygame.display.flip() #actualisation affichage

                        #affichage du texte "Votre réponse" si 5 icônes sélectionnées
                        if nbr_icones_select==5:
                            fenetre.blit(texte_reponse,(50,675))  #affichage texte
                            pygame.display.flip()
                            stop_icone=True
                else :
                    break

##
##       Faire une vérification de votre travail      ######
## Mettre toute la suite du programme en commentaires ######


        #Gestion de la saisie au clavier de la réponse -> voir outils généraux (partie 7)
        if event.type == KEYDOWN :
            #gérer la fermeture de la fenêtre avec touches "entrée" et "escape"
            if event.key in (K_RETURN, K_ESCAPE):
                continuer = False
                break
            #gérer les erreurs de frappe dans la réponse du JOUEUR 2
            elif event.key == K_BACKSPACE or event.key == K_DELETE :
                reponse_joueur2 = reponse_joueur2[:-1]
                #afficher le plateau vierge
                fenetre.fill(fond)
                #afficher le texte "texte_reponse" à la position (100,670)
                fenetre.blit(texte_reponse,(100,670))
                #affichage de la réponse en enlevant le caractère supprimé
                zone_reponse_joueur2 =  font.render(reponse_joueur2,True, ORANGE) #saisir le texte "reponse_joueur2"
                fenetre.blit(zone_reponse_joueur2,(300,670)) #Affichage de la réponse "zone_reponse_joueur2" à la position (300,670)
                pygame.display.flip() #actualisation affichage

            #Récupération de la réponse du JOUEUR 2
            else:
                reponse_joueur2 = reponse_joueur2 + event.unicode #voir outils généraux (partie 7)
            #zone de texte pour la réponse qui s'affiche au fur et mesure de la saisie
            zone_reponse_joueur2 = font.render(reponse_joueur2,True,ORANGE) #saisir le texte "reponse_joueur2"
            #Affichage de la réponse "zone_reponse_joueur2" à la position (300,670)
            fenetre.blit(zone_reponse_joueur2,(300,670))
            pygame.display.flip() #actualisation affichage


##       Faire une vérification de votre travail      ######
## Mettre toute la suite du programme en commentaires ######

#-------contre JOUEUR2-------#
if reponse_joueur2 == mot: # la réponse du JOUEUR2 est le mot à deviner
    #compléter le dico pour IA -> voir outils généraux (partie 8)
    fichier = open("dico_concept.py","a")
    fichier.close()
    #saisie du texte "Gagné"
    affichage = font.render("Gagné",True,GREEN)
else :
    #saisie du texte "Perdu"
    affichage = font.render("Perdu",True,ORANGE)
#affichage du texte "affichage" à la position (500,670)
fenetre.blit(affichage,(500,670))
pygame.display.flip() #actualisation affichage
pygame.time.wait(2000) #mettre un temps d'attente de 2000 ms


#Fermeture de la fenêtre sans temps d'attente -> voir outils généraux (partie 1)
pygame.display.update()
pygame.quit()