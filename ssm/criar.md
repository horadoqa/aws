# Acesso SSM

Um **passo a passo completo para acessar uma instância EC2 usando o AWS SSM (Session Manager)** de forma segura, sem SSH.

---

## 🔹 Pré-requisitos

1. Conta AWS ativa
2. Instância EC2 rodando (Linux ou Windows)
3. Região da AWS configurada corretamente
4. IAM Role ou usuário com permissões necessárias

---

## 1️⃣ Criar ou verificar IAM Role para a EC2

A instância precisa de **permissão para usar o SSM**:

1. No console AWS, vá em **IAM → Roles → Create Role**
2. Tipo de entidade confiável: **AWS Service → EC2**
3. Adicione a política:

   * `AmazonSSMManagedInstanceCore`
4. Nomeie a role, ex: `EC2-SSM-Role`
5. Crie a role

---

## 2️⃣ Associar a IAM Role à EC2

1. Vá em **EC2 → Instances**
2. Selecione sua instância
3. Clique em **Actions → Security → Modify IAM Role**
4. Escolha a role criada (`EC2-SSM-Role`)
5. Salve

> ✅ A instância agora tem permissão para se comunicar com o SSM

---

## 3️⃣ Verificar o SSM Agent

* **Linux AMIs recentes** já vêm com o agente instalado
* Para Windows ou AMIs antigas, instale manualmente:

```bash
# Exemplo Linux Amazon Linux 2
sudo yum install -y amazon-ssm-agent
sudo systemctl enable amazon-ssm-agent
sudo systemctl start amazon-ssm-agent
```

---

## 4️⃣ Acessar a instância pelo **Console AWS**

1. Vá em **Systems Manager → Session Manager → Start session**
2. Escolha sua instância EC2
3. Clique em **Start session**
4. Um terminal interativo abre direto no navegador
5. Pronto! Agora você pode executar comandos como se estivesse no SSH

---

## 5️⃣ Acessar via **AWS CLI**

Se preferir usar terminal local com AWS CLI:

```bash
# Listar instâncias SSM disponíveis
aws ssm describe-instance-information

# Abrir sessão
aws ssm start-session --target <INSTANCE_ID>
```

> Substitua `<INSTANCE_ID>` pelo ID da instância EC2.

---

## 6️⃣ Benefícios de usar SSM

* 🔒 **Sem abrir portas SSH/RDP**
* 📜 **Auditoria completa** (CloudTrail)
* ⚡ **Execução de scripts remota**
* 🌐 **Funciona via console ou CLI**

---