from PyQt5.QtWidgets import QApplication
from ControladorTelas import ControladorTelas
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlador = ControladorTelas()
    controlador.run()
    sys.exit(app.exec_())

