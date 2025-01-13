def maior(*num):
    cont=maior=0
    for c in num:
        print(f'{c}', end=' ')
        cont+=1
        if c != 0:
            maior=max(num)
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2,9,4,5,7,1)
maior(7,3,0)
maior(5,3)
maior(3)
maior()