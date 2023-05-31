import matplotlib
import matplotlib.pyplot as plt
import numpy as nb
from math import sqrt

def verification(nbre): #Fonction permettant de verifier que chaque nombre entré est positif
    while(nbre<0):
        nbre = int(input("Veuillez entrer un nombre positif : "))
    return nbre

#-----------------ENSEMBLE DE FONCTIONS REGROUPÉES POUR PERMETTRE LE TEST DE KHI-2-------------------------#

nkw = [] #Variable dans laquelle sera conserver la valeur du khi final

def LeKhiFinal(tab : list): #Fonction permettant de retourner la valeur du Khi-2
    somme = 0

    for elt in tab:
        for i in range(len(elt)):
            somme += elt[i]
    somme = round((somme),2)

    print("La valeur du Khi-2 est donc : X2 = ",somme)

    nkw.append(somme)

    return somme

def TabKhi(tab : list, result : list): #Fonction prenant en paramettre un tableau et le tableau des effectifs attendus correspondant, et retourne le tableau des Khi-2
    Khi = []

    for i in tab:
        Khi.append([])

    for i in range(len(tab)):
        for j in range(len(tab[0])):
            khi = round((((tab[i][j] - result[i][j])**2) / (result[i][j])),2)
            Khi[i].append(khi)
        
    print("\nTableau des Khi-2\n")

    print("")
    for i in range(len(Khi)):
        print("Ligne {} : ".format(i+1),end="\t")
        for j in Khi[i]:
            print(j,end="\t")
        print("\n")

    LeKhiFinal(Khi)

def TabEff(tab : list): #Fonction prenant en paramettre un tableau avec des effectifs observés, et retournant un tableau des effectifs attendus
    totalL = []
    totalC = []
    result = []
    total = 0
    tmp = 0  

    for G_elt in tab:
        for elt in G_elt:
            total += elt #nombre total d'individu
    
    for G_elt in tab:
        for elt in G_elt:
            tmp += elt
        totalL.append(tmp)#nombre total de chaque ligne
        tmp = 0

    tmp = 0
    k = 0

    for nkw in range(len(tab[0])):
        for G_elt in tab:
            tmp += G_elt[k]
        totalC.append(tmp) #nombre total de colonne
        k += 1
        tmp = 0

    for i in tab:
        result.append([])

    for i in range(len(totalL)):
        for j in range(len(totalC)): 
            Eij = round(((totalC[j] * totalL[i]) / total),2)
            result[i].append(Eij)
    
    print("\nTableau des effectifs attendus:\n")
    print("")
    for i in range(len(result)):
        print("Ligne {} : ".format(i+1),end="\t")
        for j in result[i]:
            print(j,end="\t")
        print("\n")
        
    return TabKhi(tab, result)
        
def Khi2(tab : list):
    print("")
    print('|*',end="Application de la loi de Khy-2".center(70,'-')+"*|")
    print("")

    return TabEff(tab)

#-----------------ENSEMBLE DE FONCTIONS REGROUPÉES POUR PERMETTRE LE TEST STUDENT--------------------------#

def moyenneX(tab : list): #Fonction retournant la moyenne en x
    somme = 0
    taille = 0

    for elt in tab[0]:
        somme += elt
        taille += 1

    return (somme / taille)

def moyenneY(tab : list): #Fonction retournant la moyenne en y
    somme = 0
    taille = 0

    for elt in tab[1]:
        somme += elt
        taille += 1

    return (somme / taille)

def aEstim(tab : list): #Fonction retournant la valeur de a chapeau (a estimé)
    num = 0
    denum = 0
    i = 0
    
    x = moyenneX(tab)
    y = moyenneY(tab)

    for elt in tab[0]:
        num += (elt - x)*(tab[1][i] - y)
        i += 1

    for elt in tab[0]:
        denum += (elt - x)**2

    return (num / denum)

def varianceErr(tab : list): #Fonction retournant la variance estimée de l'erreur
    SomY_Ychap = 0
    k = 0
    Xbar = moyenneX(tab)
    Ybar = moyenneY(tab)
    aChap = aEstim(tab)

    bChap = Ybar - (aChap * Xbar)

    for i in tab[0]:
        SomY_Ychap += (tab[1][k] - ((aChap * i) + bChap))**2
        k += 1
    
    return (SomY_Ychap / (k - 2))

def varianceX(tab : list): #Fonction retournant la variance estimée
    somX_XbarCarre = 0
    x = moyenneX(tab)

    for elt in tab[0]:
        somX_XbarCarre += (elt - x)**2

    varErr = varianceErr(tab)

    return (varErr / somX_XbarCarre)

