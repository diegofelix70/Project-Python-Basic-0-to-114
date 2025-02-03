from random import randint
na = randint(1, 10)
cont=0 
print('{}\033[34mADIVINHE O NÚMERO\033[m{}'.format('=' * 31, '=' * 31))
r=input('Acabei de pensar em um numero de 1 a 10. Você é capaz de advinha-lo? \033[33m[SIM/NAO]\033[m ').strip().upper()[0]
if r in 'S':
    n1=int(input('Digite um numero aleatorio: '))
    if n1==na:
        print('\033[32mParabens, o numero escolhido pelo computador foi {} e você advinhou em 1 tentativas\033[m'.format(na))
    else:
        while cont<3: 
            n = int(input('\033[31mNumero incorreto\033[m, tente novamnte'))
            cont+=1
            if n==na:
                print('\033[32mParabens, o numero escolhido pelo computador foi {}, e você advinhou em {} tentativas\033[m'.format(na, cont+1))
                break
        if n!=na:
            print('\033[31mVocê atingiu o maxímo de tentaivas possíveis, mais sorte da proxima vez!\033[m ')
else:
    print('\033[31mSempre soube que você não era capaz!!!!\033[m')