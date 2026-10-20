from PySide6.QtGui import QIcon, QFont, QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtCore import QPropertyAnimation, QEasingCurve

def button_css(widget):
    qss = ("""
        QPushButton {
        background-color: transparent;
            color: white;
            border: none;
            padding-left: 5px;
            text-align: center; /* Alinha o ícone e o texto à esquerda */
            font-size: 25px;
        }
        QPushButton:hover {
            background-color: #282828; /* Cor ao passar o mouse */
            border-right: 4px solid #3c3c3c; /* Linha de destaque azul na esquerda */
        }
        """)
    widget.setStyleSheet(qss)
    
def style(tela):
            
    qss = ("""QWidget {
                background-color: #3c3c3c;
                border-top-right-radius: 20px;
                border-bottom-right-radius: 20px;   
            } 
            """)
    
    tela.setStyleSheet(qss)

    

def toogle_css(widget):

    qss = ("""
        QToolButton {
        background-color: transparent;
            color: white;
            border: none;
            padding-left: 5px;
            text-align: center; /* Alinha o ícone e o texto à esquerda */
            font-size: 25px;
            
        }
        QToolButton:hover {
            background-color: #323232; /* Cor ao passar o mouse */
            border-right: 4px solid #3c3c3c; /* Linha de destaque na direita */
        }
        QToolButton:checked {
                    background-color: #303030; /* Cor ao passar o mouse */
                    border-right: 4px solid #3c3c3c; /* Linha de destaque azul na esquerda */
                }
        """)
    widget.setStyleSheet(qss)


def icon (widget, img: str):
    icone = QIcon(img)

    widget.setIcon(icone)

def fonte(widget):
    
    fonte_titulo = QFont("Segoe UI", 10, QFont.Weight.Bold)
    #fonte_titulo.setUnderline(True)
    widget.setFont(fonte_titulo)
    

    
