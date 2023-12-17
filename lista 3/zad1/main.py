from collections import deque
from itertools import islice
def longestpalindroms(t):
    text=deque(t.lower())
    maxlengpalindroms=[]
    maxleng=2
    for i in range(len(text)):
        iscurrentlypalindrom = False
        currentstart=text[i]
        for j in range(i+2,len(text)): #zaczynamy od i+2 bo i tak palindrom musi być co najmniej o długości 2
            current = ''.join(x for x in islice(text, i, j) if x.isalnum()).replace(" ","")
            if current==current[::-1] and iscurrentlypalindrom==False: iscurrentlypalindrom=True
            elif current!=current[::-1] and iscurrentlypalindrom:
                if len(''.join(islice(text,i,j-1)).replace(" ",""))>1:
                    if (j-i-1)==maxleng:
                        maxlengpalindroms.append((i+1, j-i-1))
                    elif (j-i-1)>maxleng:
                        maxleng=j-i-1
                        maxlengpalindroms.clear()
                        maxlengpalindroms.append((i+1, j-i-1))
                break
    return maxlengpalindroms

print(longestpalindroms("man Do geese see God? Long Live TeNet.. Always Race fast, safe car please"))
#(48, 20) = "Race fast, safe car "
print(longestpalindroms("Pozorny Brak Palindromów tutaj"))
print(longestpalindroms("hasudhoaisjdasopdjaois"))
print(longestpalindroms("    ."))


