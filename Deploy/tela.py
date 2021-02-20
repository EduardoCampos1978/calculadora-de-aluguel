import PySimpleGUI as sg

class TelaPython:

    def __init__(self):

        layout = [
            [sg.Text('Nome'), sg.Input()],
            [sg.Text('Idade'), sg.Input()],
            [sg.Button('Enviar Dados')] 
        ]

        janela = sg.Window('Dados do Usuário').layout(layout)
        self.button, self.values = janela.Read()

    def iniciar(self):
        print(self.values)

tela = TelaPython()
tela.iniciar()

