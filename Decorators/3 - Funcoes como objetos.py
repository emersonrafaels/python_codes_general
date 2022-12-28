def soma(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def calculadora(op, x, y):

    # INICIANDO UM DICT CONTENDO AS OPERAÇÕES
    # COMO FUNÇÕES SÃO OBJETOS, ELAS PODEM SER ARMAZENADAS
    # EM VARIÁVEIS, TAL COMO NAS CHAVES DO DICT ABAIXO
    operações = {
        '+': soma,
        '-': sub,
        '*': mul,
        '/': div
    }

    if op in operações.keys():
        return operações[op](x, y)

    else:
        return None


if __name__ == '__main__':

    result = calculadora("+", 1, 2)

    print(result)
