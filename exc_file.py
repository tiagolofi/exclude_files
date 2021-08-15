
import os

PATH_DESKTOP = 'C:/Users/usuario/Desktop/'
PATH_DOC = 'C:/Users/usuario/Documents/'

def limpezaDOCDESKTOP(path_doc, path_desktop):
	print('\nBuscando arquivos indesejados...\n')
	files_doc = os.listdir(path_doc)
	files_desktop = os.listdir(path_desktop)
	files_exc_doc = list(filter(lambda i: i[0:5] == 'temp_', files_doc))
	files_exc_desktop = list(filter(lambda i: i[0:5] == 'temp_', files_desktop))
	n_files = len(files_exc_doc) + len(files_exc_desktop)
	if n_files < 1:
		return print('Não há arquivos indesejados para remover...\n')
	else: 
		for i in files_exc_doc:
			os.remove(path_doc+i)
			print('Removendo o arquivo '+i+'\n')
		for j in files_exc_desktop:
			os.remove(path_desktop+j)
			print('Removendo o arquivo '+j+'\n')

	return print(str(n_files)+' removidos com sucesso!\n')

limpezaDOCDESKTOP(path_doc=PATH_DOC, path_desktop=PATH_DESKTOP)