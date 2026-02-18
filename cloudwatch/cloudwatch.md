# 📊 O que é o CloudWatch na AWS?

O **CloudWatch** é o serviço da Amazon Web Services para **monitoramento e observabilidade** da sua infraestrutura e aplicações na nuvem.

Em termos simples:

> 📈 CloudWatch = vigia tudo que acontece na sua AWS e avisa se algo der errado.

---

## 🎯 Para que serve?

Ele serve para:

* Monitorar métricas de serviços AWS (CPU, memória, disco, requests)
* Coletar e visualizar logs de aplicações
* Criar alarmes e notificações
* Automatizar respostas a eventos
* Diagnosticar problemas de performance

---

## 🧩 Componentes principais

### 1️⃣ Métricas (Metrics)

Valores medidos periodicamente, como:

* CPU da EC2
* Número de requisições no S3
* Latência da API

### 2️⃣ Logs

* Armazena logs de aplicações, Lambda, VPC e outros serviços
* Permite pesquisa e análise

### 3️⃣ Alarms

* Disparam ações quando uma métrica atinge um limite
* Exemplo: CPU > 80% → enviar e-mail ou escalar instância

### 4️⃣ Dashboards

* Gráficos customizados para visualizar métricas e status

---

## 📦 Exemplo prático

1. Sua EC2 tem CPU subindo acima de 80% constantemente
2. CloudWatch Alarm dispara
3. Envia notificação via SNS
4. Lambda pode iniciar nova EC2 automaticamente

---

## 🆚 CloudWatch vs Outras ferramentas

| CloudWatch                | Ferramentas tradicionais            |
| ------------------------- | ----------------------------------- |
| Integrado com AWS         | Precisa configurar agentes externos |
| Métricas, logs, alarmes   | Métricas ou logs separadamente      |
| Escalabilidade automática | Limite de servidores monitorados    |

---

## 💰 Custo

* Métricas básicas: gratuitas
* Métricas customizadas: pago por métrica
* Logs: pago por volume armazenado
* Dashboards: pago por número de dashboards

---

## 🔎 Resumo rápido

CloudWatch é:

✔️ Monitoramento e logs
✔️ Alarmes e alertas automáticos
✔️ Visualização de métricas e dashboards
✔️ Essencial para manter aplicações AWS saudáveis

---

Se quiser, posso mostrar:

* Como criar um alarme de CPU na EC2
* Como visualizar logs de Lambda
* Como criar um dashboard completo
* Como integrar CloudWatch com SNS para notificações
