# Calculadora Simples em Python

Calculadora gráfica feita em Python com a biblioteca `tkinter`. Faz as quatro operações básicas (adição, subtração, multiplicação e divisão) e porcentagem.

## Como funciona

A interface tem um visor e um teclado com dígitos e operadores:

1. Os botões numéricos (`0` a `9`) acrescentam o dígito à expressão no visor.
2. Os botões de operação (`+`, `-`, `*`, `/` e `%`) inserem o operador.
3. O botão `.` insere casas decimais.
4. O botão `=` calcula a expressão e mostra o resultado.
5. O botão `C` limpa o visor para um novo cálculo.

A expressão fica guardada em uma variável `StringVar`. Ao pressionar `=`, ela é avaliada com `eval()` e o resultado aparece no visor.

## Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/carolyneoliverr/calculadora-simples-python.git
   cd calculadora-simples-python
   ```

2. Tenha o Python 3.7 ou mais novo instalado. O `tkinter` já vem nas distribuições padrão do Python.

3. Rode uma das versões:

   ```bash
   python calculadora.py             # versão original
   python calculadora_organizada.py  # versão reorganizada e modular
   ```

## Testes

Com o ambiente Conda do projeto (`environment.yml`, com Python 3.10, pytest e flake8):

```bash
conda env create -f environment.yml
conda activate calculadora-env
pytest
```

## Estrutura

```text
calculadora-simples-python/
├── calculadora.py             # versão original
├── calculadora_organizada.py  # versão reorganizada e modular
├── tests/
│   └── test_calculadora.py    # testes automatizados
├── environment.yml            # ambiente Conda
└── README.md
```

## Contribuição

Sugestões são bem-vindas:

1. Faça um *fork* do repositório.
2. Crie uma branch: `git checkout -b feature/novo-recurso`.
3. Faça o commit: `git commit -m "Adiciona novo recurso"`.
4. Envie a branch: `git push origin feature/novo-recurso`.
5. Abra um *pull request* descrevendo a mudança.
