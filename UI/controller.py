import flet as ft

from model.model import Model


class Controller:
    def __init__(self, view):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()
        self._ddCodinsValue = None

    def handlePrintCorsiPD(self, e):
        self._view.txt_result.controls.clear()
        pd = self._view.ddPD.value

        #Verifichiamo che l'utente abbia selezionato il periodo didattico
        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico")
            self._view.update_page()
            return

        if pd=="I":
            pdInt = 1
        else:
            pdInt = 2

        #corsiPD è una lista
        corsiPD = self._model.getCorsiPD(pdInt)

        #Se la lista è lunga 0
        if not len(corsiPD):
            self._view.txt_result.controls.append(ft.Text(f"Nessun corso trovato per il {pd} periodo didattico"))
            self._view.update_page()
            return
        else:
            self._view.txt_result.controls.append(
                ft.Text(f"Di seguito i corsi del {pd} periodo didattico"))
            for c in corsiPD:
                self._view.txt_result.controls.append(
                    ft.Text(c))
            self._view.update_page()
            return

    def handlePrintIscrittiCorsiPD(self, e):
        self._view.txt_result.controls.clear()
        pd = self._view.ddPD.value

        #Verifichiamo che l'utente abbia selezionato il periodo didattico
        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico")
            self._view.update_page()
            return

        if pd=="I":
            pdInt = 1
        else:
            pdInt = 2

        #corsiPD è una lista
        corsiPD = self._model.getCorsiPDIscritti(pdInt)

        #Se la lista è lunga 0
        if not len(corsiPD):
            self._view.txt_result.controls.append(ft.Text(f"Nessun corso trovato per il {pd} periodo didattico"))
            self._view.update_page()
            return
        else:
            self._view.txt_result.controls.append(
                ft.Text(f"Di seguito i corsi del {pd} periodo didattico con dettaglio iscritti"))
            for c in corsiPD:
                self._view.txt_result.controls.append(
                    #c è una tupla e il primo elemento è il Corso mentre il secondo il nuemro di iscritti
                    ft.Text(f"{c[0]} -- N Iscritti: {c[1]}"))
            self._view.update_page()
            return

    def handlePrintIscrittiCodins(self, e):
        self._view.txt_result.controls.clear()
        if self._ddCodinsValue is None:
            self._view.create_alert("Attenzione, selezionare un insegnamento")
            self._view.update_page()
            return

        #Se arriviamo qui, posso chiedere gli studenti al modello
        studenti = self._model.getStudentiCorso(codins=self._ddCodinsValue.codins)
        if not len(studenti):
            self._view.txt_result.controls.append(
                ft.Text(f"Non ci sono studenti iscritti al corso {self._ddCodinsValue}")
            )
            self._view.update_page()
            return
        else:
            self._view.txt_result.controls.append(
                ft.Text(f"Di seguito gli studenti iscritti al corso {self._ddCodinsValue}")
            )
            for s in studenti:
                self._view.txt_result.controls.append(
                    ft.Text(s)
                )
            self._view.update_page()
            return




    def handlePrintCDSCodins(self, e):
        self._view.txt_result.controls.clear()
        if self._ddCodinsValue is None:
            self._view.create_alert("Attenzione, selezionare un insegnamento")
            self._view.update_page()
            return

        cds = self._model.getCDSofCorso(self._ddCodinsValue.codins)

        if not len(cds):
            self._view.txt_result.controls.append(
                ft.Text(f"Non ci sono corsi di studi afferenti al corso {self._ddCodinsValue}")
            )
            self._view.update_page()
            return

        else:
            self._view.txt_result.controls.append(
                ft.Text(f"Di seguito i corsi di studi afferenti al corso {self._ddCodinsValue}")
            )
            for c in cds:
                self._view.txt_result.controls.append(
                    ft.Text(f"CDS: {c[0]} -- N cds: {c[1]}")
                )
            self._view.update_page()
            return

    #Metodo che passa alla view i codice del menu a tendina di ddCodins
    def fillddCodins(self):
        #Si fa passare da un metodo del modello i codici di insegnamento (letti dal db)

        #for cod in self._model.getCodins():
            #self._view.ddCodins.options.append(ft.dropdown.Option(cod))

        #Itero sui corsi che vengono letti dal DAO e ritornati dal modello
        for c in self._model.getAllCorsi():
            #uso dei campi di option, con key che è l'attributo, data l'oggetto e on_click
            #è il metodo associato a quando clicchiamo su un dato corso nella tendina
            self._view.ddCodins.options.append(ft.dropdown.Option(
                key = c.codins,
                data = c,
                on_click = self._choiceDDCodins
            ))

    def _choiceDDCodins(self, e):
        #Salvo nella variabile l'oggetto dell'evento e, cioè l'evento che scaturisce la chiamata alla funzione
        #cioè il click sul menu a tendina
        self._ddCodinsValue = e.control.data
        #Stampo l'oggetto considerato (chiama il metodo __str__ della classe Corso)
        print(self._ddCodinsValue)

