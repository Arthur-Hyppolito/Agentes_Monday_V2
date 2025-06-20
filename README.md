# Agentes_Monday_V2

Sistema multiagentes para processamento inteligente de transcrições e automação de tarefas no Monday.com via Windlflow, Zapier MCP e fallback para API direta.

## Objetivo
Desenvolver um sistema multiagentes capaz de processar transcrições de reuniões ou comandos diretos, analisar e validar informações, e automatizar a criação/atualização de tarefas, itens e outros elementos no Monday.com, otimizando a gestão de projetos e reduzindo a entrada manual de dados.

## Arquitetura Multiagente
O sistema é composto por 7 agentes especializados, cada um em sua pasta dedicada:

- **agente_pre**: Transcritor & Limpador de texto
- **agente_analista**: Interpretação semântica, extração de entidades e intenções
- **agente_validador**: Verificação de integridade, resolução de ambiguidades e conflitos
- **agente_mapeamonday**: Tradução para payloads e formatos das integrações
- **agente_genio**: Decisor de rota (MCP ou API direta) e fallback inteligente
- **agente_executor**: Executor de integrações, tratamento de erros e autenticação
- **agente_boss**: Supervisor, coleta feedback e otimização do sistema

## Fluxo Resumido
1. Recebe transcrição/comando → 2. Limpa e pré-processa → 3. Analisa entidades/intenções → 4. Valida e resolve conflitos → 5. Mapeia para payload → 6. Decide rota (MCP/API) → 7. Executa operação → 8. Supervisiona/aprende

## Integrações
- **Zapier MCP (primário):** https://mcp.zapier.com/api/mcp/s/M2RlOTAzNmMtNmJkYS00ZDkwLTlhMGUtMTYxOTRmYmRiYzVjOjNmYWIyZTMxLWMyY2YtNDIyOS1hMDdiLWU1ZGU0NmUzMzFmZQ==/mcp
- **Monday.com API (fallback)**

## Organização sugerida de pastas
```
agentes/
  agente_pre/
  agente_analista/
  agente_validador/
  agente_mapeamonday/
  agente_genio/
  agente_executor/
  agente_boss/
```

## Requisitos
- Python 3.8+
- Bibliotecas: ver requirements.txt
- .env com tokens e URLs

## Como começar
1. Clone o repositório
2. Instale as dependências
3. Configure o .env
4. Execute o sistema principal

---
Para detalhes sobre cada agente, consulte a documentação interna de cada módulo.
