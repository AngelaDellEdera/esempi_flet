import flet as ft
"""
tasti con simboli
aggiungere riga perchè sono 3 controlli
e centrare il counter posso allineare tutta la pagina
"""
def main(page: ft.Page):
    #allineo tutta la pagina al centro
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
#2 metodi chiamati quando premo i tasti
    def handleAdd(e): #prende valore ci aggiunge 1 e lo ripubblica sul textfield
        currentVal = txtOut.value
        txtOut.value = currentVal + 1
        txtOut.update()

    def handleRemove(e): #prende valore ci sottrae 1 e lo ripubblica sul textfield
        currentVal = txtOut.value
        txtOut.value = currentVal - 1
        txtOut.update()

    #definisco i controlli e li aggiungo alla riga
    btnMinus = ft.IconButton(icon = ft.icons.REMOVE,
                             icon_color="green",
                             icon_size= 24, on_click= handleRemove)
    btnAdd = ft.IconButton(icon = ft.icons.ADD,
                             icon_color="green",
                             icon_size= 24, on_click= handleAdd)

    txtOut = ft.TextField(width=100,disabled=True, #per disabilitare la possibilità di modificarlo
                          value=0, border_color="green",
                          text_align=ft.TextAlign.CENTER)

    row1 = ft.Row([btnMinus, txtOut, btnAdd],
                  alignment=ft.MainAxisAlignment.CENTER)
    page.add(row1)

ft.app(target=main)