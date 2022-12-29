
<h1 align="center">
    <img alt="Decorators - Adicionando ou Removendo Funcionalidades de Funções já prontas" title="#DECORATORS" src="./assets/banner.jpg" />
</h1>

<h4 align="center"> 
	Decorators - Adicionando ou Removendo Funcionalidades de Funções já prontas 🚀
</h4>

<p align="center">
  	
  <a href="https://www.linkedin.com/in/emerson-rafael/">
    <img alt="Siga no Linkedin" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
  </a>
	
  
  <a href="https://github.com/emersonrafaels/python_codes_general/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/emersonrafaels/python_codes_general">
  </a>

  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
   <a href="https://github.com/emersonrafaels/python_codes_general/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/emersonrafaels/python_codes_general?style=social">
  </a>
</p>


## 💻 Sobre Decorators

O conceito de decorator preve uma maneira de alterar uma função, sem necessariamente pre-
cisar alterá-la.

Funções são trechos de códigos que recebem parâmetros, realizam operações e podem retornar
algum valor ou conjunto de valores. As **funções podem ser utilizadas como argumentos ou
retornos de funções**, ou seja, são conhecidas como **objetos de primeira ordem**.

- Nested functions

Nested functions (funções aninhadas) são funções que estão dentro de funções, e nesse caso, estamos apenas no escopo da função 'de fora'.

```
def party():
    print("Estou de fora =[")

    def start_party():
        return "Estamos dentro! Uhullll!"

    def finish_party():
        return "A festa acabou! =[")

    print(start_party())
    print(finish_party())
```

Dessa forma, caso você chame a função party(), sua saída será:

```
Estou de fora =[
Estamos dentro! Uhullll!
A festa acabou! =[
```

- Os decoradores

A adição de decoradores se deu através da Pep 318 (Python Enhancement Proposal - Proposta de melhoria na linguagem Python), que propôs a adição dos decorators ao Python.

A primeira função para entender os decorators é:

```
def decorator(funcao):

    def wrapper():
    
        print ("Estou antes da execução da função passada como argumento")
        
        funcao()
        
        print ("Estou depois da execução da função passada como argumento")

    return wrapper
```

## 🛠  Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python]

## 🚀 Como executar o projeto

1. **Instalando**: pip install -r requirements.txt

## ➊ Pré-requisitos

- Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas (O download pode ser realizado pela própria página do Python ou Anaconda):
[Python](https://www.anaconda.com/products/individual).

- Realizar a instalação do requirements, obtendo todas as bibliotecas necessárias para execução do projeto.

## 📝 Licença

Este projeto está sob a licença MIT.

Feito com ❤️ por **Emerson Rafael** 👋🏽 [Entre em contato!](https://www.linkedin.com/in/emerson-rafael/)

[Python]: https://www.python.org/downloads/