def degreLib(tab : list): #Fonction retournant le degres de liberte 
    i = 0
    for elt in tab[0]:
        i += 1
    
    return (i-2)

def Student(tab : list):
    print("")
    print('|*',end="Application de la loi de Student".center(50,'-')+"*|")
    print("")

    studTab = [12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228, 2.201, 2.178, 2.16, 2.14, 2.13, 2.11, 2.109, 2.10, 2.09, 2.08, 2.079, 2.073, 2.068, 2.063, 2.059, 2.055, 2.051, 2.048, 2.045, 2.042]
    Xbar = moyenneX(tab)
    Ybar = moyenneY(tab)
    aChap = round((aEstim(tab)),2)
    ddl = degreLib(tab)

    bChap = round((Ybar - (aChap * Xbar)),2)

    print("\nD'apres les données dans notre tableau, nous avons l'équation estimée : Y^ = {}X + {}\n".format(aChap, bChap))

    ecartX = sqrt(varianceX(tab))

    if aChap < 0:
        valAbsA = (-1)*aChap
    else:
        valAbsA = aChap

    tEtoile = round((valAbsA / ecartX),2) #valeur du test de student calculée

    print("test de student calculé : T* = ",tEtoile)
    print("test de student tabul   : Tt = ",studTab[ddl-1])

    print("\nInterpretation : ",end="")

    if(tEtoile > studTab[ddl-1]):
        print("La valeur du student calculée ({}) etant superieur a la valeur du student tabul ({}), nous pouvons donc dire que la variable exogène est significative et contribu a l'explication de la variable endogène. Ainsi, on rejette donc l'hypothese nulle (Ho) et on conclu que les variables etudées ne sont pas independantes\n".format(tEtoile,studTab[ddl-1]))
    else:
        print("La valeur du student calculée ({}) etant inferieur a la valeur du student tabul ({}), nous pouvons donc dire que la variable exogène n'est pas significative et ne contribu pas a l'explication de la variable endogène. Ainsi, on admet donc l'hypothese nulle (Ho) et on conclu que les variables etudées sont independantes\n".format(tEtoile,studTab[ddl-1]))

#-----------------ENSEMBLE DE FONCTIONS REGROUPÉES POUR PERMETTRE LE TEST DE FISHER--------------------------#

def moyenneTotal(tab : list): #Fonction permettant de retourner la moyenne total ( X bar bar)
    somme = 0
    nkw = 0
    for elt in tab[0]:
        somme += elt + tab[1][nkw]
        nkw += 1
    
    return (somme / (nkw*2))

def SCT(tab : list): #Fonction permettant de retourner la somme des carres totals
    somme = 0
    nkw = 0

    moyT = moyenneTotal(tab)

    for elt in tab[0]:
        somme += (((elt - moyT)**2) + ((tab[1][nkw] - moyT)**2))
        nkw += 1
    
    return somme

def SCintra(tab : list): #Fonction permettant de retourner la somme des carres intraclasse
    somme = 0
    nkw = 0
    xbar = moyenneX(tab)
    ybar = moyenneY(tab)

    for elt in tab[0]:
        somme += (((elt - xbar)**2) + ((tab[1][nkw] - ybar)**2))
        nkw += 1
    
    return somme

def SCinter(tab : list): #Fonction permettant de retourner la somme des carres interclasse
    somme = 0
    xbar = moyenneX(tab)
    ybar = moyenneY(tab)
    T = moyenneTotal(tab)

    for elt in tab[0]:
        somme += ((xbar - T)**2) + ((ybar - T)**2)
    
    return somme

def degreLibFish(tab : list): #Fonction retournant le degres de liberte
    m = 0

    for elt in tab[0]:
        m += 1
    
    return ((m*2)-1)

def degreLibInter(tab : list): #Fonction retournant le degres de liberte interclasse
    return (2-1)

def degreLibIntra(tab : list): #Fonction retournant le degres de liberte intraclasse
    somme = 0
    
    for elt in tab[0]:
        somme += 1 

    return (2 * (somme -1))

