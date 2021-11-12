######### Fundamentos en la arquitectura de redes neuronales
# In[]:
# Importando librerias
import numpy as np
from keras import layers, models
from keras.utils import to_categorical
from keras.datasets import mnist
import matplotlib.pyplot as plt
# %%
# Cargando el set mi de "Keras"
(train_data, train_labels), (test_data, test_labels) = mnist.load_data()

# %%
# graficando el numero y validando su valor en labels
plt.imshow(train_data[275])
print(train_labels[275])
# %%
#Creando Red Neuronal
model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
model.add(layers.Dense(10, activation='softmax'))

# %%
# Compilando el modelo
model.compile(  optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics='accuracy' )
# %%
#Con esto podemos ver la estructura de nuestra Red Neuronal
model.summary()

# %%
# Convirtiendo la data en valores desimales 
# para que puedan tener un mejor procesamiento
x_train = train_data.reshape(60000,28*28)
x_train = x_train.astype('float32')/255

x_test = test_data.reshape(10000,28*28)
x_test = x_test.astype('float32')/255

# %%
# Convirtiendo a datos categoricos
y_train = to_categorical(train_labels)
y_test = to_categorical(test_labels)

# %%
# Entrenando la Red Neuronal
model.fit(x_train, y_train, epochs=5, batch_size=120)

# %%
# Evaluando los datos
model.evaluate(x_test, y_test)

# %%
########### Funciones de Activacion #################

## SIGMOIDE
def sigmoid(a):
    return 1 / (1+np.exp(-a))
x = np.linspace(10,-10,100)
plt.plot(x, sigmoid(x))

# %%
## ESCALONADA O STEP

def escalonada(x):
    return np.piecewise(x,[x<0.0, x>0.0], [0,1])
x = np.linspace(10,-10,100)
plt.plot(x, escalonada(x))

# %%
## RELU

def relu(x):
    return np.piecewise(x,[x<0, x>0], [0,lambda x: x])
x = np.linspace(10,-10,100)
plt.plot(x, relu(x))

# %%
########### Funciones de Perdida #################

## ERROR CUADRATICO MEDIO
def mse(y, y_hat, derivative=False):
    if derivative:
        return (y_hat - y)
    else:
        return np.mean((y_hat - y)**2)

real = np.array([0,0,1,1])
preccion = np.array([0.9,0.5,0.2,0.0])

mse(real,preccion)


