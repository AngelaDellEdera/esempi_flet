import flet as ft
"""
fatta da :
-textfield e un tasto 
-più lista quadrati cliccabili
li prendo dalla libreria
nb:
label: messaggio che visulaizza utente
value: ciò che utente ha scritto
"""
def main(page: ft.Page):

    def addCheckbox(e):
        strToAdd = txtIn.value #per prendere la stringa da ciò che l'tente ha scritto
        txtIn.value = ""  #per inizializzare
        # controllare ciò che utente ha scritto con if
        if strToAdd == "":
            return
        page.add(ft.Checkbox(label=strToAdd))

    # Row 1
    txtIn = ft.TextField(label="Aggiungi un elemento.")
    btnAdd = ft.CupertinoButton(text="Add",on_click=addCheckbox) #onclick per aggiungerli uno dopo l'altro
    row1 = ft.Row([txtIn,btnAdd],alignment=ft.MainAxisAlignment.CENTER)
    page.add(row1)

ft.app(target=main)