Um projeto desenvolvido com a intenção de praticar a manipulação, validação e armazenamento de dados. O sistema permite o cadastro de veículos, usuários e aluguéis, além de gerenciar as informações relacionadas às locações.

## OBJETIVO:

Desenvolvi este projeto com o objetivo de praticar o conceito de manipulação e inserção de dados em um banco de dados, aprender a utliizar a biblioteca SQLAlchemy e aprimorar a minha lógica de programação.
## FUNCIONALIDADES:

O sistema permite a manipulação e inserção de dados em três tabelas, cada uma com suas responsabilidades e regras específicas, por meio de operações CRUD onde é possível realizar as principais operações de cadastro, consulta, atualização e exclusão dos dados.

### Usuários

- Cadastro de usuários;
- Consulta de usuários;
- Atualização de dados dos usuários;
- Exclusão de usuários;
- Controle do status do usuário;
- Validação de nome e e-mail;
- Armazenamento da senha utilizando hash.

### Veículos

- Cadastro de veículos;
- Consulta de veículos;
- Busca por ID, modelo, placa e status;
- Atualização de dados dos veículos;
- Exclusão de veículos;
- Controle da disponibilidade dos veículos;
- Validação da placa;
- Cadastro do tipo de veículo.

### Aluguéis

- Cadastro de aluguéis;
- Consulta de aluguéis;
- Listagem de aluguéis ativos e devolvidos;
- Controle da disponibilidade dos veículos;
- Registro da data de devolução;
- Cálculo do valor total do aluguel;
- Cálculo de multa por atraso.

## ESTRUTURA DO BANCO DE DADOS:

### Usuários

| Coluna  | Descrição                                  |
| ------- | ------------------------------------------ |
| `id`    | Identificador único de usuário.            |
| `nome`  | Nome do usuário.                           |
| `email` | E-mail do usuário.                         |
| `senha` | Hash da senha do usuário.                  |
| `ativo` | Indica se o usuário está ativo no sistema. |
### Veículos:
| Coluna         | Descrição                                       |
| -------------- | ----------------------------------------------- |
| `id`           | Identificador único de veículo.                 |
| `modelo`       | Modelo do veículo.                              |
| `placa`        | Placa única de identificação do veículo.        |
| `tipo`         | Tipo do veículo (Carro, Moto, Caminhão)         |
| `valor_diario` | Valor diário individual do veículo.             |
| `status`       | Indica se o veículo está alugado ou disponível. |
### Aluguel:

| Coluna           | Descrição                                                                           |
| ---------------- | ----------------------------------------------------------------------------------- |
| `id`             | Identificador único do aluguel.                                                     |
| `id_usuario`     | Chave estrangeira que referencia o usuário responsável pelo aluguel.                |
| `id_veiculo`     | Chave estrangeira que referencia o veículo alugado.                                 |
| `data_inicio`    | Data de início do aluguel.                                                          |
| `data_fim`       | Data prevista para a devolução do veículo.                                          |
| `data_devolucao` | Data em que o veículo foi efetivamente devolvido.                                   |
| `valor_diario`   | Valor da diária utilizado no aluguel.                                               |
| `valor_total`    | Valor total calculado com base no valor da diária e na quantidade de dias alugados. |
| `multa`          | Valor da multa calculada com base nos dias de atraso.                               |

## ESTRUTURA DO PROJETO


Locadora de Veículos/
│
├── sistema/
│   ├── classes.py
│   ├── criar_banco.py
│   ├── crud_aluguel.py
│   ├── crud_usuario.py
│   ├── crud_veiculo.py
│   ├── database.py
│   ├── modelos.py
│   ├── utilidades.py
│   ├── validar_database.py
│   └── main.py
│
├── .gitignore
├── LICENSE
└── README.md


### Principais arquivos