def Fisher(tab : list):
    print("")
    print('|*',end="Application de la loi de Fisher".center(50,'-')+"*|")
    print("")

    tabDeCor = [161, 18.5, 10.1, 7.71, 6.61, 5.99, 5.59, 5.32, 5.12, 4.96, 4.84, 4.75, 4.67, 4.60, 4.54, 4.49, 4.45, 4.41, 4.38, 4.35, 4.33, 4.30, 4.28, 4.26]
    xbar = moyenneX(tab)
    ybar = moyenneY(tab)

    sct = SCT(tab)
    scinter = SCinter(tab)
    scintra = SCintra(tab)
    ddl = degreLibFish(tab)
    ddl_inter = degreLibInter(tab)
    ddl_intra = degreLibIntra(tab)

    F = round(((scinter / ddl_inter) / (scintra / ddl_intra)),2)
    valCritique = tabDeCor[ddl_intra-1] - 1
    
    print("\ntest de Fisher : F = {}\nValeur critique : Vc = {}\n".format(F,valCritique))


    print("\nInterpretion : ",end="")

    if(F > valCritique):
        print("la valeur de F ({}) etant superieur a la valeur de Vc ({}), nous pouvons donc dire que le test est significatif. Ainsi, on rejette donc l'hypothese nulle (Ho) et on conclu que les variables etudiées ne sont pas independantes".format(F, valCritique))
    else:
        print("la valeur de F ({}) etant inferieur a la valeur de Vc ({}), nous pouvons donc dire que le test n'est pas significatif. Ainsi, on admet donc l'hypothese nulle et on conclu que les variables etudiées sont independantes".format(F, valCritique))
 
def menu():
    print("")
    print("BIENVENU A VOUS".center(60,'*'))
    print("")
    
    print("Soit a realiser une etude statistique en utilisant les lois de Khi-2, Student, et Fisher\n")
    l = verification(int(input("Veuillez entrer le nombre de ligne de votre tableau : ")))
    c = verification(int(input("Veuillez entrer le nombre de colonne de votre tableau : ")))

    M = []
    choix = -1

    for i in range(l):
        M.append([])

    for i in range(l):
        for j in range(c):
            nbre = verification(int(input("Element [{}][{}] : ".format((i+1),(j+1)))))
            M[i].append(nbre)
        print("")

        
    print("Nous avons donc le tableau : \n")

    for i in range(l):
        print("Ligne {} : ".format((i+1)),end="\t")
        for j in range(c):
            print(M[i][j],end="\t")
        print("\n")

    while(choix != 0):

        print("Veillez choisir une option : ")
        print("\t0) Quitter")
        print("\t1) Réaliser le test du Khi-2   ?")
        print("\t2) Réaliser le test de Student ?")
        print("\t3) Réaliser le test de Fisher  ?")

        choix = int(input("\nChoix : "))

        while(choix != 0 and choix != 1 and choix != 2 and choix != 3):
            choix = int(input("Veuillez choisir '1', '2', ou '3' selon leur correspondance : "))

        if(choix == 1):
            Khi2(M)
            D = (l-1)*(c-1) #Degres de liberte
            Corres = [3.84, 5.99, 7.82, 9.49, 11.07, 12.59, 14.06, 15.50, 16.91, 18.30, 19.67, 21.02, 22.36, 23.68, 24.99, 26.29, 27.58, 28.86, 30.14, 31.41, 32.67, 33.92, 35.17, 36.41, 37.65, 38.88, 40.11, 41.33, 42.55, 43.77]
            print("\nInterpretation : ",end="")
            if(nkw[0] <= Corres[D-1]):
                print("La valeur du khi-2 ({}) etant inferieur à la correspondance du degré de liberté ({}), nous pouvons donc dire que le test n'est pas significatif. Ainsi, on admet donc l'hypothese nulle et on conclu que les variables etudiées sont independantes".format(nkw[0], Corres[D-1]))
                print("")
            else:
                print("La valeur du khi-2 ({}) etant superieur à la correspondance du degré de liberté ({}), nous pouvons donc dire que le test est significatif. Ainsi, on rejette donc l'hypothese nulle et on conclu que les variables etudiées ne sont pas independantes".format(nkw[0], Corres[D-1]))   
                print("")   
    
        elif(choix == 2):
            Student(M)

        elif(choix == 3):
            Fisher(M)

        else:
            print("\nFin du programme...\n")
            return 

        cordoX = []
        cordoY = []
        cordo  = []

        for i in M[0]:
            cordoX.append(i)
        for i in M[1]:
            cordoY.append(i)

        cordo.append(cordoX)
        cordo.append(cordoY)

        for i in range(len(cordo[0])):
            x = cordo[0][i]
            y = cordo[1][i]
            plt.scatter(x,y, marker='o', color='b')


        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Nuage de points")
        plt.grid(True)
        plt.show()    

menu() #Appelle de la fonction principale