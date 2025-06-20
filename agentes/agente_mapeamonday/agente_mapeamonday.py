class AgenteMapeaMonday:
    """
    AgenteMapeaMonday (Tradutor de Plataforma):
    Responsável por mapear dados validados para o formato de payload das integrações.
    """
    def mapear(self, dados_validados: dict) -> dict:
        """
        Mapeia dados para o payload esperado pelas integrações.
        :param dados_validados: Dict validado pelo AgenteValidador.
        :return: Payload pronto para decisão de rota.
        """
        payload = {
            "acao": dados_validados.get("intencoes", [None])[0],
            "entidades": dados_validados.get("entidades", [])
        }
        return payload

