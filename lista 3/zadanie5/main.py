

def max_sublist_suma(lista):
    maxsum=float("-inf")
    currentreturnal=()
    for i in range(len(lista)):
        for j in range(i,len(lista)):
            if sum(lista[i:j+1])>maxsum:
                maxsum=sum(lista[i:j+1])
                currentreturnal=(i,j)
    return currentreturnal

print(max_sublist_suma([]))
print(max_sublist_suma([1,5,3,2,5,6,-2,-6,5,100,-254,23,-32]))


