# 🔎 Port Scanner

Um **port scanner simples desenvolvido em Python** para identificar portas TCP abertas em um determinado host.

O projeto foi desenvolvido com foco em **estudo de redes, Python e Ethical Hacking**.

## ⚙️ Funcionalidades

* Scan das portas mais comuns.
* Scan de todas as portas de `1` a `65535`.
* Identificação de portas TCP abertas.
* Utiliza a biblioteca nativa `socket` do Python.

## 📋 Portas comuns

O modo rápido verifica portas frequentemente utilizadas por serviços como:

`21, 22, 23, 25, 53, 80, 110, 443, 445, 3306, 3389, 5432, 8080, 27017` e outras.

## 🚀 Como executar

### 1. Clonar o projeto

```bash
git clone https://github.com/hegnerbrandao/port-scanner.git
cd port-scanner
```

### 2. Executar

```bash
python3 PortScanner.py <IP ou HOST>
```

Exemplo:

```bash
python3 PortScanner.py 192.168.1.10
```

### 3. Escolher o tipo de scan

```text
[1] Scanear as portas mais comuns
[2] Scanear todas as portas (65535)
```

Exemplo:

```text
$ python3 PortScanner.py 192.168.1.10

[1] Scanear as portas mais comuns
[2] Scanear todas as portas (65535)

1

Porta 22 [ABERTA]
Porta 80 [ABERTA]
Porta 443 [ABERTA]
```

## 🛠️ Tecnologias

* Python 3
* Socket
* TCP/IP

## 🎯 Objetivo

O objetivo deste projeto é praticar:

* Comunicação TCP/IP
* Identificação de portas abertas
* Programação de sockets em Python
* Fundamentos de Network Security
* Técnicas básicas de reconhecimento

## ⚠️ Aviso

Utilize esta ferramenta **somente em sistemas, redes e hosts para os quais você possui autorização para realizar testes**.

O uso não autorizado de ferramentas de scanning pode violar políticas de segurança ou legislação aplicável.

## 👨‍💻 Autor

**Hegner Brandão**

Projeto desenvolvido para fins **educacionais e de cibersegurança**.
