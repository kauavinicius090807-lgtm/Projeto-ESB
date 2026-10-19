
from qt_core import *
from ui.stylesheet import button_css, icon, toogle_css


class ui_left_menu(QWidget):
    def __init__(self):
        super().__init__()
        
        #self.setLineWidth(0)
        self.setMinimumWidth(50)
        self.setMaximumWidth(50)    

        self.left_layout = QVBoxLayout(self)
        self.left_layout.setContentsMargins(0, 0, 0, 0)
        self.left_layout.setSpacing(0)
        
      
                
        # Cor de fundo apenas para destacar visualmente a divisão das telas
        #self.setStyleSheet("background-color: #9e2121; border-right: 1px solid #ccc;")
               
        
        self.Left_menu = QFrame()
        self.Left_menu.setStyleSheet("background-color: #1f2020")
        self.Left_menu.setObjectName(u"Left_menu")
        
        self.left_layout.addWidget(self.Left_menu)
        
        #self.Left_menu.setFrameShape(QFrame.Shape.StyledPanel)
        #self.Left_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.Left_menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        
        
        self.Buttons = QFrame(self.Left_menu)
        self.Buttons.setStyleSheet("background-color: #1f2020")
        self.Buttons.setObjectName(u"Buttons")
        #self.Buttons.setFrameShape(QFrame.Shape.StyledPanel)
        #self.Buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Buttons)
        self.verticalLayout.addWidget(self.Buttons)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_menu = QToolButton(self.Buttons)
        self.btn_menu.setMinimumHeight(50)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy)
        self.btn_menu.setObjectName(u"button_menu")

        toogle_css(self.btn_menu)
        icon(self.btn_menu, "assets/icons/menu.png")
        self.btn_menu.setCheckable(True)
        
                
        
        self.verticalLayout_2.addWidget(self.btn_menu)
        self.btn_usuario = QToolButton(self.Buttons)
        self.btn_usuario.setObjectName(u"button_usuario")
        self.btn_usuario.setMinimumHeight(45)
        self.btn_usuario.setSizePolicy(sizePolicy)
        icon(self.btn_usuario, "assets/icons/usuario.png")
        toogle_css(self.btn_usuario)
        self.verticalLayout_2.addWidget(self.btn_usuario)
        
        self.btn_livros = QToolButton(self.Buttons)
        self.btn_livros.setObjectName(u"Button_livros")
        self.btn_livros.setSizePolicy(sizePolicy)
        icon(self.btn_livros, "assets/icons/livro.png")
        toogle_css(self.btn_livros)
        self.btn_livros.setMinimumHeight(45)
        self.verticalLayout_2.addWidget(self.btn_livros)
        
        self.btn_multas = QToolButton(self.Buttons)
        self.btn_multas.setObjectName(u"button_multas")
        self.btn_multas.setMinimumHeight(45)
        self.btn_multas.setSizePolicy(sizePolicy)
        icon(self.btn_multas, "assets/icons/multa.png")
        toogle_css(self.btn_multas)
        #self.button_multas.setEnabled(True)
        #self.button_multas.setStyleSheet(u"background-color: white")
        self.verticalLayout_2.addWidget(self.btn_multas)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.verticalLayout.addWidget(self.Buttons)
        

        self.settings = QFrame(self.Left_menu)
        self.settings.setObjectName(u"settings")
        #self.settings.setFrameShape(QFrame.Shape.StyledPanel)
        #self.settings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.settings)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_config = QToolButton(self.settings)
        self.btn_config.setMinimumHeight(50)
        self.btn_config.setObjectName(u"config")
        self.btn_config.setSizePolicy(sizePolicy)
        icon(self.btn_config, "assets/icons/engrenagem.png")
        toogle_css(self.btn_config)
        self.verticalLayout_3.addWidget(self.btn_config)
        self.verticalLayout.addWidget(self.settings)
        self.version = QLabel("v1.0.0",self.Left_menu)
        self.version.setObjectName(u"version")
        self.version.setMinimumHeight(30)
        self.verticalLayout.addWidget(self.version, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)
        
        self.group = QButtonGroup(self)
        self.group.setExclusive(True)
        
        botoes = [self.btn_usuario, self.btn_livros, self.btn_multas]
        
        for i, btn in enumerate(botoes):
            btn.setCheckable(True)        
            self.group.addButton(btn, i)
        
        
         
        
       

        

        #self.retranslateUi(left_menu)

        #QMetaObject.connectSlotsByName(left_layout)
     #setupUi

    # def retranslateUi(self, MainWindow):
    #     MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    #     self.button_menu.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    #     self.button_usuario.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    #     self.Button_livros.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    #     self.button_multas.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    #     self.setting.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    #     self.version.setText(QCoreApplication.translate("MainWindow", u"V1.0.0", None))
    # retranslateUi

            
