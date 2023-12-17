
def word_to_number(listofwords, langnumbers): #działa tylko dla polskiego lub angielskiego
    listofnumbers = []
    for word in listofwords:
        if word in langnumbers:
            listofnumbers.append(langnumbers[word])
        else:
            splitlist = word.replace("-"," ").split(" ")
            number = 0
            for w in splitlist:
                if w == "tysiące" or w == "tysięcy" or w == "thousand":
                    number *= 1000
                elif w == "hundred":
                    number *= 100
                else:
                    number += langnumbers[w]
            if splitlist[0] == "minus":
                listofnumbers.append(number * (-1))
            else:
                listofnumbers.append(number)
    return listofnumbers

def worded_nums_sort(listofwords, lang='pl', rev=False):
    liczby_pl={'minus': 0, 'zero': 0, 'jeden': 1, 'dwa': 2, 'trzy': 3, 'cztery': 4, 'pięć': 5,
        'sześć': 6, 'siedem': 7, 'osiem': 8, 'dziewięć': 9, 'dziesięć': 10,
        'jedenaście': 11, 'dwanaście': 12, 'trzynaście': 13, 'czternaście': 14,
        'piętnaście': 15, 'szesnaście': 16, 'siedemnaście': 17, 'osiemnaście': 18,
        'dziewiętnaście': 19, 'dwadzieścia': 20, 'trzydzieści': 30, 'czterdzieści': 40,
        'pięćdziesiąt': 50, 'sześćdziesiąt': 60, 'siedemdziesiąt': 70,
        'osiemdziesiąt': 80, 'dziewięćdziesiąt': 90, 'sto': 100, 'sto': 100,
        'dwieście': 200, 'trzysta': 300, 'czterysta': 400, 'pięćset': 500,
        'sześćset': 600, 'siedemset': 700, 'osiemset': 800, 'dziewięćset': 900,
        'tysiąc': 1000, 'tysiące': 1000, "tysięcy": 1000}

    liczby_eng={"minus": 0, 'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
        'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
        'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
        'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
        'eighty': 80, 'ninety': 90, 'hundred': 100, 'thousand': 1000}

    listofnumbers=[]
    if lang=='pl': listofnumbers=word_to_number(listofwords, liczby_pl)
    elif lang=='eng': listofnumbers=word_to_number(listofwords, liczby_eng)
    return sorted(listofwords, key=lambda x:listofnumbers[listofwords.index(x)], reverse=rev)

#print(worded_nums_sort(["osiemset pięćdziesiąt cztery tysiące dziewięćset siedemdziesiąt osiem","osiem","dwadzieścia cztery", "tysiąc czterdzieści siedem", "trzydzieści tysięcy dwieście", "minus osiemset piętnaście"]))
print(worded_nums_sort(["osiemset pięćdziesiąt cztery tysiące dziewięćset siedemdziesiąt osiem","osiem","dwadzieścia cztery",\
                        "tysiąc czterdzieści siedem", "trzydzieści tysięcy dwieście", "minus osiemset piętnaście"],rev=True))
print(worded_nums_sort([]))
print(worded_nums_sort(["minus ninety-eight", "eighty-three thousand two hundred sixty-four", \
                        "eight thousand seven hundred thirty-four", "minus nine", "seventeen"],lang='eng'))


