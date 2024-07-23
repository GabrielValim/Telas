from Tela import Tela

class TelaSucesso(Tela):
    def __init__(self, mensagem):
        super().__init__(
            titulo="Sucesso!",
            mensagem=mensagem, 
            botao_texto="Fechar",
            cor_fundo="#4CAF50", 
            cor_titulo="white",
            cor_texto="white", 
            hover_cor="#1A2130"
        ) 
  

    def definir_acao_botao(self, acao):
        self.botao.clicked.connect(acao)
