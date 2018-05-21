# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
import random

tours = 0
compteurBatonsPartie = 0
compteur = 0
first = 1
taille = 15
difficulty = 0
callbackVar = 0
Nom = 'Joueur 1'
Nom2 = 'Joueur 2'
j1 = 'Joueur 1'
j2 = 'Joueur 2'
LBatonnets = []
LDifficulty = ["rien", "rien", "facile", "normal", "difficile", "impossible"]
L15 = [2, 6, 10, 14]
L20 = [3, 7, 11, 15, 19]
L25 = [4, 8, 12, 16, 20, 24]
L30 = [1, 5, 9, 13, 17, 21, 25, 29]
L35 = [2, 6, 10, 14, 18, 22, 26, 30, 34]



def Fjouer():
    global jvo, jvj
    go.place_forget()
    jvj = Button(menu, text='Contre un autre joueur', command=Fjvj)
    jvo = Button(menu, text="Contre l'ordinateur", command=Fjvo)
    jvj.place(relx=0.5, rely=0.45, anchor=CENTER)
    jvo.place(relx=0.5, rely=0.55, anchor=CENTER)

def Fjvj():
    global Nom, Nom2, j1, j2, jvo, jvj, appliquer
    jvj.destroy()
    jvo.destroy()
    Nom = Entry(menu, bg="dodger blue")
    Nom2 = Entry(menu, bg="firebrick1")
    Nom.insert(END, 'Joueur 1')
    Nom2.insert(END, 'Joueur 2')
    Nom.place(relx=0.5, rely=0.3, anchor=CENTER)
    Nom2.place(relx=0.5, rely=0.4, anchor=CENTER)
    appliquer = Button(menu, text="Appliquer", command=Fname)
    appliquer.place(relx=0.5, rely=0.6, anchor=CENTER)

def Fname():
    global j1, j2, appliquer, Nom, Nom2, quiCommence, choix, bouton1, bouton2, bouton3
    quiCommence = Label(menu, text="Qui commence ?", bg="white")
    quiCommence.place(relx=0.5, rely=0.25, anchor=CENTER)
    j1 = Nom.get()
    j2 = Nom2.get()
    Nom.destroy()
    Nom2.destroy()
    appliquer.destroy()
    choix = IntVar()
    bouton1 = Radiobutton(menu, text=j1, variable=choix, value=1, command=Fcallback, bg="white")
    bouton2 = Radiobutton(menu, text=j2, variable=choix, value=2, command=Fcallback, bg="white")
    bouton3 = Radiobutton(menu, text="Aléatoire", variable=choix, value=3, command=Fcallback, bg="white")
    bouton1.place(relx=0.5, rely=0.30, anchor=CENTER)
    bouton2.place(relx=0.5, rely=0.40, anchor=CENTER)
    bouton3.place(relx=0.5, rely=0.50, anchor=CENTER)

def Fordre():
    global j1, j2, callbackVar, bouton1, bouton2, bouton3, quiCommence, first, difficulty
    callbackVar = 0
    menu['bg']='lightgray'
    ordre.place_forget()
    bouton1.destroy()
    bouton2.destroy()
    bouton3.destroy()
    quiCommence.destroy()
    if choix.get() == 1:
        difficulty = 0
        Fpattern()
    elif choix.get() == 2:
        difficulty = 1
        Fpattern()
    else :
        difficulty = random.randint(0,1)
        Fpattern()

def Fjvo():
    global jvo, jvj, soft, normal, hard, impossible
    jvo.destroy()
    jvj.destroy()
    soft = Button(menu, text="Facile", command=Fsoft)
    normal = Button(menu, text="Normal", command=Fnormal)
    hard = Button(menu, text="Difficile", command=Fhard)
    impossible = Button(menu, text="Impossible", command=Fimpossible)
    soft.place(relx=0.5, rely=0.35, anchor=CENTER)
    normal.place(relx=0.5, rely=0.45, anchor=CENTER)
    hard.place(relx=0.5, rely=0.55, anchor=CENTER)
    impossible.place(relx=0.5, rely=0.65, anchor=CENTER)


