#Calcular a média final e a situação de um aluno seguindo as seguintes condições: 3 provas e obrigação de no
#mínimo 75% de freqüência. Serão fornecidos pelo usuário as notas das três provas e o percentual de freqüência 
#de cada aluno. Com estas informações fornecidas apresentar a média final do aluno e a sua situação – aprovado
#ou reprovado. Média para aprovação maior ou igual a 7.0.

prova1 = float(input("Insira a primeira nota: "))
prova2 = float(input("Insira a segunda nota: "))
prova3 = float(input("Insira a terceira nota: "))
freqpercent = int(input("Insira o percentual de frequência: "))
media = ((prova1+prova2+prova3)/3)

if media >= 7 and freqpercent >=75:
   print("Sua média final foi ",media,",",freqpercent,"% de frequência e a situação é APROVADO.")

if media >= 7 and freqpercent < 75:
   print("Sua média final foi ",media,",",freqpercent,"% de frequência e a situação é REPROVADO.")

if media <= 6 and freqpercent >=75:
   print("Sua média final foi ",media,",",freqpercent,"% de frequência e a situação é REPROVADO.")

if media <= 6 and freqpercent < 75:
   print("Sua média final foi ",media,",",freqpercent,"% de frequência e a situação é REPROVADO.")