from main import SistemaMultiagentes, setup_logging

def teste_rapido():
    setup_logging()
    sistema = SistemaMultiagentes()
    exemplos = [
        "João Silva precisa criar uma tarefa para o projeto XPTO até 30/06/2025.",
        "Adicionar Maria como responsável pelo item Marketing até 15-07-2025.",
        "Atualizar status da tarefa Documentação para concluído."
    ]
    for exemplo in exemplos:
        print(f"\n--- Testando: {exemplo}")
        resultado = sistema.processar_transcricao(exemplo)
        print("Resultado:", resultado)

if __name__ == "__main__":
    teste_rapido()
