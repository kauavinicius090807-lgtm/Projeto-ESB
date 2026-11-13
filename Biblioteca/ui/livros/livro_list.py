
import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog,
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QPushButton, QLabel, QLineEdit, QScrollArea,
    QFrame, QFormLayout
)
from PySide6.QtCore import Qt


# Dados de exemplo
LIVROS = [
    {
        "numero_serie": "001",
        "nome": "Dom Casmurro",
        "categoria": "Literatura",
        "autor": "Machado de Assis",
        "edicao": 1,
        "ano": 1899,
        "isbn": "9788535902778"
    },
    {
        "numero_serie": "002",
        "nome": "O Pequeno Príncipe",
        "categoria": "Fantasia",
        "autor": "Antoine de Saint-Exupéry",
        "edicao": 2,
        "ano": 1943,
        "isbn": "9788522031445"
    },
    {
        "numero_serie": "003",
        "nome": "1984",
        "categoria": "Ficção",
        "autor": "George Orwell",
        "edicao": 3,
        "ano": 1949,
        "isbn": "9788535914849"
    },
    {
        "numero_serie": "004",
        "nome": "Harry Potter",
        "categoria": "Fantasia",
        "autor": "J. K. Rowling",
        "edicao": 1,
        "ano": 1997,
        "isbn": "9788532530783"
    },
    {
        "numero_serie": "005",
        "nome": "O Hobbit",
        "categoria": "Fantasia",
        "autor": "J. R. R. Tolkien",
        "edicao": 1,
        "ano": 1937,
        "isbn": "9788595084742"
    },
    {
        "numero_serie": "006",
        "nome": "A Metamorfose",
        "categoria": "Literatura",
        "autor": "Franz Kafka",
        "edicao": 2,
        "ano": 1915,
        "isbn": "9788535910667"
    },
    {
        "numero_serie": "007",
        "nome": "Capitães da Areia",
        "categoria": "Romance",
        "autor": "Jorge Amado",
        "edicao": 1,
        "ano": 1937,
        "isbn": "9788535911695"
    },
    {
        "numero_serie": "008",
        "nome": "O Cortiço",
        "categoria": "Literatura",
        "autor": "Aluísio Azevedo",
        "edicao": 1,
        "ano": 1890,
        "isbn": "9788572326972"
    }
]


# Modal com informações do livro
class DetalhesLivro(QDialog):

    def __init__(self, livro, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Detalhes do Livro")
        self.setMaximumHeight(1024)
        self.setMaximumWidth(762)
        self.setModal(True)

        layout = QVBoxLayout(self)

        titulo = QLabel("📖 Informações do Livro")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("""
            font-size: 21px;
            font-weight: bold;
            color: #26384A;
            padding: 12px;
        """)

        layout.addWidget(titulo)

        formulario = QFormLayout()
        formulario.setSpacing(15)

        campos = [
            ("Número de série:", livro["numero_serie"]),
            ("Nome do livro:", livro["nome"]),
            ("Categoria:", livro["categoria"]),
            ("Autor:", livro["autor"]),
            ("Edição:", f'{livro["edicao"]}ª edição'),
            ("Ano:", str(livro["ano"])),
            ("ISBN:", livro["isbn"])
        ]

        for nome, valor in campos:
            valor_label = QLabel(valor)
            valor_label.setWordWrap(True)
            valor_label.setStyleSheet("""
                font-size: 13px;
                color: #26384A;
            """)
            formulario.addRow(nome, valor_label)

        layout.addLayout(formulario)

        botao_fechar = QPushButton("Fechar")
        botao_fechar.clicked.connect(self.accept)

        layout.addWidget(botao_fechar)

        self.setStyleSheet("""
            QDialog {
                background-color: #1c2027;
            }

            QPushButton {
                background-color: #2878C8;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }

            QPushButton:hover {
                background-color: #1D5F9E;
            }
        """)


# Janela principal
class Biblioteca(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Biblioteca ESB")
        self.setFixedSize(1024, 768)

        self.livros = LIVROS.copy()

        self.criar_interface()
        self.carregar_livros()

    def criar_interface(self):

        central = QWidget()
        self.setCentralWidget(central)

        layout_principal = QVBoxLayout(central)
        layout_principal.setContentsMargins(25, 20, 25, 20)
        layout_principal.setSpacing(15)

        # Cabeçalho
        cabecalho = QHBoxLayout()

        titulo = QLabel("📚 Biblioteca ESB")
        titulo.setStyleSheet("""
            font-size: 26px;
            font-weight: bold;
            color: #26384A;
        """)

        cabecalho.addWidget(titulo)
        cabecalho.addStretch()

        layout_principal.addLayout(cabecalho)

        # Pesquisa
        self.pesquisa = QLineEdit()
        self.pesquisa.setPlaceholderText(
            "Pesquisar livro pelo nome..."
        )
        self.pesquisa.setFixedHeight(42)
        self.pesquisa.textChanged.connect(
            self.filtrar_livros
        )

        layout_principal.addWidget(self.pesquisa)

        # Área de rolagem
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QFrame.Shape.NoFrame)

        self.container = QWidget()

        self.grade = QGridLayout(self.container)
        self.grade.setSpacing(18)
        self.grade.setContentsMargins(5, 5, 5, 5)

        self.scroll.setWidget(self.container)

        layout_principal.addWidget(self.scroll)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #1c2027;
            }

            QLineEdit {
                background-color: white;
                border: 1px solid #CBD2D9;
                border-radius: 7px;
                padding: 8px;
                font-size: 14px;
            }

            QLineEdit:focus {
                border: 1px solid #2878C8;
            }
        """)

    # Cria um botão para cada livro
    def criar_botao_livro(self, livro):

        botao = QPushButton(
            f'📖\n\n{livro["nome"]}'
        )

        botao.setFixedSize(205, 125)
        botao.setCursor(Qt.CursorShape.PointingHandCursor)

        botao.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid #D5DCE3;
                border-radius: 10px;
                color: #26384A;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
            }

            QPushButton:hover {
                background-color: #E8F2FC;
                border: 2px solid #2878C8;
            }

            QPushButton:pressed {
                background-color: #D5E8F8;
            }
        """)

        botao.clicked.connect(
            lambda checked=False, l=livro:
            self.abrir_detalhes(l)
        )

        return botao

    # Limpa os botões anteriores
    def limpar_grade(self):

        while self.grade.count():

            item = self.grade.takeAt(0)

            widget = item.widget()

            if widget:
                widget.deleteLater()

    # Carrega os livros na grade
    def carregar_livros(self, lista=None):

        self.limpar_grade()

        if lista is None:
            lista = self.livros

        colunas = 4

        for indice, livro in enumerate(lista):

            linha = indice // colunas
            coluna = indice % colunas

            botao = self.criar_botao_livro(livro)

            self.grade.addWidget(
                botao,
                linha,
                coluna,
                alignment=Qt.AlignmentFlag.AlignCenter
            )

        self.grade.setRowStretch(
            (len(lista) + colunas - 1) // colunas,
            1
        )

    # Pesquisa de livros
    def filtrar_livros(self, texto):

        resultado = [
            livro for livro in self.livros
            if texto.lower() in livro["nome"].lower()
        ]

        self.carregar_livros(resultado)

    # Abre o modal
    def abrir_detalhes(self, livro):

        modal = DetalhesLivro(livro, self)
        modal.exec()


# Inicialização
if __name__ == "__main__":

    app = QApplication(sys.argv)

    janela = Biblioteca()
    janela.show()

    sys.exit(app.exec())

