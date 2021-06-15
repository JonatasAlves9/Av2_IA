import random

class Entradas():
    def __init__(self, input, weight):

        self.values = int(input)
        self.weight = dict(weight)


def generate_weight(qtd_weight):
    weight = {}
    for n_peso in range(qtd_weight):
        weight[f'w{n_peso}'] = round(random.random(), 2)
    return weight


def sum(input, weight):
    print(f'Sum of weight = {weight}')
    constante = 0
    soma_valor = 0
    for e in input:
        soma_valor += e['value'] * e['weight'][weight]
    return round(soma_valor + constante, 2)


def weight_randomic(valor):
    return f'w{str(random.randint(0, int(valor) - 1))}'


def print_lista_entradas(inputs):
    for item in inputs:
        print(f'|{item["name"]} value = {item["value"]} | weight = {item["weight"]} ')
    print('\n')

def generate_list(qtd_inputs, qtd_weigth_input):
    inputs = []
    for n_inputs in range(qtd_inputs):
        vars()[f'e{str(n_inputs)}'] = {
            "name": f' {str(n_inputs)}',
            "value": round(random.random(), 2),
            "weight": generate_weight(qtd_weigth_input)
        }
        inputs.append(vars()[f'e{str(n_inputs)}'])
    return inputs



def coust(value_obtained, value_ideal):
    return round(((value_obtained - value_ideal) ** 2), 2)


def run():
    qtd_input = 10
    qtd_weight = 10
                                
    print('\n--------------------Inicio----------------------\n')
    print(f'Quant of inputs: {qtd_input}\nQuant of weight inputs: {qtd_weight}\n')

    inputs = generate_list(qtd_input, qtd_weight)
    print_lista_entradas(inputs)
    somatorios = sum(inputs, weight_randomic(qtd_weight))
    print(f'Function of ativated: {somatorios}')
    custos = coust(somatorios, 1)
    print(f'Funcion of coust: {custos}')
    print('\n--------------------Fim----------------------\n')


if __name__ == '__main__':
    run()







