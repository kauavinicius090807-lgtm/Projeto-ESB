
import sys
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QComboBox,
    QSpinBox,
    QPushButton,
    QHBoxLayout,
    QMessageBox,
    QLabel
)
from PySide6.QtCore import Qt


class CadastroLivro(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Cadastro de Livro")
        self.setMaximumHeight(520)
        self.setMaximumWidth(720)
        self.setModal(True)

        self.criar_interface()

    def criar_interface(self):

        layout_principal = QVBoxLayout(self)

        # Título
        titulo = QLabel("Cadastro de Livro")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
            color: #26384A;
            padding: 10px;
        """)

        layout_principal.addWidget(titulo)

        # Formulário
        formulario = QFormLayout()
        formulario.setSpacing(15)

        # Número de série
        self.numero_serie = QLineEdit()
        self.numero_serie.setPlaceholderText("Digite o número de série")

        # Nome do livro
        self.nome_livro = QLineEdit()
        self.nome_livro.setPlaceholderText("Digite o nome do livro")

        # Categoria
        self.categoria = QComboBox()
        self.categoria.addItems([
            "Selecione uma categoria",
            "Literatura",
            "Romance",
            "Ficção",
            "Fantasia",
            "Suspense",
            "História",
            "Ciências",
            "Tecnologia",
            "Educação",
            "Outros"
        ])

        # Autor
        self.autor = QLineEdit()
        self.autor.setPlaceholderText("Digite o nome do autor")

        # Edição
        self.edicao = QSpinBox()
        self.edicao.setRange(1, 999)
        self.edicao.setValue(1)
        self.edicao.setSuffix("ª edição")

        # Ano
        self.ano = QSpinBox()
        self.ano.setRange(1000, 2100)
        self.ano.setValue(2026)

        # ISBN
        self.isbn = QLineEdit()
        self.isbn.setPlaceholderText("Ex: 9788535902778")

        # Adicionando campos ao formulário
        formulario.addRow("Número de série:", self.numero_serie)
        formulario.addRow("Nome do livro:", self.nome_livro)
        formulario.addRow("Categoria:", self.categoria)
        formulario.addRow("Autor:", self.autor)
        formulario.addRow("Edição:", self.edicao)
        formulario.addRow("Ano:", self.ano)
        formulario.addRow("ISBN:", self.isbn)

        layout_principal.addLayout(formulario)

        # Espaçamento
        layout_principal.addSpacing(20)

        # Botões
        layout_botoes = QHBoxLayout()

        self.btn_cancelar = QPushButton("Cancelar")
        self.btn_salvar = QPushButton("Salvar Livro")

        self.btn_cancelar.clicked.connect(self.reject)
        self.btn_salvar.clicked.connect(self.salvar_livro)

        layout_botoes.addWidget(self.btn_cancelar)
        layout_botoes.addWidget(self.btn_salvar)

        layout_principal.addLayout(layout_botoes)

        # Estilização
        self.setStyleSheet("""
            QDialog {
                background-color: #1c2027;
            }

            QLineEdit, QComboBox, QSpinBox {
                background-color: RGB 255,255,255,0.3;
                border: 1px solid #CBD2D9;
                border-radius: 5px;
                padding: 8px;
                min-height: 22px;
            }

            QLineEdit:focus, QComboBox:focus, QSpinBox:focus {
                border: 1px solid #2878C8;
            }

            QPushButton {
                background-color: #2878C8;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #1D5F9E;
            }
        """)

    def salvar_livro(self):

        numero = self.numero_serie.text().strip()
        nome = self.nome_livro.text().strip()
        categoria = self.categoria.currentText()
        autor = self.autor.text().strip()
        edicao = self.edicao.value()
        ano = self.ano.value()
        isbn = self.isbn.text().strip()

        # Validação dos campos
        if not numero or not nome or not autor or not isbn:
            QMessageBox.warning(
                self,
                "Atenção",
                "Preencha todos os campos!"
            )
            return

        if self.categoria.currentIndex() == 0:
            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma categoria."
            )
            return

        # Dados do livro
        self.dados_livro = {
            "numero_serie": numero,
            "nome": nome,
            "categoria": categoria,
            "autor": autor,
            "edicao": edicao,
            "ano": ano,
            "isbn": isbn
        }

        QMessageBox.information(
            self,
            "Sucesso",
            "Livro cadastrado com sucesso!"
        )

        self.accept()


# Execução para testar a janela
if __name__ == "__main__":

    app = QApplication(sys.argv)

    janela = CadastroLivro()

    if janela.exec():
        print("Dados cadastrados:")
        print(janela.dados_livro)

    sys.exit(app.exec())
