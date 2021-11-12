# %%
import time

def fibo_generator(max):
    a, b = 0, 1
    while True:
        yield a
        if a > max:
            break
        a, b = b, a + b
        
    
# %%
fi = fibo_generator(10000000000000)
for i in fi:
    print(i)
    
# %%
