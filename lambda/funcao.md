# Vamos analisar essa função passo a passo 👇

```python
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Olá, mundo!'
    }

lambda_handler()
```

---

## 🔹 1️⃣ O que é `lambda_handler`?

No **Amazon Web Services Lambda**, a função principal **precisa ter um handler**, que é o ponto de entrada da execução.

Por padrão, quando você cria uma função em Python no **AWS Lambda**, ele espera algo como:

```
arquivo.lambda_handler
```

Ou seja:

* `arquivo.py` → nome do arquivo
* `lambda_handler` → nome da função que será executada

---

## 🔹 2️⃣ Parâmetros da função

```python
def lambda_handler(event, context):
```

Ela recebe dois parâmetros obrigatórios:

### 📦 `event`

Contém os dados que acionaram a função.

Exemplos:

* Dados de uma requisição HTTP (API Gateway)
* Evento de upload no S3
* Mensagem de fila (SQS)

É basicamente o **input** da função.

---

### 🧠 `context`

Contém informações sobre a execução, como:

* ID da requisição
* Tempo restante de execução
* Nome da função
* Limite de memória

Geralmente usado para logs e controle avançado.

---

## 🔹 3️⃣ O que ela retorna?

```python
return {
    'statusCode': 200,
    'body': 'Olá, mundo!'
}
```

Isso é um **dicionário Python**.

Quando a Lambda está integrada com o Amazon API Gateway, esse formato vira uma resposta HTTP:

| Campo             | Significado           |
| ----------------- | --------------------- |
| `statusCode: 200` | Sucesso (HTTP 200 OK) |
| `body`            | Corpo da resposta     |

Então, se você chamar essa função via API, o navegador receberia:

```
Olá, mundo!
```

---

## 🔹 4️⃣ Problema na última linha ⚠️

```python
lambda_handler()
```

Isso vai dar erro ❌

Porque a função exige dois argumentos:

```python
lambda_handler(event, context)
```

Se você rodar localmente, teria que chamar assim:

```python
lambda_handler({}, None)
```

Ou:

```python
lambda_handler({"nome": "Pedro"}, None)
```

---

## 🔎 Resumo

Essa função:

* É o ponto de entrada da AWS Lambda
* Recebe dados via `event`
* Pode usar informações da execução via `context`
* Retorna uma resposta HTTP simples

---

Próximos possos:

* Mostrar como acessar dados do `event`
* Simular uma chamada HTTP real
* Transformar isso numa API de verdade
* Ou explicar o `context` em detalhe
