# 🚀 O que é o AWS Lambda?

![Image](https://upload.wikimedia.org/wikipedia/commons/5/5c/Amazon_Lambda_architecture_logo.svg)

![Image](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/9859d271-50a1-4edb-9c68-a76889346142/Face-blurring_serverless_architecture.png?t=1697379415)

![Image](https://www.researchgate.net/publication/351869252/figure/fig2/AS%3A1027630778290183%401622017678485/Serverless-Architecture.ppm)

![Image](https://www.researchgate.net/publication/317557782/figure/fig1/AS%3A504644585902080%401497328053871/Serverless-platform-architecture.png)

O **AWS Lambda** é um serviço de computação *serverless* da Amazon Web Services que permite executar código **sem precisar gerenciar servidores**.

Você apenas:

1. Envia o código
2. Define quando ele deve rodar
3. A AWS cuida do resto (infraestrutura, escalabilidade, disponibilidade)

---

## 🎯 Para que serve o Lambda?

Ele é usado para executar código automaticamente em resposta a eventos, como:

* 📤 Upload de arquivos no Amazon S3
* 🌐 Requisições HTTP via Amazon API Gateway
* 🗄️ Alterações no Amazon DynamoDB
* ⏰ Execução programada (cron jobs)
* 📩 Processamento de mensagens (SQS, SNS)

### Exemplos práticos:

* Criar uma API simples
* Processar imagens automaticamente
* Enviar e-mails
* Automatizar tarefas
* Backends leves e microsserviços

---

## 🛠️ Como criar um Lambda na AWS (Passo a passo)

### 🔹 1. Acessar o Console

* Vá para: [https://console.aws.amazon.com/](https://console.aws.amazon.com/)
* Pesquise por **Lambda**

---

### 🔹 2. Criar função

* Clique em **"Create function"**
* Escolha **Author from scratch**
* Defina:

  * Nome da função
  * Linguagem (ex: Python, Node.js)
  * Permissões (criar nova role automaticamente)

---

### 🔹 3. Escrever o código

Exemplo em **Python**:

```python
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Olá, mundo!'
    }
```

Clique em **Deploy**

---

### 🔹 4. Testar a função

* Clique em **Test**
* Crie um evento de teste
* Execute

Se tudo estiver certo → você verá o retorno no console.

---

## 💰 Quanto custa?

O AWS Lambda cobra por:

* Número de execuções
* Tempo de execução (milissegundos)
* Memória configurada

👉 Existe uma camada gratuita generosa:

* 1 milhão de execuções por mês grátis

---

## ⚡ Vantagens

✅ Não gerencia servidor
✅ Escala automaticamente
✅ Paga só pelo uso
✅ Integra com quase todos serviços AWS

---

## 📦 Resumo rápido

| Item              | Explicação                      |
| ----------------- | ------------------------------- |
| O que é           | Serviço serverless              |
| Para que serve    | Executar código sob demanda     |
| Quando usar       | APIs, automações, processamento |
| Precisa servidor? | ❌ Não                           |

---

Próximos passos:

* Como criar um Lambda que vira uma API REST
* Como integrar com banco de dados
* Como fazer deploy pelo terminal (CLI)
* Ou um exemplo mais profissional


O **AWS Lambda** é um serviço de computação serverless (sem servidor) da Amazon Web Services, que permite executar código em resposta a eventos sem precisar provisionar ou gerenciar servidores. Com o Lambda, você pode carregar o seu código (em várias linguagens, como Node.js, Python, Java, C#, entre outras) e o serviço cuida de toda a infraestrutura necessária para rodá-lo de forma escalável e eficiente.

### Características principais do AWS Lambda:
- **Execução sob demanda**: O Lambda executa o seu código apenas quando um evento ocorre, como uma requisição HTTP via API Gateway, alterações em um bucket S3, mensagens no SNS ou SQS, entre outros.
- **Escalabilidade automática**: O serviço escala automaticamente para lidar com picos de tráfego, sem a necessidade de intervenção manual.
- **Cobrança com base no uso**: A cobrança é feita com base no número de execuções e no tempo de computação consumido, ou seja, você paga apenas pelo que utiliza, sem custos fixos.
- **Sem gerenciamento de servidores**: Como é um serviço serverless, o AWS Lambda abstrai toda a configuração e manutenção de servidores, permitindo que os desenvolvedores foquem exclusivamente no código.
- **Suporte a múltiplas linguagens**: O Lambda oferece suporte a várias linguagens de programação, incluindo Node.js, Python, Ruby, Java, Go, C# (.NET Core), e também possibilita o uso de contêineres customizados.
- **Integração com outros serviços AWS**: Lambda é amplamente integrado com outros serviços da AWS, como API Gateway, DynamoDB, S3, SNS, SQS, CloudWatch, entre outros, o que facilita a criação de arquiteturas serverless complexas.

### Casos de uso comuns:
- **Processamento de dados**: Transformação e análise de dados, como o processamento de imagens, vídeos ou logs.
- **Backends de aplicações web**: Servir como backend para páginas web ou APIs, processando requisições sem a necessidade de servidores dedicados.
- **Automação de tarefas**: Execução de scripts de automação em resposta a eventos, como a criação de arquivos em um bucket S3 ou mensagens em uma fila SQS.
- **Desenvolvimento de microservices**: Construção de microserviços independentes e escaláveis que podem ser facilmente atualizados e mantidos.

Em resumo, o **AWS Lambda** permite que você crie soluções ágeis e escaláveis com baixo custo e sem se preocupar com a infraestrutura, tornando-o uma excelente escolha para desenvolvedores que buscam focar apenas na lógica de aplicação.