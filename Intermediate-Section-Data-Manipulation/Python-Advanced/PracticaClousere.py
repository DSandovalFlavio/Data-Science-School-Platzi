# %% 
# Clousure
def palabramul(palabra):
    assert type(palabra) == str, "La palabra debe ser una cadena de caracteres"
    def palabra_mul(n):
        return print(palabra * n)
    return palabra_mul

# %%
palabra = palabramul(input("Introduce una palabra: "))
palabra(int(input("Introduce un numero: ")))

# %%
def make_division_by(n):
    def division(x):
        return print(x / n)
    return division

divisionby10 = make_division_by(10)
divisionby10(100)
# %%
