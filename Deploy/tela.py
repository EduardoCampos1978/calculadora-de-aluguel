import PySimpleGUI as sg

class TelaPython:

    def __init__(self):

        layout = [
            #[sg.Text('Zona', size=(10, 0)), sg.Input(size=(10, 0), key='zona')],
            [sg.Text('Zona', size=(10, 0)), 
             sg.Combo(values=('Norte', 'Sul', 'Leste', 'Oeste'), 
                      default_value=None, 
                      size=(8, 0), 
                      key='zona')],

            [sg.Text('Nº Quartos', size=(10, 0)), sg.Input(size=(10, 0), key='quartos')], 

            [sg.Text('Área', size=(10, 0)), sg.Input(size=(10, 0), key='area')],

            [sg.Button('Calcular')] 
        ]

        janela = sg.Window('Calculadora de Imóveis - SP').layout(layout)
        self.button, self.values = janela.Read()

    def iniciar(self):
        print(self.values)

if __name__ == '__main__':
    tela = TelaPython()
    tela.iniciar()

