# try, exept

# %% 
def palindrome(string):
    return string == string[::-1]

print(palindrome(1)) # <-  Se pasa un 1 para ver el error

# TypeError: 'int' object is not subscriptable
# %%
def palindrome(string):
    return string == string[::-1]

try:
    print(palindrome(1)) # <-  Se pasa un 1 para ver el error
except TypeError:
    print("Solo se pueden ingresar strings")

# Solo se pueden ingresar strings 
# %%
def palindrome(string):
    try:
        if len(string) == 0:
            # apesar que es un string esta vacio por lo que 
            # se considera un error logico y se utiliza raise 
            # para manejarlo y generar un error de tipo ValueError
            raise ValueError("El string no puede estar vacio")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False
    
try:
    print(palindrome(input('Ingresa una palabra'))) # <-  Se pasa un 1 para ver el error 
except TypeError:
    print("Solo se pueden ingresar strings")
# %%
# finally se usa al final de un bloque de codigo para ejecutar
# codigo independiente del resultado de la ejecucion del bloque
# ejemplo cerrar un archivo o cerrar una conexion a la base de datos
try:
    f = open('archivo.txt')
finally:
    f.close()

# %%