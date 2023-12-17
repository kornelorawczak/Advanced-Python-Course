def is_palindrom(text):
    text2=''.join([l.lower() for l in text if l.isalpha()])
    return text2==text2[::-1]


print(is_palindrom("mić &% ćiM"))                           #True
print(is_palindrom("Eine güldne, gute Tugend: Lüge nie!"))  #True
print(is_palindrom("Míč omočím."))                          #True
print(is_palindrom("Kobyła ma mały bok."))                  #True
print(is_palindrom("Testuje niepoprawność"))                #False
print(is_palindrom("Eine güldne, guten Tugend: Lüge nie!")) #False