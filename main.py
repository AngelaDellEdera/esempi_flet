from time import sleep
import flet as ft


def main(page: ft.Page):
    """per scrivere riga di testo
    dare nome a oggetto che sarà uno dei controlli
    aggiungere oggetto
    text ha tantissimi parametri
    """
    txtIn = ft.Text(value="Buongiorno TdP 2024!", color="red")
    page.controls.append(txtIn)  #aggiungo l'oggetto nella pagina
    page.update()  #aggiorno pagina
    """
    oggetto parametrico
    """
    # txtOut = ft.Text(value="Counter:", color="red",size=24)
    # page.add(txtOut)

    # for i in range(1,100):
    #     txtOut.value = "Counter: " + str(i)
    #     txtOut.update()
    #     sleep(1) pausa di un secondo per visualizzare

   #tutti i metodi delle interfacce grafiche devono catturare un ingresso che è un evento "e"
    def handleBottone(e):
        #aggiungere nuova riga a listview aggiungere testo con controllo Text
        lv.controls.append(ft.Text("Tasto Cliccato!"))
        lv.update()
    #righe prima scrivo elementi poi funzione Row
    txt1 = ft.Text(value="Colonna 1", color="red")
    txt2 = ft.Text(value="Colonna 2", color="blue")
    #bottone permette di cliccare con metodi chiamati quando interagisco con il bottone
    btn = ft.ElevatedButton(text="Premi qui!", on_click=handleBottone)
    row1 = ft.Row([txt1, txt2, btn])
    txtOut = ft.Text(value="", color="red", size=24)
    page.add(row1, txtOut) #aggiunto alla pagina 2 cose
    # lista che scorre
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    page.add(lv)


ft.app(target=main, view=ft.AppView.FLET_APP)
"""
VIEW= quaderno dove aggiungo oggetti
PAGE= pagina dove aggiungo elementi grafici/controlli
"""
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)