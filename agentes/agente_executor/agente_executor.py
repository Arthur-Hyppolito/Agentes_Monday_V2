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

        # Executar apenas o fluxo Monday.com API para teste
        # 1. Tentar MCP
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
            resp = requests.post(mcp_url, json=jsonrpc_payload, timeout=5, headers=headers)
            print(f"[DEBUG] Resposta MCP: status={resp.status_code}, body={resp.text}")
            if resp.status_code == 200:
                return {
                    "status": resp.status_code,
                    "rota": "MCP",
                    "payload": payload,
                    "resposta": resp.json() if resp.headers.get('Content-Type', '').startswith('application/json') else resp.text
                }
            else:
                print("[DEBUG] MCP falhou, tentando fallback para API direta do Monday.com")
        except Exception as e:
            print(f"[DEBUG] Erro ao conectar ao MCP: {e}")
            print("[DEBUG] Tentando fallback para API direta do Monday.com")

        # 2. Fallback: API direta do Monday.com
        monday_token = os.getenv("MONDAY_API_TOKEN")
        if not monday_token:
            return {"status": "erro", "rota": "API", "payload": payload, "erro": "MONDAY_API_TOKEN não definido no .env"}
        url = "https://api.monday.com/v2"
        headers = {
            "Authorization": monday_token,
            "Content-Type": "application/json"
        }
        board_id = 9305252428
        item_name = "arthur"
        query = """
        mutation ($board_id: ID!, $item_name: String!) {
          create_item (board_id: $board_id, item_name: $item_name) {
            id
            name
          }
        }
        """
        variables = {"board_id": str(board_id), "item_name": item_name}
        data = {"query": query, "variables": variables}
        print(f"[DEBUG] Enviando para Monday.com: {data}")
        try:
            resp = requests.post(url, json=data, headers=headers, timeout=10)
            print(f"[DEBUG] Resposta Monday: status={resp.status_code}, body={resp.text}")
            return {
                "status": resp.status_code,
                "rota": "API",
                "payload": payload,
                "resposta": resp.json() if resp.headers.get('Content-Type', '').startswith('application/json') else resp.text
            }
        except Exception as e:
            print(f"[DEBUG] Erro ao conectar ao Monday.com: {e}")
            return {
                "status": "erro",
                "rota": "API",
                "payload": payload,
                "erro": str(e)
            }
