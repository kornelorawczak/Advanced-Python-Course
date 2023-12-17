import urllib.request
import bs4
#zadanie z poprzedniej listy uzupełnione o funkcje get_sentences i prawidłowe znajdywanie zdań ze słowem "Python"
def crawl(start_page, distance, action):
    visited_pages = set() #zbiór z odwiedzonymi stronami
    pages = [(start_page, 0)] #lista z krotkami w których znajdują się linki stron do odwiedzenia i dystans danej strony
    while pages:
        current_page, current_distance = pages.pop(0)
        if current_page in visited_pages: continue
        try:
            with urllib.request.urlopen(current_page) as page:
                page_content = page.read().decode('utf-8')
                yield (current_page, action(page_content))
                visited_pages.add(current_page)
                if current_distance<distance:
                    soup = bs4.BeautifulSoup(page_content, 'html.parser')
                    #links = [link.get('href') for link in soup.find_all('a')] #szuakamy hiperłącz (tag a) które przenoszą do stron internetowych lub podstron
                    links = [link.get('href') for link in soup.find_all('a') if 'http' in link.get('href')] #alternatywnie jeśli chcemy przechodzić tylko do nowych stron
                    pages.extend((link, current_distance+1) for link in links)
        except Exception as e:
            print(f"Error on {current_page}: {e}")

def get_sentences(text, word):
    return [s for s in text.split(".") if word in s]

for url, wynik in crawl("http://www.ii.uni.wroc.pl", 1, lambda tekst : get_sentences(bs4.BeautifulSoup(tekst, 'html.parser').get_text(separator="."), "Python")):
    print(f"{url}: {wynik}")