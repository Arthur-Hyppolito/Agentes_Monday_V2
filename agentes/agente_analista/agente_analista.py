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
        import re
        entidades = []
        intencoes = []
        
        # Extrai datas (formato dd/mm/yyyy ou dd-mm-yyyy)
        datas = re.findall(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b', texto_limpo)
        if datas:
            entidades.append({"tipo": "data", "valor": datas})
        
        # Extrai nomes próprios simples (inicial maiúscula)
        nomes = re.findall(r'\b([A-Z][a-z]+(?: [A-Z][a-z]+)*)\b', texto_limpo.title())
        if nomes:
            entidades.append({"tipo": "pessoa", "valor": nomes})
        
        # Detecta intenções básicas por verbos de ação
        if any(verb in texto_limpo for verb in ["criar", "adicionar", "atualizar", "remover", "excluir"]):
            intencoes.append("acao_detectada")
        
        return {"texto": texto_limpo, "entidades": entidades, "intencoes": intencoes}

