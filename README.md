<div align="center">

# 📚 Sistema de Gerenciamento de Biblioteca - ESB

<p>
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge&logo=git&logoColor=white" alt="Status do Projeto">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Escola-S%C3%A3o%20Bernardo-blue?style=for-the-badge" alt="Instituição">
</p>

**Sistema desenvolvido para planejar, organizar e otimizar os processos de empréstimo, devolução e incorporação de novos livros na biblioteca da Escola São Bernardo (ESB).**

</div>

---

## 📖 Sobre O Projeto

<details>
<summary><b>Clique para expandir os detalhes do objetivo do projeto</b></summary>
<br>

Este projeto tem como objetivo principal mapear, organizar e modernizar o fluxo de gerenciamento da biblioteca da **Escola São Bernardo (ESB)**, com foco especial no atendimento aos alunos dos cursos técnicos de **Enfermagem** e **Farmácia**.

Atualmente, grande parte das etapas operacionais é realizada de forma manual. Diante disso, a proposta visa analisar o funcionamento atual, identificar gargalos e desenhar processos mais claros, ágeis e rastreáveis por meio de modelagem de processos (BPMN), programação em Python e documentação estruturada.

</details>

---

## ⚙️ Tecnologias e Ferramentas Utilizadas

As seguintes ferramentas e abordagens foram empregadas no desenvolvimento do projeto:

* **Linguagem:** Python (Ainda não utilizado)
* **Modelagem de Processos:** BPMN (Business Process Model and Notation)
* **Documentação:** Microsoft Word / Markdown
* **Controle de Versão:** Git e GitHub

---

## 🔎 Como Funciona o Processo

O fluxo operacional do sistema divide-se em três grandes pilares: **Empréstimo**, **Devolução** e **Entrada de Novos Livros**.

### 📚 1. Empréstimo de Livros
<div style="background-color: #f6f8fa; padding: 15px; border-radius: 6px; border: 1px solid #d0d7de;">

O fluxo de retirada ocorre nas seguintes etapas:
1. O aluno pesquisa e localiza o livro desejado na biblioteca.
2. A equipe realiza a verificação da regularidade da matrícula do aluno.
3. Estando apto, o aluno recebe e preenche a ficha de retirada.
4. O atendente valida a integridade e disponibilidade do livro.
5. O empréstimo é efetivado no sistema/controle e o comprovante é entregue ao aluno.

</div>

### ⏰ 2. Devolução de Livros
<div style="background-color: #f6f8fa; padding: 15px; border-radius: 6px; border: 1px solid #d0d7de;">

* **Prazo padrão:** 7 dias corridos.
* **Prorrogações:** É permitida a renovação por até **3 vezes**, caso não haja reservas pendentes.
* **Fluxo de devolução:**
  * 📕 **Inspeção física:** A condição do livro é verificada.
  * ⚠️ **Danos:** Caso o exemplar esteja danificado, o aluno poderá ser acionado para reposição.
  * 📅 **Prazos:** A data de entrega é conferida em relação ao limite estipulado.
  * 💰 **Multas:** Em caso de atraso, o valor correspondente é calculado.
  * 📚 **Retorno ao estoque:** Após a conferência final, o livro é disponibilizado novamente para empréstimo.

</div>

---

## 📦 Entrada de Novos Livros (Doações)

<div style="background-color: #f6f8fa; padding: 15px; border-radius: 6px; border: 1px solid #d0d7de;">

O fluxo também contempla a ampliação do acervo por meio de doações (parcerias com editoras ou doadores):

1. 📋 Catalogação inicial dos títulos disponibilizados.
2. 📝 Preparação e envio da lista para avaliação interna.
3. 📩 Solicitação de autorização formal.
4. 🤝 Contato com os doadores após a aprovação.
5. 📦 Separação, embalagem e emissão da nota de doação.
6. 🚚 Envio, recebimento e conferência física na biblioteca.
7. 📚 Classificação, catalogação definitiva, etiquetagem e entrada oficial no estoque.

</div>

---

## 🔄 Fluxo do Processo (BPMN)

A modelagem completa do fluxo de trabalho pode ser visualizada no diagrama **BPMN** abaixo:

<div align="center">

![Diagrama BPMN](./BPMN.jpeg)

</div>

---

## 🎯 Objetivos do Projeto

* 📚 **Organização:** Padronizar os fluxos de empréstimo, devolução e renovação.
* 📦 **Controle de Estoque:** Manter inventário e disponibilidade dos livros atualizados.
* 📝 **Rastreabilidade:** Registrar com precisão histórico de empréstimos e usuários.
* 📅 **Gestão de Prazos:** Monitorar datas de devolução de forma automatizada/controlada.
* 💰 **Gestão de Penalidades:** Controlar atrasos e cálculo de multas aplicáveis.
* 📥 **Expansão de Acervo:** Estruturar a entrada e catalogação de livros recebidos por doação.

---

## 📋 Documentação e Arquivos

Todos os artefatos desenvolvidos durante o projeto estão centralizados neste repositório:

* 📄 **[Escopo da Documentação](./Escopo.docx)**
* 🔄 **[Diagrama BPMN em Alta Resolução](./BPMN.jpeg)**

---

## 👥 Equipe de Desenvolvimento

| Integrante | Função / Contribuição |
| :--- | :--- |
| **Enzo Alexandrino** | Desenvolvedor / Representante |
| **Kauã Vinícius** | Desenvolvedor / Scrum Master |
| **João Pedro** | Desenvolvedor / Analista Técnico |
| **Matheus Duque** | Desenvolvedor / Analista Técnico |
| **Mauro Sena** | Desenvolvedor / Designer |

---

## 📌 Status do Projeto

<div align="center">

### 🚧 Em Desenvolvimento (Fase de Modelagem e Escopo) 🚧

</div>
