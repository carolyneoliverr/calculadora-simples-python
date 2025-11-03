"""
Aplicação de calculadora simples usando tkinter.

Esta versão organiza o código em uma classe para facilitar a manutenção e
clarear a lógica.  Ela oferece os mesmos recursos da versão original —
operações aritméticas básicas, porcentagem e ponto decimal — em uma
interface gráfica amigável.
"""

import tkinter as tk
from tkinter import ttk


class Calculadora(tk.Tk):
    """Classe principal da calculadora."""

    def __init__(self) -> None:
        super().__init__()
        # Configurações da janela
        self.title("Calculadora")
        self.geometry("235x310")
        self.configure(bg="#3b3b3b")
        # Estado interno
        self.expressao: str = ""
        # Variável de texto para o visor
        self.valor_texto = tk.StringVar()
        # Construção da interface
        self._criar_widgets()

    def _criar_widgets(self) -> None:
        """Cria os widgets da interface gráfica."""
        # Frame do visor
        frame_tela = tk.Frame(self, width=235, height=50, bg="#38576b")
        frame_tela.grid(row=0, column=0)
        # Rótulo do visor
        visor = tk.Label(
            frame_tela,
            textvariable=self.valor_texto,
            width=16,
            height=2,
            padx=7,
            relief=tk.FLAT,
            anchor="e",
            justify=tk.RIGHT,
            font=("Ivy", 18),
            bg="#38576b",
            fg="#feffff",
        )
        visor.place(x=0, y=0)

        # Frame dos botões
        frame_corpo = tk.Frame(self, width=235, height=268)
        frame_corpo.grid(row=1, column=0)

        # Definição dos botões (label, largura, comando)
        botoes = [
            ["C", 11, self.limpar],
            ["%", 5, lambda: self.adicionar_valor("%")],
            ["/", 5, lambda: self.adicionar_valor("/")],
            ["7", 5, lambda: self.adicionar_valor("7")],
            ["8", 5, lambda: self.adicionar_valor("8")],
            ["9", 5, lambda: self.adicionar_valor("9")],
            ["*", 5, lambda: self.adicionar_valor("*")],
            ["4", 5, lambda: self.adicionar_valor("4")],
            ["5", 5, lambda: self.adicionar_valor("5")],
            ["6", 5, lambda: self.adicionar_valor("6")],
            ["-", 5, lambda: self.adicionar_valor("-")],
            ["1", 5, lambda: self.adicionar_valor("1")],
            ["2", 5, lambda: self.adicionar_valor("2")],
            ["3", 5, lambda: self.adicionar_valor("3")],
            ["+", 5, lambda: self.adicionar_valor("+")],
            ["0", 11, lambda: self.adicionar_valor("0")],
            [".", 5, lambda: self.adicionar_valor(".")],
            ["=", 5, self.calcular],
        ]
        # Posições iniciais
        x_pad = 0
        y_pad = 0
        # Cores dos botões
        cor_botao = "#dbcccc"
        cor_operador = "#44d0e3"

        for idx, (texto, largura, comando) in enumerate(botoes):
            # Seleciona a cor com base no tipo de botão
            cor = cor_operador if texto in {"/", "*", "-", "+", "="} else cor_botao
            # Botão limpar tem cor de botao normal
            if texto == "C":
                cor = cor_botao
            btn = tk.Button(
                frame_corpo,
                text=texto,
                width=largura,
                height=2,
                bg=cor,
                font=("Ivy", 13, "bold"),
                relief=tk.RAISED,
                overrelief=tk.RIDGE,
                command=comando,
            )
            btn.place(x=x_pad, y=y_pad)
            # Atualiza posição X
            if largura == 11:
                # Botão de largura dupla ocupa duas colunas
                x_pad += 118
            else:
                x_pad += 59
            # Quebra de linha após 4 colunas (limpar, %, /, e três números/operador)
            if (idx + 1) % 3 == 0 and largura != 11:
                x_pad = 0
                y_pad += 52
            elif largura == 11:
                # Se botão ocupa mais espaço, quebra a linha
                x_pad = 118

    def adicionar_valor(self, valor: str) -> None:
        """Adiciona um valor (número ou operador) à expressão."""
        self.expressao += valor
        self.valor_texto.set(self.expressao)

    def limpar(self) -> None:
        """Limpa a expressão atual no visor."""
        self.expressao = ""
        self.valor_texto.set("")

    def calcular(self) -> None:
        """Avalia a expressão e exibe o resultado."""
        try:
            # Avalia a expressão. Utilize eval com cuidado.
            resultado = str(eval(self.expressao))
            self.valor_texto.set(resultado)
            self.expressao = resultado  # Permite continuar calculando
        except ZeroDivisionError:
            self.valor_texto.set("Erro: divisão por zero")
            self.expressao = ""
        except Exception:
            # Captura outros erros (ex.: expressão inválida)
            self.valor_texto.set("Erro")
            self.expressao = ""


if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()