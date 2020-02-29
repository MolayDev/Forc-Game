#Game of Forc
#Created by: MolayDev
#Date: 11/02/2020



name_user = input('Qual é o seu nome? ')
welcome_user = 'Olá, {}, bem vindo(a) ao Jogo da Forca!'.format(name_user)

words_what = ['T', 'E', 'A', 'M', 'O']
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
