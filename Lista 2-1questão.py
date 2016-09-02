#ALUNO: DANIEL FARIAS HENRIQUES - 1610014278
#PROGRAMA: NOTA DE ESPECTADORES SOBRE UM FILME

cont_otimo_o=0
cont_bom_b=0
cont_regular_r=0

for i in range(10):
    opiniao = int(input("DEIXE AQUI SUA OPINIÃO, O QUE VOÇÊ ACHOU DO FILME EXIBIDO EM NOSSA SALA DE CINEMA? 1 PARA REGULAR :S, 2 PRA BOM :) e 3 PARA ÓTIMO :D : "))
    if opiniao == 1:
        cont_otimo_o = cont_otimo_o + 1
    elif opiniao == 2:
        cont_bom_b = cont_bom_b + 1
    else:
        cont_regular_r = cont_regular_r + 1

print('Quantidade de opiniao em otimo = %d' % cont_otimo_o)
print('Quantidade de opiniao em bom = %d' % cont_bom_b)
print('Quantidade de opiniao em regular = %d' % cont_regular_r)

