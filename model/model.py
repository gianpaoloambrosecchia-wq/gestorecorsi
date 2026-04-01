from database.DAO import DAO


class Model:
    def __init__(self):
        pass



    #Il modello chiede al DAO tutti i corsi e il DAO li ritorna
    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getCorsiPD(self, pd):
        return DAO.getCorsiPD(pd)

    def getCorsiPDIscritti(self, pd):
        result = DAO.getCorsiPDIscritti(pd)
        #Ordino la lista in ordine decrescente di numero di iscritti
        #cioè il secondo valore della tupla s[1]
        result.sort(key = lambda s:s[1], reverse=True)
        return result

    def getStudentiCorso(self, codins):
        studenti = DAO.getStudentiCorso(codins)
        #Ordine alfabetico in base al cognome
        studenti.sort(key = lambda s:s.cognome)
        return studenti

    def getCDSofCorso(self,codins):
        cds = DAO.getCDSofCorso(codins)
        #Ordiniamo per nuemro di iscritti decrescente
        cds.sort(key = lambda c:c[1], reverse=True)
        return cds
