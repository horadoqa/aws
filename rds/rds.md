# 🗄️ O que é o RDS na AWS?

O **RDS (Relational Database Service)** é um serviço da Amazon Web Services para **criar, operar e escalar bancos de dados relacionais na nuvem** sem precisar administrar o servidor manualmente.

Em resumo:

> 🗄️ RDS = Banco de dados gerenciado pela AWS.

---

## 🎯 Para que serve?

Você usa RDS quando precisa de um banco de dados relacional como:

* MySQL
* PostgreSQL
* MariaDB
* Oracle Database
* Microsoft SQL Server

Ideal para:

* Backends de APIs
* Sistemas web
* ERPs
* Aplicações corporativas

---

## 🔧 O que significa “gerenciado”?

Se você instalar banco numa EC2, você precisa:

* Instalar o banco
* Configurar backup
* Atualizar versão
* Configurar replicação
* Monitorar performance

Com o **RDS**, a AWS cuida de:

✅ Backups automáticos
✅ Atualizações de segurança
✅ Monitoramento
✅ Alta disponibilidade (Multi-AZ)
✅ Escalabilidade

---

## 🆚 RDS vs Banco na EC2

| RDS                  | Banco na EC2   |
| -------------------- | -------------- |
| Gerenciado           | Você gerencia  |
| Backup automático    | Manual         |
| Fácil escalar        | Mais complexo  |
| Menos controle do SO | Controle total |

---

## 🏗️ Como funciona na prática?

1. Você escolhe o tipo de banco (ex: PostgreSQL)
2. Define CPU, memória e armazenamento
3. Cria usuário e senha
4. AWS gera um **endpoint** (ex: `meubanco.xxxxxx.rds.amazonaws.com`)
5. Sua aplicação conecta usando host + usuário + senha

---

## 💰 Como funciona o custo?

Você paga por:

* Tipo da instância (CPU e RAM)
* Armazenamento
* Backup adicional
* Multi-AZ (se ativado)

---

## 📦 Exemplo real

Se você tem uma API rodando em:

* EC2 ou Lambda

Ela pode se conectar ao RDS usando:

```python
host = "meubanco.xxxxxx.rds.amazonaws.com"
```

E pronto — banco rodando sem você precisar administrar servidor.

---

## 🔎 Resumo rápido

RDS é:

✔️ Banco relacional na nuvem
✔️ Gerenciado pela AWS
✔️ Ideal para aplicações web
✔️ Mais simples que instalar banco manualmente

---

Próximos passos:

* Como criar um RDS passo a passo
* O que é Multi-AZ
* Diferença entre RDS e DynamoDB
* Como conectar Lambda ao RDS
