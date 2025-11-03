# Calculadora Simples em Python

Esta aplicacao e uma calculadora grafica desenvolvida em Python usando a biblioteca `tkinter`. Ela permite realizar operacoes aritmeticas basicas — adicao, subtracao, multiplicacao e divisao — de forma intuitiva.

## Como a calculadora funciona

A interface consiste em um visor numerico e um conjunto de botoes que representam os digitos e operadores. O fluxo basico de funcionamento e:

1. Cada botao numerico (`0` a `9`) adiciona o respectivo digito a expressao exibida.
2. Os botoes de operacao (`+`, `-`, `*`, `/` e `%`) inserem o operador na expressao.
3. O botao `.` permite inserir casas decimais.
4. O botao `=` avalia a expressao atual e mostra o resultado no visor.
5. O botao `C` limpa a expressao, permitindo iniciar um novo calculo.

O codigo mantem a expressao em uma variavel do tipo `StringVar`. Quando o botao `=` e pressionado, a expressao e avaliada usando a funcao `eval()`, e o resultado e exibido. Tratamentos de erro podem ser adicionados para lidar com divisoes por zero ou entradas invalidas.

## Passo a passo para executar o projeto

1. **Obtenha o codigo:** clone este repositorio para a sua maquina ou faca o download dos arquivos.

   ```bash
   git clone https://github.com/carolyneoliverr/calculadora-simples-python.git
   cd calculadora-simples-python
   ```

2. **Certifique-se de ter o Python instalado:** a calculadora requer Python 3.7 ou superior. A biblioteca `tkinter` ja vem incluida nas distribuicoes padrao do Python.

3. **Execute o script:** no terminal, rode o arquivo Python correspondente a calculadora.

   ```bash
   # Versao original
   python calculadora.py

   # Versao reorganizada com codigo modular
   python calculadora_organizada.py
   ```

   Uma janela aparecera com a calculadora. Use o mouse para clicar nos botoes e realizar as operacoes desejadas.

## Estrutura do repositorio

```
calculadora-simples-python/
├── calculadora.py            # Codigo original da calculadora
├── calculadora_organizada.py # Versao reorganizada e modular
├── README.md                 # Este arquivo
```

## Contribuicao

Contribuicoes sao bem‑vindas! Se voce tiver sugestoes de melhorias ou novas funcionalidades:

1. Crie um *fork* deste repositorio.
2. Crie uma branch para a sua feature: `git checkout -b feature/novo-recurso`.
3. Faca commit das suas alteracoes: `git commit -m 'Adiciona novo recurso'`.
4. Envie a branch para o seu repositorio: `git push origin feature/novo-recurso`.
5. Abra um *pull request* descrevendo as mudancas propostas.
