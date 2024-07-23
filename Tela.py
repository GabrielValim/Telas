from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QDesktopWidget

class Tela(QWidget):
    def __init__(self, titulo, mensagem, botao_texto, cor_fundo, cor_titulo, cor_texto, hover_cor):
        super().__init__()

        self.setWindowTitle(titulo)

        # Define o tamanho da tela
        self.setFixedSize(500, 400)  # Largura x Altura304463

        # Define a cor de fundo da janela
        self.setStyleSheet(f"background-color: {cor_fundo};")

        # Cria o label com o título
        self.titulo = QLabel(titulo)
        self.titulo.setStyleSheet(f"font-size: 20px; font-weight: bold; color: {cor_titulo};")
        self.titulo.setAlignment(Qt.AlignCenter)


        # Cria o label com a mensagem
        self.label = QLabel(mensagem)
        self.label.setStyleSheet(f"font-size: 16px; font-weight: semi-bold; color: {cor_texto}")
        self.label.setAlignment(Qt.AlignCenter)

        # Cria o botão
        self.botao = QPushButton(botao_texto)
        self.botao.clicked.connect(self.acao_botao)
        self.botao.setStyleSheet(f"""
            QPushButton {{
                background-color: white; 
                color: #1A2130; 
                padding: 10px 20px; 
                border: none; 
                border-radius: 15px; 
                font-size: 16px; 
            }}

            QPushButton:hover {{
                background-color: {hover_cor}; 
                color: white
            }}
        """)

        # Cria o layout vertical para organizar os widgets
        layout = QVBoxLayout()
        layout.addWidget(self.titulo)
        layout.addSpacing(50)
        layout.addWidget(self.label)
        layout.addSpacing(50)
        layout.addWidget(self.botao)
        layout.setAlignment(Qt.AlignCenter)

        # Define o layout da tela
        self.setLayout(layout)

        # Centraliza a tela na tela do usuário
        self.center_on_screen()

        # Define o ícone da janela
        self.setWindowIcon(QIcon('imgs/domini-removebg-preview.png')) 

    def acao_botao(self):
        # Método a ser implementado pelas classes filhas
        pass

    def center_on_screen(self):
        # Centraliza a tela na tela do usuário
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())