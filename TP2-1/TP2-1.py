#IMPORTS
import matplotlib.pyplot as plot
import random as rand
import numpy as np
import math
import scipy.stats as stats
import matplotlib.dates as mdates

valor_inicial = 7

def parte_media_cuadrados():
    semilla = (rand.choice(range(2000, 9999)))
    lista_numeros = []
    for i in range(50):
        semilla_square = pow(semilla, 2)
        string_semilla_square = str(semilla_square)
        # Si la longitud de string_semilla_square es menor que 8, se le agregan 0s al principio
        if(len(string_semilla_square)!= 8): 
          string_semilla_square = string_semilla_square.zfill(8)
        string_semilla_square = string_semilla_square[2: 6]
        semilla = int(string_semilla_square)
        nuevo_numero = round((int(string_semilla_square)/9999), 5)
        lista_numeros.append(nuevo_numero)
    print(lista_numeros)

def generador_congruencial_lineal(i=0):
    # GCL: X de i+1 = (a xi + c) mod(m)
    # ri: xi / m-1
    # a = 1+4k, donde k es un numero entero, en este caso 'a' es un valor de la lista 'valores'
    # c es un numero arbitrario impar
    # x0 es valor inicial
    # m=2^g, en este caso 2^48
    valores =  [25214903917, 23245346567, 26786768767, 25372867686, 28964866456,
                23468735854, 25245346867, 25857586678, 26768687557, 24564676787]
    m = pow(2, 48)
    a = valores[i]
    c = 11
    x0 = valor_inicial
    lista = []
    for i in range(50):
        xi = (a * x0 + c) % m
        ri = xi / (m - 1)
        lista.append(ri)
        x0 = xi
    print(lista)
    return lista

def python_generator():
    lista = []
    for i in range(50):
        randomNumber = (rand.choice(range(0, 99999999)))
        fl = randomNumber / 99999999
        fl = round(fl, 5)
        lista.append(fl)
    return lista

