class AgenteGenio:
    """
    AgenteGenio (Decisor de Execução):
    Decide se a requisição será executada via Zapier MCP ou API direta do Monday.com.
    """
    def decidir_rota(self, payload: dict) -> tuple:
        """
        Decide a rota de execução e ajusta payload se necessário.
        :param payload: Payload mapeado pelo AgenteMapeaMonday.
        :return: (rota: str, payload_final: dict)
        """
        return ("MCP", payload)

