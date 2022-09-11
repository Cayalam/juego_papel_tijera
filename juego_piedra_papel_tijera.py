# juego de piedra papel tijera

print("------------------------------")
print("---Juego piedra papel tijera---")
print("--------------------------------")
import random

# comienza el sistema
bandera=True 
suerte= random.randint(1,3)
num_pc=""
print("1=piedra") 
print("2=papel")
print("3=tijera")
# da un numero el usuario
opcion= int(input(" \n ingrese la opcion a jugar: "))

if opcion == 1:
    num_usuario="1"
elif opcion == 2:
    num_usuario="2"
elif opcion == 3:
    num_usuario="3"
print("tu suerte esta en: ", num_usuario)

if suerte == 1:
    num_pc="1"
elif suerte == 2:
    num_pc="2"
elif suerte == 3:
    num_pc="3"
print("la pc eligio: ", num_pc)
print("...")
if num_usuario == "1" and num_pc =="1":
    print("Es ingreible,acaba de a ver un empate")
elif num_usuario == "1" and num_pc =="2":
    print("Rayos,acaba de ganar la pc")
elif num_usuario == "1" and num_pc =="3":
    print("sos un pro,ganaste")
if num_usuario == "2" and num_pc =="2":
    print("Es ingreible,acaba de a ver un empate")
elif num_usuario == "2" and num_pc =="1":
    print("sos un pro,ganaste")
elif num_usuario == "2" and num_pc =="3":
    print("Rayos,acaba de ganar la pc")
if num_usuario == "3" and num_pc =="3":
    print("Es ingreible,acaba de a ver un empate")
elif num_usuario == "3" and num_pc =="1":
    print("Rayos,acaba de ganar la pc")
elif num_usuario == "3" and num_pc =="2":
    print("sos un pro,ganaste")



