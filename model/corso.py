from dataclasses import dataclass

#Creo il DTO della tabella corsi del database
@dataclass

class Corso:
    #attributi della tabella
    codins: str
    crediti: int
    nome: str
    pd: int

    #Metodo confronto sulle chiavi primarie
    def __eq__(self, other):
        return self.codins == other.codins

    #Rende immutabile la classe
    def __hash__(self):
        return hash(self.codins)

    #Stampa l'istanza
    def __str__(self):
        return f"{self.nome} ({self.codins}) - {self.crediti} CFU"

