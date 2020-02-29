#Game of Forc v2
#Created by: MolayDev
#Date: 23/02/2020


name_user = input('Qual é o seu nome? ')
welcome_user = 'Olá, {}! \nBem vindo(a) ao jogo da Forca!'.format(name_user)

def PalavraONE():

    perg = input('Deseja uma dica? S/N ')
    if (perg == 'S'):
         print('Comida que toda criança gosta!')
    else:
         print('Ok!')
            
    words_what = ['B', 'I', 'S', 'C', 'O', 'I', 'T', 'O',]
    what_words = []

    for i in range(0, len(words_what)):
        what_words.append('-')

    Ok = False

    while Ok == False:
         Word = str(input('Digite uma letra: '))

         for i in range(0, len(words_what)):
             if Word == words_what[i] :
                 what_words[i] = Word

             print(what_words[i])
             

         Ok = True

         for x in range(0, len(what_words)):
                    if what_words[x] == '-' :
                        Ok = False

    print('Parabéns {}! Você conseguiu ganhar!'.format(name_user))
         

op = True

while op:
    print('Primeira Pergunta: Digite 1')
    
    op = int(input('Digite: '))

    if (op == 0):
        print('Adeus!')
    if (op == 1):
        PalavraONE()













        
