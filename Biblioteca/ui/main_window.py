import sys

from PySide6.QtGui import QMouseEvent
from qt_core import *
from ui.stylesheet import style
#from gui.ui_pages import Ui_StackedWidget
from ui.principal.left_pages import ui_left_pages
from ui.principal.left_menu import ui_left_menu
from ui.principal.pages import ui_pages



class ui_MainWindow(QMainWindow):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        parent.resize(1024, 768)
        

        #CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        
        
        #CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        
        #CREATE BARRA LATERAL
        self.left_menu = ui_left_menu()
        
        #CREATE FRAME PRINCIPAL
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #1f2020")


        #CREATE MENU DE OPÇÕES
        self.left_pages = QFrame()
        self.left_pages.setMinimumWidth(0)
        self.left_pages.setMaximumWidth(0)
        #style(self.left_pages)
        #self.left_pages.hide()

        #TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setStyleSheet("background-color: #282828")

        #BOTTOM BAR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #282828")


        #PÁGINA DO MENU
        self.menu = QStackedWidget()
        self.ui_menu = ui_left_pages()
        self.ui_menu.setupUi(self.menu)
        self.menu.setCurrentWidget(self.ui_menu.livro)


        #MAIN LAYOUT
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.left_pages)
        self.main_layout.addWidget(self.content)


        #LAYOUT PÁGINA DE CONTEUDO
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)
        
        self.layout_pages = QVBoxLayout(self.left_pages)
        self.layout_pages.addWidget(self.menu)
        self.layout_pages.setContentsMargins(0, 0, 0, 0)
        self.layout_pages.setSpacing(0)
       

        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addStretch()
        self.content_layout.addWidget(self.bottom_bar)
        self.label = QLabel("fonte")
        
        self.menu.setCurrentWidget(self.ui_menu.usuario)
        self.left_menu.btn_usuario.clicked.connect(lambda: self.menu.setCurrentWidget(self.ui_menu.usuario))
        self.left_menu.btn_livros.clicked.connect(lambda: self.menu.setCurrentWidget(self.ui_menu.livro))
        self.left_menu.btn_multas.clicked.connect(lambda: self.menu.setCurrentWidget(self.ui_menu.multa))
        
        
        self.left_menu.btn_usuario.clicked.connect(self.animation2)
        self.left_menu.btn_livros.clicked.connect(self.animation2)
        self.left_menu.btn_multas.clicked.connect(self.animation2)

        
        self.left_menu.btn_menu.clicked.connect(self.animation)
        
        parent.setCentralWidget(self.central_frame)
   
        
    def animation(self):

        if self.left_pages.width() == 0:
            start_width = 0
            end_width = 100
        else:
            start_width = self.left_pages.width()
            end_width = 0

        self.anim = QPropertyAnimation(self.left_pages, b"maximumWidth")
        self.anim.setDuration(200) # Tempo em milissegundos
        self.anim.setStartValue(start_width)
        self.anim.setEndValue(end_width)

        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)

        self.anim.valueChanged.connect(
            lambda value: self.left_pages.setMinimumWidth(value)
        )
        
        if end_width == 100:
           statusTela = True
        else: 
            statusTela = False
            
        self.left_menu.btn_menu.blockSignals(True)
        self.left_menu.btn_menu.setChecked(statusTela)
        self.left_menu.btn_menu.blockSignals(False)
        self.anim.start()
        
        if end_width == 0:
            self.left_menu.group.setExclusive(False)
            checked_button = self.left_menu.group.checkedButton()
            if checked_button is not None:
                checked_button.setChecked(False)
        
        
        
    def animation2(self):

        if self.left_pages.width() == 0:
            start_width = 0
            end_width = 100
        else:
            start_width = self.left_pages.width()
            end_width = 100

        self.anim = QPropertyAnimation(self.left_pages, b"maximumWidth")
        self.anim.setDuration(200) # Tempo em milissegundos
        self.anim.setStartValue(start_width)
        self.anim.setEndValue(end_width)

        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)

        self.anim.valueChanged.connect(
            lambda value: self.left_pages.setMinimumWidth(value)
        )
        
        if end_width == 100:
            statusTela = True
        else: 
            statusTela = False
            
            
        self.left_menu.btn_menu.blockSignals(True)
        self.left_menu.btn_menu.setChecked(statusTela)
        self.left_menu.btn_menu.blockSignals(False)
        self.anim.start()
      
        self.left_menu.group.setExclusive(True)
        
        
        
        
        
        
    
    
        

        

