#Création du dictionnaire réponse
#clé =mot
#valeur = liste des icones
dico={}
dico['tronçonneuse']=[23,41,71,65]
dico['parapluie']=[0,34,56]
dico['Titanic']=[10,20,56,64,37]
dico['Sapin']=[7,94,108,19]
dico['Football']=[5,51,91,115,116]

#liste_icones=listes des icones sélectionnées par les clic souris
#reponse=mot saisi
def verif_reponse(liste_icones,reponse):
    if reponse in dico.keys() :
        print(dico[reponse])
        print(liste_icones)
        compteur=0
        for val in liste_icones:
            if val in dico[reponse]:
                compteur=compteur+1
        if compteur==len(liste_icones):
            return True
    else :
        return False


liste_mots=['vampire','musee','camion','lion','cheval','perceuse',
'pilote','pyjama','licorne','etoile de mer','singe',
'casque','pere noel','fee','la panthere rose','moulin',
'fourchette','garage','dauphin','moustique','cinema',
'loup','cafe','radar','Peter Pan','ping-pong','tigre',
'ambulance','parfum','pie','montre','abeille','puits',
'vache','kangourou','télé-achat','docteur','canari',
'dentier','grenouille','marguerite','canadair','GPS',
'caleçon','guitare','le seigneur des anneaux','squelette',
'croissant','cochon','piscine','fusil','citrouille','natation',
'tricycle','vigneron','clown','valise','Casper','les Tortues Ninja',
'BD','airbag','vélo','escargot','tondeuse','chocolat',
'chauve-souris','espadon','gymnase','cuisine','lac',
'Dumbo','Spiderman','Iron Man','la Reine des neiges',
'Bambi','ferrari','sapin','ecluse','boite de conserve',
'Saint-Valentin','assassin','montagne','taupe','tempête',
'parasol','soleil','covid 19','fraise','pecheur','tracteur',
'coca-cola','cantine','lycée','Bob Marley','Michael Jordan',
'Thomas Pesquet','Robin des Bois','Titanic','football','rugby',
'escalade','ski','roller','parapluie','immeuble','vacances']
