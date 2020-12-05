import sympy as sym
import math

r_esfera = 2
a_cubo = 2
b_prisma = 2
a_prisma = 2
l_prisma = 2

lista_fluidos = ["agua", "aceite", "glicerina", "etanol"]
lista_materiales = ["madera", "aluminio", "hielo", "corcho"]
lista_figuras = ["esfera", "cubo", "prismat"]

#Aquí en realidad van los input
fluido = "agua"
material = "madera"
figura = "esfera"

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
        h_figura = h_esfera(peso, densidad_fluido[fluido])
    else:
        h_figura = h_prisma(peso, densidad_fluido[fluido])

    return h_figura


def h_esfera(peso, densidad):
    #ARREGLAR ESTO PARA QUE CALCULE, NO SÉ QUE LIBRERIA USAR
    sym.init_printing()
    h = sym.symbols('h')
    h_eu, h_en, h_ep = sym.solveset(sym.Eq(peso/densidad*3/math.pi, h**2*(3*sym.sqrt(r_esfera*2*h-h**2)-h)),h)
    print(h_ep)
    # sym.init_printing()
    # h,r = sym.symbols('h,r')
    # eq_1 = sym.Eq(peso/densidad*3/math.pi, h**2*(3*r-h))
    # eq_2 = sym.Eq (sym.sqrt(r_esfera*2*h-h**2),r)
    # h_ec, r_ec = sym.solve([eq_1, eq_2],(h,r))
    # return h_ec

def h_prisma(peso, densidad):
    #ARREGLAR ESTO PARA QUE CALCULE, NO SÉ QUE LIBRERIA USAR
    sym.init_printing()
    h = sym.symbols('h')
    h_pn, h_pp = sym.solveset(sym.Eq(peso/(densidad*l_prisma), (h*b_prisma/a_prisma)*h),h)
    return(h_pp)

h_ec = get_h(figura, material, fluido)
print(h_ec)

    





