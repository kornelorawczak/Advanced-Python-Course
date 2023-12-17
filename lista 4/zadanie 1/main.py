import math,timeit
from tabulate import tabulate #moduł tabulate który instalujemy z pipa, aby nie zagłębiać się bardzo w pretty printing tablicy z czasami na końcu

# def pierwsze_imperatywna_sito(n):
#     tab = [True]*(n+1)
#     prime_numbers=[]
#     for i in range(2, n):
#         if tab[i]:
#             prime_numbers.append(i)
#             for j in range(i, n, i):
#                 tab[j]=False
#     return prime_numbers

def pierwsze_imperatywna(n):
    tab=[]
    for x in range(2,n):
        isprime=True
        for y in range(2,int(math.sqrt(x))+1):
            if x%y==0:
                isprime=False
                break
        if isprime: tab.append(x)
    return tab


def pierwsze_skladana(n):
    return [x for x in range(2, n) if True not in [x%y==0 for y in range(2,int(math.sqrt(x))+1)]] #możnaby to uprościć używając funkcji all() ale nie byłem pewny czy w tej wersji zadania można takiej użyć

def pierwsze_funkcyjna(n):
    return list(filter(lambda x: all(x%y!=0 for y in range(2,int(math.sqrt(x))+1)), [x for x in range (2,n)]))


n = [100,200,1000,10000,100000]
t=[['n','imperatywna','skladana','funkcyjna']]
for x in n:
    tt=[str(x)+":"]
    start = timeit.default_timer()
    pierwsze_imperatywna(x)
    tt.append(format(timeit.default_timer()-start,'f'))

    start = timeit.default_timer()
    pierwsze_skladana(x)
    tt.append(format(timeit.default_timer() - start, 'f'))

    start = timeit.default_timer()
    pierwsze_funkcyjna(x)
    tt.append(format(timeit.default_timer() - start, 'f'))
    t.append(tt)

print(tabulate(t))


# print(pierwsze_imperatywna(20))
# print(pierwsze_skladana(20))
# print(pierwsze_funkcyjna(20))
