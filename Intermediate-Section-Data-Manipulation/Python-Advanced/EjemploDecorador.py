# %%
from datetime import datetime

def execution_time(func):
    def wrapper():
        initial_time = datetime.now()
        func()
        final_time = datetime.now()
        print(f'El tiempo de ejecución fue de {final_time - initial_time}')
    return wrapper()

@execution_time
def random_func():
    for _ in range(100000000000):
        pass

random_func()
# %%
def execution_time(func):
    def wrapper(*args, **kwargs): # *args, **kwargs para recibir argumentos los que sean necesarios
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        print(f'El tiempo de ejecución fue de {final_time - initial_time}')
    return wrapper()