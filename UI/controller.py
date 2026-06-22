import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDs(self):
        anni=self._model.getAnni()
        for a in anni:
            self._view._ddAnno1.options.append(ft.dropdown.Option(key=a,text=a))
            self._view._ddAnno2.options.append(ft.dropdown.Option(key=a, text=a))
        self._view.update_page()



    def handleCreaGrafo(self,e):
        try:
            if not self._view._ddAnno1.value or not self._view._ddAnno2.value:
                self._view.txt_result.controls.clear()
                self._view.txt_result.controls.append(ft.Text("Errore: Selezionare entrambi i valori di rating."))
                self._view.update_page()
                return

            val1 = float(self._view._ddAnno1.value)
            val2 = float(self._view._ddAnno2.value)
            valore1 = min(val1, val2)
            valore2 = max(val1, val2)

            self._model.buildGrafo(valore1, valore2)
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text(
                    f"Grafo correttamente creato. Nodi: {self._model.getNumNodi()} nodi e {self._model.getNumArchi()} archi ")
            )
            self._view.update_page()
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Errore: Seleziona un range valido. "))
            self._view.update_page()


    def handleDettagli(self, e):
        self._view.txt_result.controls.clear()
        archi_top=self._model.ArchiPeso3Maggiore()
        for u,v,dati in archi_top:
            self._view.txt_result.controls.append(
                ft.Text(f"{u},{v} -- peso : {dati["weight"]}")
            )

        self._view.txt_result.controls.append(
            ft.Text(f"il numero di componenti connesse è : {self._model.getNumCompConnessa()}")
        )
        num_nodi,componente=self._model.getMaggioreConnessa()
        self._view.txt_result.controls.append(
            ft.Text(f"la componente connessa maggiore contiene {num_nodi} nodi")
        )
        for nodo in componente:
            self._view.txt_result.controls.append(
                ft.Text(f"{nodo}")
            )

        self._view.update_page()

    def handleCerca(self, e):
        pass