def Fsoft():
    global difficulty
    difficulty = 2
    Fpattern()

def Fnormal():
    global difficulty
    difficulty = 3
    Fpattern()

def Fhard():
    global difficulty
    difficulty = 4
    Fpattern()

def Fimpossible():
    global difficulty
    difficulty = 5
    Fpattern()

def Fretour():
    global callbackVar, jvo, jvj, soft, normal, hard, impossible, difficulty, bouton1, bouton2, bouton3, quiCommence, appliquer, finPartie, arretPartie, relancer, Nom, Nom2, ordre, scaleBaton, labelBaton, labelPattern, taille, LBatonnets, debutPartie, labelNbBaton, compteurBatonsPartie, commence, aQuiLeTour
    callbackVar = 0
    difficulty = 0
    scaleBaton.place_forget()
    scaleBaton.place(relx=0.5, rely=0.1, anchor=CENTER)
    labelNbBaton.place_forget()
    labelNbBaton.place(relx=0.5, rely=0.025, anchor=CENTER)
    try :
        soft.destroy()
    except NameError:
        pass
    try :
        normal.destroy()
    except NameError:
        pass
    try :
        hard.destroy()
    except NameError:
        pass
    try :
        impossible.destroy()
    except NameError:
        pass
    try :
        jvo.destroy()
    except NameError:
        pass
    try :
        jvj.destroy()
    except NameError:
        pass
    try :
        ordre.destroy()
    except NameError:
        pass
    try :
        bouton1.destroy()
    except NameError:
        pass
    try :
        bouton2.destroy()
    except NameError:
        pass
    try :
        bouton3.destroy()
    except NameError:
        pass
    try :
        Nom.destroy()
    except (NameError, AttributeError):
        pass
    try :
        Nom2.destroy()
    except (NameError, AttributeError):
        pass
    try :
        appliquer.destroy()
    except NameError:
        pass
    try :
        quiCommence.destroy()
    except NameError:
        pass
    try :
        labelPattern.destroy()
    except NameError:
        pass
    try :
        photoPattern.destroy()
    except NameError:
        pass
    try :
        debutPartie.destroy()
    except NameError :
        pass
    try :
        finPartie.destroy()
    except NameError:
        pass
    try :
        relancer.destroy()
    except NameError :
        pass
    try :
        arretPartie.destroy()
    except NameError:
        pass
    try :
        commence.destroy()
    except NameError:
        pass
    try :
        aQuiLeTour.destroy()
    except NameError:
        pass

    for i in range(0, taille) :
        try :
            LBatonnets[i].destroy()
        except (NameError, IndexError) :
            pass

    LBatonnets[:] = []
    compteurBatonsPartie = 0

    go.place(relx=0.5, rely=0.5, anchor=CENTER)
    menu.geometry("500x500")
    menu['bg']='white'

def Fcallback():
    global callbackVar, ordre
    if callbackVar == 0:
        ordre = Button(menu, text="Lancer", command=Fordre)
        ordre.place(relx=0.5, rely=0.7, anchor=CENTER)
        callbackVar = 1



def Fpattern():
    global soft, normal, hard, impossible, difficulty, taille, stock1, scaleVar, scaleBaton, labelBaton, labelPattern, debutPartie, labelNbBaton, tourJOUEUR
    scaleBaton.place_forget()
    labelNbBaton.place_forget()
    try :
        soft.destroy()
    except NameError:
        pass
    try :
        normal.destroy()
    except NameError:
        pass
    try :
        hard.destroy()
    except NameError:
        pass
    try :
        impossible.destroy()
    except NameError:
        pass
    menu.geometry("1100x500")
    menu['bg']='lightgray'
    taille = scaleVar.get()
    if taille == 35 :
        photoPattern = PhotoImage(file='Pattern35.pgm')
        stock1 = 58
    elif taille == 30 :
        photoPattern = PhotoImage(file='Pattern30.pgm')
        stock1 = 130
    elif taille == 25 :
        photoPattern = PhotoImage(file='Pattern25.pgm')
        stock1 = 203
    elif taille == 20 :
        photoPattern = PhotoImage(file='Pattern20.pgm')
        stock1 = 275
    else :
        photoPattern = PhotoImage(file='Pattern15.pgm')
        stock1 = 348
    tourJOUEUR = True
    labelPattern = Label(image=photoPattern)
    labelPattern.image = photoPattern
    labelPattern.place(relx=0.5, rely=0.5, anchor=CENTER)
    menu.after(1500, Fbatonnets)
    debutPartie = Label(menu, text="Lancement de la partie...", font=("Helvetica", 20))
    debutPartie.place(relx=0.5, rely=0.2, anchor=CENTER)


