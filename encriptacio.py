from cryptography.fernet import Fernet
# Genera una clave de encriptación
clave = Fernet.generate_key()
# Crea un objeto Fernet con la clave generada
fernet = Fernet(clave)
# Contraseña original
contraseña_original = input('ingresa la clave a encriptar:  ')
# Encripta la contraseña
contraseña_encriptada = fernet.encrypt(contraseña_original.encode())
# Guarda la contraseña encriptada en un archivo
with open('contra.txt', 'wb') as archivo_encriptado:
    archivo_encriptado.write(contraseña_encriptada)
print('la clave encriptada es: ',contraseña_encriptada)



# Lee la contraseña encriptada desde el archivo
with open('contra.txt', 'rb') as archivo_encriptado:
    contraseña_encriptada = archivo_encriptado.read()

# Desencripta la contraseña
contraseña_desencriptada = fernet.decrypt(contraseña_encriptada)

# Decodifica la contraseña a formato de texto
contraseña_final = contraseña_desencriptada.decode()

# Imprime la contraseña desencriptada
print("Contraseña desencriptada:", contraseña_final)
