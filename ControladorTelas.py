# Importando as Janelas
from TelaInstrucoes import TelaInstrucoes
from PyQt5.QtWidgets import QApplication
from TelaProgresso import TelaProgresso
from TelaSucesso import TelaSucesso
from TelaInicial import TelaInicial
from TelaLogin import TelaLogin
from TelaPasta import TelaPasta
from TelaData import TelaData
from TelaErro import TelaErro
from Tela import Tela

# Importacão da RPA
from rpa import executar_rpa

# Tipagem
from typing import Optional

# Variáveis globais para armazenar os dados
from variaveis_globais import data_inicial, data_final, email_login, senha_login, caminho_pasta

class ControladorTelas:
    def __init__(self, script: Optional[callable] = None):
        self.script = script
        self.telas: list[Tela] = []

        # Crie as instâncias das telas
        self.telaInicial = TelaInicial()
        self.telaInstrucoes = TelaInstrucoes()
        self.telaPasta = TelaPasta(self)
        self.TelaLogin = TelaLogin(self)
        self.telaData = TelaData(self)
        self.telaSucesso = TelaSucesso("A automação foi concluída com sucesso! 😁")
        self.telaErro = TelaErro("Ocorreu um erro durante o processo 😭")
        self.telaProgresso = TelaProgresso()

        # Adicione as telas à lista de telas
        self.telas.append(self.telaInicial)
        self.telas.append(self.telaInstrucoes)
        self.telas.append(self.telaPasta)
        self.telas.append(self.TelaLogin)
        self.telas.append(self.telaData)
        self.telas.append(self.telaSucesso)
        self.telas.append(self.telaErro)
        self.telas.append(self.telaProgresso)

        # Defina as ações dos botões
        self.telaInicial.definir_acao_botao(lambda: self.mostrar_tela(self.telaInstrucoes))
        self.telaInstrucoes.definir_acao_botao(lambda: self.mostrar_tela(self.telaPasta))
        self.telaPasta.definir_acao_botao(lambda: (self.telaPasta.selecionar_pasta(), self.mostrar_tela(self.TelaLogin)))
        self.TelaLogin.definir_acao_botao(lambda: (self.TelaLogin.tela_login_acao_botao(), self.mostrar_tela(self.telaData)))
        self.telaData.definir_acao_botao(lambda: (self.telaData.acao_botao(),  self.executar_automacao()))
        

    def run(self):
        if len(self.telas) > 1:
            self.mostrar_tela(self.telas[0])

    def esconder_todas_as_telas(self):
        for tela in self.telas:
            tela.hide()

    def mostrar_tela(self, tela: Tela):
        print(f"Mostrando a tela {tela}")
        self.esconder_todas_as_telas()
        tela.show()
  
    def mostrar_tela_pasta(self):
        tela_pasta = TelaPasta(self)
        self.mostrar_tela(tela_pasta)
        tela_pasta.definir_acao_botao(lambda: self.tela_pasta.selecionar_pasta())
        tela_pasta.selecionar_pasta()
        tela_pasta.hide()
        return 

    def mostrar_tela_data(self):
        tela_data = TelaData(self) 
        self.mostrar_tela(tela_data)

        tela_data.definir_acao_botao(lambda: tela_data.close())

        while tela_data.isVisible():
            QApplication.processEvents()

        tela_data.acao_botao()

        return

    def mostrar_tela_login(self):
        tela_login = TelaLogin(self)  # Crie uma instância da tela de login
        self.mostrar_tela(tela_login) 

        tela_login.definir_acao_botao(lambda: tela_login.close())

        while tela_login.isVisible():
            QApplication.processEvents()

        tela_login.tela_login_acao_botao()

        return

    def mostrar_tela_sucesso(self):
        self.mostrar_tela(self.telaSucesso)
        QApplication.processEvents()
        self.telaSucesso.definir_acao_botao(lambda: exit())

    def mostrar_tela_erro(self):
        self.mostrar_tela(self.telaErro)
        self.telaErro.definir_acao_botao(lambda: exit())

    def mostrar_tela_progresso(self):
        self.mostrar_tela(self.telaProgresso)
    
    # Métodos para definir os dados
    def set_data_inicial(self, data):
        global data_inicial
        data_inicial = data

    def set_data_final(self, data):
        global data_final
        data_final = data

    def set_email(self, email):
        global email_login
        email_login = email

    def set_senha(self, senha):
        global senha_login
        senha_login = senha

    def set_caminho_pasta(self, caminho):
        global caminho_pasta
        caminho_pasta = caminho

    # Métodos para obter os dados
    def get_data_inicial(self):
        return data_inicial

    def get_data_final(self):
        return data_final

    def get_email(self):
        return email_login

    def get_senha(self):
        return senha_login

    def get_caminho_pasta(self):
        return caminho_pasta
    
    def executar_automacao(self):
        print(f"Executando automação com data inicial: {self.get_data_inicial()} e data final: {self.get_data_final()}  caminho da pasta {self.get_caminho_pasta()}  email {self.get_email()}  senha {self.get_senha()}")
        executar_rpa(self)
    

