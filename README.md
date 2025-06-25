**projeto em andamento**

# Gerador de Políticas de Segurança da Informação 

Este projeto é um **gerador automatizado de documentos de políticas de segurança da informação**, executado via terminal (até o momento) , desenvolvido em **Python**.   
Auxilia  na criação de documentos de políticas formais com base em boas práticas e normas de segurança da informação.

---
## Objetivo

Fornecer uma maneira simples, interativa e estruturada de gerar políticas de segurança da informação, com base nas necessidades da empresa e em perguntas-chave para cada tipo de política.

---
##  Funcionalidades

* Menu interativo com 8 tipos de políticas disponíveis
* Questionário personalizado para cada política
* Geração automática de documentos `.txt` baseados nas respostas do usuário
* Simples de executar e adaptar para diferentes contextos empresariais

---

## 📑 Políticas Disponíveis

1. **Política de Segurança da Informação**
2. **Política de Controle de Acesso**
3. **Política de Gerenciamento de Riscos**
4. **Política de Uso Aceitável**
5. **Política de Conformidade**
6. **Política de Backup e Recuperação de Desastres**
7. **Política de Incidentes de Segurança**
8. **Política de Treinamento e Conscientização**

---

##  Como Usar

### 1. Pré-requisitos

* Python 3 instalado

### 2. Executar o script

```bash
python gerador_politicas_si.py
```

### 3. Escolher a política

Um menu será apresentado com as 8 opções. Escolha o número correspondente à política que deseja gerar.

### 4. Responder às perguntas

Você será guiado por um conjunto de perguntas específicas para a política escolhida. Suas respostas serão usadas para compor o documento.

### 5. Documento gerado

Ao final, será criado um arquivo `.txt` no mesmo diretório com o nome da política, contendo as perguntas e respostas.


---

## 💡 Exemplos de Uso

### Geração da Política de Uso Aceitável:

```
> Escolha a política que deseja gerar: 4
> Quais recursos os usuários podem usar?
Resposta: Computadores da empresa, rede interna, e-mail corporativo.
...

Documento 'Política de Uso Aceitável.txt' gerado com sucesso!
```
# Melhorias em andamento

* Exportação em PDF ou DOCX
* Interface Web (HTML, CSS, JS)
* Armazenamento em banco de dados
* Integração com ferramentas de compliance (ex: OneTrust, GRC tools)
* Tradução para outros idiomas (inglês, espanhol)
* mais questões
* mais abrangencia
* tornar o corpo de cada documento mais completo e personalizado
  
---

## Importância do Projeto

Este gerador contribui para a padronização de documentos fundamentais em Segurança da Informação e pode ser utilizado como ponto de partida para empresas que ainda não possuem uma estrutura formal de GRC (Governança, Riscos e Conformidade).


---

## Autora

Desenvolvido por \Kalli.

Caso tenha dúvidas, sugestões ou queira contribuir, entre em contato ou abra uma issue neste repositório.

---
