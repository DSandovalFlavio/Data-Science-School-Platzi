# %%
# Nested functions:
# Son funciones que se ejecutan dentro de otra funcion.

def main():
    a = 1
    
    def nested_func():
        print(a)
    
    return nested_func

my_func = main()
my_func()

# %%
# Clousure:
# Un closure se da cuando una variable de un scope superior es recordada
# Reglas:
# Debemos tener una nested function
# La nested function debe referenciar un valor de un scope superior
# La funcion que envuelve a la nested function debe retornarla tambien

def main():
    a = 1
    
    def nested_func():
        print(a)
    
    return nested_func

my_func = main()
my_func()

del(main)

my_func()

# %%
def make_multiplier(x):
    
    def multipler(n):
        return x * n
    
    return multipler
# %%
times10 = make_multiplier(10)
times4 = make_multiplier(4)
# %%
print(times10(2))
print(times4(2))
print(times10(times4(2)))
# %%
