#!/usr/bin/python3
# -*- coding: utf-8 -*-


class User:
    def __init__(self):
        self.carte = []
        self.init_deck()

    def init_deck(self):
        print("tapez les deux carte que vous avez reçu (exemple pour 4 de pique et 3 de coeur tapez: 4P 3C):")
        message = input("user: ").split(" ")
        self.carte.append(message[0])
        self.carte.append(message[1])

user = User()