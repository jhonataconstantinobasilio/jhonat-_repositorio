compra = int (input('digite seu numero\n'))
print(100*0.05)

compra2 = int(input('digite seu numero\n'))
print(500*0.10)

compra3 = int(input('digite seu numero\n'))
print(1000*0.15)


total = compra+compra2+compra3
if total >1000:
   print('recebe desconto de 15%\n')

elif total >500:
     print('recebe desconto de 10%\n')

elif total >100:
    print('recebe desconto de 5%\n')
else:
    print('não recebe desconto\n')    
