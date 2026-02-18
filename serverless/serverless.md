# ☁️ O que é **Serverless** na AWS?

O termo **serverless** na Amazon Web Services refere-se a **uma forma de construir aplicações sem precisar gerenciar servidores diretamente**.

Em termos simples:

> 🚫💻 Serverless ≠ sem servidor fisicamente, mas você **não se preocupa com a infraestrutura**, apenas com o código e eventos.

---

## 🎯 Para que serve?

O Serverless é ideal para:

* Criar funções ou microsserviços que respondem a eventos
* Automatizar processos sem se preocupar com servidores
* Construir APIs, backends, pipelines de processamento
* Escalar automaticamente conforme a demanda

---

## 🏗️ Como funciona?

1. Você escreve código em serviços serverless, como:

   * **AWS Lambda** (funções que executam sob demanda)
   * **API Gateway** (expor APIs)
   * **DynamoDB** (banco NoSQL gerenciado)
   * **S3** (armazenamento de arquivos)
   * **SNS/SQS** (mensageria e filas)

2. Define o **evento que dispara o código**:

   * Upload de arquivo no S3
   * Requisição HTTP para API Gateway
   * Mensagem em fila SQS
   * Cron jobs com EventBridge

3. AWS executa o código, escala conforme necessário, e você paga **só pelo uso real**.

---

## 🔹 Principais vantagens

* ✅ Sem gerenciar servidores
* ✅ Escala automática
* ✅ Pago só pelo que usa
* ✅ Mais ágil para desenvolvimento e deploy
* ✅ Fácil integração com outros serviços AWS

---

## 🆚 Serverless vs Tradicional (EC2)

| Característica            | EC2 / Servidor Tradicional | Serverless (Lambda)                      |
| ------------------------- | -------------------------- | ---------------------------------------- |
| Gerenciamento de servidor | Você cuida                 | AWS cuida                                |
| Escalabilidade            | Manual ou Auto Scaling     | Automática                               |
| Cobrança                  | Fixa por hora              | Pelo tempo de execução e recursos usados |
| Tempo de execução         | Sempre ligado              | Só quando acionado                       |

---

## 📦 Exemplo prático

Imagine um site que envia e-mails quando um usuário se cadastra:

1. Usuário envia formulário → evento
2. **Lambda** executa código Python para enviar e-mail
3. **SNS** pode notificar outros sistemas
4. Tudo isso acontece sem nenhuma instância EC2 rodando 24h

---

## 🔎 Resumo rápido

Serverless na AWS é:

✔️ Executar código sem se preocupar com servidores
✔️ Escalar automaticamente
✔️ Pagar só pelo que é usado
✔️ Baseado em eventos (HTTP, S3, SQS, cron)

---

Criar um **exemplo prático de arquitetura serverless na AWS**, mostrando Lambda + API Gateway + DynamoDB + S3 funcionando juntos.


