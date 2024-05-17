import random as rand
import string as str

def generar_contraseña(longitud):
    caracteres = str.ascii_letters + str.digits + str.punctuation
    contraseña = ''.join(rand.choice(caracteres) for i in range(longitud));
    return contraseña

longitudDeContraseña = int(input("Ingresa la longitud deseada para la contraseña: "));

print("La contraseña generada es:", generar_contraseña(longitudDeContraseña));
