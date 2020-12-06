import sympy as sym
import math
import numpy as np
from scipy.optimize import fsolve

r_esfera = 2
a_cubo = 2
b_prisma = 2
a_prisma = 2
l_prisma = 2

lista_fluidos = ["agua", "aceite", "glicerina", "etanol"]
lista_materiales = ["madera", "aluminio", "hielo", "corcho"]
lista_figuras = ["esfera", "cubo", "prisma"]

#Aquí en realidad van los input
fluido = "agua"
material = "madera"
figura = "prisma"

#Densidades fluidos
densidad_fluido = {'agua': 998, 'aceite': 933.7, 'glicerina': 1260, 'etanol': 789}

#Densidades materiales
densidad_material = {'madera': 450, 'aluminio': 2700, 'hielo': 916.8, 'corcho': 240}

#Volumen figuras
v_esfera = 4*math.pi*r_esfera**3/3
v_cubo = a_cubo**3
v_prisma = b_prisma*a_prisma*l_prisma/2
volumen_figura = {'esfera': v_esfera, 'cubo': v_cubo, 'prisma': v_prisma}

#Volumen carena
# carena_esfera = (math.pi*h_esfera*(3*r_caresfera-h_esfera))/3
# carena_cubo = a_cubo**2*h_cubo
# carena_prisma = h_prisma*b_carprisma*l_prisma


def get_peso(figura, material):
    volumen = volumen_figura[figura]
    densidad = densidad_material[material]
    peso = volumen*densidad
    return peso

def get_h(figura, material, fluido):
    if densidad_fluido[fluido] > densidad_material[material]:
        flota = True
    else:
        flota = False
    peso = get_peso(figura, material)
    if figura == "cubo":
        h_figura = peso/(densidad_material[material]*a_cubo**2)
    elif figura == "esfera":
        h_figura = h_esfera(peso, densidad_fluido[fluido], flota)
    else:
        h_figura = h_prisma(peso, densidad_fluido[fluido], flota)

    return h_figura


def h_esfera(peso, densidad, flota):
    
    car = lambda h: peso/densidad*3/np.pi-h**2*(3*np.sqrt(r_esfera*2*h-h**2)-h)
    rcar = fsolve(car, 0.001)
    return rcar[0]


    #REVISIÓN SI LA SOLUCIÓN ES MAYOR O MENOR AL RADIO SI FLOTA
    # if h_s1 >= 0:
    #     if flota:
    #         if h_s1 <= r_esfera:
    #             h_esfera = h_s1
    #     else:
    #         if h_s1 > r_esfera:
    #             h_esfera = h_s1
    # elif h_s2 >= 0:
    #     if flota:
    #         if h_s2 <= r_esfera:
    #             h_esfera = h_s2
    #     else:
    #         if h_s2 > r_esfera:
    #             h_esfera = h_s2 


    #sym.init_printing()
    #h = sym.symbols('h')
    #h_ep = sym.solveset(sym.Eq(peso/densidad*3/math.pi, h**2*(3*sym.sqrt(r_esfera*2*h-h**2)-h)),h)

    

def h_prisma(peso, densidad, flota):
    #sym.init_printing()
    #h = sym.symbols('h')
    #h_p1, h_p2 = sym.solveset(sym.Eq(peso/(densidad*l_prisma), (h*b_prisma/a_prisma)*h),h)
    car = lambda h: peso/(densidad*l_prisma)- (h*b_prisma/a_prisma)*h
    rcar = fsolve(car, 0.001)
    return (rcar[0])
    

h_ec = get_h(figura, material, fluido)
print(h_ec)

    





