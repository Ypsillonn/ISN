# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
import random

stock2 = 55
taille = 30
difficulty = 0
callbackVar = 0
Nom = 'Joueur 1'
Nom2 = 'Joueur 2'
j1 = 'Joueur 1'
j2 = 'Joueur 2'


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
    quiCommence.place(relx=0.5, rely=0.1, anchor=CENTER)
    j1 = Nom.get()
    j2 = Nom2.get()
    Nom.destroy()
    Nom2.destroy()
    appliquer.destroy()
    choix = IntVar()
    bouton1 = Radiobutton(menu, text=j1, variable=choix, value=1, command=Fcallback, bg="white")
    bouton2 = Radiobutton(menu, text=j2, variable=choix, value=2, command=Fcallback, bg="white")
    bouton3 = Radiobutton(menu, text="Aléatoire", variable=choix, value=3, command=Fcallback, bg="white")
    bouton1.place(relx=0.5, rely=0.15, anchor=CENTER)
    bouton2.place(relx=0.5, rely=0.25, anchor=CENTER)
    bouton3.place(relx=0.5, rely=0.35, anchor=CENTER)

def Fordre():
    global j1, j2, callbackVar, bouton1, bouton2, bouton3, quiCommence
    callbackVar = 0
    menu['bg']='lightgray'
    ordre.place_forget()
    bouton1.destroy()
    bouton2.destroy()
    bouton3.destroy()
    quiCommence.destroy()
    if choix.get() == 1:
       menu.geometry("1100x500")
       print(j1)
       print(j2)
    elif choix.get() == 2:
        menu.geometry("1100x500")
    else :
        menu.geometry("1100x500")

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
    difficulty = 1
    Fpattern()

def Fnormal():
    global difficulty
    difficulty = 2
    Fpattern()

def Fhard():
    global difficulty
    difficulty = 3
    Fpattern()

def Fimpossible():
    global difficulty
    difficulty = 4
    Fpattern()

def Fretour():
    global callbackVar, jvo, jvj, soft, normal, hard, impossible, difficulty, bouton1, bouton2, bouton3, quiCommence, appliquer, Nom, Nom2, ordre, scaleBaton, labelBaton, labelPattern, taille
    callbackVar = 0
    difficulty = 0
    scaleBaton.place_forget()
    scaleBaton.place(relx=0.5, rely=0.1, anchor=CENTER)
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

    go.place(relx=0.5, rely=0.5, anchor=CENTER)
    menu.geometry("500x500")
    menu['bg']='white'


def Fcallback():
    global callbackVar, ordre
    if callbackVar == 0:
        ordre = Button(menu, text="Lancer", command=Fordre)
        ordre.place(relx=0.5, rely=0.6, anchor=CENTER)
        callbackVar = 1





def Fpattern():
    global soft, normal, hard, impossible, difficulty, taille, stock1, scaleVar, scaleBaton, labelBaton, labelPattern
    scaleBaton.place_forget()
    soft.destroy()
    normal.destroy()
    hard.destroy()
    impossible.destroy()
    menu.geometry("1100x500")
    menu['bg']='lightgray'
    taille = scaleVar.get()
    if taille == 35 :
        photoPattern = PhotoImage(file='Pattern35.pgm')
    elif taille == 30 :
        photoPattern = PhotoImage(file='Pattern30.pgm')
    elif taille == 25 :
        photoPattern = PhotoImage(file='Pattern25.pgm')
    elif taille == 20 :
        photoPattern = PhotoImage(file='Pattern20.pgm')
    else :
        photoPattern = PhotoImage(file='Pattern15.pgm')

    labelPattern = Label(image=photoPattern)
    labelPattern.image = photoPattern
    labelPattern.place(relx=0.5, rely=0.5, anchor=CENTER)



def Fposition():
    posX = menu.winfo_pointerx()
    posY = menu.winfo_pointery()
    if 340 < posX < 369 and 250 < posY < 350 :
        print("c'est bon")
    else :
        Fposition()



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


menu.config(menu=menubar)
menu.mainloop()
