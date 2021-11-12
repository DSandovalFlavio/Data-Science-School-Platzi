# Una variable solo esta disponible en la region donde fue creada

# %%
# Local Scope
def funcion(): # X solo esta disponible
    y = 1      # en la region de esta  
    print(y)   # funcion
    
y = 2          # Scope Global puede ser accedido
               # en cualquier region del codigo

print(y)
funcion()
 
# %%
z = 5

def my_func():
    z = 10
    
    def my_inner_func():
        z = 15
        print(z)
    
    my_inner_func()
    
    print(z)
    
my_func()

print(z)

# %%
