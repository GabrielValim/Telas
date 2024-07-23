
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QVBoxLayout, QGridLayout, QPushButton, QMessageBox)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import re
from Tela import  Tela

from typing import Optional

class TelaLogin(QWidget):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador

        self.setWindowTitle("Login")

        self.setFixedSize(500, 400)

        self.setStyleSheet("background-color: #304463;")

        # Cria o label do título
        self.titulo_label = QLabel("Login")
        self.titulo_label.setAlignment(Qt.AlignCenter)
        self.titulo_label.setFont(QFont('Times', 18))  # Define a fonte e o tamanho do título
        self.titulo_label.setStyleSheet("color: white;")  # Define a cor do título

        self.email_label = QLabel("Email:")
        self.email_label.setAlignment(Qt.AlignCenter)
        self.email_label.setFont(QFont('Times', 12))
        self.email_label.setStyleSheet("color: white;")

        self.email_edit = QLineEdit(self)
        self.email_edit.setFixedSize(150, 30)
        self.email_edit.setStyleSheet("QLineEdit { border: 2px solid white; color: white; border-radius: 15px; padding: 0px 8px; }")  # Define o estilo do QLineEdit

        self.senha_label = QLabel("Senha:")
        self.senha_label.setAlignment(Qt.AlignCenter)
        self.senha_label.setFont(QFont('Times', 12))
        self.senha_label.setStyleSheet("color: white;")

        self.senha_edit = QLineEdit(self)
        self.senha_edit.setEchoMode(QLineEdit.Password)  # Define o modo de exibição da senha como asteriscos
        self.senha_edit.setFixedSize(150, 30)
        self.senha_edit.setStyleSheet("QLineEdit { border: 2px solid white; color: white; border-radius: 15px; padding: 0px 8px; }")

        # Cria o botão e define o estilo
        self.botao = QPushButton("Entrar")
        self.botao.setStyleSheet("QPushButton { background-color : white; color: #1A2130; padding: 10px 20px; border: none; border-radius: 15px; font-size: 16px;  } QPushButton:hover { background-color: #4CAF50; color: white}");

        self.layout = QVBoxLayout()

        #Define o ícone da janela
        self.setWindowIcon(QIcon('imgs/domini-removebg-preview.png')) 

        # Adiciona o label do título ao layout
        self.layout.addWidget(self.titulo_label)

        # Adiciona um espaçamento entre o título e as labels
        self.layout.addSpacing(30)  

        # Cria o layout de grade
        self.grid_layout = QGridLayout()

        # Adiciona os labels e QLineEdits ao layout de grade
        self.grid_layout.addWidget(self.email_label, 0, 0, Qt.AlignCenter)
        self.grid_layout.addWidget(self.email_edit, 0, 1, Qt.AlignCenter)
        self.grid_layout.addWidget(self.senha_label, 1, 0, Qt.AlignCenter)
        self.grid_layout.addWidget(self.senha_edit, 1, 1, Qt.AlignCenter)

        # Adiciona o layout de grade ao layout vertical
        self.layout.addLayout(self.grid_layout)

        # Define o espaçamento entre as linhas do layout de formulário
        self.grid_layout.setSpacing(30)  

        # Adiciona o layout de formulário ao layout vertical
        self.layout.addLayout(self.grid_layout)

        # Adiciona um espaçamento entre o layout de formulário e o botão
        self.layout.addSpacing(20)  # Define o espaçamento para 20 pixels

        # Adiciona o botão ao layout
        self.layout.addWidget(self.botao)

        # Centraliza o layout vertical
        self.layout.setAlignment(Qt.AlignCenter)

        self.setLayout(self.layout)

    def definir_acao_botao(self, acao):
        self.botao.clicked.connect(acao)

    def tela_login_acao_botao(self):
        from PyQt5.QtWidgets import QMessageBox
        from PyQt5 import QtGui

        if self.validar_campos() and self.validar_email():
            # Se os campos forem válidos, realiza o login
            email_input = self.email_edit.text()
            senha_input = self.senha_edit.text()

            # Se o login for válido, armazena os dados
            self.controlador.set_email(email_input)  # Use o método 'set_email'
            self.controlador.set_senha(senha_input)  # Use o método 'set_senha'

            msg = QMessageBox()
            msg.setText("Login realizado com sucesso!")
            msg.setWindowTitle("Aviso.")
            msg.setWindowIcon(QtGui.QIcon("imgs/dominiremovebgpreview.png"))
            msg.setIcon(QMessageBox.Information)
            msg.setStyleSheet(" background-color: #304463; color: white; ")
            msg.exec_()
        
        else:
            # Se o login for inválido, exibe uma mensagem de erro
            msg = QMessageBox()
            msg.setText("Email ou senha inválidos.")
            msg.setWindowTitle("Aviso.")
            msg.setWindowIcon(QtGui.QIcon("imgs/dominiremovebgpreview.png"))
            msg.setIcon(QMessageBox.Warning)
            msg.setStyleSheet("background-color: #304463; color: white;")
            msg.exec_()

    def validar_campos(self):
        email_input = self.email_edit.text()
        senha_input = self.senha_edit.text()

        if not email_input or not senha_input:
            # Exibe uma mensagem de erro se algum campo estiver vazio
            msg = QMessageBox()
            msg.setText("Por favor, preencha todos os campos.")
            msg.setWindowTitle("Aviso.")
            msg.setWindowIcon(QtGui.QIcon("imgs/dominiremovebgpreview.png"))
            msg.setIcon(QMessageBox.Warning)  
            msg.setStyleSheet(" background-color: #304463; color: white; ")
            msg.exec_()
            return False
        
        return True
        
    def validar_email(self):
        email_input = self.email_edit.text()

        # Validação do email usando expressão regular
        if "@" not in email_input:
            # Exibe uma mensagem de erro se o email estiver no formato inválido
            msg = QMessageBox()
            msg.setText("Por favor, digite um email válido.")
            msg.setWindowTitle("Aviso.")
            msg.setWindowIcon(QtGui.QIcon("imgs/dominiremovebgpreview.png"))
            msg.setIcon(QMessageBox.Warning)  
            msg.setStyleSheet(" background-color: #304463; color: white; ")
            msg.exec_()
            return False

        return True


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     tela_login = TelaLogin()
#     tela_login.show()
#     sys.exit(app.exec_())