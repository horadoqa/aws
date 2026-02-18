# 🌱 O que é o AWS Elastic Beanstalk?

O **AWS Elastic Beanstalk** é um serviço da Amazon Web Services que facilita o **deploy e gerenciamento de aplicações na nuvem**.

Em termos simples:

> 🚀 Beanstalk = você envia seu código e a AWS cuida de **servidores, escalabilidade, balanceamento e monitoramento**.

---

## 🎯 Para que serve?

Beanstalk é ideal quando você quer:

* Subir uma aplicação rapidamente sem gerenciar infraestrutura
* Fazer deploy de aplicativos web em várias linguagens
* Escalar automaticamente conforme a demanda
* Integrar com serviços AWS como RDS, S3 e CloudWatch

---

## 🏗️ Como funciona?

1. Você envia seu **código** (ex: Node.js, Python, Java, .NET, PHP, Go)
2. Beanstalk cria o **ambiente**:

   * EC2 para rodar sua aplicação
   * Auto Scaling para ajustar a quantidade de instâncias
   * Load Balancer para distribuir tráfego
   * CloudWatch para monitoramento
3. Beanstalk gerencia o deploy, atualizações e rollback automático

---

## 🔹 Linguagens e plataformas suportadas

* Python (Django, Flask)
* Node.js
* Java (Tomcat, Spring)
* PHP
* .NET
* Ruby
* Go

---

## 🆚 Beanstalk vs EC2 / Lambda

| Serviço           | Quando usar                                      |
| ----------------- | ------------------------------------------------ |
| EC2               | Você quer controle total do servidor             |
| Lambda            | Funções serverless pequenas e rápidas            |
| Elastic Beanstalk | Aplicações web completas com mínima configuração |

Beanstalk combina **controle limitado** com **simplicidade de deploy**.

---

## 📦 Exemplo prático

1. Você cria app em Flask (Python)
2. Zip do código enviado para Beanstalk
3. Elastic Beanstalk cria EC2, Load Balancer e monitora logs
4. Sua aplicação já está online em minutos
5. Quando houver muito tráfego, Auto Scaling adiciona instâncias automaticamente

---

## 🔎 Resumo rápido

Elastic Beanstalk é:

✔️ Serviço de deploy e gerenciamento de apps
✔️ Automatiza infraestrutura e escalabilidade
✔️ Suporta várias linguagens
✔️ Ideal para quem quer focar no código, não no servidor

---

Próximos passos:

* Como criar uma aplicação no Beanstalk passo a passo
* Como conectar Beanstalk com RDS
* Como atualizar sua aplicação sem downtime