class AgentePre:
    """
    AgentePre (Transcritor & Limpador):
    Responsável por receber o texto bruto e realizar limpeza inicial,
    removendo ruídos, caracteres especiais e padronizando o texto.
    """
    def limpar_texto(self, texto_bruto: str) -> str:
        """
        Executa limpeza básica do texto (remover ruídos, caracteres especiais, etc).
        :param texto_bruto: Texto original da transcrição ou comando.
        :return: Texto limpo e padronizado.
        """
        import re
        texto = texto_bruto.lower()
        texto = re.sub(r'[^\w\s]', '', texto)  # Remove pontuação
        texto = re.sub(r'\s+', ' ', texto)      # Remove múltiplos espaços
        return texto.strip()
