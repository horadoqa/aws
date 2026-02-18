# 📢 O que é o SNS na AWS?

O **SNS (Simple Notification Service)** é um serviço de **mensageria baseado em publicação e assinatura (pub/sub)** da Amazon Web Services.

Em termos simples:

> 📣 SNS = serviço que envia mensagens para vários destinos ao mesmo tempo.

---

## 🎯 Para que serve?

Ele é usado para:

* Enviar notificações por e-mail
* Disparar SMS
* Acionar funções Lambda
* Enviar mensagens para filas (SQS)
* Integrar sistemas diferentes

---

## 🧠 Como funciona?

### 1️⃣ Você cria um **Topic**

O *topic* é como um canal de comunicação.

Exemplo:

```
pedido-criado
usuario-cadastrado
erro-sistema
```

### 2️⃣ Inscreve assinantes (Subscribers)

Podem ser:

* 📧 E-mail
* 📱 SMS
* 📨 Amazon SQS
* ⚡ AWS Lambda
* 🌐 Endpoint HTTP

### 3️⃣ Publica uma mensagem

O SNS envia automaticamente para todos os assinantes.

---

## 📦 Exemplo prático

Imagine um sistema de pedidos:

Quando um pedido é criado:

* Envia e-mail para o cliente
* Atualiza estoque
* Notifica time financeiro
* Dispara processamento em outra aplicação

Tudo isso com **uma única publicação no SNS**.

---

## 🆚 SNS vs SQS

| SNS                        | SQS                             |
| -------------------------- | ------------------------------- |
| Pub/Sub (1 → muitos)       | Fila (1 → 1 consumidor por vez) |
| Envia para vários destinos | Processamento assíncrono        |
| Notificações               | Processamento de tarefas        |

👉 Muitas arquiteturas usam **SNS + SQS juntos**.

---

## 🚀 Vantagens

✅ Escala automaticamente
✅ Alta disponibilidade
✅ Integração com vários serviços AWS
✅ Ideal para eventos

---

## 💰 Como funciona o custo?

Você paga por:

* Número de publicações
* Entregas de mensagens
* SMS enviados (se usar)

Existe camada gratuita mensal.

---

## 🔎 Resumo rápido

SNS é:

✔️ Serviço de notificações
✔️ Modelo publish/subscribe
✔️ Envia para múltiplos destinos
✔️ Muito usado em arquitetura orientada a eventos

---

Próximos passos:

* Como integrar SNS com SQS
* Diferença prática entre SNS e SQS
* Exemplo de código em Python
* Como enviar e-mail via SNS