# Se le pasa un valor k y se devuelve el array de esa posicion
def random_org_generator(i=0):
    # Datos obtenidos de la página random.org
    valores = [
    [0.37284, 0.90373, 0.29825, 0.27447, 0.07067, 0.40272, 0.06370, 0.40464, 0.54952, 0.29061,
    0.71561, 0.12418, 0.40787, 0.29635, 0.25928,  0.78972, 0.46169, 0.22608, 0.86818, 0.76114,
    0.68963, 0.32498, 0.49337, 0.00622, 0.23036, 0.64089, 0.86464, 0.18276, 0.38125,  0.76023,
    0.27453, 0.29679, 0.02903, 0.05443, 0.76387, 0.47491, 0.43909, 0.14894, 0.30201, 0.18568,
    0.10899, 0.11536, 0.57590,  0.88861, 0.97871, 0.25461, 0.96477, 0.50360, 0.76231, 0.48128],

    [0.69872, 0.26619, 0.09218, 0.89994, 0.25549, 0.62878, 0.66906, 0.37543, 0.14649, 0.82128,
    0.16109, 0.02114, 0.74250, 0.70832, 0.72843,  0.79371, 0.57175, 0.57294, 0.23009, 0.19812,
    0.29702, 0.27952, 0.08448, 0.51543, 0.08629, 0.31274, 0.23496, 0.93689, 0.33322,  0.83916,
    0.30843, 0.06558, 0.42133, 0.57363, 0.77593, 0.05224, 0.11804, 0.20962, 0.11021, 0.72971,
    0.96051, 0.88190, 0.42307,  0.49972, 0.97637, 0.58763, 0.02085, 0.41839, 0.92331, 0.06603],

    [0.68585, 0.93356, 0.36103, 0.19126, 0.34974, 0.37004, 0.91032, 0.25947, 0.71309, 0.32862,
    0.22026, 0.25534, 0.69037, 0.46701, 0.66642,  0.55318, 0.64907, 0.90507, 0.69464, 0.77307,
    0.96677, 0.64962, 0.50149, 0.48537, 0.83782, 0.01498, 0.18679, 0.68991, 0.43202,  0.93574,
    0.54957, 0.92295, 0.39190, 0.92461, 0.29358, 0.25343, 0.34334, 0.57401, 0.03876, 0.01471,
    0.15566, 0.74191, 0.13633,  0.19786, 0.49074, 0.21667, 0.46112, 0.21220, 0.58165, 0.83588],

    [0.98943, 0.07050, 0.57129, 0.84376, 0.58014, 0.72417, 0.20639, 0.43498, 0.06605, 0.09502,
    0.99486,  0.21323, 0.41817, 0.24514, 0.59492, 0.95906, 0.41513, 0.68518, 0.35331, 0.35167,
    0.12232,  0.06552, 0.53498, 0.50421, 0.90494, 0.60327, 0.03521, 0.17886, 0.29747, 0.03553,
    0.68470,  0.12744, 0.99644, 0.11019, 0.64811, 0.08827, 0.60834, 0.40070, 0.36987, 0.78485,
    0.98785,  0.08928, 0.97176, 0.99436, 0.50511, 0.36808, 0.11678, 0.55177, 0.73236, 0.99495],

    [0.65440, 0.34447, 0.89159, 0.88718, 0.74800, 0.67109, 0.62157, 0.14901, 0.32851, 0.20951,
    0.63728,  0.07824, 0.18534, 0.98687, 0.84203, 0.89490, 0.17698, 0.91684, 0.66842, 0.12533,
    0.28085,  0.82100, 0.92082, 0.29374, 0.04634, 0.61413, 0.61272, 0.05748, 0.43651, 0.62218,
    0.87582,  0.00168, 0.28876, 0.17248, 0.97904, 0.04568, 0.98109, 0.78770, 0.02805, 0.42620,
    0.42342,  0.99719, 0.46592, 0.89023, 0.59398, 0.37945, 0.33526, 0.49465, 0.44148, 0.79830],

    [0.31678, 0.32732, 0.09319, 0.47806, 0.95573, 0.20234, 0.59893, 0.69466, 0.75039, 0.75408,
    0.28415,  0.97592, 0.60505, 0.36221, 0.97910, 0.06741, 0.39251, 0.82290, 0.74946, 0.16202,
    0.24268,  0.90566, 0.32099, 0.78065, 0.23368, 0.83908, 0.15369, 0.14777, 0.47098, 0.38339,
    0.89427,  0.39306, 0.93919, 0.56444, 0.37821, 0.97546, 0.36426, 0.80919, 0.75380, 0.00995,
    0.21617,  0.67397, 0.46349, 0.00178, 0.73291, 0.14996, 0.15414, 0.51854, 0.13186, 0.65499],

    [0.83530,	0.02321,	0.74251,	0.41443,	0.32419,	0.70120,	0.69096,	0.22197,	0.14971,	0.14989,
    0.80798,	0.56797,	0.05125,	0.53256,	0.86330,	0.33651,	0.76595,	0.44744,	0.46876,	0.55072,
    0.12064,	0.40881,	0.78871,	0.48031,	0.65781,	0.43812,	0.75408,	0.77750,	0.78944,	0.42059,
    0.12887,	0.93994,	0.90661,	0.17798,	0.90325,	0.80177,	0.77335,	0.92404,	0.86226,	0.75172,
    0.31103,	0.00939,	0.68850,	0.41834,	0.84904,	0.98668,	0.87855,	0.08753,	0.66919,	0.36951],

    [0.46636, 0.85391, 0.02381, 0.28369, 0.76393, 0.50598, 0.88934, 0.34222, 0.91604, 0.74971,
    0.48246,  0.72365, 0.59013, 0.63084, 0.54739, 0.21790, 0.70438, 0.91714, 0.65813, 0.32648,
    0.22722,  0.64466, 0.91624, 0.56061, 0.07384, 0.44748, 0.42394, 0.17286, 0.53017, 0.47117,
    0.69723,  0.30573, 0.60684, 0.58357, 0.36894, 0.38381, 0.19376, 0.40895, 0.81999, 0.69293,
    0.91503,  0.75682, 0.64518, 0.63549, 0.40920, 0.04476, 0.06819, 0.70392, 0.50623, 0.50690],

    [0.87107, 0.99382, 0.42393, 0.35463, 0.95204, 0.77799, 0.05182, 0.73966, 0.76132, 0.52119,
    0.95243,  0.50584, 0.30680, 0.76825, 0.66489, 0.89918, 0.01429, 0.35976, 0.48339, 0.30023,
    0.54422,  0.33134, 0.63049, 0.18408, 0.84935, 0.09307, 0.85543, 0.95526, 0.08893, 0.04821,
    0.59853,  0.06732, 0.36702, 0.71407, 0.70153, 0.65110, 0.75996, 0.11369, 0.96103, 0.23695,
    0.55040,  0.09310, 0.79050, 0.20797, 0.78262, 0.06465, 0.26498, 0.40586, 0.39608, 0.99242],

    [0.13245, 0.08899, 0.12432, 0.94657, 0.00934, 0.29334, 0.56661, 0.44375, 0.30921, 0.63685,
    0.66438,  0.89739, 0.29979, 0.18254, 0.17026, 0.29732, 0.08331, 0.59847, 0.38759, 0.29634,
    0.45950,  0.12461, 0.93011, 0.44243, 0.12086, 0.77529, 0.01900, 0.30718, 0.13217, 0.05848,
    0.45039,  0.65003, 0.28984, 0.65449, 0.54799, 0.58637, 0.72332, 0.62517, 0.08274, 0.91914,
    0.16561,  0.63143, 0.52559, 0.27295, 0.86695, 0.98685, 0.06566, 0.88013, 0.00443, 0.85391]]
    return valores[i]

