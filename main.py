# TechFlow Solutions - Sistema de Logística
class LogisticaTasks:
    def __init__(self):
        self.entregas = []

    def adicionar_entrega(self, pacote, prioridade):
        if not pacote:
            return "Erro: Nome do pacote vazio"
        entrega = {"item": pacote, "prioridade": prioridade, "status": "Pendente"}
        self.entregas.append(entrega)
        return f"Sucesso: {pacote} adicionado ao fluxo."

    def listar_entregas(self):
        return self.entregas

    def atualizar_status(self, indice, novo_status):
        if 0 <= indice < len(self.entregas):
            self.entregas[indice]["status"] = novo_status
            return True
        return False

# Simulação rápida
if __name__ == "__main__":
    sistema = LogisticaTasks()
    print(sistema.adicionar_entrega("Carga Frágil - Setor A", "Alta"))
    print("Fila de Logística:", sistema.listar_entregas())
