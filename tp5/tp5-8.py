alunos = [["luiz",5,7,4],["paulo",5,6,7],["maria",3,5,2],["luiza",4,5,6],["felipe",8,9,7],["fabiana",2,6,4]]
maior = -1
allmedia = 0
for aluno in alunos:
    soma = aluno[1] + aluno[2] + aluno[3]
    media = (soma / 3)
    allmedia += media
    print(aluno[0], round(media,1))
    if (media >= maior):
        maior = media
        melhoraluno = aluno[0]
print("media da turma:", round(allmedia/len(alunos),1), "melhor aluno:", melhoraluno)