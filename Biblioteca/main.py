import os
import ctypes
import sys

from ui.main_window import ui_MainWindow
from qt_core import *
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_MainWindow()
        self.ui.setup_ui(self)
        

        self.show()
    


if __name__ == "__main__":
    # ---> CORREÇÃO PARA A BARRA DE TAREFAS NO WINDOWS <---
    # Cria uma identificação única para o seu aplicativo no Windows
    myappid = "Alliance_app_v1.0"  # Substitua pelo nome do seu aplicativo
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowIcon(QIcon("assets/Icons/image.png"))
    sys.exit(app.exec())
