# 🔐 O que é o AWS SSM (Systems Manager) – Session Manager?

O **SSM (Systems Manager) – Session Manager** é um serviço da Amazon Web Services que permite **acessar e gerenciar instâncias EC2 de forma segura sem precisar de SSH ou RDP**.

Em termos simples:

> 🖥️💻 Session Manager = terminal seguro para gerenciar servidores na nuvem, direto do navegador ou CLI, sem abrir portas na internet.

---

## 🎯 Para que serve?

Você usa o Session Manager para:

* Acessar instâncias EC2 de forma segura
* Evitar abrir portas SSH/RDP (melhora a segurança)
* Auditar quem acessou o servidor e o que foi feito
* Automatizar tarefas administrativas sem chave privada

---

## 🏗️ Como funciona?

1. Você habilita **SSM Agent** na sua instância EC2
2. Concede permissões via **IAM Role** para a instância
3. Você abre uma sessão no console AWS ou via CLI:

```bash
aws ssm start-session --target i-0123456789abcdef0
```

4. A AWS cria um **canal seguro criptografado** para você acessar o terminal

---

## 🔹 Principais benefícios

* 🔒 **Segurança:** Sem abrir portas SSH/RDP
* 📜 **Auditoria:** Logs de todas as ações no CloudTrail
* ⚡ **Automação:** Scripts podem ser executados remotamente
* 🌐 **Acesso centralizado:** Multiplas instâncias de diferentes regiões

---

## 🆚 SSM vs SSH/RDP

| Característica            | SSH/RDP                  | Session Manager (SSM)             |
| ------------------------- | ------------------------ | --------------------------------- |
| Porta aberta na internet  | Sim                      | Não                               |
| Gerenciamento de chave    | Sim, precisa de key pair | Não, IAM controla                 |
| Auditoria                 | Limitada                 | CloudTrail registra todas sessões |
| Acesso via CLI ou console | SSH/RDP client           | AWS CLI ou Console                |

---

## 📦 Exemplo prático

Você tem uma EC2 Linux:

1. Instala o **SSM Agent** (já vem em AMIs recentes)
2. Cria IAM Role com permissão `AmazonSSMManagedInstanceCore`
3. Abre console AWS → Session Manager → Start Session
4. Terminal pronto para executar comandos, sem precisar de chave SSH

---

## 🔎 Resumo rápido

SSM Session Manager é:

✔️ Acesso seguro a instâncias EC2
✔️ Sem SSH/RDP e sem abrir portas
✔️ Logs e auditoria integrados
✔️ Pode executar scripts e comandos remotamente

---

Próximos passos:

* Como configurar SSM passo a passo
* Como acessar EC2 via Session Manager pelo CLI
* Diferença entre Session Manager e Systems Manager Run Command

