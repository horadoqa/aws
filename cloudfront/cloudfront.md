# ☁️ O que é o CloudFront na AWS?

O **CloudFront** é o serviço de **Content Delivery Network (CDN)** da Amazon Web Services.

Em termos simples:

> 🌐 CloudFront = distribui seu conteúdo (site, vídeos, imagens, APIs) **globalmente**, rápido e seguro, usando servidores próximos dos usuários.

---

## 🎯 Para que serve?

CloudFront é usado para:

* Acelerar sites e aplicações web
* Distribuir vídeos e arquivos grandes
* Reduzir latência global
* Melhorar segurança com HTTPS e WAF (Web Application Firewall)
* Distribuir APIs e conteúdo dinâmico

---

## 🏗️ Como funciona?

1. Você tem seu conteúdo armazenado em um **origin**:

   * Amazon S3
   * Amazon EC2
   * Outros servidores HTTP/HTTPS

2. CloudFront cria **edge locations** (servidores ao redor do mundo).

3. Quando um usuário acessa o conteúdo:

   * O CloudFront entrega o arquivo do **servidor mais próximo**.
   * Se não estiver no cache, busca do origin.

---

## 🌍 Benefícios

* ⚡ **Velocidade**: menor latência, entrega mais rápida
* 📈 **Escalabilidade automática**
* 🔒 **Segurança**: HTTPS, integração com WAF e Shield
* 💰 **Redução de custo**: menos tráfego direto do origin

---

## 🆚 CloudFront vs S3

| Serviço    | Função                                 |
| ---------- | -------------------------------------- |
| S3         | Armazena arquivos na nuvem             |
| CloudFront | Distribui arquivos globalmente via CDN |

💡 Normalmente você combina os dois: S3 armazena o arquivo, CloudFront entrega para usuários no mundo todo.

---

## 📦 Exemplo prático

Você tem um site em S3:

1. Cria distribuição CloudFront apontando para o bucket
2. Usuário acessa `www.meusite.com`
3. CloudFront entrega arquivos do edge location mais próximo
4. Resultado: site muito mais rápido

---

## 🔎 Resumo rápido

CloudFront é:

✔️ CDN global
✔️ Reduz latência
✔️ Aumenta desempenho e segurança
✔️ Integrado com S3, EC2 e Lambda

---

Próximos passos:

* Como criar uma distribuição CloudFront passo a passo
* Diferença entre distribuição web e RTMP
* Como usar CloudFront com HTTPS
* Como invalidar cache

