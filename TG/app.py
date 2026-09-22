from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# =========================
# DADOS
# =========================

livros = {
    1: {
        "titulo": "Anatomia Humana",
        "autor": "J. D. Smith",
        "categoria": "Enfermagem",
        "disponivel": True
    },
    2: {
        "titulo": "Farmacologia Básica",
        "autor": "Katzung",
        "categoria": "Farmácia",
        "disponivel": True
    },
    3: {
        "titulo": "Python para Iniciantes",
        "autor": "Autor Exemplo",
        "categoria": "Tecnologia",
        "disponivel": True
    }
}

# =========================
# PÁGINA PRINCIPAL
# =========================

@app.route("/")
def index():
    return render_template(
        "index.html",
        livros=livros
    )


# =========================
# CADASTRAR LIVRO
# =========================

@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    titulo = request.form["titulo"]
    autor = request.form["autor"]
    categoria = request.form["categoria"]

    novo_id = max(livros.keys()) + 1

    livros[novo_id] = {
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "disponivel": True
    }

    return redirect("/")

@app.route("/editar/<int:livro_id>", methods=["GET", "POST"])
def editar(livro_id):
    if livro_id not in livros:
        return redirect("/")
    
    livro = livros[livro_id]
    
    if request.method == "POST":
        livro["titulo"] = request.form["titulo"]
        livro["autor"] = request.form["autor"]
        livro["categoria"] = request.form["categoria"]
        # Se o checkbox estiver marcado, fica True, senão False
        livro["disponivel"] = "disponivel" in request.form
        return redirect("/")
        
    return render_template("editar.html", livro=livro, livro_id=livro_id)


# =========================
# INICIAR SERVIDOR
# =========================

if __name__ == "__main__":
    app.run(debug=True)
