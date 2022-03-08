import filecmp 

LINE_BREAK = "\n"
fileA = "C:\\compareFiles\\files\\a.txt"
fileB = "C:\\compareFiles\\files\\b.txt"
pathResult = "C:\\Users\\Erison\\Documents\\python\\compareFiles\\files\\r.txt"

print("Comparando arquivos.")
comparisonResult = filecmp.cmp(fileA, fileB, shallow=False) #Shallow False para comparar conteúdo do arquivo, não só metadados

# Abrindo aquivos para comparação linha a linha (atributo enconding disponível se necessário)
print("Abrindo arquivos para comparação linha a linha.")
openFileA = open(fileA)
rowsFileA = openFileA.readlines()
openFileB = open(fileB)
rowsFileB = openFileB.readlines()

if comparisonResult == False:
    rowCount = 0
  
    # Criando arquivo para gravação do resultado da comparação
    fileResult = open(pathResult, "w+") # w+ = cria arquivo se não existir e habilita modo de gravação
    fileResult.close()
  
    # Varrendo linhas do arquivo A
    print("Iniciando comparação linha a linha.")
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
            print("Linhas do arquivo A fora do limite de linhas do arquivo B.")
            break
        rowCount += 1
else:
    print("Os arquivos são iguais.")

print("Comparação finalizada.")