def Fbatonnets():
    global LBatonnets, compteur, taille, stock1, debutPartie, difficulty
    compteur = compteur +1
    photoBatonnet = PhotoImage(file='Batonnet.pgm')
    labelBatonnet = Label(image=photoBatonnet)
    labelBatonnet.image = photoBatonnet
    labelBatonnet.place(x=stock1, rely=0.5, anchor=CENTER)
    LBatonnets.append(labelBatonnet)
    stock1 = stock1 +29
    if compteur == taille:
        compteur = 0
        try :
            debutPartie.destroy()
        except NameError :
            pass
        if difficulty < 2 :
            Fposition()
        else :
            FaQuiLeTourJVO()
    else :
        menu.after(50, Fbatonnets)



def Fposition():
    global compteurBatonsPartie, LBatonnets, taille, compteurBatonsPartie2, difficulty, commence, tours, aQuiLeTour
    compteurBatonsPartie2 = compteurBatonsPartie +1
    LBatonnets[compteurBatonsPartie].bind("<1>", Fclic1)
    if taille-compteurBatonsPartie2 != 0 :
        LBatonnets[compteurBatonsPartie2].bind("<1>", Fclic2)
        compteurBatonsPartie2 = compteurBatonsPartie2 +1
        if taille-compteurBatonsPartie2 != 0 :
            LBatonnets[compteurBatonsPartie2].bind("<1>", Fclic3)
        else : pass
    else : pass
    if compteurBatonsPartie == 0 :
        if difficulty == 0 :
            commence = Label(menu, text=j1 + " commence !", font=("Helvetica", 10))
        elif difficulty == 1 :
            commence = Label(menu, text=j2 + " commence !", font=("Helvetica", 10))
        commence.place(relx=0.5, rely=0.2, anchor=CENTER)

    elif tours % 2 == 0 :
        if difficulty == 0 :
            aQuiLeTour = Label(menu, text= "C'est à " + j1 +  " de jouer !", font=("Helvetica", 10))
        elif difficulty == 1 :
            aQuiLeTour = Label(menu, text= "C'est à " + j2 +  " de jouer !", font=("Helvetica", 10))
        aQuiLeTour.place(relx=0.5, rely=0.2, anchor=CENTER)

    elif tours % 2 == 1 :
        if difficulty == 0 :
            aQuiLeTour = Label(menu, text= "C'est à " + j2 +  " de jouer !", font=("Helvetica", 10))
        elif difficulty == 1 :
            aQuiLeTour = Label(menu, text= "C'est à " + j1 +  " de jouer !", font=("Helvetica", 10))
        aQuiLeTour.place(relx=0.5, rely=0.2, anchor=CENTER)



def Fclic1(event):
    global compteurBatonsPartie, LBatonnets, taille, tours, commence, aQuiLeTour, difficulty, tourJOUEUR, winner
    if tours == 0 : commence.destroy()
    else : aQuiLeTour.destroy()
    tours = tours +1
    LBatonnets[compteurBatonsPartie].unbind("<1>")
    LBatonnets[compteurBatonsPartie].place_forget()
    compteurBatonsPartie = compteurBatonsPartie +1
    if taille-compteurBatonsPartie != 0 :
        LBatonnets[compteurBatonsPartie].unbind("<1>")
        stock = compteurBatonsPartie + 1
        if taille-stock != 0 :
            LBatonnets[stock].unbind("<1>")
        else : pass
        if difficulty < 2 :
            Fposition()
        else :
            tourJOUEUR = False
            FaQuiLeTourJVO()
    else :
        if difficulty > 1 :
            winner = 3
        else :
            pass
        menu.after(500, Fwinner)

