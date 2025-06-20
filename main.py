import os
import logging
from agentes.agente_pre import AgentePre
from agentes.agente_analista import AgenteAnalista
from agentes.agente_validador import AgenteValidador
from agentes.agente_mapeamonday import AgenteMapeaMonday
from agentes.agente_genio import AgenteGenio
from agentes.agente_executor import AgenteExecutor
from agentes.agente_boss import AgenteBoss

# Configuração básica de logging
def setup_logging():
    log_level = os.getenv("LOG_LEVEL", "INFO")
    log_file = os.getenv("LOG_FILE", "agentes.log")
    logging.basicConfig(
        level=getattr(logging, log_level),
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
    )

class SistemaMultiagentes:
    """
    Orquestrador principal do sistema multiagentes para Monday.com
    """
    def __init__(self):
        self.pre = AgentePre()
        self.analista = AgenteAnalista()
        self.validador = AgenteValidador()
        self.mapeamonday = AgenteMapeaMonday()
        self.genio = AgenteGenio()
        self.executor = AgenteExecutor()
        self.boss = AgenteBoss()

    def processar_transcricao(self, texto_bruto):
        logging.info("Iniciando processamento da transcrição...")
        # 1. Limpeza e pré-processamento
        texto_limpo = self.pre.limpar_texto(texto_bruto)
        logging.info(f"Texto limpo: {texto_limpo}")
        
        # 2. Análise semântica e extração de entidades/intenções
        dados_semi = self.analista.analisar(texto_limpo)
        logging.info(f"Entidades/intenções extraídas: {dados_semi}")
        
        # 3. Validação e resolução de ambiguidades/conflitos
        validacao = self.validador.validar(dados_semi)
        if validacao.get('necessita_intervencao'):
            logging.warning("Necessita intervenção humana: %s", validacao.get('mensagem'))
            return {'status': 'pendente', 'motivo': validacao.get('mensagem')}
        logging.info("Dados validados: %s", validacao)
        
        # 4. Mapeamento para payload de integração
        payload = self.mapeamonday.mapear(validacao)
        logging.info(f"Payload mapeado: {payload}")
        
        # 5. Decisão de rota (MCP ou API direta)
        rota, payload_final = self.genio.decidir_rota(payload)
        logging.info(f"Rota escolhida: {rota}")
        
        # 6. Execução da operação
        resultado_execucao = self.executor.executar(rota, payload_final)
        logging.info(f"Resultado da execução: {resultado_execucao}")
        
        # 7. Supervisão e feedback
        self.boss.registrar_feedback(texto_bruto, resultado_execucao)
        logging.info("Processamento finalizado.")
        return resultado_execucao

if __name__ == "__main__":
    setup_logging()
    sistema = SistemaMultiagentes()
    print("Sistema Multiagentes para Monday.com - V2")
    texto = input("Digite ou cole a transcrição/comando:\n")
    resultado = sistema.processar_transcricao(texto)
    print("\nResultado:")
    print(resultado)
