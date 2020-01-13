#!/usr/bin/python
# -*- coding: utf-8 -*-

class Carte:
    def __int__(self):
        self.all_cartes = 52


class PIQUE(Carte):
    def __init__(self):
        self.all_carte = 13

class CARREAUX(Carte):
    def __init__(self):
        self.all_carte = 13

class TREFLE(Carte):
    def __init__(self):
        self.all_carte = 13

class COEUR(Carte):
    def __init__(self):
        self.all_carte = 0


