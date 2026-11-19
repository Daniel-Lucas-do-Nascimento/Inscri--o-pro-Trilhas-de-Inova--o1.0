from service.funcionalidades import inscricao,consulta_de_inscricao
def validar_op():
     while True:
          try:
               op = int(input('Digite sua escolha: '))
               if op == 1:
                    inscricao()
                    break
               elif op == 2:
                    consulta_de_inscricao()
                    break
               elif op == 100:
                    break
                    break
               else:
                    print('Opção Inválida!')
          except ValueError:
               print('Digite um número inteiro!')