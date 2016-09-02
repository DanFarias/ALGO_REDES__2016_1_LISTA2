#ALUNO: DANIEL FARIAS HENRIQUES - 1610014278
#PROGRAMA: NOTA DE ESPECTADORES SOBRE UM FILME

avaliacao = [int(input("DEIXE AQUI SUA OPINIÃO, O QUE VOÇÊ ACHOU DO FILME EXIBIDO EM NOSSA SALA DE CINEMA? 1 PARA REGULAR :S, 2 PRA BOM :) e 3 PARA ÓTIMO :D : ")),
             int(input("DEIXE AQUI SUA OPINIÃO, O QUE VOÇÊ ACHOU DO FILME EXIBIDO EM NOSSA SALA DE CINEMA? 1 PARA REGULAR :S, 2 PRA BOM :) e 3 PARA ÓTIMO :D : ")),
             int(input("DEIXE AQUI SUA OPINIÃO, O QUE VOÇÊ ACHOU DO FILME EXIBIDO EM NOSSA SALA DE CINEMA? 1 PARA REGULAR :S, 2 PRA BOM :) e 3 PARA ÓTIMO :D : ")),
             int(input("DEIXE AQUI SUA OPINIÃO, O QUE VOÇÊ ACHOU DO FILME EXIBIDO EM NOSSA SALA DE CINEMA? 1 PARA REGULAR :S, 2 PRA BOM :) e 3 PARA ÓTIMO :D : ")),
             int(input("DEIXE AQUI SUA OPINIÃO, O QUE VOÇÊ ACHOU DO FILME EXIBIDO EM NOSSA SALA DE CINEMA? 1 PARA REGULAR :S, 2 PRA BOM :) e 3 PARA ÓTIMO :D : ")),]

regular = 0
bom = 0
otimo = 0
invalido = 0

for opniao in avaliacao:
  if opniao == 3:
    otimo = otimo + 1
  if opniao == 2:
    bom = bom + 1
  if opniao == 1:
    regular = regular + 1
  if opniao > 3:
    invalido = invalido + 1

print(" %d PESSOAS QUE ACHARAM ÓTIMO" % otimo)
print(" %d PESSOAS QUE ACHARAM BOM" % bom)
print(" %d PESSOAS QUE ACHARAM REGULAR" % regular)
print(" %d PESSOAS QUE ENTRARAM COM NUMEROS INVALIDOS" % invalido)