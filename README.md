# TechFlow Task Manager - Sistema de Gestão Logística

## 1. Introdução e Objetivo
Este projeto foi desenvolvido para a **TechFlow Solutions**, atendendo a uma startup de logística. O objetivo é fornecer um sistema de gerenciamento de tarefas que permita o acompanhamento do fluxo de trabalho em tempo real, utilizando as melhores práticas da Engenharia de Software.

## 2. Metodologia de Desenvolvimento (Unidade 1)
Adotámos as **Metodologias Ágeis**, especificamente o framework **Scrum** combinado com um quadro **Kanban**. 
- **Porquê Ágil?** Devido à necessidade de flexibilidade e resposta rápida a mudanças, conforme os princípios do Manifesto Ágil.
- **Gestão:** O progresso é monitorizado através do GitHub Projects, utilizando limites de WIP (Work in Progress) para evitar gargalos.

## 3. Levantamento de Requisitos (Unidade 2)
### Requisitos Funcionais (RF)
* **RF01:** O sistema deve permitir a criação de tarefas de entrega.
* **RF02:** O sistema deve permitir a listagem de tarefas pendentes.
* **RF03:** O sistema deve permitir marcar tarefas como concluídas.

### Requisitos Não Funcionais (RNF)
* **RNF01:** O sistema deve garantir a integridade dos dados das tarefas.
* **RNF02:** O sistema deve possuir testes automatizados (Garantia de Qualidade).
* **RNF03:** A interface deve ser simples e intuitiva (Usabilidade).

## 4. Modelagem UML (Unidade 3)
O sistema foi planeado utilizando Diagramas de Casos de Uso para identificar as interações dos atores (Gestor de Logística) com as funcionalidades principais.

## 5. Gestão de Mudanças (Unidade 4)
Durante o desenvolvimento, simulámos uma mudança de escopo (adição de níveis de prioridade). Esta mudança foi gerida através do refinamento do Backlog, demonstrando a adaptabilidade do processo ágil sem comprometer o cronograma principal.

---
### 6. Gestão de Mudanças e Qualidade
Durante o desenvolvimento da Sprint 1, identificamos a necessidade de incluir um campo de 'Prioridade' nas entregas, algo não previsto no escopo inicial. Seguindo a **Agilidade**, o Product Owner priorizou essa mudança no Backlog, e a implementação foi realizada sem atrasar o cronograma principal.

Para garantir a confiabilidade, o projeto utiliza **GitHub Actions** para Integração Contínua (CI), assegurando que cada nova funcionalidade seja testada antes da entrega final.

graph TD
    A[Operador Logístico] -->|Cria Tarefa| B(Sistema TechFlow)
    B -->|Valida Dados| C{Dados OK?}
    C -->|Sim| D[Tarefa Salva no Banco]
    C -->|Não| E[Exibir Erro]
