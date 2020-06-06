from BoyerMoore import MatchWithBoyerMoore
from KMP import MatchWithKMP
from Regex import MatchWithRegex

while True:
    print("1. Indonesia-Sunda")
    print("2. Sunda-Indonesia")
    no = int(input())
    print("Method: ")
    print("1. KMP")
    print("2. Boyer Moore")
    print("3. Regex")
    method = int(input())
    if (no == 1):
        print("Indonesia - Sunda")
        print("Indonesia :",end=' ')
        tobetranslated = str(input())   
        if (method == 1):
            a = MatchWithKMP(tobetranslated,True)
            a.solve()
        elif (method == 2):
            a = MatchWithBoyerMoore(tobetranslated, True)
            a.solve()
        elif (method == 3):
            a = MatchWithRegex(tobetranslated, True)
            a.solve()
        print("Sunda : "+a.translated)
    elif (no == 2):
        print("Sunda - Indonesia")
        print("Sunda :",end=' ')
        tobetranslated = str(input())   
        if (method == 1):
            a = MatchWithKMP(tobetranslated,False)
            a.solve()
        elif (method == 2):
            a = MatchWithBoyerMoore(tobetranslated, False)
            a.solve()
        elif (method == 3):
            a = MatchWithRegex(tobetranslated, False)
            a.solve()
        print("Indonesia : "+a.translated)