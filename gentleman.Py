importar sys
importar os

def load_config():
	list_of_wordlists = []
	com open("config.list") como f:
		list_of_wordlists = [linha para linha em f. read(). linhas divisas()]
	list_of_wordlists de retorno


def load_wordlist(wordlist_path):
	lista de palavras = []
	com open(wordlist_path, "rb") como f:
		wordlist = [linha para linha em f. read(). linhas divisas()]
	return wordlist (lista de palavras de retorno)

def log (msg):
	print(f"[*] {msg}")

def main():
	config = load_config()
	loaded_wordlists = []
	final_wordlist = []
	para wordlist em config:
		loaded_wordlists. append(load_wordlist(wordlist))
	log("listas de palavras carregadas do config.list")

	# Comece o processo de análise
	wordlist_pointer = 0
	log("começando a processar listas de palavras")
	enquanto loaded_wordlists:
		se len(loaded_wordlists[wordlist_pointer]) > 0:
			
			current_word = loaded_wordlists[wordlist_pointer]. pop(0)
			Se current_word:
				# Remova a barra no início (acontece em algumas listas de palavras e parafusos com filtragem duplicada)
				se current_word[0] == b'/':
					current_word = current_word[1:]

				Se não current_word  em final_wordlist:
					final_wordlist. append(current_word)


				# Vá para a próxima lista de palavras, ou se no final redefinir ponteiro para o início.
				se wordlist_pointer == len(loaded_wordlists)-1:
					wordlist_pointer = 0
				senão:
					wordlist_pointer += 1


		senão:
			log(f"Chegou ao fim da lista de palavras {wordlist_pointer}.")
			loaded_wordlists. pop(wordlist_pointer)
			wordlist_pointer = 0
	log(f"A lista de palavras final está pronta, com entradas {len(final_wordlist)}.")
	com open("output.txt", "wb") como f:
		log("Gravando na saída.txt")
		f. write(b"\n". junte(final_wordlist))

	# A lista de palavras final está pronta, imprimindo algumas informações.






se __name__ == '__main__':
	principal()
# load_wordlist("/usr/share/seclists/Discovery/Web-Content/raft-small-words.txt")
