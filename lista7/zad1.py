import urllib.request
import bs4
import threading
#zadanie z poprzedniej listy uzupełnione o funkcje get_sentences i prawidłowe znajdywanie zdań ze słowem "Python"
#w tej implementacji użyjemy thread lock aby zapobiec problemowi w którym dwa wątki są odpalone i działają na tych samych stronach internetowych
lock = threading.Lock()
def lockprint(msg): #będziemy używać tej funkcji do wywoływania funkcji action, która dzięki aktywacji blokady lock uniemożliwi jednoczesnemy
                    # wykonywaniu się kilku procesów o współdzielonych danych
    with lock:
        print(msg)
def crawl(start_page, distance, action):
    visited_pages = set() #zbiór z odwiedzonymi stronami
    pages = [(start_page, 0)] #lista z krotkami w których znajdują się linki stron do odwiedzenia i dystans danej strony
    def process_page(url, current_distance):
        try:
            with urllib.request.urlopen(url) as page:
                page_content = page.read().decode('utf-8')
                soup = bs4.BeautifulSoup(page_content, 'html.parser')
            lockprint(f"{url}: {action(soup)}")
            visited_pages.add(url)
            if current_distance<distance:
                #links = [link.get('href') for link in soup.find_all('a')] #szuakamy hiperłącz (tag a) które przenoszą do stron internetowych lub podstron
                links = [link.get('href') for link in soup.find_all('a') if 'http' in link.get('href')] #alternatywnie jeśli chcemy przechodzić tylko do nowych stron
                pages.extend((link, current_distance+1) for link in links)
                for link in links:
                    if link not in visited_pages:
                        threading.Thread(target=process_page, args=(link, distance+1)).start()
        except Exception as e:
            print(f"Error on {url}: {e}")

    while pages:
        current_page, current_distance = pages.pop(0)
        if current_page in visited_pages: continue
        threading.Thread(target=process_page, args=(current_page, current_distance)).start()

def get_sentences(text, word):
    return [s for s in text.split(".") if word in s]

crawl("http://www.ii.uni.wroc.pl", 1, lambda tekst : get_sentences(tekst.get_text(separator="."), "Python"))

# for url, wynik in crawl("http://www.ii.uni.wroc.pl", 1, lambda tekst : get_sentences(bs4.BeautifulSoup(tekst, 'html.parser').get_text(separator="."), "Python")):
#     print(f"{url}: {wynik}")

#Obecne zastosowanie thread lock sprawia że dane są thread-safe, jednak bez tego występywały problemy z otwieraniem w osobynch wątkach tych samych stron
#jednocześnie i double printowanie. Do rozwiązania problemu posiłkowałem się następującymi linkami:
#https://stackoverflow.com/questions/70396519/make-sure-each-print-is-on-a-newline-when-threading-indefinitely-in-python
#https://www.pythontutorial.net/python-concurrency/python-threading-lock/