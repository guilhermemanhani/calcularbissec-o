
#from numpy import array

x5, x4, x3, x2, x1, x = 0.000, 0.000, 1.000, 0.000, -9.000, 3.000
calc_intervalo_real_num = []
interacaoX= []
interacaoFdeX= []
interacaoBmenosA= []

def calcFdeX(interacao):
    return x5*interacao**5 + x4*interacao**4 + x3*interacao**3 + x2*interacao**2 + x1*interacao + x

def calcularIsolamento(intervalo):
    resultadoFinal =[]
    for i in range(len(intervalo)):
        result = calcFdeX(intervalo[i])
        resultadoFinal.append(result)
        
    return resultadoFinal

def calcularIntervalo(array_resultado, intervalo):
    resultadoFinal =[]
    # print(array_resultado, intervalo)
    for i in range(len(intervalo)-1):
        if array_resultado[i]<1 and array_resultado[i+1]>-1 or array_resultado[i]>-1 and array_resultado[i+1]<1:
            resultadoFinal.append(intervalo[i])
            resultadoFinal.append(intervalo[i+1])
            calc_intervalo_real_num.append(array_resultado[i])
            calc_intervalo_real_num.append(array_resultado[i+1])
    # print(resultadoFinal)
    return resultadoFinal

def calcZeroReais (a, b):
    resultFdeX = 0
    interacao = (a+b)/2
    criterio_de_parada = abs((b-a)/2)
    resultFdeX = calcFdeX(interacao)
    # print(a, b)
    print(interacao, resultFdeX, criterio_de_parada)
# #     print(interacao)
#     print(resultFdeX)
    interacaoX.append(interacao) #esse e o resultado do b - a
    interacaoFdeX.append(resultFdeX)
    interacaoBmenosA.append(abs(b-a)/2)
    if criterio_de_parada < 10**-3:
        # print(interacao, resultFdeX, criterio_de_parada)
        interacaoX.append(interacao)
        return interacaoX

    if resultFdeX < 0:
        calcZeroReais(a, interacao)
    if resultFdeX > 0:
        calcZeroReais(interacao, b)
def filtraParaCalcular(calc_intervalo_real_num, calc_intervalo):
    #calcZeroReais(0, 1)
    tamanho_array = len(calc_intervalo)
    for i in range (0, tamanho_array, 2):
        if calc_intervalo_real_num[i]>0:
            # print(calc_intervalo[i], calc_intervalo[i+1])
            calcZeroReais(calc_intervalo[i], calc_intervalo[i+1])
        else:
            # print(calc_intervalo[i], calc_intervalo[i+1])
            calcZeroReais(calc_intervalo[i+1], calc_intervalo[i])

intervalo = list(range(-500, 501))
resultado = calcularIsolamento(intervalo)
calc_intervalo = calcularIntervalo(resultado, intervalo)
# print (calc_intervalo, calc_intervalo_real_num)
filtraParaCalcular(calc_intervalo_real_num, calc_intervalo)


# print(interacaoX)
# print(interacaoFdeX)
# print(interacaoBmenosA)
# print(resultado)
# print(calc_intervalo_real_num)
# print(calc_intervalo)
#print(calcFdeX(x5, x4, x3, x2, x1, x, -5))


