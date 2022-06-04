import numpy as np
import sympy as sym
import math
import sys
import time





       
    
    

def tabela_x(n, L):
    a = - L                                         #devolve o array completo das raizes xi, dado n e as raizes positivas
    if n % 2 == 0:
        return np.concatenate((a, L))                 
    return np.concatenate((a, [0], L))

def tabela_w(n, L):                                         #cria a lista completa dos pesos wi dado n e os pesos positivos, 
    if n % 2 ==0:
        return np.concatenate((L, L))      #usa o fato de que a soma de todos os pesos é o tamanho do intervalo
    return np.concatenate((L, [2-2*(L.sum())], L))
#
def integra(a, b, c, d, f, n, r, w):    #na integral dupla calcula-se primeiro para cada ponto x fixo, a integral em y que corresponde a area A(x) determinada pela interseção do plano correspondente com o sólido. Após isso                   
    I = 0
    for j in range(len(r)):                #laço que atualiza a integral dupla
        x_t = 1/2*((b-a)*r[j]+a+b)      #transformação de coordenadas para o intervalo de integração em x
        I_int = 0                       #aproximação para a integral interna, correspondente aos A(y) para x fixp
        for i in range(0,n):
            I_int += w[i]*f(x_t,((d(x_t)-c(x_t))*r[i]+d(x_t)+c(x_t))/2)   # atualização de I_int a cada iteração, considerando os nós em y_i (e portanto função de x_i) correspondentes e já com a transformação de coordenadas correspondente
        I_int = I_int*w[j]*((d(x_t)-c(x_t))/2)                                 # multiplicação pelo fator de escala da integral interna
        I += I_int
    I *= (b-a)/2                                                        # multipl. pelo fator de escala da integral externa
    return I    

    
if __name__ == "__main__":
    #dados do enunciado
    x6 = np.array([0.2386191860831969086305017, 0.6612093864662645136613996, 0.9324695142031520278123016])
    x8 = np.array([0.1834346424956498049394761, 0.5255324099163289858177390, 0.7966664774136267395915539, 0.9602898564975362316835609])	
    x10 = np.array([0.1488743389816312108848260, 0.4333953941292471907992659, 0.6794095682990244062343274, 0.8650633666889845107320967, 0.9739065285171717200779640])	
    w6 = np.array([0.4679139345726910473898703, 0.3607615730481386075698335, 0.1713244923791703450402961])
    w8 = np.array([0.3626837833783619829651504, 0.3137066458778872873379622, 0.2223810344533744705443560, 0.1012285362903762591525314])
    w10 = np.array([0.2955242247147528701738930, 0.2692667193099963550912269, 0.2190863625159820439955349, 0.1494513491505805931457763, 0.0666713443086881375935688])

    start_time = time.time()
    print(integra(0,1, lambda x: 0, lambda x: 1, lambda x,y: 1, 6, tabela_x(6,x6), tabela_w(6,w6)))
    print(integra(0,1, lambda x: 0, lambda x: 1-x, (lambda x,y: 1-x-y), 6, tabela_x(6,x6), tabela_w(6,w6)))
    print(integra(0,1, lambda x: 0, lambda x: 1-x**2, (lambda x,y: 1), 6, tabela_x(6,x6), tabela_w(6,w6)))
    print(integra(0.1, 0.5, lambda x: x**3, lambda x: x**2, lambda x,y: (math.e)**(y/x), 6, tabela_x(6,x6), tabela_w(6,w6)))
    
    print("Tempo decorrido para gerar solucao: ", time.time() - start_time)


