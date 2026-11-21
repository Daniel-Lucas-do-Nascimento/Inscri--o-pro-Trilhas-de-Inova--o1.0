from service.funcionalidades import inscricao,consulta_de_inscricao



def validar_op(op):
     if op == 1:
          inscricao()
     elif op == 2:
          consulta_de_inscricao()
     elif op == 100:
          print('\033[31mSaindo...\033[m')
     else:
          print('Opção Inválida!')
