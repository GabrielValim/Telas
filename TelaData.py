from PyQt5.QtWidgets import QLabel, QMessageBox, QDateEdit, QVBoxLayout, QWidget, QFormLayout, QPushButton
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QIcon
from PyQt5 import QtGui
from datetime import datetime

class TelaData(QWidget):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador

        self.setWindowTitle("Coleta de Datas")

        self.setFixedSize(500, 400)

        self.setStyleSheet("background-color: #304463;")

        # Cria o label do título
        self.titulo_label = QLabel("Prencha as datas 📅")
        self.titulo_label.setAlignment(Qt.AlignCenter)
        self.titulo_label.setFont(QFont('Times', 18))  # Define a fonte e o tamanho do título
        self.titulo_label.setStyleSheet("color: white;")  # Define a cor do título

        #label data inicial
        self.data_inicial_label = QLabel("Data Inicial:")
        self.data_inicial_label.setAlignment(Qt.AlignCenter)
        self.data_inicial_label.setFont(QFont('Times',10))
        self.data_inicial_label.setStyleSheet("color: white;")

        self.data_inicial_edit = QDateEdit(self)
        self.data_inicial_edit.setDisplayFormat("dd/MM/yyyy")
        self.data_inicial_edit.setDate(QDate.currentDate())
        self.data_inicial_edit.setFixedSize(150, 30)
        self.data_inicial_edit.setAlignment(Qt.AlignCenter)
        self.data_inicial_edit.setStyleSheet("QDateEdit { border: 2px solid white; color: white; }")  # Define o estilo do QDateEdit

        # label data final
        self.data_final_label = QLabel("Data Final:")
        self.data_final_label.setAlignment(Qt.AlignCenter)
        self.data_final_label.setFont(QFont('Times',10))
        self.data_final_label.setStyleSheet("color: white;")

        self.data_final_edit = QDateEdit(self)
        self.data_final_edit.setDisplayFormat("dd/MM/yyyy")
        self.data_final_edit.setDate(QDate.currentDate())
        self.data_final_edit.setFixedSize(150, 30)
        self.data_final_edit.setAlignment(Qt.AlignCenter)
        self.data_final_edit.setStyleSheet("QDateEdit { border: 2px solid white; color: white; }")  # Define o estilo do QDateEdit


         # Cria o botão e define o estilo
        self.botao = QPushButton("Confirmar")
        self.botao.setStyleSheet("QPushButton { background-color : white; color: #1A2130; padding: 10px 20px; border: none; border-radius: 15px; font-size: 16px;  } QPushButton:hover { background-color: #4CAF50; color: white}");

        # Conecta o evento de clique do botão ao método `acao_botao`
        self.botao.clicked.connect(self.acao_botao)

        self.layout = QVBoxLayout()

        # Define o ícone da janela
        self.setWindowIcon(QIcon('imgs/domini-removebg-preview.png')) 

        # Adiciona o label do título ao layout
        self.layout.addWidget(self.titulo_label)
        self.layout.addSpacing(30)

        # Cria um layout de formulário para organizar os labels e QDateEdit
        form_layout = QFormLayout()
        form_layout.addRow(self.data_inicial_label, self.data_inicial_edit)
        form_layout.addRow(self.data_final_label, self.data_final_edit)

        # Define o espaçamento entre as linhas do layout de formulário
        form_layout.setSpacing(40)

        # Adiciona o layout de formulário ao layout vertical
        self.layout.addLayout(form_layout)

        # Adiciona um espaçamento entre o layout de formulário e o botão
        self.layout.addSpacing(40)  # Define o espaçamento para 20 pixels

        # Adiciona o botão ao layout
        self.layout.addWidget(self.botao)

        # Centraliza o layout vertical
        self.layout.setAlignment(Qt.AlignCenter)

        self.setLayout(self.layout)

    def definir_acao_botao(self, acao):
        self.botao.clicked.connect(acao)

    def acao_botao(self):
        # Captura as datas selecionadas
        global data_inicial, data_final
        data_inicial = self.data_inicial_edit.date().toString("dd/MM/yyyy")
        data_final = self.data_final_edit.date().toString("dd/MM/yyyy")

        # Chama a função validar_datas
        if self.validar_datas(data_inicial, data_final):
            # Se as datas forem válidas, atualiza as variáveis globais
            self.controlador.set_data_inicial(data_inicial)
            self.controlador.set_data_final(data_final) 



    
        else:
            # Se as datas forem inválidas, exibe uma mensagem de erro
            msg = QMessageBox()
            msg.setText("As datas informadas são inválidas.")
            msg.setWindowTitle("Aviso.")
            msg.setWindowIcon(QtGui.QIcon("imgs/dominiremovebgpreview.png"))
            msg.setIcon(QMessageBox.Warning)  
            msg.setStyleSheet(" backgroundcolor: #304463; color: white; ")
            msg.exec_()

    def validar_datas(self, data_inicial, data_final):
        try:
            data_inicial_obj = datetime.strptime(data_inicial, '%d/%m/%Y')
            data_final_obj = datetime.strptime(data_final, '%d/%m/%Y')

            # Definir o intervalo de datas
            data_inicial_range = datetime.strptime('01/01/2024', '%d/%m/%Y')
            data_final_range = datetime.strptime('31/12/2024', '%d/%m/%Y')

            # Validar se as datas estão dentro do intervalo
            if not (data_inicial_range <= data_inicial_obj <= data_final_range and data_inicial_range <= data_final_obj <= data_final_range):
                msg = QMessageBox()
                msg.setText("As datas devem estar entre 01/01/2024 e 31/12/2024.")
                msg.setWindowTitle("Aviso.")
                msg.setWindowIcon(QtGui.QIcon("imgs/dominiremovebgpreview.png"))
                msg.setIcon(QMessageBox.Warning)  
                msg.setStyleSheet(" backgroundcolor: #304463; color: white; ")
                msg.exec_()
                return False  

            # Validar se a data final é posterior à data inicial
            if data_final_obj < data_inicial_obj:
                msg = QMessageBox()
                msg.setText("A data final deve ser posterior à data inicial.")
                msg.setWindowTitle("Aviso.")
                msg.setWindowIcon(QtGui.QIcon("imgs/dominiremovebgpreview.png"))
                msg.setIcon(QMessageBox.Warning)  
                msg.setStyleSheet(" backgroundcolor: #304463; color: white; ")
                msg.exec_()
                return False  

            # Se as datas forem válidas, exibe as datas selecionadasS
            msg = QMessageBox()
            msg.setText(f"Data inicial: {data_inicial}\nData final: {data_final}")
            msg.setWindowTitle("Sucesso.")
            msg.setWindowIcon(QtGui.QIcon("imgs/dominiremovebgpreview.png"))
            msg.setIcon(QMessageBox.Information)  
            return True

        except ValueError:
            msg = QMessageBox()
            msg.setText("Data inválida. Use o formato DD/MM/AAAA.")
            msg.setWindowTitle("Aviso.")
            msg.setWindowIcon(QtGui.QIcon("imgs/domini-removebg-preview.png"))
            msg.setIcon(QMessageBox.Warning) 
            msg.setStyleSheet(" background-color: #304463; color: white; ")
            msg.exec_()
            return False  