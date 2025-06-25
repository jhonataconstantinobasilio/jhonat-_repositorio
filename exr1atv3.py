
peso = float(input("digite seu peso\n"))

altura = float(input("digite sua altura \n"))

imc= peso/(altura**2)

msg_Padrao = 'você está no pesso adequado para sua idade,obrigado por verificar sua saude conosco'
msg_para_abixodopesso = 'você está abaixo do pesso precisa se comer mais'
msg_para_obesos = 'você está muito acima do pesso precisa enmagraçer'
if imc < 18.5:
    print('abaixo do pesso\n',msg_Padrao)

elif 18.5<= imc < 25:
     print('pesso normal\n',msg_Padrao)

elif 25<= imc <30: 
      print('sobre pesso\n',msg_para_obesos)

elif imc >=30:
     print('obesidade\n',msg_para_obesos)

else:
     print('você está no pesso adequado para sua idade,obrigado por verificar sua saude conosco \n')     