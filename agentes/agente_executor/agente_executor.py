class AgenteExecutor:
    """
    AgenteExecutor (Executor de Integração):
    Responsável por executar a requisição na rota escolhida (MCP ou API direta).
    """
    def executar(self, rota: str, payload: dict) -> dict:
        """
        Executa a operação na plataforma de destino.
        :param rota: 'MCP' ou 'API'.
        :param payload: Payload final para execução.
        :return: Resultado da execução.
        """
        import os
        import requests
        from dotenv import load_dotenv
        import os
        dotenv_path = r"c:\\Users\\hyppo\\Documents\\Agentes_Monday_V2\\.env"
        load_dotenv(dotenv_path=dotenv_path)

        if rota == "MCP":
            mcp_url = os.getenv("MCP_URL")
            print(f"[DEBUG] MCP_URL lido do .env: {mcp_url}")
            try:
                headers = {"Accept": "application/json, text/event-stream"}
                mcp_method = os.getenv("MCP_METHOD", "criar_tarefa")
                jsonrpc_payload = {
                    "jsonrpc": "2.0",
                    "method": mcp_method,
                    "params": payload,
                    "id": 1
                }
                print(f"[DEBUG] Enviando para MCP: {jsonrpc_payload}")
                try:
                    resp = requests.post(mcp_url, json=jsonrpc_payload, timeout=5, headers=headers)
                    print(f"[DEBUG] Resposta MCP: status={resp.status_code}, body={resp.text}")
                    return {
                        "status": resp.status_code,
                        "rota": rota,
                        "payload": payload,
                        "resposta": resp.json() if resp.headers.get('Content-Type', '').startswith('application/json') else resp.text
                    }
                except Exception as e:
                    print(f"[DEBUG] Erro ao conectar ao MCP: {e}")
                    return {
                        "status": "erro",
                        "rota": rota,
                        "payload": payload,
                        "erro": str(e)
                    }
            except Exception as e:
                return {
                    "status": "erro",
                    "rota": rota,
                    "payload": payload,
                    "erro": str(e)
                }
        else:
            # Fallback simulado para API direta
            return {"status": "simulado", "rota": rota, "payload": payload}

