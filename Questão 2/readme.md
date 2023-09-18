# Sistema de E-commerce com API REST em Python

Este projeto consiste em uma implementação simplificada de um sistema de e-commerce com uma API REST em Python. O sistema inclui três classes principais: `Product`, `Cart`, e `Order`, e oferece endpoints de API para listar produtos, gerenciar o carrinho de compras e criar pedidos.

## Estrutura do Código

- `API_REST.py`: Este é o arquivo principal que inicia o aplicativo Flask e define os endpoints da API.

- `models`: Esta pasta contém as definições das classes principais:
    - `product.py`: Representa um produto com atributos como nome, preço e estoque.
    - `cart.py`: Modela um carrinho de compras que permite adicionar, remover produtos e calcular o total da compra.
    - `order.py`: Representa um pedido contendo informações sobre os produtos comprados e o total do pedido.

## Endpoints da API

- `/products`:
    - `GET`: Retorna a lista de produtos disponíveis.
    - `POST`: Adiciona um novo produto à lista de produtos disponíveis.

- `/cart`:
    - `GET`: Retorna o conteúdo atual do carrinho de compras.
    - `POST`: Adiciona um produto ao carrinho de compras.
    - `DELETE`: Remove um produto do carrinho de compras.

- `/order`:
    - `POST`: Cria um pedido com base no conteúdo do carrinho de compras.

## Por que Implementar Dessa Forma?

Este projeto foi implementado com o objetivo de demonstrar uma estrutura básica de um sistema de e-commerce com uma API REST. Algumas razões para essa abordagem incluem:

- **Modelagem de Classes Simples**: As classes `Product`, `Cart`, e `Order` são projetadas para serem simples e representar os conceitos fundamentais de um sistema de e-commerce.

- **API RESTful**: A implementação da API segue os princípios REST, o que a torna adequada para integrações com aplicativos web e móveis, bem como facilmente compreensível por desenvolvedores.

- **Uso do Flask**: O Flask é um framework web leve e amplamente adotado que facilita a criação de endpoints da API e a manipulação de solicitações HTTP.

- **Simplicidade para Fins de Demonstração**: Este projeto serve como uma demonstração simplificada. Em um ambiente de produção, você expandiria o sistema com recursos como autenticação de usuários, armazenamento de dados em um banco de dados e lógica de negócios mais complexa.

## Como Executar o Projeto

Para executar o projeto em sua máquina, siga as instruções fornecidas no arquivo `app.py` e certifique-se de ter o Flask instalado.

Lembre-se de que esta é uma implementação básica e pode ser aprimorada e adaptada de acordo com as necessidades específicas do seu sistema de e-commerce.
