#kwadrat będzie o wymiarach 2x2, wyznaczać go będą współrzędne x,y z przedziału [-1,1]
import random, math
def rounding_pi_simulator1(shots): #sposób pierwszy, z wpisaniem w argument funkcji ilość strzałów w tarczę
    cltwt=ltwo=0
    for i in range(shots):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        cltwt+=1
        if x**2+y**2<=1: ltwo+=1
        print(4*ltwo/cltwt)

def rounding_pi_simulator2(diff): #sposób drugi, z wpisaniem różnicy przybliżanego pi do naszego symulowanego pi
    cltwt = ltwo = 0
    simpi=0
    while abs(math.pi-simpi)>diff:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        cltwt += 1
        if x ** 2 + y ** 2 <= 1: ltwo += 1
        simpi=4 * ltwo / cltwt
        print(simpi)
    print("Przybliżenie liczby pi naszą symulacją z dokładnością do "+str(diff)+" zakończyło się po "+str(cltwt)+" rzutach w tarczę.")

rounding_pi_simulator2(0.001)