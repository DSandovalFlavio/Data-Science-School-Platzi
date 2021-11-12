# %%
# Decorador:
# Es un closure especial por que es una funcion
# que recibe como parametro otra funcion y le añade cosas
# retorna una funcion modificada

def decorador(funcion):
    def envoltura():
        print("Esto se añade a mi funcion original")
        funcion()
    return envoltura

def saludar():
    print("Hola")

saludar()
print('------------')
saludo = decorador(saludar)
saludo()

# %%
# SugarSyntax:
@decorador
def saludar():
    print("Hola")

saludo()
# %%
