import time
from io import open
te_texto=open("ptn6.txt","r")
texto=te_texto.read()
te_texto.close()
print (chr(27)+"[1;34m"+texto)


print("\n\n\n\n")
print(chr(27)+"[0;36m"+"     ▂ ▃ ▄ ▅ ▆ ▇ █ ")
print(chr(27)+"[1;37m"+"={ManualPro v5.0.0]")
print("   ={Create by Mart_Lex]\n\n")

print("Escribe (show) para acceder al menu")
print("\n")
a=input(chr(27)+"[1;34m"+"MT "+chr(27)+"[1;31m"+"{}Inicio >>> "+chr(27)+"[1;32m"+"")

while a!="show":
               print (chr(27)+"[0;31m"+"\t---[Error decomando]---")
               a=input(chr(27)+"[1;34m"+"\nMT// "+chr(27)+"[1;31m"+"{}Inicio >>>")
time.sleep(2)
print ("\n\n\n")


print(chr(27)+"[1;37m"+"\__PROPOSITOS DEL PROGRAMA|||\n\n")
print(chr(27)+"[0;37m"+"°•Este programa tiene como proposito mostrar\ntodo los comandos existentes en termux,\nherramientas y apts/pkgs ,mostrarte un\npanorama amplio su aplicacion y de su\npotencial como distribucion de linux y GNU\nmostrate que puedes hacer maravillas con esta ventana\nlinux.\n\n\n\n")
