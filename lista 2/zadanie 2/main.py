def sudan(n, x, y, memo={}, ismemo=False):
    if x<0 or y<0: return "x i y muszą być nieujemne!"
    if n==0: return x+y
    elif y==0: return x
    elif ismemo==True:
        if (n,x,y) in memo: return memo[(n,x,y)]
        else:
            result = sudan(n-1, sudan(n,x,y-1,memo,ismemo=True), sudan(n,x,y-1,memo,ismemo=True)+y+1,memo,ismemo=True)
            memo.update({(n,x,y):result})
            return result
    return sudan(n-1, sudan(n,x,y-1), sudan(n,x,y-1)+y+1)
print(sudan(2,20,1))
print(sudan(1,994,997, ismemo=True))


#bez spamiętywania jest sens dla n<3 (dla n=2 -> x<24, y<2) i (dla n=1 -> x raczej dowolny, y<25)
#z spamiętywaniem jest sens dla n<3 (dla n=2 i y=2 -> x<5; dla n=2 i y=1 -> x<995) i (dla n=1 -> x raczej dowolny, y<997)

#oczywiście to testowane na moim, trochę przestarzyłym komputerze