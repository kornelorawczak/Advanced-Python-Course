import random
import urllib.request, re

def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
    output=""
    for zdanie in tekst.replace("! ",". ").replace("? ",". ").split(". "):
        slowa=[x for x in zdanie.split(" ") if len(x)<=dl_slowa]
        while len(slowa)>liczba_slow: slowa.remove(random.choice(slowa))
        slowa[0]=slowa[0].capitalize()
        obecnezdanie=' '.join(slowa)
        if obecnezdanie[-1]!=".": obecnezdanie+=". "
        output+=obecnezdanie
    return output




tekst = "Podział peryklinalny inicjałów wrzecionowatych \
kambium charakteryzuje się ścianą podziałową inicjowaną \
w płaszczyźnie maksymalnej."
print(uprosc_zdanie(tekst, 10, 5)+"\n")
tekst="Lista światowego dziedzictwa UNESCO w Kirgistanie – lista miejsc w Kirgistanie wpisanych na listę światowego dziedzictwa UNESCO, ustanowioną na mocy Konwencji w sprawie ochrony światowego dziedzictwa kulturowego i naturalnego, przyjętą przez UNESCO na 17 sesji w Paryżu 16 listopada 1972[1] i ratyfikowaną przez Kirgistan 3 lipca 1995 roku[2]? Podział peryklinalny inicjałów wrzecionowatych kambium charakteryzuje się ścianą podziałową inicjowaną w płaszczyźnie maksymalnej."
print(uprosc_zdanie(tekst, 10, 5)+"\n")

url = "https://www.gutenberg.org/cache/epub/98/pg98-images.html#link2H_4_0002" #jeden z możliwych kodów pobierania tekstu ze strony internetowej, taki który nie potrzebuje instalacji dodatkowych modułów
response = urllib.request.urlopen(url)
html_content = response.read().decode('utf-8')
pattern = r"In England, (.*?)<p>"
matches=re.findall(pattern, html_content, re.DOTALL)
if matches: text=matches[0].strip().replace("      ","")[:-9] #komendy potrzebne aby ten tekst miał sensowną składnie
print(uprosc_zdanie(text, 10,8))