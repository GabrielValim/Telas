from Tela import Tela

class TelaErro(Tela):
    def __init__(self, mensagem_erro):
        super().__init__(
            titulo="Erro!",
            mensagem=mensagem_erro,
            botao_texto="Fechar",
            cor_fundo="#f44336",  
            cor_titulo="white",
            cor_texto="white",
            hover_cor="#1A2130"
        )

    def definir_acao_botao(self, acao):
        self.botao.clicked.connect(acao)

 