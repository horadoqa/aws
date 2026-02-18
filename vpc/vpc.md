# 🌐 O que é uma VPC na AWS?

A **VPC (Virtual Private Cloud)** é uma **rede virtual privada dentro da AWS** criada na infraestrutura da Amazon Web Services.

Em termos simples:

> 🌐 VPC = sua própria rede privada dentro da AWS.

É como se você tivesse um **data center isolado**, mas na nuvem.

---

## 🎯 Para que serve?

A VPC permite que você:

* Defina faixas de IP
* Crie sub-redes (subnets)
* Controle quem acessa o quê
* Configure roteamento
* Controle acesso à internet

Ela é a base de serviços como:

* Amazon EC2
* Amazon RDS
* AWS Lambda (quando conectada a rede)

---

## 🏗️ Componentes principais

### 🏠 Subnets

Dividem a VPC em partes menores.

* Subnet pública → acesso à internet
* Subnet privada → sem acesso direto à internet

---

### 🌍 Internet Gateway

Permite que recursos da VPC acessem a internet.

---

### 🔒 Security Groups

Firewall da instância (controla portas e tráfego).

---

### 🛣️ Route Tables

Definem para onde o tráfego deve ir.

---

## 🧠 Exemplo prático

Imagine um sistema com:

* EC2 pública → recebe requisições
* RDS privado → banco de dados protegido

Arquitetura:

```
Internet
   ↓
EC2 (Subnet Pública)
   ↓
RDS (Subnet Privada)
```

O banco não fica exposto à internet 🔐

---

## 🆚 VPC é obrigatória?

Sim. Toda conta AWS já tem uma **VPC padrão (Default VPC)**.

Mas em projetos profissionais, você cria uma VPC personalizada para ter mais controle.

---

## 📦 Resumo rápido

VPC é:

✔️ Rede privada na AWS
✔️ Controla IP, subnets e segurança
✔️ Base de toda arquitetura cloud
✔️ Essencial para produção

---

Próximos passos:

* Diferença entre subnet pública e privada
* O que é NAT Gateway
* Como montar uma arquitetura segura
* Como criar uma VPC passo a passo

