def common_prefix(lista_slow):
    maxlen=max([len(slowo) for slowo in lista_slow])
    prefixlength=1
    maxprefixcount = 0
    while True:
        for i in range(len(lista_slow)):
            currentprefix=lista_slow[i][:prefixlength].lower()
            currentprefixcount=0
            for slowo in lista_slow:
                if slowo.lower().startswith(currentprefix): currentprefixcount+=1
            if currentprefixcount>maxprefixcount:
                maxprefixcount=currentprefixcount
                currentmaxprefix=currentprefix
        if maxprefixcount>2:
            returnableprefix=currentmaxprefix
            prefixlength+=1
            if prefixlength>maxlen: return returnableprefix
            maxprefixcount = 0
        elif prefixlength == 1: return "no common prefix"
        else: return returnableprefix



print(common_prefix(["Cyprian", "cyberotoman", "cynik", "ceniąc", "czule"]))
print(common_prefix(["Cyprian", "Cyprian", "Cyprian", "Cyprian" ]))
print(common_prefix(["Cyprian", "abprian", "efprian", "Cyprian" ]))
print(common_prefix(["Aczkolwiek","Cyprian", "cyberotoman", "cynik", "ceniąc", "czule"]))