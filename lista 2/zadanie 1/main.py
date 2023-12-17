
def mandates_given(votes, mandates):
    allvotes=sum(votes.values())
    current_mandates=dict.fromkeys(votes,0)
    division = sorted([(komitet,G/i) for i in range(1,mandates+1) for komitet,G in votes.items() if G/i>=allvotes*0.05],key=lambda x:x[1],reverse=True)[:8]
    for d in division:
        current_mandates[d[0]]+=1
    return current_mandates


votes = {"Komitet A":720, "Komitet B":300, "Komitet C":480}
print(mandates_given(votes,8))