eletkor= 17
diak = True

if eletkor < 6: 
   print("Ingyenes jegy.")
elif eletkor < 18 and diak:
   print("Diákjegy: 1.800 Ft")
elif eletkor > 65: 
   print("Nyugdíjas jegy: 2.000 Ft")
else:
   print("Felnőttjegy: 3.000 Ft")


