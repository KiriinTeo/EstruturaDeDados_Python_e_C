nomes = []
matriculas = []
notasMatematica = []
notasPortugues = []
notasCiencias = []
medias = []

for i in range(3):
    nome = input("\nDigite o nome do aluno: ")
    nomes.append(nome)

    matricula = int(input("Digite a matrícula deste aluno: "))
    matriculas.append(matricula)

    Mat = float(input("Informe a nota de Matemática: "))
    notasMatematica.append(Mat)

    Port = float(input("Informe a nota de Português: "))
    notasPortugues.append(Port)

    Cien = float(input("Informe a nota de Ciências: "))
    notasCiencias.append(Cien)

    media = (Mat + Port + Cien) / 3
    medias.append(media)


def lista_Alunos():
    print("\nLista de Alunos e suas Médias:")
    for i in range(len(nomes)):
        print(f"Matrícula: {matriculas[i]}, Nome: {nomes[i]}, Média: {medias[i]:.2f}")

def buscar_aluno_por_matricula(matricula_busca):
    if matricula_busca in matriculas:
        indice = matriculas.index(matricula_busca)
        print(f"\nAluno encontrado: Nome: {nomes[indice]}, Média: {medias[indice]:.2f}")
    else:
        print("\nAluno não encontrado.")


def exibir_notas_matematica():
    print("\nNotas de Matemática de todos os alunos:")
    for i in range(len(nomes)):
        print(f"Matrícula: {matriculas[i]}, Nome: {nomes[i]}, Nota de Matemática: {notasMatematica[i]}")

#teste
lista_Alunos()

matricula_busca = int(input("\nDigite a matrícula do aluno que deseja buscar: "))
buscar_aluno_por_matricula(matricula_busca)

exibir_notas_matematica()
