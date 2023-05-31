from math import sqrt

def nombreElement(nombre, i): # Fonction permettant de se rassurer que la taille du tableau/matrice soit au moins >= 2 avant l'arret de l'enregistrement
    while((nombre == -1) and (i <= 2)):
        print("!!!Erreur, vous essayez d'arreter l'enregistrement des valeurs or la taille du tableau est inferieur a 2, veuiller entrer au moins 2 elements avant de marquer l'arret en saisissant '-1'")
        nombre = int(input("Veuiller entrer la Valeur X{} : ".format(i)))
        if(nombre == -1):
            return nombreElement(nombre,i)
        else:
            while(nombre < 0):
                nombre = int(input("Veuillez entrer un nombre positif : "))
    
    return nombre

def Verification(nombre): # Fonction permettant de se rassurer qu'aucun nombre negatif excepte -1(qui permet de mettre fin a la recuperation des nombres) ne sera enregistre dans le jeu de donnees
    while(nombre < 0):
        if(nombre == -1):
            return nombre
        else:
            nombre = int(input("Veuillez entrer un nombre positif : "))
    return nombre

def PlusGrandDirect(tableau, nombre): #Fonction permettant de recuperer l'indice d'un quartile dans le tableau des ECC, ou alors son superieur directe
    for elt in tableau:
        if(elt >= nombre):
            return elt

def Taille(tableau): #Fonction permettant de retourner la taille d'un tableau
    nbre = 0
    for elt in tableau:
        nbre += 1
    return nbre


###################  A) Cas des variables discretes  ##################

