# Universidade Federal do Tocantins _ Câmpus Palmas _ 22/05/2024
# Disciplina de Linguagens Formais e Autômatos
# Professor: Alexandre Rossini
# Aluno: Luiz Filipe de Souza Alves
# Trabalho Individual
# Link do projeto no GitHub: <https://github.com/LuFi-1227/Linguagens-Formais-e-Automatos>

import re as r #X)
import tkinter as t
from tkinter import filedialog

# Configuração das variaveis globais:
global resposta_nome
global resposta_cpf
global resposta_telefone
global resposta_email
global resposta
global botao1
global botao2
global dir
global escolha
dir = None
WIDTH = 50 # Constante que determina tamanho dos inputs (entrys)
Tipo_TELA = None
# Configuração das Expressões regulares
nome_regex = r"[a-zA-Z\ ]{1,50}"
cpf_regex = r"((\d{3}\.\d{3}\.\d{3}-\d{2})|\d{11})"
telefone_regex = r"[+]\d{2,3}((\(\d{2}\)[9]?\d{4}-\d{4})|(\d{2}[9]?\d{8}))"
email_regex = r"[\w\._]{2,}\@([\w]{2,}\.)+([\w]{3})+(([\w\.]{2,})+)?"

# Função de Validação:
def validaDados(nome, cpf, telefone, email):
    global resposta_nome
    global resposta_cpf
    global resposta_telefone
    global resposta_email

    resposta_nome['foreground'] = "red"
    resposta_cpf['foreground'] = "red"
    resposta_telefone['foreground'] = "red"
    resposta_email['foreground'] = "red"

    if nome:
        if r.fullmatch(nome_regex, nome):
            resposta_nome['text'] = "Nome valido!\n"
            resposta_nome['foreground'] = "green"
        else:
            resposta_nome['text'] = "Nome invalido!\n"
    else:
        resposta_nome['text'] = "Nome vazio!\n"
    
    if cpf:
        if r.fullmatch(cpf_regex, cpf):
            resposta_cpf['text'] = "CPF valido!\n"
            resposta_cpf['foreground'] = "green"
        else:
            resposta_cpf['text'] = "CPF invalido!\n"
    else:
        resposta_cpf['text'] = "CPF vazio!\n"
    
    if telefone:
        if r.fullmatch(telefone_regex, telefone):
            resposta_telefone['text'] = "Telefone valido!\n"
            resposta_telefone['foreground'] = "green"
        else:
            resposta_telefone['text'] = "Telefone invalido!\n"
    else:
        resposta_telefone['text'] = "Telefone vazio!\n"
    
    if email:
        if r.fullmatch(email_regex, email):
            resposta_email['text'] = "Email valido!\n"
            resposta_email['foreground'] = "green"
        else:
            resposta_email['text'] = "Email invalido!\n"
    else:
        resposta_email['text'] = "Email vazio!\n"

     # Devolve ao usuário a saída da Função pela janela

# Função de Configuração da Janela Principal:
def forms():
    # Deletando tela anterior antes de Iniciar a tela de formulario
    global botao2
    botao2.destroy()

    global botao1
    botao1.destroy()

    # Iniciando nova tela de formulário
    global Tipo_TELA
    Tipo_TELA = 1
    global janela
    global resposta_nome
    global resposta_cpf
    global resposta_telefone
    global resposta_email

    janela.title("Formulário do Usuário")

    texto_nome = t.Label(janela, text="Digite o seu nome:")
    texto_nome.config(font=("arial", 10))

    texto_cpf = t.Label(janela, text="Digite o seu CPF:")
    texto_cpf.config(font=("arial", 10))

    texto_telefone = t.Label(janela, text="Digite o seu telefone:")
    texto_telefone.config(font=("arial", 10))

    texto_email = t.Label(janela, text="Digite o seu email:")
    texto_email.config(font=("arial", 10))

    input_nome = t.Entry(janela)
    input_nome.config(font=("arial", 10), width=WIDTH)

    input_cpf = t.Entry(janela)
    input_cpf.config(font=("arial", 10), width=WIDTH)

    input_telefone = t.Entry(janela)
    input_telefone.insert(0, "+55")
    input_telefone.config(font=("arial", 10), width=WIDTH)

    input_email = t.Entry(janela)
    input_email.config(font=("arial", 10), width=WIDTH)

    Title = t.Label(janela, text="Preencha o Formulário")
    Title.config(font=("arial", 14))
    Title.grid(column=0, row=0, padx=0, pady=10)

    texto_nome.grid(column=0, row=1, padx=10, pady=0, sticky = 'w')
    input_nome.grid(column=0, row=2, padx=10, pady=10)

    texto_cpf.grid(column=0, row=3, padx=10, pady=0, sticky = 'w')
    input_cpf.grid(column=0, row=4, padx=10, pady=10)

    texto_telefone.grid(column=0, row=5, padx=10, pady=0, sticky = 'w')
    input_telefone.grid(column=0, row=6, padx=10, pady=10)

    texto_email.grid(column=0, row=7, padx=10, pady=0, sticky = 'w')
    input_email.grid(column=0, row=8, padx=10, pady=10, sticky = 'n')

    botão = t.Button(janela, text="Validar informações!", bg='#6495ED', fg='white', command=lambda: validaDados(input_nome.get(), input_cpf.get(), input_telefone.get(), input_email.get()))
    botão.grid(column=0, row=9)

    voltar = t.Button(janela, text="Voltar", command=choose)
    voltar.grid(column=0, row=10, sticky='w', padx=10, pady=10)

    resposta_nome = t.Label(janela, text="")
    resposta_nome.config(font=("arial", 12))
    resposta_nome.grid(column=0, row=11)

    resposta_cpf = t.Label(janela, text="")
    resposta_cpf.config(font=("arial", 12))
    resposta_cpf.grid(column=0, row=12)

    resposta_telefone = t.Label(janela, text="")
    resposta_telefone.config(font=("arial", 12))
    resposta_telefone.grid(column=0, row=13)

    resposta_email = t.Label(janela, text="")
    resposta_email.config(font=("arial", 12))
    resposta_email.grid(column=0, row=14)