def chi_cuadrado(lista, titulo):
    n = len(lista)
    m = 10
    ei = n/m
    intervalos = [[], [], [], [], [], [], [], [], [], []]

    for i in lista:
        if ((i > 0) and (i < 0.1)):
            intervalos[0].append(i)
        if ((i > 0.1) and (i < 0.2)):
            intervalos[1].append(i)
        if ((i > 0.2) and (i < 0.3)):
            intervalos[2].append(i)
        if ((i > 0.3) and (i < 0.4)):
            intervalos[3].append(i)
        if ((i > 0.4) and (i < 0.5)):
            intervalos[4].append(i)
        if ((i > 0.5) and (i < 0.6)):
            intervalos[5].append(i)
        if ((i > 0.6) and (i < 0.7)):
            intervalos[6].append(i)
        if ((i > 0.7) and (i < 0.8)):
            intervalos[7].append(i)
        if ((i > 0.8) and (i < 0.9)):
            intervalos[8].append(i)
        if ((i > 0.9) and (i < 1)):
            intervalos[9].append(i)

    suma_resultados = 0
    for j in intervalos:
        oi = len(j)
        formula_chi = (math.pow((oi-ei), 2)/ei)
        suma_resultados += formula_chi;
        print(oi, ei, formula_chi)

    chi = stats.chi2.ppf(0.95,9)
    grafica_barras(intervalos, suma_resultados, chi, titulo)

    if suma_resultados < chi:
        print('No se puede descartar que la lista de números sea aleatoria')
    else:
        print('La lista de numeros no es aleatoria')


