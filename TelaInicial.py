from Tela import Tela

class TelaInicial(Tela):
    def __init__(self):
        super().__init__(
            titulo="Início do Processo",
            mensagem="Bemvindo a automação TAX!",
            botao_texto="Iniciar Processo",
            cor_fundo="#304463",
            cor_titulo="white",
            cor_texto="white",
            hover_cor="#4CAF50"
        )
      
    def definir_acao_botao(self, acao):
        self.botao.clicked.connect(acao)

