def tabliczka(x1, x2, y1, y2, d, prec=1):
    tabx=[]; taby=[]
    for i in range(int((x2-x1)/d)+1): tabx.append(x1+i*d)
    for i in range(int((y2 - y1) / d) + 1): taby.append(y1 + i * d)
    width = max([len(str(round(x * y, prec))) for x in tabx for y in taby])
    if all(i > 0 for i in tabx + taby)==False: width+=1
    print(" "*(width-prec)+''.join([" "*(1+(width-len(str(round(x,prec)))))+str(round(x,prec)) for x in tabx]))
    for y in range(len(taby)):
        print(" "*(width-len(str(round(taby[y],prec)))-prec) + str(round(taby[y],prec)),end="")
        for x in range(len(tabx)):
            c=round(taby[y]*tabx[x],prec)+0
            print(" "*(1+(width-len(str(c))))+str(c),end="")
        print("")

tabliczka(3.0, 5.0, 2.0, 4.0, 1.0)
print("-"*50)
tabliczka(3.2, 7.2, 2.3, 4.3, 1.0,2)
print("-"*50)
tabliczka(3.0, -3.0, 2.5, -5.5, -2.0)
print("-"*50)
tabliczka(-2.0, 10, -4, 8, 2.0)