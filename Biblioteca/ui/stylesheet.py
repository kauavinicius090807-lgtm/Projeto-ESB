from PySide6.QtGui import QIcon, QFont, QColor


def greenButton(widget):
    qss = ("""
        QPushButton {        background-color: #23451a;
        border: none;
        border-left: 10px solid #0a3000;            
	    text-align: left;             /* Alinha o ícone e o texto à esquerda */
	    font-size: 12px;
	    font-weight: bold;
        padding-left: 4px;
        }
        QPushButton:hover {
            background-color: #0a3000; /* Cor ao passar o mouse */
            border-left: 10px solid #23451a; /* Linha de destaque azul na esquerda */
                        }
        QPushButton:checked {
                            background-color: #242930; /* Cor ao passar o mouse */
                            border-left: 4px solid #00db42; /* Linha de destaque azul na esquerda */
                            
                        }
        """)
    widget.setStyleSheet(qss)

def yellowButton(widget):
    qss = ("""
        QPushButton {        background-color: #949100;
        border: none;
        border-left: 10px solid #767400;            
	    text-align: left;             /* Alinha o ícone e o texto à esquerda */
	    font-size: 12px;
	    font-weight: bold;
        padding-left: 4px;
        }
        QPushButton:hover {
            background-color: #767400; /* Cor ao passar o mouse */
            border-left: 10px solid #949100; /* Linha de destaque azul na esquerda */
                        }
        QPushButton:checked {
                            background-color: #242930; /* Cor ao passar o mouse */
                            border-left: 4px solid #fffb00; /* Linha de destaque azul na esquerda */
                            
                        }
        """)
    widget.setStyleSheet(qss)

def redButton(widget):
    qss = ("""
        QPushButton {        background-color: #8a0000;
        border: none;
        border-left: 10px solid #610000;            
	    text-align: left;             /* Alinha o ícone e o texto à esquerda */
	    font-size: 12px;
	    font-weight: bold;
        padding-left: 4px;
        }
        QPushButton:hover {
            background-color: #610000; /* Cor ao passar o mouse */
            border-left: 10px solid #8a0000; /* Linha de destaque azul na esquerda */
                        }
        QPushButton:checked {
                            background-color: #242930; /* Cor ao passar o mouse */
                            border-left: 4px solid #ff0000; /* Linha de destaque azul na esquerda */
                            
                        }
        """)
    widget.setStyleSheet(qss)
    
def style(tela):
            
    qss = ("""QWidget {
                background-color: #383b43;
                border-top-right-radius: 20px;
                border-bottom-right-radius: 20px;   
            } 
            """)
    
    tela.setStyleSheet(qss)
def StyleLeftbar(widget):
    
    qss = ("""QWidget {
                background-color: #1c2027
            }""")
    
    widget.setStyleSheet(qss)

def StyleTopbar(widget):
    
    qss = ("""QWidget {
                background-color: #23262d
            }""")
    
    widget.setStyleSheet(qss)

def StyleBotbar(widget):
    
    qss = ("""QWidget {
                background-color: #23262d
            }""")
    
    widget.setStyleSheet(qss)

def StyleLeftpages(widget):
    
    qss = ("""QWidget {
                background-color: #383b43;
                  
            } 
            """)
    
    widget.setStyleSheet(qss)
    
def StyleContent(widget):
    
    qss = ("""QWidget {
                background-color: #1c2027
            }""")
    
    widget.setStyleSheet(qss)    

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
            background-color: #242930; /* Cor ao passar o mouse */
            border-left: 4px solid #333c4d; /* Linha de destaque na direita */
        }
        QToolButton:checked {
                    background-color: #242930; /* Cor ao passar o mouse */
                    border-left: 4px solid #7a93c2; /* Linha de destaque azul na esquerda */
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
    

    
