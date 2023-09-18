## Desenvolvedor Odoo - Gustavo Kertisz Maciel


## Este repositório contem as soluções da prova para Desenvolvedor Odoo

## Questão 1 - Sequencia Fibonacci
### Implemente uma função em Python chamada `fibonacci(n)` que retorna o n-ésimo termo da sequência de Fibonacci.

## Questão 2 - Modelagem e Arquitetura de Sistemas Web com API REST

### Você está trabalhando em um sistema de e-commerce. Modele classes em Python que representem os seguintes elementos: `Produto`, `Carrinho`, e `Pedido`.

 - `A)`  `Produto`: Deve ter atributos como `nome`, `preço` e `estoque`.
 - `B)`  `Pedido`:  Deve conter informações sobre os produtos comprados e o total do pedido.

 - `C)` `Carrinho`: Deve ser capaz de adicionar e remover produtos, calcular o total e
finalizar a compra.

### Implemente também uma API REST para fornecer acesso a esses recursos.

## Questão 3 - Módulo de Contabilidade do Odoo

### Suponha que você esteja desenvolvendo um sistema de contabilidade para uma empresa com operações internacionais. A empresa lida com várias moedas e precisa de uma funcionalidade para converter automaticamente transações em diferentes moedas para a moeda base da empresa.

 - `A)` Crie um novo modelo chamado `account.foreign.exchange.rate` que permita o registro de taxas de câmbio entre diferentes moedas. O modelo deve conter os
    seguintes campos:
    - a) `date` (Date): Data da taxa de câmbio.
    - b) `currency_from_id` (Many2one): Moeda de origem.
    - c) `currency_to_id` (Many2one): Moeda de destino.
    - d) `exchange_rate` (Float): Taxa de câmbio.
- `B)` Modifique o modelo `account.move` para incluir um campo `currency_id` que
represente a moeda em que a transação está sendo registrada. Certifique-se de que
este campo esteja relacionado com o modelo `res.currency`.

- `C)` Implemente uma função no Odoo que, ao criar um lançamento contábil, verifique se
a moeda da transação é diferente da moeda base da empresa. Em caso afirmativo,
a função deve converter o valor da transação para a moeda base usando a taxa de
câmbio correspondente.

### Observações:
### - Considere que os modelos `res.currency` e `account.move` já estão definidos no sistema.

## Questão 4 - Integração com Sistemas Externos no Módulo de Contas a Receber do Odoo

### Suponha que você esteja trabalhando em um projeto de implementação do módulo de contas a receber do Odoo para uma empresa que precisa integrar dados de faturas com seu sistema de gestão financeira externo. O sistema externo utiliza um serviço RESTful para receber e registrar informações de faturas.

- `A)` Crie um módulo personalizado no Odoo chamado `account_invoice_integration` que
permita a integração de faturas com o sistema financeiro externo. Este módulo deve
incluir um modelo chamado `account.invoice.integration` com os seguintes campos:
    - a) `invoice_id` (Many2one): Relacionamento com a fatura no Odoo.
    - b) `external_system_id` (Char): ID da fatura no sistema externo
    - c) `status` (Selection): Status da integração (pendente, sucesso, erro).
    - d) `response_message` (Text): Mensagem de resposta do sistema externo

- `B)` Implemente uma função no módulo personalizado que, quando uma fatura é
validada e confirmada no Odoo, envie automaticamente os dados da fatura para o
sistema externo via API REST. A função deve atualizar o registro no modelo `account.invoice.integration` com o status da integração e a mensagem de resposta
do sistema externo.

- `C)` Simule a integração de uma fatura de exemplo no sistema Odoo. Crie uma fatura no
Odoo e confirme-a. Certifique-se de que os dados da fatura sejam enviados
corretamente ao sistema externo e que o registro no modelo
`account.invoice.integration` seja atualizado com o status e a mensagem de
resposta.

### Observações:
### Considere que o sistema externo já possui uma API RESTful configurada para receber informações de faturas e retornar mensagens de resposta.