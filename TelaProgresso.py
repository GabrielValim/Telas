from PyQt5.QtWidgets import (QWidget, QLabel, QProgressBar, QVBoxLayout, QSpacerItem)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class TelaProgresso(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aguarde o processo...  ")
        self.setFixedSize(500, 400)  # Largura x Altura
        self.setWindowIcon(QIcon('imgs/domini-removebg-preview.png'))

        # Cria o rótulo para o título
        self.titulo = QLabel("Processos em andamento... ⏳", self)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet("font-size: 24px; color: white;")  # Define o tamanho e a cor do título

        # Cria a barra de progresso
        self.barra_progresso = QProgressBar(self)
        self.barra_progresso.setGeometry(50, 150, 400, 25)  # Ajusta a posição da barra
        self.barra_progresso.setValue(0)

        # Define o estilo da barra de progresso
        self.barra_progresso.setStyleSheet("""
            QProgressBar {
                border-radius: 10px;
                background-color: #e0e0e0;
                text-align: center;
                font-size: 16px
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
                border-radius: 10px;
            }
            QProgressBar::chunk:disabled {
                background-color: #ccc;
            }
        """)

        # Cria um layout vertical para a janela
        layout = QVBoxLayout()
        layout.addWidget(self.titulo)

        # Adiciona um espaçador para criar uma distância entre o título e a barra de progresso
        layout.addSpacerItem(QSpacerItem(0, 0))  # Define a altura do espaçador

        layout.addWidget(self.barra_progresso)
        self.setLayout(layout)

        # Define a cor de fundo da janela
        self.setStyleSheet("background-color: #304463;")  # Define a cor de fundo

        # Define as margens da janela para evitar que a barra de progresso fique encostada na parte inferior
        self.setContentsMargins(0, 10, 10, 100)  # Define as margens superior, esquerda, direita e inferior
