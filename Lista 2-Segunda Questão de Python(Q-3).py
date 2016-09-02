#Aluno:Daniel Farias Henriques
#Programa: Calculo de nota

nota1 = float(input("Digite aqui a sua primeira Nota: "))
nota2 = float(input("Digite aqui a sua segunda Nota: "))
nota3 = float(input("Digite aqui a sua terceira Nota: "))

media = (nota1 + nota2 + nota3)/3
if media <= 4:
        print(media, "Você está REPROVADO")
elif media >= 5 and media < 7:
        print(media, "Você irar fazer a PROVA FINAL")
else:
        print(media, "Parabéns você foi APROVADO")