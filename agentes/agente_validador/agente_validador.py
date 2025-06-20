class AgenteValidador:
    """
    AgenteValidador (Verificador de Integridade):
    Responsável por validar entidades e intenções, resolver ambiguidades e conflitos,
    e sinalizar necessidade de intervenção humana se necessário.
    """
    def validar(self, dados_semi: dict) -> dict:
        """
        Valida entidades, resolve ambiguidades e conflitos.
        :param dados_semi: Dict semi-estruturado do AgenteAnalista.
        :return: Dict validado ou sinalização de intervenção.
        """
        if dados_semi.get("entidades") and dados_semi.get("intencoes"):
            return {"validado": True, **dados_semi}
        else:
            return {"necessita_intervencao": True, "mensagem": "Entidades ou intenções insuficientes para prosseguir.", **dados_semi}

