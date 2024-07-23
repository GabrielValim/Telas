from Tela import Tela

class TelaInstrucoes(Tela):
    def __init__(self):
        super().__init__(
            titulo="Instruções Importantes",
            mensagem="Antes de iniciar o processo, por favor, certifiquese de:\n\n" \
                     " Ter a VPN conectada.\n" \
                     " Não interromper a conexão com a internet.\n" \
                     " Não utilizar o computador para outras tarefas.", 
            botao_texto="Continuar",
            cor_fundo="#304463",
            cor_titulo="yellow",
            cor_texto="yellow",
            hover_cor="#4CAF50"
        )

    def definir_acao_botao(self, acao):
        self.botao.clicked.connect(acao)
