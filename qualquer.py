# emprestimo
# escadinha (escolhendo o material)
# função q serve para embaralhar uma lista
# função que recebe uma lista de meninos e uma lista de meninas. Ela deve imprimir na tela TODOS os parzinhos possíveis para uma quadrilha
# em uma quadrilha tradicional, pode haver parzinhos de qualquer natureza. mostre todos os parzinhos independente de menino ou menina.
# função que recebe uma lista e retornar True se Todos os elementos da lista forem Iguais, False se houver ao menos UM diferente.


# Exercício do Emprestimo

# REGRAS para aceita o empréstimo:
# //    - Entre 22 e 55 anos;
# //    - Valor a partir de 1000 reais;
# //    - Valor não pode ultrapassar 15x o que ele recebe

# //    RESPONDER: ACEITO OU NÃO ACEITO

# //    EXTRA:
# //    - Perguntar também a quantidade de parcelas (3 a 20 vezes) e calcular juros de 8% ao mês (COMPOSTO)
# //    RESPONDER VALOR TOTAL DO EMPRESTIMO E VALOR Da PARCELA.


# print("Qual a sua idade")
# idade = input()

# print("Qual o valor emprestimo")
# valor_emprestimo = input()

# print("Qual o salário")
# salario = input()

# print("Quantas parcelas")
# qtd_parcelas = input()

def emprestimo (idade, valor_emprestimo, salario, qtd_parcelas):
    if idade < 22 or idade > 55 or valor_emprestimo < 1000 or valor_emprestimo > salario * 15 or qtd_parcelas < 3 or qtd_parcelas > 20:
        print('Não será aceito')

    else:
        print('Será Aceito')
        montante
        montante = valor_emprestimo * (1 + 0.08) ** qtd_parcelas
        montante =  

emprestimo (22, 1100, 5000, 4)


# et montante;
#         montante = valorEmprestimo * (1 + 0.08) ** qtdParcelas;
#         montante = montante.toFixed(2);
#         let parcela = montante/qtdParcelas;
#         parcela = parcela.toFixed(2);
#         console.log(`O valor total do empréstimo é de ${montante} e o valor da parcela é de ${parcela}`);