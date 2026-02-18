# ☁️ O que é uma EC2 na AWS?

A **EC2 (Elastic Compute Cloud)** é um serviço da Amazon Web Services que permite criar **servidores virtuais na nuvem**.

Em outras palavras:

> 🖥️ EC2 = um computador (servidor) rodando dentro da infraestrutura da AWS.

Você escolhe:

* Sistema operacional (Linux, Windows)
* Quantidade de CPU
* Memória (RAM)
* Armazenamento
* Região do mundo

E a AWS cria a máquina virtual para você.

---

## 🎯 Para que serve?

Você usa EC2 quando precisa de:

* Hospedar sites
* Rodar APIs
* Backend de aplicações
* Banco de dados
* Processamento pesado
* Sistemas legados
* Aplicações que precisam ficar sempre ligadas

---

## 🆚 EC2 vs Lambda

| EC2                      | Lambda                     |
| ------------------------ | -------------------------- |
| Você gerencia o servidor | Serverless                 |
| Fica sempre rodando      | Executa sob demanda        |
| Mais controle            | Mais simples               |
| Ideal para apps longas   | Ideal para funções rápidas |

---

## 🛠️ Como funciona na prática?

1. Você cria uma instância EC2
2. A AWS fornece um IP público
3. Você acessa via SSH (Linux) ou RDP (Windows)
4. Instala o que quiser (Node, Python, Docker, etc.)

É literalmente como ter um servidor físico, só que na nuvem.

---

## 💰 Como funciona o custo?

Você paga por:

* Tempo que a instância fica ligada
* Tipo da instância (mais CPU = mais caro)
* Armazenamento
* Tráfego de rede

Existe também um **Free Tier** com instâncias pequenas gratuitas por 12 meses.

---

## 📦 Exemplo simples

Se você quiser subir um site em Node.js:

* Cria uma EC2
* Instala Node
* Roda `node app.js`
* Abre a porta 80 no Security Group
* Pronto 🚀

---

## 🔎 Resumo rápido

EC2 é:

✔️ Um servidor virtual
✔️ Totalmente configurável
✔️ Sempre disponível enquanto estiver ligado
✔️ Mais controle, mais responsabilidade

---

Próximo passo:

* Como criar uma EC2 passo a passo
* O que são tipos de instância (t2, t3, etc.)
* O que é VPC, Security Group e Elastic IP
* Ou quando escolher EC2 vs Lambda