# Função que procura um diretório
def diretorio():
    global dir 
    global escolha
    dir = filedialog.askopenfilename(initialdir="./", title="Selecione seu arquivo .txt", filetypes = (('text files', '*.txt'),('All files', '*.*')))
    escolha['text'] = dir

# Analisa as entradas do arquivo txt
def projeto_de_lex(entrada):
    entrada = r.sub("\n", '', entrada)
    if r.fullmatch(cpf_regex, entrada):
        return "<CPF, " + entrada + ">\n"
    if r.fullmatch(email_regex, entrada):
        return "<email, " + entrada + ">\n"
    if r.fullmatch(telefone_regex, entrada):
        return "<telefone, " + entrada + ">\n"
    if r.fullmatch(nome_regex, entrada):
        return "<nome, " + entrada + ">\n"
    if r.search("[=]{2}", entrada) or entrada == "":
        return entrada + "\n"
    return "<Nenhum tipo, " + entrada + ">\n"

# Função que faz leitura do txt escolhido pelo usuário
def lerArquivo():
    global dir
    global resposta
    if dir == None:
        resposta['foreground'] = "red"
        resposta['text'] = "Arquivo não escolhido!"
        return 0
    else:
        with open(dir, "r") as arquivo:
            log = open("./log.txt", "w")
            linha = arquivo.readline()
            while linha:
                log.write(projeto_de_lex(linha))
                linha = arquivo.readline()
            arquivo.close()
            log.close()
            resposta['foreground'] = "green"
            resposta['text'] = "Processamento finalizado, veja os logs!"

# Função que lê a partir do TXT:
def text():
    # Deletando tela anterior antes de Iniciar a tela de formulario
    global botao2
    botao2.destroy()

    global botao1
    botao1.destroy()

    # Iniciando nova tela de formulário
    global Tipo_TELA
    Tipo_TELA = 1

    global janela
    global dir
    global resposta
    global escolha
    janela.title("Ler a partir de Arquivo")

    Title = t.Label(janela, text="Escolha o arquivo:")
    Title.config(font=("arial", 14))
    Title.grid(column=0, row=0, padx=0, pady=10)

    botao = t.Button(janela, text="Escolher diretório do arquivo txt", command=diretorio)
    botao.grid(column=0, row=1, padx=10, pady=10)

    escolha = t.Label(janela, text="")
    escolha.grid(column=0, row=2)

    botao_final = t.Button(janela, text="Ler Arquivo!", command=lerArquivo)
    botao_final.grid(column=0, row=3, padx=10, pady=10)

    voltar = t.Button(janela, text="Voltar", command=choose)
    voltar.grid(column=0, row=4, sticky='w', padx=10, pady=10)
    
    resposta = t.Label(janela, text="")
    resposta.config(font=("arial", 12))
    resposta.grid(column=0, row=5)
    
# Função principal do Aplicativo
def choose():
    global botao1
    global botao2
    global janela
    global Tipo_TELA

    if Tipo_TELA != None:
        janela.destroy()
        janela = t.Tk()

    botao1 = t.Button(janela, text="Carregar configuração de formulário", command=forms, bg='#6495ED', fg='white')
    botao2 = t.Button(janela, text="Carregar configuração de arquivos de texto", command=text)

    botao1.grid(column=0, row=0, padx=10, pady=10)
    botao2.grid(column=0, row=1, padx=10, pady=10)

# Início da configuração da janela
janela = t.Tk()

choose()

janela.mainloop()
# Fim da configuração da Janela

"""
# Referências e Curiosidades:
## Menor nome do Mundo:
https://www.portalinsights.com.br/perguntas-frequentes/qual-e-a-pessoa-que-tem-o-menor-nome-do-mundo#:~:text=6%20Mart%C3%ADnez%20Medina%2C%20de%2020,o%20menor%20nome%20do%20mundo%E2%80%9D.

## Maior nome do mundo:
https://pt.wikipedia.org/wiki/Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu

## Site para gerar CPF:
https://www.4devs.com.br/gerador_de_cpf
"""