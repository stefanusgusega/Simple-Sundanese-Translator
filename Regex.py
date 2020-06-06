# from nltk import tokenize
import re
# import os

class MatchWithRegex:
    def __init__(self,sentence,indotosunda):
        self.sent = sentence
        self.res = []
        self.indokesunda = indotosunda
        self.kalimat = sentence.split(' ')
        if (not indotosunda):
            self.sundaindo = open('sunda.txt','r')
            self.dictsundaindo = self.sundaindo.read()
            while ("teh" in self.kalimat):
                self.kalimat.remove("teh")
        elif (indotosunda):
            self.indosunda = open('indonesia.txt','r')
            self.dictindosunda = self.indosunda.read()

        self.translated = ""
    def solve(self):
        # for c in self.content:
        #     temp_res = []
        #     for c1 in c:
        #         temp_ress = []
        #         for c2 in c1:
        #             if (re.search(self.keyword,c2) == None):
        #                 temp_ress.append(-1)
        #             else:
        #                 temp_ress.append(re.search(self.keyword,c2).start())
        #         temp_res.append(temp_ress)
        #     self.res.append(temp_res)
        if (not self.indokesunda):
            for word in self.kalimat:
                found = re.search(r'(\n|^)%s\b\s='%word,self.dictsundaindo)
                if (found == None):
                    self.res.append(word)
                else:
                    result = ""
                    it = found.end()+1
                    while (self.dictsundaindo[it] != '\n'):
                        result += self.dictsundaindo[it]
                        it += 1
                    self.res.append(result)
        else:
            for word in self.kalimat:
                # found = re.search(r'\n'+word+r'\b\s=',self.dictindosunda)
                found = re.search(r'(\n|^)%s\b\s='%word,self.dictindosunda)

                if (found == None):
                    self.res.append(word)
                else:
                    result = ""
                    it = found.end()+1
                    while (self.dictindosunda[it] != '\n'):
                        result += self.dictindosunda[it]
                        it += 1
                    if (word == "saya" or word == "kamu"):
                        result += " teh"
                    self.res.append(result)
        for word in self.res:
            self.translated += (word + ' ')
# while True:
#     print("1. Indonesia-Sunda")
#     print("2. Sunda-Indonesia")
#     no = int(input())
#     if (no == 1):
#         print("Indonesia - Sunda")
#         print("Indonesia :",end=' ')
#         tobetranslated = str(input())   
#         a = MatchWithRegex(tobetranslated,True)
#         a.solve()
#         print("Sunda : "+a.translated)
#     elif (no == 2):
#         print("Sunda - Indonesia")
#         print("Sunda :",end=' ')
#         tobetranslated = str(input())   
#         a = MatchWithRegex(tobetranslated,False)
#         a.solve()
#         print("Indonesia : "+a.translated)
                

# p = "Good morning Dr. Adams. 2.000 was died. The patient is waiting for you in room number 3."
# print(tokenize.sent_tokenize(p))
# print(re.search("morning",p).start())

# class RegexMatcher:
#     def __init__(self,keyword,folder):
#         self.source = MatchWithRegex(keyword,folder)
#         self.source.solve()
#         self.listres = []
#         self.num = {}
#         self.times = {}
#         self.pair = []
#         self.folder = folder
#         it1 = 0 #filenumber
#         for i in self.source.res:
#             it2 = 0 # line number
#             for j in i:
#                 it3 = 0 # sentence number
#                 for k in j: # k : karakter keberapa
#                     if (k != -1):
#                         self.listres.append((it1,it2,it3,k))
#                     it3 += 1
#                 it2 += 1
#             it1 += 1
#         self.getDictionaryOfNumber()
#         self.time()
#         self.getNumber()
#     def getDictionaryOfNumber(self):
#         pattern = r'(\d+([\.,]?\d+)*)+'
#         thestring = ""
#         for i in range(self.listres.__len__()):
#             delta = 9999999
#             for matching in re.finditer(pattern,self.source.content[self.listres[i][0]][self.listres[i][1]][self.listres[i][2]]):
#                 # print(matching.end())
#                 # print(self.listres[i][3])
#                 # print(delta)
#                 if (abs(matching.end() - self.listres[i][3]) < delta):
#                     delta = abs(matching.end() - self.listres[i][3])
#                     thestring = matching.group()
#                     self.num[self.source.content[self.listres[i][0]][self.listres[i][1]][self.listres[i][2]]] = thestring
    
#     def printRes(self):
#         j = 1
#         for i in self.pair:
#             print(j)
#             j+=1
#             print("Jumlah: "+i[0])
#             print("Waktu: "+i[1])
#             print("Kalimat: "+i[2])
#             # print("File: "+)
#     def getNumber(self):
#         for i in self.num:
#             if (i not in self.times):
#                 self.pair.append((self.num[i],"Unavailable",i))
#             else:
#                 self.pair.append((self.num[i],self.times[i],i))
#         return self.pair
#     def openFile(self,i):
#         f = open(self.folder+'/'+self.source.files[self.listres[i][0]],'r')
#         return f.read().lower()
#     def time(self):
#         pattern = r'[\n]*((senin|selasa|rabu|kamis|jumat|sabtu)[, ]?[ ]*[\(]*\d+[ ]*(/)?(\d+|jan|januari|feb|februari|mar|maret|apr|april|mei|jun|juni|jul|juli|agu|agustus|sep|september|okt|oktober|nov|november|des|desember)(/)?( )*\d+[\)]*)+ (pukul )?(\d+[\.:]?\d+ wib|wit|wita)?[\n]*'
#         for i in range(self.listres.__len__()):
#             delta = 9999999
#             # print(self.openFile(i))
#             if (re.search(pattern,self.openFile(i)) != None):
#                 # print("mskk")
#                 thestring = re.search(pattern,self.openFile(i)).group()
#                 # if (re.finditer(pattern,self.source.content[self.listres[i][0]][self.listres[i][1]][self.listres[i][2]]) == None):
#                 self.times[self.source.content[self.listres[i][0]][self.listres[i][1]][self.listres[i][2]]] = thestring
#             for matching in re.finditer(pattern,self.source.content[self.listres[i][0]][self.listres[i][1]][self.listres[i][2]]):
#                 # print(matching.end())
#                 # print(self.listres[i][3])
#                 # print(delta)
#                 if (abs(matching.end() - self.listres[i][3]) < delta):
#                     delta = abs(matching.end() - self.listres[i][3])
#                     thestring = matching.group()
#                     self.times[self.source.content[self.listres[i][0]][self.listres[i][1]][self.listres[i][2]]] = thestring
# # a = MatchWithRegex("terkonfirmasi positif",os.path.curdir)
# # print(a.content)
# # a.solve()
# # print(a.res)
# # c = RegexMatcher("meninggal dunia",os.path.curdir)
# # print(c.getDictionaryOfNumber())
# # print(c.time())