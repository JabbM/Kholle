#!/usr/bin/python3.6

#####################
#      Khôlle       #
#   Jullian Bacle   #
#     25/11/2018    #
#####################

import csv
import argparse

parser = argparse.ArgumentParser(description='Ce programme est une sorte d’utilitaire permettant de faire des opérations simple surune liste d’entiers, qui sera stockée dans un fichier au format csv.')
parser.add_argument('-l', action='store_true', help='Affiche le contenu de la liste.')
parser.add_argument('-a', nargs='+', help='Ajoute des éléments à la liste (... -a [val1] [val2] ...')
parser.add_argument('-c', action='store_true', help='Supprime tous les éléments de la liste.')
parser.add_argument('-t', action='store_true', help='Trie la liste dans l’ordre croissant.')
parser.add_argument('--desc', action='store_true', help='Trie la liste dans l’ordre décroissant.')
subparsers = parser.add_argument_group(title='subcommands', description='Commande qui ont besoin de l\'argument -s')
subparsers.add_argument('-s', action='store_true', help='')
subparsers.add_argument('--max', action='store_true', help='Affiche la valeur maximum contenu dans la liste.')
subparsers.add_argument('--min', action='store_true', help='Affiche la valeur minimum contenu dans la liste.')
subparsers.add_argument('--moy', action='store_true', help='Affiche la moyenne de tous les éléments dans la liste.')
subparsers.add_argument('--sum', action='store_true', help='Affiche la somme de tous les éléments dans la liste.')
args = parser.parse_args()

tab = []


def reader():
  with open('./test.csv', 'r', newline='') as fich:
    csv_r = csv.reader(fich)
    for row in csv_r:
        for i in range(len(row)):
            tab.append(row[i])

def writer(value):
  with open('./test.csv', 'w', newline='') as fich:
    csv_w = csv.writer(fich)
    csv_w.writerow(value)

def add(arg):
    tab.append(arg)

def delete():
  with open('./test.csv', 'w', newline='') as fich:
    csv_d = csv.writer(fich)
    csv_d.writerow('')


if args.l:
    reader()
    if len(tab) == 0:
        print("Le fichier est vide")
    else:
        print(tab)
elif args.a:
    reader()
    for n in args.a:
        add(n)
    writer(tab)
    print("les données ont bien été ajouté")
elif args.c:
    delete()
    print("Les données ont bien été supprimé")
elif args.s and args.max:
    reader()
    maxi = 0
    if len(tab) == 0:
        print("Le fichier est vide")
    else:
        for i in range(len(tab)):
            if int(tab[i]) > maxi:
                maxi = int(tab[i])
        print("La valeur maximal est : ",maxi)
elif args.s and args.min:
    reader()
    min = 999999
    if len(tab) == 0:
        print("Le fichier est vide")
    else:
        for i in range(len(tab)):
            if int(tab[i]) < min:
                min = int(tab[i])
        print("La valeur minimum est : ", min)
elif args.s and args.moy:
    reader()
    moy = 0
    nbr = 0
    if len(tab) == 0:
        print("Le fichier est vide")
    else:
        for i in range(len(tab)):
            moy = moy + int(tab[i])
        result = moy/len(tab)
        print(result)
elif args.s and args.sum:
    reader()
    somme = 0
    if len(tab) == 0:
        print("Le fichier est vide")
    else:
        for i in range(len(tab)):
            somme = somme + int(tab[i])
        print("La somme de tous les éléments de la liste : ",somme)
elif args.t and args.desc:
    reader()
    if len(tab) == 0:
        print("Le fichier est vide")
    else:
        trieDesc = sorted(tab, reverse=True)
        print(trieDesc)
elif args.t:
    reader()
    if len(tab) == 0:
        print("Le fichier est vide")
    else:
        trieAsc = sorted(tab)
        print(trieAsc)
