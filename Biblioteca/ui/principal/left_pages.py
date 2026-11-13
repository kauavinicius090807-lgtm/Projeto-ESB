
from qt_core import *
from ui.stylesheet import fonte, StyleLeftpages, greenButton, redButton, yellowButton

class ui_left_pages(object):
    def setupUi(self, left_StackedWidget):
        if not left_StackedWidget.objectName():
            left_StackedWidget.setObjectName(u"left_pages")
        #StackedWidget.resize(865, 738)
        left_StackedWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        left_StackedWidget.setFrameShape(QFrame.Shape.Panel)
        left_StackedWidget.setFrameShadow(QFrame.Shadow.Raised)
        left_StackedWidget.setLineWidth(1)
        self.usuario = QWidget()
        #self.usuario.setMaximumWidth(100)
        self.txt_usr = QLabel("USUARIO", self.usuario)
        self.linha = QLabel(self.usuario)
        self.consultar_usr = QPushButton()
        self.cadastrar_usr = QPushButton()
        self.excluir_usr = QPushButton()

        StyleLeftpages(self.usuario)
        
        self.usuario.setObjectName(u"usuario")
        self.horizontalLayout = QVBoxLayout(self.usuario)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.linha.setMaximumHeight(25)
        self.linha.setMaximumWidth(97)
        self.linha.setFrameShape(QFrame.Shape.HLine)
        self.linha.setFrameShadow(QFrame.Shadow.Plain)

        self.txt_usr.setMinimumHeight(25)
        self.txt_usr.setMaximumWidth(97)
        self.txt_usr.setMargin(-3)
        self.txt_usr.setFrameShape(QFrame.Shape.NoFrame)
        self.txt_usr.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        fonte(self.txt_usr)
        

        greenButton(self.cadastrar_usr)
        yellowButton(self.consultar_usr)
        redButton(self.excluir_usr)
        self.group = QButtonGroup()
                 
        config_botoes = [
                {"btn": self.consultar_usr, "texto": " Consultar", "icone": "biblioteca/assets/Icons/usuarios-alt.png"},
                {"btn": self.cadastrar_usr,  "texto": " Cadastrar",  "icone": "biblioteca/assets/Icons/adicionar-usuario.png"},
                {"btn": self.excluir_usr,  "texto": " Excluir",  "icone": "biblioteca/assets/Icons/remover-usuario.png"}
                ]

            # 2. Configure o grupo e aplique os ícones/textos em um único loop
        self.group.setExclusive(True)

        for i, config in enumerate(config_botoes):
            btn = config["btn"]
            btn.setCheckable(True)
            #btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            # Define o texto e o ícone na esquerda
            btn.setText(config["texto"])
            btn.setIcon(QIcon(config["icone"]))
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            btn.setMaximumWidth(97)
            btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
            btn.setMinimumHeight(40)
            
            # (Opcional) Ajusta o tamanho do ícone se achar muito pequeno
            #btn.setIconSize(QtCore.QSize(24, 24)) 
            
            self.group.addButton(btn, i)
        
        self.horizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.addWidget(self.txt_usr)
        self.horizontalLayout.addWidget(self.linha)
        self.horizontalLayout.addWidget(self.consultar_usr)
        self.horizontalLayout.addWidget(self.cadastrar_usr)
        self.horizontalLayout.addWidget(self.excluir_usr)    
        self.horizontalLayout.addStretch()

        left_StackedWidget.addWidget(self.usuario)
        
        self.livro = QWidget()
        self.livro.setObjectName(u"livro")
        StyleLeftpages(self.livro)
        
        self.horizontalLayout_2 = QVBoxLayout(self.livro)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        
        self.linha2 = QLabel(self.livro)
        self.consultar_lvr = QPushButton()
        self.cadastrar_lvr = QPushButton()
        self.excluir_lvr = QPushButton()
        greenButton(self.cadastrar_lvr)
        yellowButton(self.consultar_lvr)
        redButton(self.excluir_lvr)
        
                    
        config_botoes2 = [
                {"btn": self.consultar_lvr, "texto": " Consultar", "icone": "biblioteca/assets/Icons/usuarios-alt.png"},
                {"btn": self.cadastrar_lvr,  "texto": " Cadastrar",  "icone": "biblioteca/assets/Icons/adicionar-usuario.png"},
                {"btn": self.excluir_lvr,  "texto": " Excluir",  "icone": "biblioteca/assets/Icons/remover-usuario.png"}
                ]

        for i, config in enumerate(config_botoes2):
            btn = config["btn"]
            btn.setCheckable(True)
            #btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            # Define o texto e o ícone na esquerda
            btn.setText(config["texto"])
            btn.setIcon(QIcon(config["icone"]))
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            btn.setMaximumWidth(97)
            btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
            btn.setMinimumHeight(40)
          
            self.group.addButton(btn, i)
        
        self.linha2.setMaximumHeight(25)
        self.linha2.setMaximumWidth(97)
        self.linha2.setFrameShape(QFrame.Shape.HLine)
        self.linha2.setFrameShadow(QFrame.Shadow.Plain)
        
        self.txt_lvr = QLabel("USUARIO", self.usuario)
        self.txt_lvr.setMinimumHeight(25)
        self.txt_lvr.setMaximumWidth(97)
        self.txt_lvr.setMargin(-3)
        self.txt_lvr.setFrameShape(QFrame.Shape.NoFrame)
        self.txt_lvr.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        fonte(self.txt_lvr)


        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.addWidget(self.txt_lvr)
        self.horizontalLayout_2.addWidget(self.linha2)
        self.horizontalLayout_2.addWidget(self.consultar_lvr)
        self.horizontalLayout_2.addWidget(self.cadastrar_lvr)
        self.horizontalLayout_2.addWidget(self.excluir_lvr)
        self.horizontalLayout_2.addStretch()
        

        left_StackedWidget.addWidget(self.livro)
        
        
        
        self.multa = QWidget()
        #self.multa.setMaximumWidth(100)
        
        
        self.multa.setObjectName(u"multa")
        StyleLeftpages(self.multa)

        self.horizontalLayout_3 = QVBoxLayout(self.multa)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_multa = QLabel("USUARIO", self.usuario)
        self.txt_multa.setMinimumHeight(25)
        self.txt_multa.setMaximumWidth(97)
        self.txt_multa.setMargin(-3)
        self.txt_multa.setFrameShape(QFrame.Shape.NoFrame)
        self.txt_multa.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        fonte(self.txt_multa)

        self.horizontalLayout_3.addWidget(self.txt_multa)


        left_StackedWidget.addWidget(self.multa)

        #self.retranslateUi(left_StackedWidget)

        left_StackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(left_StackedWidget)
    # setupUi

    # def retranslateUi(self, left_StackedWidget):
    #     left_StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
    #     self.label_3.setText(QCoreApplication.translate("StackedWidget", u"TextLabel", None))
    #     self.label.setText(QCoreApplication.translate("StackedWidget", u"TextLabel", None))
    #     self.label_2.setText(QCoreApplication.translate("StackedWidget", u"TextLabel", None))
    # retranslateUi
