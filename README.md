# TechFlow Logistics System

## 1. Sobre o Projeto
Este sistema foi desenvolvido pela **TechFlow Solutions** para uma startup de logística. O objetivo é gerenciar o fluxo de entregas em tempo real, garantindo priorização e eficiência.

## 2. Metodologia de Trabalho
Utilizamos o **Framework Scrum** com suporte visual do **Kanban**. 
- **Ciclo de Vida:** Iterativo e Incremental.
- **Gestão Visual:** Uso de quadro Kanban no GitHub Projects.

## 3. Arquitetura do Sistema (UML)
Abaixo, representamos o fluxo básico de interação do usuário com o sistema:


graph TD
    A[Operador Logístico] -->|Cadastra Entrega| B(Sistema TechFlow)
    B -->|Processa Dados| C{Dados Válidos?}
    C -->|Sim| D[Tarefa Salva e Listada]
    C -->|Não| E[Alerta de Erro] 


## 4. Engenharia de Requisitos
Requisitos Funcionais (RF)
RF01: O sistema deve permitir o cadastro de novas tarefas de logística.

RF02: O sistema deve permitir a atualização do status da entrega.

RF03: O sistema deve listar tarefas por ordem de prioridade.

Requisitos Não Funcionais (RNF)
RNF01: Desenvolvimento em Python 3.

RNF02: Garantia de qualidade via GitHub Actions.

5. Gestão de Mudanças e Qualidade
Durante a primeira sprint, o cliente solicitou a inclusão de um campo de "Prioridade". Como utilizamos métodos ágeis, a mudança foi integrada ao backlog e implementada imediatamente no arquivo main.py.

