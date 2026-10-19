from qt_core import *

class ui_pages(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"pages")
        StackedWidget.resize(865, 738)
        StackedWidget.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.usuario = QWidget()
        self.usuario.setMaximumWidth(100)
        self.usuario.setStyleSheet("background-color: white")
        self.usuario.setObjectName(u"usuario")
        self.horizontalLayout = QVBoxLayout(self.usuario)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalSlider = QSlider(self.usuario)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout.addWidget(self.verticalSlider)

        self.label_3 = QLabel("usuario",self.usuario)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        StackedWidget.addWidget(self.usuario)
        self.livro = QWidget()
        self.livro.setMaximumWidth(100)
        self.livro.setObjectName(u"livro")
        self.horizontalLayout_2 = QVBoxLayout(self.livro)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel("livros",self.livro)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.verticalScrollBar = QScrollBar(self.livro)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_2.addWidget(self.verticalScrollBar)

        StackedWidget.addWidget(self.livro)
        self.multa = QWidget()
        self.multa.setMaximumWidth(100)
        
        self.multa.setObjectName(u"multa")
        self.horizontalLayout_3 = QVBoxLayout(self.multa)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel("multas",self.multa)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSlider = QSlider(self.multa)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalSlider)

        StackedWidget.addWidget(self.multa)

        # self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(1)


    #     QMetaObject.connectSlotsByName(StackedWidget)
    # # setupUi

    # def retranslateUi(self, StackedWidget):
    #     StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
    #     self.label_3.setText(QCoreApplication.translate("StackedWidget", u"TextLabel", None))
    #     self.label.setText(QCoreApplication.translate("StackedWidget", u"TextLabel", None))
    #     self.label_2.setText(QCoreApplication.translate("StackedWidget", u"TextLabel", None))
    # # retranslateUi

