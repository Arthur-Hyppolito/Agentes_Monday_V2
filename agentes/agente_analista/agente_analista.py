class AgenteAnalista:
    """
    AgenteAnalista (Interpretador de Intenções):
    Responsável por analisar semanticamente o texto limpo, extrair entidades e intenções,
    e estruturar os dados para as próximas etapas.
    """
    def analisar(self, texto_limpo: str) -> dict:
        """
        Analisa o texto limpo, identifica entidades e ações, e estrutura como JSON.
        :param texto_limpo: Texto já limpo e pré-processado.
        :return: Dict semi-estruturado com entidades e intenções.
        """
        # TODO: Implementar análise real (PLN)
        return {"texto": texto_limpo, "entidades": [], "intencoes": []}