# GRAFICA DE PRUEBA DE CORRIDAS ARRIBA Y ABAJO DE LA MEDIA
def prueba_medias(lista, titulo):
    # n = cantidad_menores + cantidad_mayores, o sea, el total
    n = len(lista)
    media = np.mean(lista)
    secuencia = []
    alfa = 0.05

    cantidad_hasta_cambio = 0
    lista_cantidad_hasta_cambio = []
    cantidad_corridas = 1

    for index, num in enumerate(lista):
        if num < media:
            secuencia.append(0)
        else:
            secuencia.append(1)
        if index >= 1:
            cantidad_hasta_cambio += 1
            if secuencia[-2] != secuencia[-1]:
                lista_cantidad_hasta_cambio.append(cantidad_hasta_cambio)
                cantidad_hasta_cambio = 0
                cantidad_corridas = cantidad_corridas + 1

    frecuencia_absoluta_cantidad_cambios = []
    for cantidad_hasta_cambio in range(0, max(lista_cantidad_hasta_cambio)):
        frecuencia_absoluta_cantidad_cambios.append(lista_cantidad_hasta_cambio.count(cantidad_hasta_cambio))
    frecuencia_relativa_cantidad_cambios = np.array(frecuencia_absoluta_cantidad_cambios) / cantidad_corridas

    print(frecuencia_relativa_cantidad_cambios[0:15])
    
    # Grafica frecuencia cambio
    grafica_medias(frecuencia_relativa_cantidad_cambios, titulo)

    cantidad_menores = secuencia.count(0)
    cantidad_mayores = secuencia.count(1)
    num = secuencia[0]

    # u_co y var_co son formulas
    u_co = ((2 * cantidad_menores * cantidad_mayores) / (cantidad_menores + cantidad_mayores)) + 1
    var_co = (2 * cantidad_menores * cantidad_mayores * (2 * cantidad_menores * cantidad_mayores - n)) / (n ** 2 * (n - 1))
    z0 = (cantidad_corridas - u_co) / math.sqrt(var_co)

    print(z0)

    z_alfa = 1.96

    if (-z_alfa < z0 < z_alfa):
        print("Los valores son independientes")
    else:
        print("Los valores no son independientes.")

def prueba_rachas(lista, titulo):
    media = ((2 * len(lista) - 1) / 3 )
    varianza = ((16 * len(lista) - 29) / 90)
    bits = []
    for i in range(1, len(lista)):
        if (lista[i] > lista[i-1]):
            bits.append(1)
        else:
            bits.append(0)

    cambios = 1
    dato = bits[0]

    # Comparamos cada dígito con el observado, cuando cambia es una nueva corrida
    for j in range(0, len(bits)):
        if (bits[j] != dato):
            cambios = cambios + 1
            dato = bits[j]

    z = abs(( cambios - media) / math.sqrt(varianza))

    # 90% de confianza
    alpha = 0.05
    znorm = 1 - (alpha / 2)
    prob = stats.norm.ppf(znorm)
    grafica_rachas(lista, z, prob, titulo)
    # Si z > prob no aprueba

def prueba_autocorrelacion(lista):
    comparados = []
    N = len(lista)
    print('N', N)
    i = 2
    m = 3
    rs = 0
    M = math.trunc( ((N - i) / m ) - 1)
    comparados.append(lista[i - 1])
    while i + m <= N:
        rs = rs + (float(lista[i - 1]) * float(lista[i - 1 + m]))
        i = i + m
        comparados.append((lista[i - 1]))
    R = 1 / (M + 1) * rs
    print(M)
    D = round((math.sqrt(13 * M + 7)) / (12 * (M + 1)), 3)
    Z = (R - 0.25) / D
    limite = stats.norm.ppf(0.975)
    print(lista)
    print(comparados)
    return Z

def autocorrelacion(lista, titulo):
    conjunto_arreglos = []
    for k in range (0, 10):
        conjunto_arreglos.append(prueba_autocorrelacion(lista))
    grafica_autocorrelacion(conjunto_arreglos, titulo)

