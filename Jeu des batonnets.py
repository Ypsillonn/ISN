# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
import random

difficulty = 0
callbackVar = 0
Nom = 'Joueur 1'
Nom2 = 'Joueur 2'
j1 = 'Joueur 1'
j2 = 'Joueur 2'


def jouer():
    go.place_forget()
    jvj.place(relx=0.5, rely=0.45, anchor=CENTER)
    jvo.place(relx=0.5, rely=0.55, anchor=CENTER)

def jvj():
    global Nom, Nom2, j1, j2
    jvj.place_forget()
    jvo.place_forget()
    Nom.insert(END, 'Joueur 1')
    Nom2.insert(END, 'Joueur 2')
    Nom.place(relx=0.5, rely=0.3, anchor=CENTER)
    Nom2.place(relx=0.5, rely=0.4, anchor=CENTER)
    appliquer.place(relx=0.5, rely=0.6, anchor=CENTER)

def name():
    global j1, j2
    quiCommence.place(relx=0.5, rely=0.1, anchor=CENTER)
    bouton1.place(relx=0.5, rely=0.15, anchor=CENTER)
    bouton2.place(relx=0.5, rely=0.25, anchor=CENTER)
    bouton3.place(relx=0.5, rely=0.35, anchor=CENTER)
    j1 = Nom.get()
    j2 = Nom2.get()
    Nom.place_forget()
    Nom2.place_forget()
    appliquer.place_forget()

def ordre():
    global j1, j2, callbackVar
    callbackVar = 0
    menu['bg']='lightgray'
    ordre.place_forget()
    bouton1.place_forget()
    bouton2.place_forget()
    bouton3.place_forget()
    quiCommence.place_forget()
    if choix.get() == 1:
       menu.geometry("1000x500")
       print(j1)
       print(j2)
    elif choix.get() == 2:
        menu.geometry("1000x500")
    else :
        menu.geometry("1000x500")

def jvo():
    jvo.place_forget()
    jvj.place_forget()
    soft.place(relx=0.5, rely=0.35, anchor=CENTER)
    normal.place(relx=0.5, rely=0.45, anchor=CENTER)
    hard.place(relx=0.5, rely=0.55, anchor=CENTER)
    impossible.place(relx=0.5, rely=0.65, anchor=CENTER)

def soft():
    global difficulty
    soft.place_forget()
    normal.place_forget()
    hard.place_forget()
    impossible.place_forget()
    menu.geometry("1000x500")
    menu['bg']='lightgray'
    difficulty = 1

def normal():
    global difficulty
    soft.place_forget()
    normal.place_forget()
    hard.place_forget()
    impossible.place_forget()
    menu.geometry("1000x500")
    menu['bg']='lightgray'
    difficulty = 2

def hard():
    global difficulty
    soft.place_forget()
    normal.place_forget()
    hard.place_forget()
    impossible.place_forget()
    menu.geometry("1000x500")
    menu['bg']='lightgray'
    difficulty = 3

def impossible():
    global difficulty
    soft.place_forget()
    normal.place_forget()
    hard.place_forget()
    impossible.place_forget()
    menu.geometry("1000x500")
    menu['bg']='lightgray'
    difficulty = 4

def retour():
    global callbackVar, difficulty
    callbackVar = 0
    difficulty = 0
    soft.place_forget()
    normal.place_forget()
    hard.place_forget()
    impossible.place_forget()
    jvo.place_forget()
    jvj.place_forget()
    ordre.place_forget()
    bouton1.place_forget()
    bouton2.place_forget()
    bouton3.place_forget()
    Nom.place_forget()
    Nom2.place_forget()
    appliquer.place_forget()
    quiCommence.place_forget()
    go.place(relx=0.5, rely=0.5, anchor=CENTER)
    menu.geometry("500x500")
    menu['bg']='white'

def callback():
    global callbackVar
    if callbackVar == 0:
       ordre.place(relx=0.5, rely=0.6, anchor=CENTER)
       callbackVar = 1

def aide():
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
menu1.add_command(label="Retour menu", command=retour)
menu1.add_command(label="Aide", command=aide)
menu1.add_separator()
menu1.add_command(label="Quitter", command=menu.destroy)
menubar.add_cascade(label="Fichier", menu=menu1)


go = Button(menu, text='Lancer la partie', command=jouer)
go.place(relx=0.5, rely=0.5, anchor=CENTER)
jvj = Button(menu, text='Contre un autre joueur', command=jvj)
jvo = Button(menu, text="Contre l'ordinateur", command=jvo)
soft = Button(menu, text="Facile", command=soft)
normal = Button(menu, text="Normal", command=normal)
hard = Button(menu, text="Difficile", command=hard)
impossible = Button(menu, text="Impossible", command=impossible)
appliquer = Button(menu, text="Appliquer", command=name)
choix = IntVar()
bouton1 = Radiobutton(menu, text="Joueur 1", variable=choix, value=1, command=callback, bg="white")
bouton2 = Radiobutton(menu, text="Joueur 2", variable=choix, value=2, command=callback, bg="white")
bouton3 = Radiobutton(menu, text="Aléatoire", variable=choix, value=3, command=callback, bg="white")
Nom = Entry(menu, bg="dodger blue")
Nom2 = Entry(menu, bg="firebrick1")

ordre = Button(menu, text="Lancer", command=ordre)
quiCommence = Label(menu, text="Qui commence ?", bg="white")
menu.config(menu=menubar)
menu.mainloop()
