import urllib.request, re, string

def kompresja(tekst):
    # necessary = string.ascii_letters + string.punctuation + " " + "’" + "”" + "“" #tworzenie ciągu znaków które są literami albo znakami przestankowymi (z założenia zadania) i dodatkowo spacja, bo inaczej dłuższy tekst nie ma sensu
    # tekst=''.join(l for l in tekst if l in necessary)
    counter=1
    previous = tekst[0]
    cipher=[]
    for i in range(1,len(tekst)):
        if tekst[i]==previous: counter+=1
        else:
            cipher.append((counter,previous))
            previous=tekst[i]
            counter=1
    cipher.append((counter, previous))
    return cipher

def dekompresja(tekst_skompresowany):
    return ''.join(x[0]*x[1] for x in tekst_skompresowany)

print(kompresja("suupeer teeleeeffon"))
print(dekompresja(kompresja("suupeer teeleeeffon")))
print("suupeer teeleeeffon"==dekompresja(kompresja("suupeer teeleeeffon")))

url = "https://www.gutenberg.org/cache/epub/98/pg98-images.html#link2H_4_0002" #jeden z możliwych kodów pobierania tekstu ze strony internetowej, taki który nie potrzebuje instalacji dodatkowych modułów
response = urllib.request.urlopen(url)
html_content = response.read().decode('utf-8')
pattern = r"In England, (.*?)<p>"
matches=re.findall(pattern, html_content, re.DOTALL)
if matches: text=matches[0].strip().replace("      "," ")[:-9] #komendy potrzebne aby ten tekst miał sensowną składnie
text=" ".join(text.split())

print(kompresja(text))
print(dekompresja(kompresja(text)))
print(text==dekompresja(kompresja(text)))