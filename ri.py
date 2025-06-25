# Gerador de Políticas de Segurança da Informação - CLI

import os

def menu():
    print("""
    ================= MENU =================
    [1] Política de Segurança da Informação
    [2] Política de Controle de Acesso
    [3] Política de Gerenciamento de Riscos
    [4] Política de Uso Aceitável
    [5] Política de Conformidade
    [6] Política de Backup e Recuperação de Desastres
    [7] Política de Incidentes de Segurança
    [8] Política de Treinamento e Conscientização
    [0] Sair
    =======================================
    """)
    return input("Escolha a política que deseja gerar: ")

def perguntar(perguntas):
    respostas = {}
    for p in perguntas:
        resposta = input(f"{p}\n> ")
        respostas[p] = resposta
    return respostas

def gerar_documento(nome_politica, respostas):
    with open(f"{nome_politica}.txt", "w", encoding="utf-8") as f:
        f.write(f"POLÍTICA: {nome_politica.upper()}\n\n")
        for pergunta, resposta in respostas.items():
            f.write(f"{pergunta}\nResposta: {resposta}\n\n")
    print(f"\nDocumento '{nome_politica}.txt' gerado com sucesso!\n")

politicas = {
    "1": ("Política de Segurança da Informação", [
        
        "Qual o tamanho da empresa?",
        "Que tipo de dados sensíveis são tratados?",
        "Existe criptografia em repouso e em trânsito?",
        "Há classificação da informação?",
        "Existem controles de integridade e disponibilidade?",
        "Há um responsável pela Segurança da Informação?"
    ]),
    "2": ("Política de Controle de Acesso", [

         "Define de acessos a sistemas, aplicações e dados determinados, com base necessidades e responsabilidades de cada usuário. "

        "Os acessos são concedidos com base em quê?",
        "Há uso de autenticação multifator (MFA)?",
        "Existem revisões periódicas de acesso?",
        "Os acessos são revogados após desligamento?",
        "Os sistemas possuem controle de sessão?"
    ]),
    "3": ("Política de Gerenciamento de Riscos", [
        "A organização já possui uma matriz de riscos?",
        "Quais frameworks são utilizados?",
        "Há um processo formal de tratamento de riscos?",
        "Com que frequência são feitas análises de risco?",
        "Quem é responsável pelo processo?"
    ]),
    "4": ("Política de Uso Aceitável", [
        "Quais recursos os usuários podem usar?",
        "Quais são as restrições de uso?",
        "É permitido uso pessoal dos recursos?",
        "Existe política de monitoramento?",
        "Existe termo de ciência para os usuários?"
    ]),
    "5": ("Política de Conformidade", [
        "A empresa está sujeita a quais leis e normas?",
        "Quem acompanha as atualizações regulatórias?",
        "Há auditorias internas ou externas?",
        "Há um programa de conformidade estruturado?",
        "Como os dados são tratados segundo as leis?"
    ]),
    "6": ("Política de Backup e Recuperação de Desastres", [
        "Com que frequência os backups são feitos?",
        "Onde são armazenados os backups?",
        "Os backups são testados regularmente?",
        "Existe plano de continuidade de negócios (PCN)?",
        "Quem é o responsável pelo plano?"
    ]),
    "7": ("Política de Incidentes de Segurança", [
        "Existe um plano de resposta a incidentes?",
        "Qual o tempo máximo aceitável de resposta?",
        "Existe uma equipe responsável por incidentes?",
        "Incidentes são registrados? Como?",
        "Os usuários são instruídos a reportar?"
    ]),
    "8": ("Política de Treinamento e Conscientização", [
        "Com que frequência os treinamentos são realizados?",
        "O conteúdo é personalizado por função?",
        "Existem simulações de ataques (ex: phishing)?",
        "Há registro de participação nos treinamentos?",
        "Quem é o responsável pelo programa?"
    ])
}

while True:
    opcao = menu()
    if opcao == "0":
        print("Saindo...")
        break
    elif opcao in politicas:
        nome, perguntas = politicas[opcao]
        print(f"\n>> Gerando {nome} <<\n")
        respostas = perguntar(perguntas)
        gerar_documento(nome, respostas)
    else:
        print("\nOpção inválida. Tente novamente.\n")
