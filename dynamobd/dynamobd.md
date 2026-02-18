# 🗄️ O que é o DynamoDB na AWS?

O **DynamoDB** é um serviço de **banco de dados NoSQL totalmente gerenciado** da Amazon Web Services.

Em termos simples:

> 🗂️ DynamoDB = banco de dados rápido, escalável e sem esquema fixo, na nuvem.

Ele é **diferente de um banco relacional** (como RDS), pois usa **tabelas e itens**, mas não exige relacionamentos complexos entre tabelas.

---

## 🎯 Para que serve?

DynamoDB é ideal para aplicações que precisam de:

* Alta performance e baixa latência
* Escalabilidade automática
* Armazenar grandes volumes de dados semi-estruturados
* Apps móveis, IoT, jogos e APIs em tempo real

---

## 🏗️ Como funciona?

1. **Tabelas** → estrutura principal do banco
2. **Itens** → linhas (cada item é único)
3. **Atributos** → colunas, mas você pode ter itens com atributos diferentes
4. **Chave primária** → define unicidade do item
5. **Índices secundários** → permitem consultas rápidas por outros atributos

Exemplo de tabela de usuários:

| user_id (PK) | nome  | email                                     | idade |
| ------------ | ----- | ----------------------------------------- | ----- |
| 1            | Pedro | [pedro@email.com](mailto:pedro@email.com) | 25    |
| 2            | Ana   | [ana@email.com](mailto:ana@email.com)     | 30    |

---

## 🔹 Diferença entre RDS e DynamoDB

| Característica | RDS                        | DynamoDB                              |
| -------------- | -------------------------- | ------------------------------------- |
| Tipo de banco  | Relacional                 | NoSQL (Key-Value / Document)          |
| Esquema        | Fixo                       | Flexível                              |
| Escalabilidade | Vertical (mais CPU/RAM)    | Horizontal (mais tabelas / partições) |
| Latência       | Normal                     | Muito baixa, microssegundos           |
| Uso            | ERP, apps web tradicionais | Apps em tempo real, jogos, IoT        |

---

## 🚀 Vantagens

✅ Totalmente gerenciado
✅ Escala automática sem downtime
✅ Altíssima performance
✅ Integrado com Lambda, API Gateway, S3, CloudWatch

---

## 💰 Como funciona o custo?

Você paga por:

* Capacidade de leitura e escrita (ou modo on-demand)
* Armazenamento de dados
* Índices secundários

---

## 📦 Exemplo prático

Se você tem uma API que registra pedidos:

1. Cria tabela `Pedidos`
2. Define chave primária `pedido_id`
3. Cada pedido é um item com atributos: `usuario_id`, `valor`, `status`
4. Lambda ou EC2 escreve/consulta dados direto na tabela
5. Escala automaticamente conforme aumenta o número de pedidos

---

## 🔎 Resumo rápido

DynamoDB é:

✔️ Banco NoSQL totalmente gerenciado
✔️ Escalável e rápido
✔️ Ideal para apps em tempo real
✔️ Flexível, sem esquema fixo

---

Próximos passos:

* Como criar uma tabela DynamoDB passo a passo
* Exemplo de inserir e consultar dados com Python
* Diferença entre modos **provisioned** e **on-demand**
* Como integrar Lambda + DynamoDB