def Fclic2(event):
    global compteurBatonsPartie, LBatonnets, taille, tours, commence, aQuiLeTour, difficulty, tourJOUEUR, winner
    if tours == 0 : commence.destroy()
    else : aQuiLeTour.destroy()
    tours = tours +1
    LBatonnets[compteurBatonsPartie].unbind("<1>")
    LBatonnets[compteurBatonsPartie].place_forget()
    compteurBatonsPartie = compteurBatonsPartie +1
    LBatonnets[compteurBatonsPartie].unbind("<1>")
    LBatonnets[compteurBatonsPartie].place_forget()
    compteurBatonsPartie = compteurBatonsPartie +1
    if taille-compteurBatonsPartie != 0 :
        LBatonnets[compteurBatonsPartie].unbind("<1>")
        if difficulty < 2 :
            Fposition()
        else :
            tourJOUEUR = False
            FaQuiLeTourJVO()
    else :
        if difficulty > 1 :
            winner = 3
        else :
            pass
        menu.after(500, Fwinner)

def Fclic3(event):
    global compteurBatonsPartie, LBatonnets, taille, tours, commence, aQuiLeTour, difficulty, tourJOUEUR, winner
    if tours == 0 :
        commence.destroy()
    else :
        aQuiLeTour.destroy()
    tours = tours +1
    LBatonnets[compteurBatonsPartie].unbind("<1>")
    LBatonnets[compteurBatonsPartie].place_forget()
    compteurBatonsPartie = compteurBatonsPartie +1
    LBatonnets[compteurBatonsPartie].unbind("<1>")
    LBatonnets[compteurBatonsPartie].place_forget()
    compteurBatonsPartie = compteurBatonsPartie +1
    LBatonnets[compteurBatonsPartie].unbind("<1>")
    LBatonnets[compteurBatonsPartie].place_forget()
    compteurBatonsPartie = compteurBatonsPartie +1
    if taille-compteurBatonsPartie == 0 :
        if difficulty > 1 :
            winner = 3
        else :
            pass
        menu.after(500, Fwinner)
    else :
        if difficulty < 2 :
            Fposition()
        else :
            tourJOUEUR = False
            FaQuiLeTourJVO()


def FpositionJVO():
    global compteurBatonsPartie, LBatonnets, taille, compteurBatonsPartie2, difficulty, commence, tours, aQuiLeTour, tourJOUEUR
    compteurBatonsPartie2 = compteurBatonsPartie +1
    LBatonnets[compteurBatonsPartie].bind("<1>", Fclic1)
    if taille-compteurBatonsPartie2 != 0 :
        LBatonnets[compteurBatonsPartie2].bind("<1>", Fclic2)
        compteurBatonsPartie2 = compteurBatonsPartie2 +1
        if taille-compteurBatonsPartie2 != 0 :
            LBatonnets[compteurBatonsPartie2].bind("<1>", Fclic3)
        else : pass
    else : pass


