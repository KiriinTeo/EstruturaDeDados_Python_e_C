#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <locale.h>

struct Carro {
    char marca[50];
    char modelo[50];
    int anoFabri;
    float preco;
};

int main() {
    setlocale(LC_NUMERIC, "pt_BR.UTF-8");

    while (1) {
        int escolha;

        printf("\n\nBem-vindo! Esta é uma lista unindo estruturas de dados relevantes revisados em 2024 (não todas, até 01/07/2024).\n");
        printf("Funções disponíveis:\n");
        printf("1. Definição de Triângulos\n");
        printf("2. Cálculo de Fatorial\n");
        printf("3. Cálculo de IMC\n");
        printf("4. Sequência de Fibonacci\n");
        printf("5. Urna de Eleição\n");
        printf("6. Média de Turma\n");
        printf("7. Registro de Carros\n");
        printf("8. Registro de Notas em Arquivo\n");
        printf("\nDigite um número para acessar a função (qualquer outro número para sair): ");
        scanf("%d", &escolha);

        switch (escolha) {
            case 1: {
                float lad1, lad2, lad3;

                printf("Informe o comprimento dos lados do triângulo (3 valores): ");
                scanf("%f %f %f", &lad1, &lad2, &lad3);

                if (lad1 == 0 || lad2 == 0 || lad3 == 0) {
                    printf("O triângulo não é possível! (não há lado de comprimento 0 em um triângulo)\n");
                } else if (lad1 + lad2 > lad3 && lad2 + lad3 > lad1 && lad1 + lad3 > lad2) {
                
                    if (lad1 == lad2 && lad2 == lad3) {
                        printf("É um Triângulo Equilátero.\n");
                        break;
                    } else if (lad1 == lad2 || lad2 == lad3 || lad1 == lad3) {
                        printf("É um Triângulo Isósceles.\n");
                        break;
                    } else {
                        printf("É um Triângulo Escaleno.\n");
                        break;
                    }
                } else {
                    printf("O triângulo não é possível! (as medidas não formam um triângulo válido)\n");
                }
                break;
            }


            case 2: {
                int i = 1, n, f = 1;
                printf("Digite um número inteiro não-negativo: ");
                scanf("%d", &n);

                while (i <= n) {
                    f *= i;
                    i++;
                }
                printf("Fatorial = %d\n", f);
                break;
            }

            case 3: {
                float peso, altura, imc;
                printf("Informe o seu peso: ");
                scanf("%f", &peso);

                printf("Informe a sua altura: ");
                scanf("%f", &altura);

                while (altura <= 0 || peso <= 0) {
                    printf("Altura e peso inválidos. Informe novamente.\n");
                    printf("Informe o seu peso: ");
                    scanf("%f", &peso);
                    printf("Informe a sua altura: ");
                    scanf("%f", &altura);
                }

                imc = peso / (altura * altura);
                if (imc < 18.5) {
                    printf("Sua classificação: Abaixo do peso (IMC: %.2f)\n", imc);
                    break;
                } else if (imc < 25.0) {
                    printf("Sua classificação: Peso normal (IMC: %.2f)\n", imc);
                    break;
                } else if (imc < 30.0) {
                    printf("Sua classificação: Sobrepeso (IMC: %.2f)\n", imc);
                    break;
                } else if (imc < 35.0) {
                    printf("Sua classificação: Obesidade grau 1 (IMC: %.2f)\n", imc);
                    break;
                } else if (imc < 40.0) {
                    printf("Sua classificação: Obesidade grau 2 (IMC: %.2f)\n", imc);
                    break;
                } else {
                    printf("Sua classificação: Obesidade grau 3 (IMC: %.2f)\n", imc);
                    break;
                }
                break;
            }

            case 4: {
                int fibbonaci, num = 0, unid, add = 1;
                printf("Digite quantos números à frente na sequência exibir: ");
                scanf("%d", &unid);

                printf("Sequência: %d, %d, ", num, add);
                for (int cont = 0; cont < unid; cont++) {
                    fibbonaci = num + add;
                    num = add;
                    add = fibbonaci;

                    printf("%d", fibbonaci);
                    if (cont < unid - 1) {
                        printf(", ");
                    }
                }
                printf("\n");
                break;
            }

            case 5: {
                int votoNulo = 0, votoWant = 0, votoPaf = 0, votoHerme = 0, votoBranco = 0;
            int alunos;
            char rep;
            float porcNulo, porcBranco, porcWant, porcPaf, porcHerme;
    
            printf("Votação de Representante de Sala.\nPor Favor, diga quantos votantes teremos: ");
            scanf("%d", &alunos);
    
            int votos = 0;
            for(; votos < alunos; votos++){
            
                printf("Agora selecione o candidato\n\nHermenigildo = H,h\nPafônsia = P,p\nWantuildes = W,w\nBranco = B,b\nNulo = Qualquer outra tecla\n\n");;
                scanf(" %c", &rep);
            
                    switch(rep){
                
                        case 'H':
                        case 'h':
                        votoHerme++;
                        break;
                
                        case 'P':
                        case 'p':
                        votoPaf++;
                        break;
                    
                        case 'W':
                        case 'w':
                        votoWant++;
                        break;
                    
                        case 'B':
                        case 'b':
                        votoHerme++; 
                        votoPaf++; 
                        votoWant++;
                        votoBranco++;
                        break;
                    
                        default:
                        votoNulo++;
                        break;
                   }
            
            }
            porcHerme = ((float) votoHerme / votos) * 100; 
            porcPaf = ((float) votoPaf / votos) * 100; 
            porcWant = ((float) votoWant / votos) * 100;
            porcNulo = ((float) votoNulo / votos) * 100;
            porcBranco = ((float) votoBranco / votos) * 100;
            
            if(votoHerme > votoPaf && votoHerme > votoWant){
            
                printf("Resultados da Votação: \nTotal de Votos = %d\nHermenigildo = %.1f\nPafônsia = %.1f\nWantuildes = %.1f\nBranco = %.1f\nNulo = %.1f\n", votos, porcHerme, porcPaf, porcWant, porcBranco, porcNulo);
                printf("O vencedor é: Hermenigildo, com %d votos", votoHerme);
                break;
            }
            else if (votoPaf > votoHerme && votoPaf > votoWant){
            
                printf("Resultados da Votação: \nTotal de Votos = %d\nHermenigildo = %.1f\nPafônsia = %.1f\nWantuildes = %.1f\nBranco = %.1f\nNulo = %.1f\n", votos, porcHerme, porcPaf, porcWant, porcBranco, porcNulo);
                printf("O vencedor é: Pafônsia, com %d votos", votoPaf);
                break;
            }
            else if (votoWant > votoHerme && votoWant > votoPaf){
            
                printf("Resultados da Votação: \nTotal de Votos = %d\nHermenigildo = %.1f\nPafônsia = %.1f\nWantuildes = %.1f\nBranco = %.1f\nNulo = %.1f\n", votos, porcHerme, porcPaf, porcWant, porcBranco, porcNulo);
                printf("O vencedor é: Wantuildes, com %d votos", votoWant);
                break;
            }
            else if (votoWant == votoPaf || votoWant == votoHerme || votoHerme == votoPaf) {
            
                printf("Empate Detectado: Segundo Turno\n");
                printf("Por Favor, vote novamente\n\n");
                votoNulo = 0;
                votos = -1;
            }
            
            do{
                if (votoHerme == votoPaf){
                        
                    votoHerme = 0;
                    votoPaf = 0;
                    printf("Escolha entre:\n\nHermenigildo = H,h\nPafônsia = P,p\nNulo = Qualquer Tecla\n");
                    scanf(" %c", &rep);
                        
                        switch(rep){
                                
                            case 'H':
                            case 'h':
                                votoHerme++;
                                break;
                                   
                            case 'P':
                            case 'p':
                                votoPaf++;
                                break; 
                                
                            default:
                                votoNulo++;
                                break;
                        }
                }         
                else if (votoPaf == votoWant){
                        
                    votoPaf = 0;
                    votoWant = 0;
                    printf("Escolha entre:\n\nPafônsia = P,p\nWantuildes = W,w\nNulo = Qualquer Tecla\n");
                    scanf(" %c", &rep);
                        
                        switch(rep){
                                
                            case 'W':
                            case 'w':
                                votoWant++;
                                break;
                                   
                            case 'P':
                            case 'p':
                                votoPaf++;
                                break;   
                                    
                            default:
                                votoNulo++;
                                break;
                        }
                }
                            
                else if (votoHerme == votoWant){
                        
                    votoHerme = 0;
                    votoWant = 0;
                    printf("Escolha entre:\n\nHermenigildo = H,h\nWantuildes = W,w\nNulo = Qualquer Tecla\n");
                    scanf(" %c", &rep);
                        
                        switch(rep){
                                
                            case 'W':
                            case 'w':
                                votoWant++;
                                break;
                                   
                            case 'H':
                            case 'h':
                                votoHerme++;
                                break;  
                                
                            default:
                                votoNulo++;
                                break;
                        }
                }
                votos++;
            }
            while(votos < alunos);
                
            porcHerme = ((float) votoHerme / votos) * 100; 
            porcPaf = ((float) votoPaf / votos) * 100; 
            porcWant = ((float) votoWant / votos) * 100;
            porcNulo = ((float) votoNulo / votos) * 100;
                
            if (votoHerme > votoPaf && votoHerme > votoWant) {
                printf("O vencedor do segundo turno é: Hermenigildo, com %.1f votos\nForam: %d dos votos nulos\n", porcHerme, votoNulo);
                break;
            } 
            else if (votoPaf > votoHerme && votoPaf > votoWant) {
                printf("O vencedor do segundo turno é: Pafônsia, com %.1f votos\nForam: %d votos nulos\n", porcPaf, votoNulo);
                break;
            } 
            else if (votoWant > votoHerme && votoWant > votoPaf) {
                printf("O vencedor do segundo turno é: Wantuildes, com %.1f votos\nForam: %d dos votos nulos\n", porcWant, votoNulo);
                break;
            } 
            else {
                printf("Segundo turno empatado\n");
            }
            break;
            }

            case 6: {
                int alunos, incr = 1;
                float nota, total = 0, med;

                printf("Quantos alunos tem a sala? ");
                scanf("%d", &alunos);

                float* notas = (float*)malloc(alunos * sizeof(float));
                if (notas == NULL) {
                    printf("Erro na alocação de memória!\n");
                    return 1;
                }

                while (incr <= alunos) {
                    printf("Digite a nota do aluno %d: ", incr);
                    scanf("%f", &nota);

                    if (nota >= 0 && nota <= 10) {
                        notas[incr - 1] = nota;
                        total += nota;
                        incr++;
                    } else {
                        printf("Nota inválida. Informe novamente.\n");
                    }
                }

                med = total / alunos;
                printf("A média da sala é: %.2f\n", med);

                free(notas);
                break;
            }

            case 7: {
                int vezes, cont;
                printf("Quantos carros iremos registrar? ");
                scanf("%d", &vezes);

                struct Carro* carros = (struct Carro*)malloc(vezes * sizeof(struct Carro));
                getchar(); // Limpar buffer

                for (cont = 0; cont < vezes; cont++) {
                    printf("\nDigite a marca do carro: ");
                    fgets(carros[cont].marca, sizeof(carros[cont].marca), stdin);
                    carros[cont].marca[strcspn(carros[cont].marca, "\n")] = 0;

                    printf("Digite o modelo do carro: ");
                    fgets(carros[cont].modelo, sizeof(carros[cont].modelo), stdin);
                    carros[cont].modelo[strcspn(carros[cont].modelo, "\n")] = 0;

                    printf("Informe o ano de fabricação: ");
                    scanf("%d", &carros[cont].anoFabri);

                    printf("Informe o preço do carro: ");
                    scanf("%f", &carros[cont].preco);
                    getchar();
                }

                for (cont = 0; cont < vezes; cont++) {
                    printf("\nCarro %d:\n", cont + 1);
                    printf("Marca: %s\n", carros[cont].marca);
                    printf("Modelo: %s\n", carros[cont].modelo);
                    printf("Ano: %d\n", carros[cont].anoFabri);
                    printf("Preço: %.2f\n", carros[cont].preco);
                }

                free(carros);
                break;
            }

            case 8: {
                int alunos = 5;
                float* nota = (float*)malloc(alunos * sizeof(float));
                if (nota == NULL) {
                    printf("Erro ao alocar memória.\n");
                    return 1;
                }

                for (int cont = 0; cont < alunos; cont++) {
                    printf("Digite a nota do aluno %d: ", cont + 1);
                    scanf("%f", &nota[cont]);
                }

                for (int cont = 0; cont < alunos; cont++) {
                    printf("Nota do aluno %d: %.2f\n", cont + 1, nota[cont]);
                }

                free(nota);
                break;
            }

            default:
                return 0;
        }
    }

    return 0;
}
