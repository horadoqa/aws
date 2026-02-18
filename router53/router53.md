# 🌍 O que é o Route 53 na AWS?

O **Route 53** é o serviço de **DNS (Domain Name System)** da Amazon Web Services.

Em termos simples:

> 🌐 Route 53 = serviço que conecta seu domínio (ex: meusite.com) ao seu servidor na AWS.

---

## 🧠 O que é DNS?

DNS é o sistema que transforma:

```
meusite.com
```

em um endereço IP:

```
3.95.120.45
```

Sem DNS, teríamos que acessar sites digitando IP.

---

## 🎯 Para que serve o Route 53?

Ele permite:

* Registrar domínios
* Gerenciar DNS
* Direcionar tráfego para:

  * Amazon EC2
  * Amazon S3
  * Elastic Load Balancing
  * AWS Lambda (via API Gateway)

---

## 🏗️ Como funciona na prática?

### 1️⃣ Você compra ou registra um domínio

Exemplo:

```
meusite.com
```

### 2️⃣ Cria uma Hosted Zone

É onde ficam os registros DNS.

### 3️⃣ Cria registros (records)

Exemplo:

* A → aponta para IP
* CNAME → aponta para outro domínio
* MX → e-mails

---

## 🚦 Tipos de roteamento inteligentes

O Route 53 pode:

* 🔄 Fazer balanceamento de carga
* 🌎 Direcionar para servidor mais próximo (latência)
* 💥 Fazer failover automático
* ⚖️ Distribuir tráfego por peso

Muito usado em sistemas globais.

---

## 🔢 Por que o nome "53"?

Porque o DNS usa a **porta 53**.

---

## 🆚 Route 53 vs Outros DNS

* Total integração com AWS
* Alta disponibilidade
* Escala global
* Monitoramento com health checks

---

## 📦 Exemplo real

Você tem:

* EC2 rodando backend
* Quer acessar via:

```
api.meusite.com
```

Você cria um registro A apontando para o IP da EC2.

Pronto 🚀

---

## 🔎 Resumo rápido

Route 53 é:

✔️ Serviço de DNS
✔️ Conecta domínio ao servidor
✔️ Pode registrar domínios
✔️ Faz roteamento inteligente

---

Próximos passos:

* Como apontar domínio para EC2 passo a passo
* Diferença entre A e CNAME
* O que é hosted zone
* Como configurar HTTPS com Route 53
