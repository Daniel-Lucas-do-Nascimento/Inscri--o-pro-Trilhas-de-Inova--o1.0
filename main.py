from utills.auxiliar import titulo
from utills.auxiliar2 import validar_op



op = 1
while op != 100:
    titulo('Inscrição Trilhas de Inovação 7ª Edição')
    print('''[1] Inscrição 
[2] Consultar Inscrição
[100] Sair''')
    try:
        op = int(input('Digite sua escolha: '))
        validar_op(op)
    except ValueError:
              print('Digite um número inteiro!')
    



