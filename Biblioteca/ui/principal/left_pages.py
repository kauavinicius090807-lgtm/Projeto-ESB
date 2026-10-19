
from qt_core import *
from ui.stylesheet import fonte

class ui_left_pages(object):
    def setupUi(self, left_StackedWidget):
        if not left_StackedWidget.objectName():
            left_StackedWidget.setObjectName(u"left_pages")
        #StackedWidget.resize(865, 738)
        left_StackedWidget.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.usuario = QWidget()
        #self.usuario.setMaximumWidth(100)
        
        self.usuario.setStyleSheet("background-color: #3c3c3c")
        self.usuario.setObjectName(u"usuario")
        self.horizontalLayout = QVBoxLayout(self.usuario)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_usuario = QLabel("USUARIO", self.usuario)
        self.txt_usuario.setStyleSheet("background-color: grey")
        fonte(self.txt_usuario)
        self.txt_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        # self.txt_linha = QLabel("______________")
        # self.txt_linha.setMaximumHeight(10)
        # self.txt_linha.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        self.consultar = QToolButton()
        self.cadastrar = QToolButton()
        self.excluir = QToolButton()
        
        self.group = QButtonGroup()
                 
        config_botoes = [
                {"btn": self.consultar, "texto": " Consultar", "icone": "Icons/image.png"},
                {"btn": self.cadastrar,  "texto": " Cadastrar",  "icone": "Icons/image.png"},
                {"btn": self.excluir,  "texto": " Excluir",  "icone": "Icons/image.png"}
]

            # 2. Configure o grupo e aplique os ícones/textos em um único loop
        self.group.setExclusive(True)

        for i, config in enumerate(config_botoes):
            btn = config["btn"]
            btn.setCheckable(True)
            btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            # Define o texto e o ícone na esquerda
            btn.setText(config["texto"])
            btn.setIcon(QIcon(config["icone"]))
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
            
            # (Opcional) Ajusta o tamanho do ícone se achar muito pequeno
            # btn.setIconSize(QtCore.QSize(24, 24)) 
            
            self.group.addButton(btn, i)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.addWidget(self.txt_usuario)
        #self.horizontalLayout.addWidget(self.txt_linha)
        self.horizontalLayout.addWidget(self.consultar)
        self.horizontalLayout.addWidget(self.cadastrar)
        self.horizontalLayout.addWidget(self.excluir)
        
        
        self.horizontalLayout.addStretch()
        #self.txt_usuario.setText("USUARIO")

        left_StackedWidget.addWidget(self.usuario)
        self.livro = QWidget()
        #self.livro.setMaximumWidth(100)
        self.livro.setObjectName(u"livro")
        self.livro.setStyleSheet("background-color: #3c3c3c")
        self.horizontalLayout_2 = QVBoxLayout(self.livro)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        # self.label = QLabel("livro",self.livro)
        # self.label.setObjectName(u"label")
        # self.label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

        #self.horizontalLayout_2.addWidget(self.label)


        left_StackedWidget.addWidget(self.livro)
        self.multa = QWidget()
        #self.multa.setMaximumWidth(100)
        
        self.multa.setObjectName(u"multa")
        self.multa.setStyleSheet("background-color: #3c3c3c")
        self.horizontalLayout_3 = QVBoxLayout(self.multa)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel("multas",self.multa)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)


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