- `main.py` — Arquivo responsável pelo menu principal e pela execução do sistema.
- `database.py` — Responsável pela configuração do banco de dados e pela sessão utilizada pelo SQLAlchemy.
- `criar_banco.py` — Responsável pela criação das tabelas do banco de dados.
- `modelos.py` — Contém os modelos das tabelas `Usuario`, `Veiculo` e `Aluguel`.
- `classes.py` — Contém as classes utilizadas para o cálculo do valor dos aluguéis de acordo com o tipo de veículo.
- `crud_usuario.py` — Contém as operações relacionadas aos usuários.
- `crud_veiculo.py` — Contém as operações relacionadas aos veículos.
- `crud_aluguel.py` — Contém as operações relacionadas aos aluguéis.
- `validar_database.py` — Contém funções responsáveis pela validação e leitura dos dados.
- `utilidades.py` — Contém funções auxiliares utilizadas pelo sistema.


## REGRAS DE NEGÓCIO

### Disponibilidade dos veículos

Um veículo disponível pode ser alugado.
Ao realizar um aluguel, o status do veículo é alterado para indicar que ele está alugado.
Após a devolução, o status do veículo volta a indicar que está disponível.

### Cálculo do aluguel

O valor do aluguel é calculado de acordo com o tipo do veículo.
- **Carro:** valor da diária multiplicado pela quantidade de dias.
- **Moto:** possui desconto de 10% quando o período do aluguel é igual ou superior a 7 dias.
- **Caminhão:** possui sua própria regra de cálculo definida pela classe correspondente.

### Devolução e multa

Ao realizar a devolução, o sistema registra a data em que o veículo foi efetivamente devolvido.
Caso a devolução ocorra após a data prevista, os dias de atraso são calculados e uma multa é aplicada com base no valor da diária.
Caso não exista atraso, não é aplicada multa.


## CONCEITOS APLICADOS

Durante o desenvolvimento do projeto, foram praticados conceitos como:

- Programação Orientada a Objetos (POO);
- Classes e objetos;
- Herança;
- Polimorfismo;
- Classes abstratas;
- Encapsulamento;
- Operações CRUD;
- Validação de dados;
- Chaves primárias e estrangeiras;
- ORM (Object-Relational Mapping);
- Manipulação de banco de dados;
- Hash de senhas.

## POLIMORFISMO

O projeto utiliza polimorfismo para definir diferentes formas de cálculo do valor do aluguel de acordo com o tipo do veículo.

A classe abstrata `Veículo_pagamento` define o método responsável pelo cálculo do valor total do aluguel, que é implementado pelas classes:

- `Carro`;
- `Moto`;
- `Caminhao`.

Dessa forma, cada tipo de veículo pode possuir sua própria regra para calcular o valor do aluguel.

## TECNOLOGIAS UTILIZADAS

- **Python 3.14:** linguagem de programação utilizada no projeto, responsável pela lógica e pelas funcionalidades do sistema.
- **SQLAlchemy:** biblioteca Python responsável pela integração entre o código Python e o banco de dados SQLite, sendo fundamental para o funcionamento das operações CRUD.
- **SQLite:** sistema de gerenciamento de banco de dados utilizado para armazenar os dados do sistema de forma local e organizada.
- **Werkzeug:** biblioteca Python utilizada para gerar o hash das senhas antes de armazená-las no banco de dados, contribuindo para a segurança dos dados dos usuários.


## COMO EXECUTAR

### 1. Clone o repositório

git clone URL_DO_REPOSITORIO

### 2. Acesse a pasta do projeto

cd "Locadora de Veículos"

### 3. Instale as dependências

pip install sqlalchemy werkzeug

### 4. Crie o banco de dados

python sistema/criar_banco.py

### 5. Execute o sistema

python sistema/main.py


## BANCO DE DADOS

O projeto utiliza o SQLite para armazenar os dados localmente.

O SQLAlchemy é utilizado como ORM, realizando a comunicação entre as classes Python e as tabelas do banco de dados.

## AUTOR

Desenvolvido por **Gabriel Müller**.

Projeto desenvolvido com fins de estudo e prática de programação, banco de dados, SQLAlchemy e Programação Orientada a Objetos.