def grafica_barras(lista, sumRes, chi, titulo):
    labels = ['0.0 - 0.1', '0.1 - 0.2', '0.2 - 0.3', '0.3 - 0.4', '0.4 - 0.5',
              '0.5 - 0.6', '0.6 - 0.7', '0.7 - 0.8', '0.8 - 0.9', '0.9 - 1.0']
    width = 0.35.
    fig, ax = plot.subplots()
    val = 50/10
    plot.axhline(val, color='black', ls="dotted", xmax=len(lista))
    for i in range(0, 9):
        ax.bar(labels[i], len(lista[i]), width, color='red')
    ax.set_ylabel('Cantidad de apariciones')
    if (sumRes < chi):
        text = 'Aprueba. '
        ax.set_title('Prueba de bondad de ajuste: ' + str(round(sumRes, 1)) + ' es menor a ' + str(round(chi, 2)) + '\n' + text + titulo)
    else:
        text = 'No aprueba. '
        ax.set_title('Prueba de bondad de ajuste: ' + str(round(sumRes, 1)) + ' es mayor a ' + str(round(chi, 2)) + '\n' + text + titulo)

    plot.savefig("grafica_barras_bondad_"+str(titulo)+".svg")
    

def grafica_autocorrelacion(conjunto_arreglos, titulo):
    limiteInf = stats.norm.ppf(0.975) * (-1)
    limiteSup = stats.norm.ppf(0.975)

    fig = plot.figure()
    ax = plot.stem(conjunto_arreglos)
    plot.axhline(limiteInf, color='black', ls="dotted", xmax=len(conjunto_arreglos))
    plot.axhline(limiteSup, color='black', ls="dotted", xmax=len(conjunto_arreglos))
    plot.axhline(0, color='blue', xmax=len(conjunto_arreglos))
    # ax.grid()
    fig.suptitle('Test de autocorrelación: ' + titulo)
    plot.savefig("grafica_autocorrelacion_"+str(titulo)+".svg")
    


def grafica_rachas(lista, z, prob, titulo):
    fig = plot.figure()
    ax = plot.plot(lista, marker='o')
    plot.axhline(1, color='black', ls="dotted", xmax=len(lista))
    plot.axhline(0, color='black', ls="dotted", xmax=len(lista))
    plot.axhline(0.5, color='blue', xmax=len(lista))
    if (z < prob):
        fig.suptitle('Valor de estadístico Z: ' + str(round(z, 2)) + ' es menor a ' + str(round(prob, 2)) + '\n Aprueba. ' + titulo)
    else:
        fig.suptitle('Valor de estadístico Z: ' + str(round(z, 2)) + ' es mayor a ' + str(round(prob, 2)) + '\n No aprueba. ' + titulo)
    plot.savefig("grafica_rachas_"+str(titulo)+".svg")
    

def grafica_medias(frecuencia_relativa_cantidad_cambios, titulo):
    plot.title('Frecuencia relativa de cambio. ' + titulo)
    plot.bar(range(0, len(frecuencia_relativa_cantidad_cambios)), (frecuencia_relativa_cantidad_cambios))
    plot.xlabel("cantidad de números en la corrida")
    plot.ylabel("Frecuencia relativa de cambio")
    plot.ylim(0, 1)
    plot.xlim(0, 15)
    plot.savefig("grafica_medias_"+str(titulo)+".svg")
    

def main():
  # GENERADORES
  #parte_media_cuadrados()
  lista_GCL = generador_congruencial_lineal(valor_inicial)
  lista_random_org = random_org_generator()
  lista_python = python_generator()
  
  # PRUEBAS
  # Python GEN
  chi_cuadrado(lista_python, 'Python generator')
  prueba_medias(lista_python, 'Python generator')
  prueba_rachas(lista_python, 'Python generator')
  autocorrelacion(lista_python, 'Python generator')

  #### GCL
  chi_cuadrado(lista_GCL, 'GCL')
  prueba_medias(lista_GCL, 'GCL')
  prueba_rachas(lista_GCL, 'GCL')
  autocorrelacion(lista_GCL, 'GCL')

  #### RANDOM.ORG
  chi_cuadrado(lista_random_org, 'Random.org')
  prueba_medias(lista_random_org, 'Random.org')
  prueba_rachas(lista_random_org, 'Random.org')
  autocorrelacion(lista_random_org, 'Random.org')
if __name__ == "__main__":
    main()