# 🔐 O que é IAM na AWS?

O **IAM (Identity and Access Management)** é o serviço da Amazon Web Services responsável por **controlar quem pode acessar o quê dentro da sua conta AWS**.

Em termos simples:

> 🔐 IAM = sistema de permissões da AWS.

---

## 🎯 Para que serve?

Ele permite que você:

* Criar usuários
* Criar grupos
* Criar roles (papéis)
* Definir permissões (policies)
* Controlar acesso a serviços como S3, EC2, RDS etc.

---

## 🧩 Componentes principais

### 👤 Usuários (Users)

Pessoa ou aplicação que precisa acessar a AWS.

Exemplo:

* Usuário do desenvolvedor
* Usuário para CI/CD

---

### 👥 Grupos (Groups)

Conjunto de usuários com as mesmas permissões.

Exemplo:

* Grupo “Desenvolvedores”
* Grupo “Administradores”

---

### 🎭 Roles (Funções)

Permissões temporárias usadas por serviços AWS.

Exemplo:

* Uma função Lambda acessando S3
* Uma EC2 acessando RDS

👉 Muito usado para comunicação segura entre serviços.

---

### 📜 Policies (Políticas)

Regras que definem o que pode ou não pode fazer.

Exemplo simples de policy:

```json
{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "*"
}
```

Isso permite baixar arquivos do S3.

---

## 🔎 Exemplo prático

Imagine que você tem:

* Uma aplicação rodando na EC2
* Arquivos no S3

Você cria:

1. Uma **Role**
2. Dá permissão de acesso ao S3
3. Associa a role na EC2

Pronto. A EC2 acessa o S3 **sem precisar senha no código** 🔐

---

## 🆚 IAM vs Login da AWS

* Login root → Dono da conta (perigoso usar no dia a dia)
* IAM → Usuários controlados com permissões específicas

Boa prática:
✅ Nunca usar root no dia a dia
✅ Criar usuários IAM
✅ Aplicar princípio do menor privilégio

---

## 📦 Resumo rápido

IAM é:

✔️ Controle de acesso
✔️ Sistema de permissões
✔️ Base de segurança da AWS
✔️ Essencial para qualquer projeto

---

Próximos passos:

* Diferença entre User e Role
* Como criar uma policy correta
* O que é princípio do menor privilégio
* Como funciona autenticação com Access Key
