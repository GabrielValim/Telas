from PyQt5.QtWidgets import QFileDialog
from Tela import Tela

class TelaPasta(Tela):
    def __init__(self, controlador):
        super().__init__(
            titulo="Selecione uma pasta... ",
            mensagem="Selecione a pasta onde os arquivos serão guardados.",
            botao_texto="Selecionar Pasta",
            cor_fundo="#304463",
            cor_titulo="white",
            cor_texto="white",
            hover_cor="#4CAF50"
        )
        self.controlador = controlador

    def selecionar_pasta(self):
        pasta = QFileDialog.getExistingDirectory(self, "Selecione a Pasta")
        if pasta:
            self.controlador.set_caminho_pasta(pasta)
            

    def definir_acao_botao(self, acao):
        self.botao.clicked.connect(acao)


        

    # def obter_caminho_pasta():
    #     tela_pasta = TelaPasta(controlador)  # Crie uma nova instância da tela
    #     tela_pasta.show()  # Mostre a tela
    #     tela_pasta.definir_acao_botao(lambda: tela_pasta.close())  # Feche a tela após a seleção

    #     return controlador.get_caminho_pasta()