def FaQuiLeTourJVO():
    global compteurBatonsPartie, commence, aQuiLeTour, difficulty, taille, tourJOUEUR
    if compteurBatonsPartie == 0 :
        if difficulty == 2 :
            commence = Label(menu, text=j1 + " commence !", font=("Helvetica", 10))
        elif difficulty == 3 :
            commence = Label(menu, text=j1 + " commence !", font=("Helvetica", 10))
        elif difficulty == 4 :
            if taille == 25 : commence = Label(menu, text="L'ordinateur commence !", font=("Helvetica", 10))
            else : commence = Label(menu, text=j1 + " commence !", font=("Helvetica", 10))
        elif difficulty == 5 :
            if taille == 25 : commence = Label(menu, text=j1 + " commence !", font=("Helvetica", 10))
            else : commence = Label(menu, text="L'ordinateur commence !", font=("Helvetica", 10))
        commence.place(relx=0.5, rely=0.2, anchor=CENTER)

    elif tourJOUEUR == True :
        aQuiLeTour = Label(menu, text= "C'est à " + j1 +  " de jouer !", font=("Helvetica", 10))
        aQuiLeTour.place(relx=0.5, rely=0.2, anchor=CENTER)
    else :
        aQuiLeTour = Label(menu, text= "C'est à l'ordinateur de jouer !", font=("Helvetica", 10))
        aQuiLeTour.place(relx=0.5, rely=0.2, anchor=CENTER)
    if tourJOUEUR == True :
        FpositionJVO()
    else :
        menu.after(1250, FalgoBot)




def FalgoBot():
    global difficulty, taille, compteurBatonsPartie, LBatonnets, winner, L15, L20, L25, L30, L35, tourJOUEUR, commence, aQuiLeTour, batonsAEnlever
    if compteurBatonsPartie == 0 :
        commence.destroy()
    else :
        aQuiLeTour.destroy()
    if difficulty == 2 :

        if taille - compteurBatonsPartie > 2 :
            batonsAEnlever = random.randint(1,3)
        elif taille - compteurBatonsPartie == 2 :
            batonsAEnlever = random.randint(1,2)
        else :
            batonsAEnlever = 1

    elif difficulty == 3 :
        if taille - compteurBatonsPartie > 10 :
            batonsAEnlever = random.randint(1,3)
        elif taille - compteurBatonsPartie == 1 :
            batonsAEnlever = 1
        else :
            for i in range(1, 4):
                test = compteurBatonsPartie + i
                if taille == 15 :
                    if test in L15 :
                        batonsAEnlever = i
                        break
                    elif i == 3 :
                        batonsAEnlever = random.randint(1,3)
                elif taille == 20 :
                    if test in L20 :
                        batonsAEnlever = i
                        break
                    elif i == 3 :
                        batonsAEnlever = random.randint(1,3)
                elif taille == 25 :
                    if test in L25 :
                        batonsAEnlever = i
                        break
                    elif i == 3 :
                        batonsAEnlever = random.randint(1,3)
                elif taille == 30 :
                    if test in L30 :
                        batonsAEnlever = i
                        break
                    elif i == 3 :
                        batonsAEnlever = random.randint(1,3)
                else :
                    if test in L35 :
                        batonsAEnlever = i
                        break
                    elif i == 3 :
                        batonsAEnlever = random.randint(1,3)



    elif difficulty == 4 :
        if taille == 25 : commence = Label(menu, text="L'ordinateur commence !", font=("Helvetica", 10))
        else : commence = Label(menu, text=j1 + " commence !", font=("Helvetica", 10))

    else :
        if taille == 25 : commence = Label(menu, text=j1 + " commence !", font=("Helvetica", 10))
        else : commence = Label(menu, text="L'ordinateur commence !", font=("Helvetica", 10))



    for i in range (batonsAEnlever) :
        LBatonnets[compteurBatonsPartie].place_forget()
        compteurBatonsPartie = compteurBatonsPartie +1


    if taille - compteurBatonsPartie == 0 :
        winner = 1
        menu.after(500, Fwinner)
    else :
        tourJOUEUR = True
        FaQuiLeTourJVO()









