# Importar as bibliotecas necessárias

import os
import csv

# Função para carregar o arquivo CSV.

print('Diretorio atual: ', os.getcwd())

def carregar_arquivo(nome_arquivo):
	try:
		print(f'Tentando abrir o arquivo: {nome_arquivo}')
		with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
			leitor = csv.reader(arquivo)
			dados = list(leitor)
			return dados
	except FileNotFoundError:
		print('Arquivo não foi encontrado. Tente novamente!')

# Função mostrar os dados.

def exibir_dados(dados):
	for linha in dados:
		print(linha)

# Função para calcular a media de uma coluna númerica.

def calcular_media(dados, coluna):
	try:
		valores = [float(linha[coluna]) for linha in dados[1:]]
		media = sum(valores) / len(valores)
		return media
	except IndexError:
		print('Erro: Coluna Invalida')
	return None

# Função principal.

def main ():
	nome_arquivo = input('Digite o nome do arquivo CSV: ')
	dados = carregar_arquivo(nome_arquivo)
	if dados:
		print('\nDados do arquivo: ')
		exibir_dados(dados)

		coluna = int(input('\nDigite o indice da coluna para calcular a media (0 para primeira coluna): '))
		media = calcular_media(dados, coluna)
		if media is not None:
			print(f'Media da coluna {coluna}: {media: .2f}')

#inicio do programa.

if __name__ == '__main__':
	main()