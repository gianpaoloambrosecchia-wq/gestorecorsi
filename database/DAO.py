from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


class DAO():

    #Il DAO non ha costruttore, ma metodi statici


    @staticmethod
    def getAllCorsi():
        #Apriamo la connessione
        cnx = DBConnect.get_connection()
        #Creiamo l'oggetto di tipo cursoe
        cursor = cnx.cursor(dictionary=True)
        #Scriviamo e poi eseguiamo la query
        query = """select *
                   from corso"""
        cursor.execute(query)

        #Leggiamo ed elaboriamo i dati del cursore, che salviamo nella lista res
        res=[]
        for row in cursor:
             #In questo caso creo un oggetto di tipo corso, con i dati pari alle colonne del cursore
            res.append(Corso(
                codins = row["codins"],
                crediti = row["crediti"],
                nome = row ["nome"],
                pd = row["pd"],
            ))

        cursor.close()
        cnx.close()
        return res

    #Metodo che considera tutti i corsi di un dato periodo didattico
    @staticmethod
    def getCorsiPD(pd):
        #Apriamo la connessione
        cnx = DBConnect.get_connection()
        #Creiamo l'oggetto di tipo cursoe
        cursor = cnx.cursor(dictionary=True)
        #Scriviamo e poi eseguiamo la query
        query = """select *
                from corso c
                where c.pd = %s"""
        cursor.execute(query, (pd,))

        #Leggiamo ed elaboriamo i dati del cursore, che salviamo nella lista res
        res=[]
        for row in cursor:
             #In questo caso creo un oggetto di tipo corso, con i dati pari alle colonne del cursore
             #si può usare **row solo se la selet considera tutti e soli gli attributi di un oggetto
            res.append(Corso(**row))

        cursor.close()
        cnx.close()
        return res


    #Metodo che considera tutti i corsi di un dato periodo didattico e il numero di iscritti per ogni corso
    @staticmethod
    def getCorsiPDIscritti(pd):
        #Apriamo la connessione
        cnx = DBConnect.get_connection()
        #Creiamo l'oggetto di tipo cursoe
        cursor = cnx.cursor(dictionary=True)
        #Scriviamo e poi eseguiamo la query
        query = """select c.codins, c.crediti, c.nome, c.pd, count(*) as n
                   from corso c, iscrizione i
                   where c.codins = i.codins
                   and c.pd = %s
                   group by c.codins, c.crediti, c.nome, c.pd"""
        cursor.execute(query, (pd,))

        #Leggiamo ed elaboriamo i dati del cursore, che salviamo nella lista res
        res=[]
        for row in cursor:
             #In questo caso creo una tupla con un oggetto di tipo corso e il numero di iscritti per quel corso
            res.append((Corso(
                codins = row["codins"],
                crediti = row["crediti"],
                nome = row ["nome"],
                pd = row["pd"],
            ) ,row["n"]))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStudentiCorso(codins):
        #Apriamo la connessione
        cnx = DBConnect.get_connection()
        #Creiamo l'oggetto di tipo cursoe
        cursor = cnx.cursor(dictionary=True)
        #Scriviamo e poi eseguiamo la query
        query = """select s.*
                   from studente s, iscrizione i 
                   where s.matricola = i.matricola 
                   and i.codins = %s"""
        cursor.execute(query, (codins,))

        #Leggiamo ed elaboriamo i dati del cursore, che salviamo nella lista res
        res=[]
        for row in cursor:
             #In questo caso creo una tupla con un oggetto di tipo corso e il numero di iscritti per quel corso
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res


    @staticmethod
    def getCDSofCorso(codins):
        #Apriamo la connessione
        cnx = DBConnect.get_connection()
        #Creiamo l'oggetto di tipo cursoe
        cursor = cnx.cursor(dictionary=True)
        #Scriviamo e poi eseguiamo la query
        #DObbiamo considerare il numero di studenti in un dato corso con lo stesso corso di studi
        #con il secondo and ignoriamo gli studenti che non hanno un CDS assegnato
        query = """select s.CDS, count(*) as n
                   from studente s, iscrizione i
                   where s.matricola = i.matricola
                   and i.codins = %s
                   and s.CDS != ""     
                   group by s.CDS"""
        cursor.execute(query, (codins,))

        #Leggiamo ed elaboriamo i dati del cursore, che salviamo nella lista res
        res=[]
        for row in cursor:
             #In questo caso creo una tupla con corso di studi e numero di persone iscritte al quel corso di studi
            res.append((row["CDS"], row["n"]))

        cursor.close()
        cnx.close()
        return res


