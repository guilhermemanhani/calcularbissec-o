# from numpy import array
x5, x4, x3, x2, x1, x = 0.000, 0.000, 1.000, 0.000, -9.000, 3.000
interacaoX= []
interacaoFdeX= []
interacaoBmenosA= []

def calcFdeX(interacao):
    return x5*interacao**5 + x4*interacao**4 + x3*interacao**3 + x2*interacao**2 + x1*interacao + x

def calcularIsolamento(x5, x4, x3, x2, x1, x, intervalo):
    resultadoFinal =[]
    for _ in range (intervalo*-2):
        result = x5*intervalo**5 + x4*intervalo**4 + x3*intervalo**3 + x2*intervalo**2 + x1*intervalo + x
        intervalo = intervalo +1
        resultadoFinal.append(result) 
    return resultadoFinal

def calcularIntervalo(array_resultado, intervalo):
    resultadoFinal =[]
    for i in range (intervalo*-2-1):
        if (array_resultado[i]<0 and array_resultado[i+1]>0) or (array_resultado[i]>0 and array_resultado[i+1]<0) :
            resultadoFinal.append(intervalo)
            resultadoFinal.append(intervalo+1)
        intervalo = intervalo+1
    return resultadoFinal

def calcZeroReais (x5, x4, x3, x2, x1, x, a, b):
    resultFdeX = 0
    interacao = abs((a+b)/2)
    print(interacao)
    if interacao < 10**-3:
        interacaoX.append(interacao)
        return interacaoX
    resultFdeX = calcFdeX(x5, x4, x3, x2, x1, x, interacao)
    print(resultFdeX)
    interacaoX.append(interacao) #esse e o resultado do b - a
    interacaoFdeX.append(resultFdeX)
    interacaoBmenosA.append(abs(b-a)/2)

    if resultFdeX < 0:
        calcZeroReais(x5, x4, x3, x2, x1, x, interacao, b)
    if resultFdeX > 0:
        calcZeroReais(x5, x4, x3, x2, x1, x, a, interacao)

intervalo = -5
resultado = calcularIsolamento(x5, x4, x3, x2, x1, x, intervalo)
calc_intervalo = calcularIntervalo(resultado, intervalo)
zeroReal = calcZeroReais(x5, x4, x3, x2, x1, x, 0, 1)
# print(interacaoX)
# print(interacaoFdeX)
# print(interacaoBmenosA)
# print(resultado)
# print(calc_intervalo)
#print(calcFdeX(x5, x4, x3, x2, x1, x, -5))

