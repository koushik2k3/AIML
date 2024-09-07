import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(start : float,gradient: float,learn_rate: float, max_iter: int):
 
    x = start
    steps = [start] # history tracking

    for i in range(max_iter):
        diff =  learn_rate * gradient(x)

        x = x -  diff
        steps.append(x)
        
    return steps, x

def func1(x: float):
    
    return x**2-4*x+1

def gradient_1(x:float):

    return 2*x-4

history, result = gradient_descent(9,gradient_1, 0.1, 100)

print(history)

print("--------")

print(result)




