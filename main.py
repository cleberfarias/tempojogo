horaI = int(input("digite hora inicial: "))
minI = int(input("digite o minuto inicial: "))
horaF = int(input("digite a hora final: "))
minF = int(input("digite a minuto final: "))

# horas iguais 
if (horaF==horaI):
  if(minF>=minI):
    minT=minF-minI
    horaT=0
  else:
    minT=60-minI+minF
    horaT=23
elif(horaF>horaI):
    horaT=horaF-horaI
    if(minF>=minI):
      minT=minF-minI
    else:
      minT=60-minI+minF
      horaT-= 1

print("Horas: ",horaT)
print("Minuto: ",minT)