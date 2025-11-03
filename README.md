# Calculadora Simples em Python

Esta aplicacao e uma **calculadora grafica** construida com a biblioteca `tkinter` em Python.  
Ela permite realizar operacoes aritmeticas basicas (adicao, subtracao, multiplicacao e divisao), incluindo porcentagem e ponto decimal, em uma interface amigavel.

## Demonstracao

![Interface da calculadora](assets/preview.png)

> *A interface utiliza botoes coloridos e um visor digital para exibir os valores digitados e o resultado.*

## Funcionalidades

| Funcao             | Descricao                                                         |
|--------------------|-------------------------------------------------------------------|
| C (Limpar)         | Limpa a expressao atual no visor                                   |
| `+`, `-`, `*`, `/` | Executa as operacoes de soma, subtracao, multiplicacao e divisao    |
| `%`                | Calcula porcentagem                                                |
| `=`                | Avalia a expressao e mostra o resultado                            |
| Pontuacao (`.`)    | Permite inserir numeros decimais                                   |

## Requisitos

Para executar o projeto voce precisara de:

- Python 3.7 ou superior
- Biblioteca **tkinter** (ja incluida na instalacao padrao do Python)

## Como executar

1. **Clone este repositorio** em sua maquina:

   ```bash
   git clone https://github.com/carolyneoliverr/calculadora-simples-python.git
   cd calculadora-simples-python
   ```

2. **Execute o script** no terminal:

   ```bash
   python calculadora.py
   ```

Ao executar, uma janela sera aberta com a calculadora.  
Pressione os botoes para inserir valores e utilize `=` para calcular o resultado.  
Para apagar a expressao atual, clique em **C**.

## Estrutura do projeto

```
calculadora-simples-python/
├── calculadora.py        # Codigo principal da interface grafica
├── README.md             # Este arquivo, com informacoes e instrucoes
└── assets/
    └── preview.png       # Imagem de demonstracao da calculadora
```

## Contribuicao

Contribuicoes sao bem‑vindas! Se voce tiver ideias para melhorar a interface ou adicionar novas funcionalidades, siga estes passos:

1. Faca um *fork* deste repositorio.
2. Crie uma *branch* para a sua funcionalidade (`git checkout -b feature/novo‑recurso`).
3. *Commit* suas alteracoes (`git commit -m 'Adiciona novo recurso'`).
4. Faca um *push* para a branch (`git push origin feature/novo‑recurso`).
5. Abra um *Pull Request* descrevendo suas mudancas.

## Licenca

Este projeto e distribuido sob a licenca MIT.  
Sinta‑se livre para usa-lo e modifica-lo conforme necessario.