def Vdiscrete():
    M = [[],[]] # simulation d'une matrice de taille 2*n. la liste d'indice 0 represente les valeurs de la variable tandis que la liste d'indice 1 represente les valeurs des effectifs correspondants.
    nombre = 0
    i = 1
    total = 0
    print("---------------------Cas de variables discretes---------------------")
    print("\n")
    print("Veuillez entrer les valeurs de la variable X observee")
    print("Une fois toutes les valeurs entrees, tapez '-1' pour marquer la fin")
    print("")
    
    while(nombre != -1):
        nombre = int(input("Valeur X{} : ".format(i)))
        nombre = Verification(nombre)
        nombre = nombreElement(nombre,i)
        M[0].append(nombre)
        i += 1
    M[0].remove(-1)

    nombre = 0
    i = 1
    tailleMatrice = Taille(M[0])

    print("")
    print("Veuillez a present entrer respectivement les effectifs enregistres pour chaque valeur Xi")

    for i in range(tailleMatrice):
        nombre = int(input("Effectif n{} : ".format(i+1)))
        while(nombre < 0):
            nombre = int(input("Veuillez entrer un nombre positif : "))        
        M[1].append(nombre)

    for elt in M[1]:  #calcul de l'effectif total
        total += elt

    #       1) Affichage de la matrice     #
    
    print("\nSoit a avoir les donnees statistiques suivantes : \n")  

    print("Valeur(X)    : ",end="\t")
    for elt in M[0]:
        print(elt,end="\t")
    
    print("\n")
    print("Effectif(ni) : ",end="\t")

    for elt in M[1]:
        print(elt,end="\t")
    
    print("\n")

    #       2-a) Calcule et affichage des ECC       #
    
    T1 = []
    y = 0

    T1.append(M[1][0])

    for k in range(tailleMatrice-1):
        T1.append(round((T1[y] + M[1][k+1]),2))
        y += 1

    print("\nLe tableau des Effectifs Cumules Croissant est : \n")
    print("T1(ECC)      : ",end="\t")
    
    for elt in T1:
        print(elt,end="\t")

    print("")

    #       2-b) Calcule et affichage des FCC       #
    T2 = []

    for elt in T1:
        T2.append(round((elt / total),2))

    print("\nLe tableau des Frequences  Cumulees Croisante est : \n")
    print("T2(FCC)      : ",end="\t")

    for elt in T2:
        print(elt,end="\t")
    
    print("")

    #       3) Calcule et affichage de toutes les valeurs de la tendance centrale.
    print("\nValeurs de la tendance centrale : \n")
    #recherche du mode
    Max = -1
    Mode = []
    for elt in M[1]:
        if elt >= Max:
            Max = elt
    
    for i in range(tailleMatrice):
        if M[1][i] == Max:
            Mode.append(M[0][i])
    

    #recherche de la moyenne
    i = 0
    som = 0
    for elt in M[0]:
        som += (elt * M[1][i])
        i += 1

    Moyenne = round((som / total),2) #Valeur de la moyenne

    #recherche de la mediane
    n = total / 2
    indMed = PlusGrandDirect(T1,n)
    Mediane = -1
    i = 0

    for elt in T1:
        if(elt == indMed):
            Mediane = M[0][i]
        i += 1

    #recherche des quartiles
    Q1 = Q3 = -1   
    Q2 = Mediane

    n1 = total / 4
    indQ1 = PlusGrandDirect(T1,n1)
    i = 0

    for elt in T1:
        if(elt == indQ1):
            Q1 = M[0][i] #Valeur du premier quartile
        i += 1
    
    n3 = (3*total) / 4
    indQ3 = PlusGrandDirect(T1,n3)
    i = 0

    for elt in T1:
        if(elt == indQ3):
            Q3 = M[0][i] #Valeur du troisieme quartile
        i += 1

    print("******************************")
    print("Mode = ",Mode)
    print("Moyenne = ",Moyenne)
    print("Mediane = ",Mediane)
    print("Q1 = ",Q1)
    print("Q2 = ",Q2)
    print("Q3 = ",Q3)
    print("******************************")

    #       4) Calcule et affichage de toutes les valeurs de dispersion
    print("\nValeurs de la dispersion: \n")
    #recherche de la variance
    R = 0
    Vtmp = 0
    for elt in M[1]:
        Vtmp += (elt * (((M[0][R]) - Moyenne)*((M[0][R]) - Moyenne)))
        R += 1

    Variance = round((Vtmp / total),2) #Valeur de la Variance

    #recherche de l'ecart-type
    EcartType = round((sqrt(Variance)),2) #Valeur de l'ecart-type

    #recherche de l'intervalle interquartile
    EIQ = Q3 - Q1 #Valeur de l'intervalle interquartile

    #recherche de l'etendu
    etendu = M[0][tailleMatrice-1] - M[0][0] #Valeur de l'etendu

    #recherche du coefficient de variation
    CV = round((EcartType / Moyenne),2) #Valeur du coefficient de variation

    print("******************************")
    print("Variance = ",Variance)
    print("Ecart-type = ",EcartType)
    print("Ecart interquartile = ",EIQ)
    print("Etendu = ",etendu)
    print("Coefficient de variation = ",CV)
    print("******************************")

##################   B) Cas des variables continues  ##################

