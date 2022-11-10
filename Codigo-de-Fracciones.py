print("<OPERACION DE DOS FRACCIONES>\n")

class Fractions:
    def __init__(self,nA,dA,nB,dB):
        self.nA=nA
        self.dA=dA
        self.nB=nB
        self.dB=dB
        
    def summation(self):
        nT = int(self.nA*self.dB)+(self.dA*self.nB)    #OPERACION DE SUMA
        dT = int(self.dA*self.dB)
        return (nT/dT)

    def subtraction(self):
        nT = int(self.nA*self.dB-self.dA*self.nB)      #OPERACION DE RESTA
        dT = int(self.dA*self.dB)
        return (nT/dT) 

    def multiplication(self):
        nT = int(self.nA*self.nB)                      #OPERACION DE MULTIPLICACION
        dT = int(self.dA*self.dB)
        return (nT/dT)

    def division(self):
        nT = int(self.nA*self.dB)                      #OPERACION DE DIVISION
        dT = int(self.dA*self.nB)
        return (nT/dT)

nA=int(input("Ingrese el numerador de la primera fraccion: "))        #INGRESO DE VALORES DE LOS NUMEROS 
dA=int(input("Ingrese el denominador de la primera fraccion: "))
nB=int(input("Ingrese el numerador de la segunda fraccion: "))
dB=int(input("Ingrese el denominador de la segunda fraccion: "))

print("\nSELECCIONE LA OPERACION A REALIZAR")                         #SELECCION DE OPERACION 
print("1) SUMA\n2) RESTA\n3) MULTIPLICACION\n4) DIVISION\n")

p=int(input("Que operacion desea realizar: "))
if(p==1):
  print("El resultado de la suma (",nA,"/",dA,") + (",nB,"/",dB,") es: ")                #RESULTADO SUMA
  obj = fractions(nA,dA,nB,dB)
  print("{:.5f}".format(obj.summation()))
elif(p==2):
  print("El resultado de la resta (",nA,"/",dA,") - (",nB,"/",dB,") es: ")               #RESULTADO RESTA
  obj = fractions(nA,dA,nB,dB) 
  print("{:.5f}".format(obj.subtraction()))
elif(p==3):
  print("El resultado de la multiplicacion (",nA,"/",dA,") * (",nB,"/",dB,") es: ")      #RESULTADO MULTIPLICACION
  obj = fractions(nA,dA,nB,dB)
  print("{:.5f}".format(obj.multiplication()))
elif(p==4):
  print("El resultado de la division (",nA,"/",dA,") / (",nB,"/",dB,") es: ")            #RESULTADO DIVISION
  obj = fractions(nA,dA,nB,dB)
  print("{:.5f}".format(obj.division()))
else:
  print("\nLa operacion escogida no se encuentra en los numeros solicitados")            #CASO EN EL QUE EL NUMERO INGRESADO NO ESTA EN LAS OPERACIONES DADAS ANTERIORMENTE 
