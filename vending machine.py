invalid = ('Invalid Drink Picked')
drinks = ('Coca Cola, Fanta, Sprite and Dr Pepper')
confirmed = ('Your Payment Has Been Confirmed. Have a Good day and stay hydrated!')
print(drinks)
choice = input('Pick A Drink: ')
if choice == 'Coca Cola':
   payment = input('Will you be paying with cash or card?: ')
elif choice == 'Fanta':
   payment = input('Will you be paying with cash or card?: ')
elif choice == 'Sprite':
   payment = input('Will you be paying with cash or card?: ')
elif choice == 'Dr Pepper':
   payment = input('Will you be paying with cash or card?: ')
else:
   print(invalid)
 
if payment == 'cash':
   print('That Will Be £2.49. Please Insert Coins')
elif payment == 'card':
   print('That WIll Be £2.49. PLease Insert Your Card')
 
question = input('Have You Payed?')
 
if question == 'yes' or 'Yes':
   print(confirmed)
elif question == 'no' or 'No':
   print('Please Insert Them Now.')