def Vcontinue():
    M1 = [[],[],[]] # simulation d'une matrice de taille 3*n. la liste d'indice 0 represente la borne inferieur de l'intervalle, la liste d'indice 1 represente la borne superieure, et la liste d'indice 2 represente les effectifs correspondants
    inf = 0
    i = 1
    print("---------------------Cas de variables continues---------------------")
    print("\n")
    print("Veuillez entrer les valeurs de la variable X observee")
    print("Une fois toutes les valeurs entrees, tapez '-1' pour marquer la fin")
    print("NB: Le remplissage se fera directement par classe, de la borne inferieur vers la borne superieur\n")
    print("A SAVOIR : l'arret du remplissage des donnees ne peut etre effectuee lors de la recuperation de la borne superieur, en d'autres termes, une fois la borne inferieur saisi, il est obligatoire d'entrer egalement la borne superieur avant de saisir '-1' pour signaler l'arret de la recuperation\n")

    while(inf != -1):
        inf = int(input("Borne inferieur {} : ".format(i)))
        inf = Verification(inf)
        inf = nombreElement(inf,i)
        if(inf != -1):
            sup = int(input("Borne superieur {} : ".format(i)))
            while(sup < 0):
                sup = int(input("Veuillez entrer un nombre positif : "))
            
        i += 1

        M1[0].append(inf) #Enregistrement de la borne inferieur
        M1[1].append(sup) #Enregistrement de la borne superieur

    M1[0].remove(-1)
    tailleMatrice2 = Taille(M1[0])
    M1[1].pop(tailleMatrice2-1)
    nombre = 0
    print("")
    print("Veuillez a present entrer respectivement les effectifs enregistres pour chaque intervale : \n")
    for i in range(tailleMatrice2):
        nombre = int(input("Effectif n{} : ".format(i+1)))
        while(nombre < 0):
            nombre = int(input("Veuillez entrer un nombre positif : "))        
        M1[2].append(nombre)
        

    #       1) Affichage de la matrice     #
    
    print("\nSoit a avoir les donnees statistiques suivantes : \n")  

    print("Borne inferieur : ",end="\t")
    for elt in M1[0]:
        print(elt,end="\t")
    
    print("\n")
    print("Borne superieur : ",end="\t")

    for elt in M1[1]:
        print(elt,end="\t")

    print("\n")
    print("Effectifs (ni)  : ",end="\t")

    for elt in M1[2]:
        print(elt,end="\t")    
    print("\n")

    #       2-a) Calcule et affichage des densites      #
    T3 = []
    i = 0
    for elt in M1[2]:
        tmp = M1[1][i] - M1[0][i]
        T3.append(round((elt / tmp),2))
        i += 1
    
    print("Le tableau des densites est : \n")
    print("T3(densites)    : ",end="\t")
    for elt in T3:
        print(elt,end="\t")
    print("")


    #       2-b) Calcule et affichage des ECC     #

    T4 = []
    y = 0

    T4.append(M1[2][0])

    for k in range(tailleMatrice2-1):
        T4.append(round((T4[y] + M1[2][k+1]),2))
        y += 1

    print("\nLe tableau des Effectifs Cumules Croissant est : \n")
    print("T4(ECC)         : ",end="\t")
    
    for elt in T4:
        print(elt,end="\t")

    print("")

    #       2-b) Calcule et affichage des FCC     #
    total = 0
    for elt in M1[2]:
        total += elt

    T5 = []

    for elt in T4:
        T5.append(round((elt / total),2))

    print("\nLe tableau des Frequences  Cumulees Croisante est : \n")
    print("T5(FCC)         : ",end="\t")

    for elt in T5:
        print(elt,end="\t")
    
    print("")    


    #       3) Calcule et affichage de toutes les valeurs de la tendance centrale.      #

    print("\nValeurs de la tendance centrale : \n")
    #recherche de la classe modale
    Dmax = -1
    for elt in T3:
        if(elt >= Dmax):
            Dmax = elt
    
    i = 0
    pos = 0 #pos ici representera la position de la densite maximal
    trouve = False
    for elt in T3:
        if(elt == Dmax):
            trouve = True
            aClassMod = M1[0][i]
            bClassMod = M1[1][i]
        if(trouve == False):
            pos += 1

        i += 1

    #recherche du mode

    ampli = M1[1][pos] - M1[0][pos]
    d1 = M1[2][pos] - M1[2][pos-1]
    d2 = M1[2][pos] - M1[2][pos+1]

    Mode = round((M1[0][pos] + ((d1 / (d1 + d2))*ampli)),2)
    

    #recherche de la moyenne
    i = 0
    som = 0
    for elt in M1[2]:
        centre = (M1[0][i] + M1[1][i]) / 2
        som += (elt * centre)
        i += 1

    Moyenne = round((som / total),2) #Valeur de la moyenne

    #recherche de la mediane
    n = (total * 50) / 100
    indMed = PlusGrandDirect(T4,n)
    
    trouve = False
    i = 0
    pos = 0

    for elt in T4:
        if(elt == indMed):
            trouve = True
        if(trouve == False):
            pos += 1

    Mediane = round(((((n - T4[pos-1]) * (M1[1][pos] - M1[0][pos])) / (T4[pos] - T4[pos-1])) + M1[0][pos]),2)

    #recherche des quartiles
    
    n1 = (total * 25) / 100
    indQ1 = PlusGrandDirect(T4,n1)
    
    trouve = False
    i = 0
    pos = 0

    for elt in T4:
        if(elt == indQ1):
            trouve = True
        if(trouve == False):
            pos += 1
    if(pos == 0):
        Q1 = round(M1[0][pos],2)
    else:
        Q1 = round(((((n1 - T4[pos-1]) * (M1[1][pos] - M1[0][pos])) / (T4[pos] - T4[pos-1])) + M1[0][pos]),2) #premier quartile
    Q2 = Mediane # deuxieme quartile

    n3 = (total * 75) / 100
    indQ3 = PlusGrandDirect(T4,n3)
    
    trouve = False
    i = 0
    pos = 0

    for elt in T4:
        if(elt == indQ3):
            trouve = True
        if(trouve == False):
            pos += 1

    Q3 = round(((((n3 - T4[pos-1]) * (M1[1][pos] - M1[0][pos])) / (T4[pos] - T4[pos-1])) + M1[0][pos]),2) #troisieme quartile   


    print("******************************")
    print("Classe modale = [{} ; {}[ ".format(aClassMod,bClassMod))
    print("Mode = ",Mode)
    print("Moyenne = ",Moyenne)
    print("Mediane = ",Mediane)
    print("Q1 = ",Q1)
    print("Q2 = ",Q2)
    print("Q3 = ",Q3)
    print("******************************")


    #       4) Calcule et affichage de toutes les valeurs de dispersion

    print("\nValeurs de la dispersion: \n")
    #recherche de la variance
    R = 0
    Vtmp = 0
    for elt in M1[2]:
        centre = (M1[0][R] + M1[1][R]) / 2
        Vtmp += (((centre - Moyenne) * (centre - Moyenne)) * M1[2][R])
        R += 1
    #carMoy = Moyenne * Moyenne
    Variance = round((Vtmp/total),2) #Valeur de la Variance

    #recherche de l'ecart-type
    EcartType = round((sqrt(Variance)),2) #Valeur de l'ecart-type

    #recherche de l'intervalle interquartile
    EIQ = Q3 - Q1 #Valeur de l'intervalle interquartile

    #recherche de l'etendu
    etendu = M1[1][tailleMatrice2-1] - M1[0][0] #Valeur de l'etendu

    #recherche du coefficient de variation
    CV = round(((EcartType / Moyenne)),2) #Valeur du coefficient de variation

    print("******************************")
    print("Variance = ",Variance)
    print("Ecart-type = ",EcartType)
    print("Ecart interquartile = ",EIQ)
    print("Etendu = ",etendu)
    print("Coefficient de variation = ",CV)
    print("******************************")

    print("\nFin du programme...\n")

##################   C) MENU    #################

def menu():
    print("")
    print("********************* BIENVENU A VOUS *********************")
    print("")
    print("Voulez-vous realiser une etude : ")
    print("\t1) Sur variable discrete ?")
    print("\t2) Sur variable continue ?")
    
    choix = int(input("Choix : "))
    while((choix != 1) and (choix != 2)):
        choix = int(input("Veuillez choisir un nombre entre 1 et 2 selon leur correspondance : "))
    
    if(choix == 1):
        Vdiscrete()
    else:
        Vcontinue()

menu()