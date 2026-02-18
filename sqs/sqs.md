# 📬 O que é o SQS na AWS?

O **SQS (Simple Queue Service)** é um serviço de **fila de mensagens** da Amazon Web Services.

Em termos simples:

> 📩 SQS = uma fila que guarda mensagens até outra aplicação processá-las.

---

## 🎯 Para que serve?

Ele é usado para **desacoplar sistemas**.

Exemplo:

1. Um sistema envia uma mensagem
2. A mensagem fica na fila
3. Outro sistema processa depois

Isso evita que um sistema dependa diretamente do outro.

---

## 🧠 Exemplo prático

Imagine um e-commerce:

* Cliente faz pedido
* Sistema envia mensagem para fila
* Serviço separado processa:

  * Pagamento
  * Envio de e-mail
  * Atualização de estoque

Se o processamento falhar, a mensagem continua na fila.

---

## 🏗️ Como funciona?

1. **Producer (Produtor)** envia mensagem para a fila
2. O SQS armazena
3. **Consumer (Consumidor)** lê e processa
4. Mensagem é removida da fila

---

## 📦 Tipos de fila

### 🔹 Standard

* Alta performance
* Pode entregar mensagem mais de uma vez
* Ordem não garantida

### 🔹 FIFO (First In, First Out)

* Ordem garantida
* Sem duplicação
* Um pouco mais lento

---

## 🔐 Recursos importantes

* Visibilidade temporária (Visibility Timeout)
* Dead Letter Queue (mensagens com erro)
* Escala automática
* Integração com Lambda

---

## 🆚 SQS vs Comunicação Direta

| Sem SQS                       | Com SQS                |
| ----------------------------- | ---------------------- |
| Sistemas dependem um do outro | Sistemas independentes |
| Se um falha, outro quebra     | Fila segura a mensagem |
| Difícil escalar               | Fácil escalar          |

---

## 💰 Como funciona o custo?

Você paga por:

* Número de requisições
* Volume de mensagens

Existe camada gratuita mensal.

---

## 📦 Exemplo real com Lambda

Você pode configurar:

* Mensagem chega no SQS
* O AWS Lambda processa automaticamente

Muito usado para processamento assíncrono.

---

## 🔎 Resumo rápido

SQS é:

✔️ Fila de mensagens
✔️ Comunicação assíncrona
✔️ Sistema mais resiliente
✔️ Ideal para microsserviços

---

Próximos passos:

* O que é Visibility Timeout
* O que é Dead Letter Queue
* Como integrar SQS com Lambda
* Exemplo de código em Python
