import filecmp 
from datetime import datetime

LINE_BREAK = "\n"
DATE_FORMAT = '%d/%m/%Y %H:%M:%S'

# Parametrizar variáveis abaixo
pathFileA = "C:\\compareFiles\\files"
pathFileB = "C:\\compareFiles\\files"
nameFileA = "a.txt"
nameFileB = "b.txt"

fileA = pathFileA + "\\" + nameFileA
fileB = pathFileB + "\\" + nameFileB
pathResult = "C:\\compareFiles\\r.txt"

print("Comparando arquivos. Início em " + str(datetime.today().strftime(DATE_FORMAT)))
comparisonResult = filecmp.cmp(fileA, fileB, shallow=False) #Shallow False para comparar conteúdo do arquivo, não só metadados
print("Comparando arquivos. Finalizado em " + str(datetime.today().strftime(DATE_FORMAT)))

if comparisonResult == False:
    rowCount = 0
    
    # Abrindo aquivos para comparação linha a linha (atributo enconding disponível se necessário)
    print("Comparando arquivos linha a linha. Início em " + str(datetime.today().strftime(DATE_FORMAT)))
    print("Abrindo arquivos.")
    openFileA = open(fileA)
    rowsFileA = openFileA.readlines()
    openFileB = open(fileB)
    rowsFileB = openFileB.readlines()
  
    # Criando arquivo para gravação do resultado da comparação
    fileResult = open(pathResult, "w+") # w+ = cria arquivo se não existir e habilita modo de gravação
    fileResult.close()
  
    # Varrendo linhas do arquivo A
    print("Comparando linhas.")
    for rowFileA in rowsFileA: 
        if rowCount < len(rowsFileB):
            rowFileA = rowFileA.replace(LINE_BREAK, "")
            rowFileB = rowsFileB[rowCount].replace(LINE_BREAK, "")
            if rowFileA != rowFileB:
                messageRow = "Linha " + str(rowCount + 1) + " está incorreta.\nConteúdo: " + rowFileA + "\nEsperado: " + rowFileB + "\n\n"
                fileResult = open(pathResult, "a") # a = abre arquivo para gravação e habilita modo "append" para não sobrescrever
                fileResult.write(messageRow)
                fileResult.close()
        else:
            print("Linhas do arquivo " + nameFileA + " fora do limite de linhas do arquivo " + nameFileB + ".")
            break
        rowCount += 1
    print("Comparando arquivos linha a linha. Finalizado em " + str(datetime.today().strftime(DATE_FORMAT)))
else:
    print("Os arquivos são iguais.")
print("Comparação finalizada.")
