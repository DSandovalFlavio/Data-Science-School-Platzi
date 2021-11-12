# %%
def palindrome(word):
    """
    Función que verifica si una palabra es palíndroma
    """
    assert len(word) > 0, "La palabra no puede ser vacía"
    return word == word[::-1]

print(palindrome(""))
# AssertionError: La palabra no puede ser vacía

# %%
