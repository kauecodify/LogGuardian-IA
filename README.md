# LogGuardian - Detecção Inteligênte de Anomalias em Logs com Go + IA + FastAPI

LogGuardian é um sistema de monitoramento inteligente que combina a alta performance do Go com modelos de machine learning não supervisionado para detectar anomalias em logs de servidores — como tentativas de invasão, falhas em massa ou comportamentos suspeitos — sem regras manuais.

---

# Tecnologias Utilizadas

<img width="80" height="80" alt="golang-svgrepo-com" src="https://github.com/user-attachments/assets/e9293609-5cee-41aa-8ef0-b342689c099e" />


<img width="80" height="80" alt="python-svgrepo-com" src="https://github.com/user-attachments/assets/03e77df9-ace9-43ca-905b-e746e9796442" />

<img width="80" height="80" alt="json-svgrepo-com" src="https://github.com/user-attachments/assets/616686fe-0c5e-419e-9595-f22833d2c0a6" />

<img width="80" height="80" alt="docker-svgrepo-com" src="https://github.com/user-attachments/assets/6d123e80-4dd4-4c98-bd93-0f5c1d4571bc" />

<img width="80" height="80" alt="ai-svgrepo-com" src="https://github.com/user-attachments/assets/6bc0d3f0-3a8c-4d64-9b38-80bb007233a8" />



---

# Estrutura do Projeto

<img width="264" height="349" alt="image" src="https://github.com/user-attachments/assets/b586c69c-28fd-43e4-9918-3de96532988f" />

---
# Finalidade do Projeto

Auditar o que aconteceu e quando;

Detectar anomalias (como comportamentos fora do padrão);

Identificar ataques cibernéticos (como brute force, SQL injection, etc.);

Investigar incidentes (forense digital);

Melhorar a performance e monitorar falhas operacionais.

---

exemplo na prática:

microserviço de IA usa os logs como entrada (log_line) para prever se uma linha de log parece normal ou anômala.

Log	Resultado	Interpretação

"User admin logged in"	is_anomaly = false >> Evento normal de autenticação.

"Failed login for root from 203.0.113.5"	is_anomaly = true	>> Tentativa suspeita de acesso indevido.

"rm -rf / --no-preserve-root"	is_anomaly = true	>> Comando potencialmente destrutivo — alerta crítico.

---

✅ Totalmente open-source

✅ Pronto para rodar com docker-compose

✅ Inclui script para treinar seu próprio modelo de IA

---

# 🧠 Como Treinar o Modelo de IA

O modelo usa Isolation Forest (algoritmo não supervisionado) para detectar anomalias em logs. Você pode treiná-lo com seus próprios dados históricos.

# Passo 1: Prepare seus dados
Crie um arquivo CSV com uma coluna chamada log ("sample_logs") contendo mensagens reais de log 

(exemplo):

<img width="477" height="281" alt="image" src="https://github.com/user-attachments/assets/fa85ddef-0db1-4278-955f-02a0bff0103e" />

Dica: Use logs de produção (sem dados sensíveis!) ou o sample_logs.csv incluso como base. 

# Passo 2: Treine o modelo

(exemplo):

<img width="481" height="136" alt="image" src="https://github.com/user-attachments/assets/43403e2d-94ae-4ed4-b9c0-a63840fd9d86" />

Isso gera: 

model.pkl > modelo serializado

vectorizer.pkl > vetor TF-IDF salvo

---

# Passo 3: Suba tudo com Docker Compose

<img width="275" height="114" alt="image" src="https://github.com/user-attachments/assets/73d39009-444f-4059-908e-55b1fe4a2f63" />


✅ Após, o modelo já está pronto para ser usado pela API! 


# Passo 4: Teste manual 

<img width="482" height="156" alt="image" src="https://github.com/user-attachments/assets/3cec28ee-9eed-49fe-800c-b2883f698dfe" />

---

# Resultado Esperado

<img width="269" height="156" alt="image" src="https://github.com/user-attachments/assets/068eba92-9f0f-450c-9635-3015a62fedf6" />

---

✅ Go como cliente — ultrarrápido, sem dependências pesadas

✅ FastAPI assíncrono — máximo desempenho no Python

✅ Modelos serializados em disco (carregados uma vez só)

✅ Docker Compose — isolamento e portabilidade

✅ Uso de TF-IDF + IsolationForest (não supervisionado e leve)

✅ Escalável: pode rodar vários clientes Go apontando para o mesmo serviço de IA sendo nuvem aws ou qualquer outra a escolha do admin

✅ Recomendações: Apontar para o server e manter users da aplicação no server para autenticação, após, gestionar o acesso ao serviço em nuvem via encrypt data por acesso.

---

mitlicence

by k :copilot:

<img width="30" height="30" alt="brazil-svgrepo-com" src="https://github.com/user-attachments/assets/7b4046da-14ce-42ab-944a-31c2ab505947" />


