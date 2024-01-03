Um banco oferece três tipos de contas:
 conta corrente comum;
 conta corrente com limite;
 conta poupança.
Para esses três tipos é necessário armazenar o número da conta, o nome do
correntista e o saldo. Para a conta poupança deve-se guardar o dia do aniversário da
conta (quando são creditados os juros). Já para a conta com limite é preciso guardar o
valor do limite.
As contas também armazenam uma lista de transações. Uma transação é definida por
uma data, valor da transação e descrição. Se o valor for negativo, a transação é
considerada um débito (crédito caso contrário).
As operações possíveis são: depósito, retirada e impressão de extrato. A operação de
depósito é igual nos três tipos de conta. A retirada só é diferente na conta com limite,
pois esta admite que o saldo fique negativo até o limite estabelecido. O extrato, por
sua vez, é diferente para os três tipos de conta:
 na conta comum exibe o número da conta, nome do cliente, transações e o
saldo;
 na conta limite imprime também o valor do limite;
 na conta poupança imprime também o dia do aniversário.
No sentido de implementar corretamente essas operações, deve-se definir a classe
abstrata Conta, a qual deve conter o método abstrato ImprimirExtrato. Para a retirada,
deve-se utilizar o conceito de sobrescrita de métodos.
Implemente a hierarquia de classes das contas explorando polimorfismo. Em seguida,
escreva um código de teste que:
 Cria três instâncias, uma para cada tipo de conta;
 Realiza ao menos 3 operações, as quais devem incluir depósitos e retiradas;
 Coloca as instâncias numa lista e processa a lista chamando o método que
realiza a impressão de extrato.
