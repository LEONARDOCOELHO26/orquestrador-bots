# 🤖 Orquestrador Bots - Test Suite

Este repositório contém bots de teste para validar funcionalidades de um orquestrador Python.

## Bots incluídos

### 1. Heartbeat

Loop infinito que escreve logs continuamente.

### 2. Financeiro

Simula comportamento financeiro de usuários.

### 3. API

Testa integração com API externa.

### 4. Config

Lê variáveis de `.env` e `config.ini`.

### 5. Decisor

Simula decisões aleatórias.

---

## ⚙️ Instalação

```bash
git clone <repo>
cd orquestrador-bots
pip install -r requirements.txt
```

---

## ▶️ Execução manual

```bash
python heartbeat/bot_heartbeat.py
python financeiro/bot_financeiro.py
python api/bot_api.py
python config/bot_config.py
python decisor/bot_decisor.py
```

---

## 🔐 Variáveis de ambiente

Copie:

```bash
cp .env.example .env
```

---

## 🧪 Objetivo

Este projeto serve para testar:

* execução de bots
* monitoramento de logs
* leitura de config
* integração com Git
* falhas e comportamento dinâmico