def Fwinner():
    global difficulty, tours, j1, j2, finPartie, arretPartie, relancer, compteurBatonsPartie, winner, LDifficulty
    compteurBatonsPartie = 0
    try :
        labelPattern.destroy()
    except NameError:
        pass
    try :
        photoPattern.destroy()
    except NameError:
        pass
    for i in range(0, taille) :
        try :
            LBatonnets[i].destroy()
        except (NameError, IndexError) :
            pass
    if difficulty == 0 :
        if tours % 2 == 0 : winner = 1
        else : winner = 2
    elif difficulty == 1 :
        if tours % 2 == 0 : winner = 2
        else : winner = 1
    else :
        pass
    if winner == 1 :
        if difficulty < 2 :
            finPartie = Label(menu, text=j1 + " a gagné cette partie !", font=("Helvetica", 40))
        else :
            nomDifficulty = LDifficulty[difficulty]
            finPartie = Label(menu, text="Vous avez battu l'ordinateur en mode " + nomDifficulty + " !", font=("Helvetica", 40))
    elif winner == 2 :
        finPartie = Label(menu, text=j2 + " a gagné cette partie !", font=("Helvetica", 40))
    else :
        nomDifficulty = LDifficulty[difficulty]
        finPartie = Label(menu, text="L'ordinateur vous a battu en mode " + nomDifficulty + " !", font=("Helvetica", 40))
    finPartie.place(relx=0.5, rely=0.5, anchor=CENTER)


    relancer = Button(menu, text="Relancer avec les mêmes paramètres", command=Frelancer)
    relancer.place(relx=0.5, rely=0.8, anchor=CENTER)
    arretPartie = Button(menu, text="Retourner au menu principal", command=Fretour)
    arretPartie.place(relx=0.5, rely=0.9, anchor=CENTER)

def Frelancer():
    global arretPartie, relancer, finPartie, tours
    arretPartie.destroy()
    relancer.destroy()
    finPartie.destroy()
    LBatonnets[:] = []
    compteurBatonsPartie = 0
    tours = 0
    Fpattern()


def Faide():
    if askyesno('Aide : Comment gagner ?', "Vous n'arrivez pas à gagner au jeu des bâtonnets ? Voulez-vous connaître l'astuce ?"):
        if askyesno('Aide : Comment gagner ?', "Le principe est très simple, pour gagner vous devez vous assurer de prendre l'avant dernier bâtonnet. Mais pour cela vous devez contrôler la partie. Voulez-vous savoir comment faire ?"):
            if askyesno('Aide : Comment gagner ?', "Comme l'on peut tirer 1 à 3 bâtonnets, cela signifie que vous pouvez toujours compléter le tirage de l'adversaire pour arriver à  4. Ainsi le but est d'aller de 4 en 4 jusqu'à l'avant dernier bâtonnet. Avez-vous besoin d'un exemple ?"):
                 showwarning('Aide : Comment gagner ?', "Prenons l'exemple d'une partie courte à 15 bâtonnets. En suivant le raisonemment précédent, vous devez pour gagner, obtenir le 14ème bâtonnet. Or pour l'atteindre vous devez aller de 4 en 4 et donc tenter de vous emparer des bâtonnets 2, 6 ou 10. Une fois ceci fait, il suffit de compléter le tirage de l'adversaire comme vu précédemment. Vous êtes maintenant au point, bonne chance !")



menu = Tk()
menu.title('Le jeu des bâtonnets')
menu.geometry("500x500")
menu.resizable(0, 0)
menu['bg']='white'

menubar = Menu(menu)
menu1 = Menu(menubar, tearoff=100)
menu1.add_command(label="Retour menu", command=Fretour)
menu1.add_command(label="Aide", command=Faide)
menu1.add_separator()
menu1.add_command(label="Quitter", command=menu.destroy)
menubar.add_cascade(label="Fichier", menu=menu1)



go = Button(menu, text='Lancer la partie', command=Fjouer)
go.place(relx=0.5, rely=0.5, anchor=CENTER)

scaleVar = IntVar()
scaleBaton = Scale(menu, from_=15, to=35, resolution=5, variable=scaleVar, orient=HORIZONTAL, background='white')
scaleBaton.place(relx=0.5, rely=0.1, anchor=CENTER)
labelNbBaton = Label(menu, text="Nombre de bâtonnets :", background='white')
labelNbBaton.place(relx=0.5, rely=0.025, anchor=CENTER)

menu.config(menu=menubar)
menu.mainloop()
