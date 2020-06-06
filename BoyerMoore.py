# from nltk import tokenize
# import os
import re

class MatchWithBoyerMoore:
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
        # for f_name in os.listdir(folder):
        #     if f_name.endswith(".txt"):
        #         f = open(folder+'/'+f_name,'r')
        #         self.files.append(f_name)
        #         temp_content = []
        #         for line in f.readlines():
        #             temp_content.append(tokenize.sent_tokenize(line.lower()))
        #         self.content.append(temp_content)
        # self.res = []
    def buildLast(self): # saving last occurence of each ASCII char in pattern.
        last = [[-1 for i in range (128)] for j in range(self.kalimat.__len__())]
        j = 0
        for word in self.kalimat:
            for i in range(word.__len__()):
                last[j][ord(word[i])] = i
            j += 1
        return last


    def solve(self):
        # last = self.buildLast()
        # for c in self.content:
        #     temp_res = []
        #     for c1 in c:
        #         temp_ress = []
        #         for c2 in c1:
        #             n = c2.__len__()
        #             m = self.keyword.__len__()
        #             i = m-1
        #             # if (i > n-1):
        #             #     temp_ress.append(-1)
        #                 # return -1 # no match if pattern is longer than text
        #             j = m-1
        #             found = False
        #             while(i <= n-1 and not found):
        #                 if (self.keyword[j] == c2[i]):
        #                     if (j == 0):
        #                         temp_ress.append(i)
        #                         found = True
        #                         # return i # match
        #                     else:
        #                         i -= 1
        #                         j -= 1
        #                 else:
        #                     lo = last[ord(c2[i])]
        #                     i = i + m - min(j, 1+lo)
        #                     j = m-1
        #             if (not found):
        #                 temp_ress.append(-1)
        #             # return -1
        #         temp_res.append(temp_ress)
        #     self.res.append(temp_res)

        last = self.buildLast()
        if (self.indokesunda):
            sen = 0
            for word in self.kalimat:
                n = self.dictindosunda.__len__()
                m = word.__len__()
                i = m-1
                # if (i > n-1):
                #     self.res.append(word)
                #     sen += 1
                j = m-1
                found = False
                while (i <= n-1 and not found) :
                    if (word[j] == self.dictindosunda[i] and j >= 0):
                        if (j==0 and (self.dictindosunda[i-1]=='\n' or i==0) and self.dictindosunda[i+word.__len__()+1]=='='):# kalo 2 kar stlhnya samadengan
                            result = ""
                            it = i + word.__len__() + 3
                            while (self.dictindosunda[it] != '\n'):
                                result += self.dictindosunda[it]
                                it += 1
                            if (word == "saya" or word == "kamu"):
                                result += " teh"
                            found = True
                            sen += 1
                            self.res.append(result)
                        else :
                            i -= 1
                            j -= 1
                    else:
                        # print(sen)
                        # print(ord(self.dictindosunda[i]))
                        lo = last[sen][ord(self.dictindosunda[i])]
                        i = i + m - min(j, 1+lo)
                        j = m-1
                if (not found) :
                    sen += 1
                    self.res.append(word)
        else:
            sen = 0
            for word in self.kalimat:
                n = self.dictsundaindo.__len__()
                m = word.__len__()
                i = m-1
                # if (i > n-1):
                #     self.res.append(word)
                #     sen += 1
                j = m-1
                found = False
                while (i <= n-1 and not found) :
                    # print(str(j)+" "+str(i))
                    # print(self.dictsundaindo[i])
                    # print(word[j])
                    # print(self.dictsundaindo[i+word.__len__()+1])
                    if (word[j] == self.dictsundaindo[i] and j >= 0):
                        if (j==0 and (self.dictsundaindo[i-1]=='\n' or i==0) and self.dictsundaindo[i+word.__len__()+1]=='='):# kalo 2 kar stlhnya samadengan
                            result = ""
                            it = i + word.__len__() + 3
                            while (self.dictsundaindo[it] != '\n'):
                                result += self.dictsundaindo[it]
                                it += 1
                            found = True
                            sen += 1
                            self.res.append(result)
                        else :
                            i -= 1
                            j -= 1
                    else:
                        # print(sen)
                        # print(ord(self.dictindosunda[i]))
                        lo = last[sen][ord(self.dictsundaindo[i])]
                        i = i + m - min(j, 1+lo)
                        j = m-1
                if (not found) :
                    sen += 1
                    self.res.append(word)
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
#         a = MatchWithBoyerMoore(tobetranslated,True)
#         a.solve()
#         print("Sunda : "+a.translated)
#     elif (no == 2):
#         print("Sunda - Indonesia")
#         print("Sunda :",end=' ')
#         tobetranslated = str(input())   
#         a = MatchWithBoyerMoore(tobetranslated,False)
#         a.solve()
#         print("Indonesia : "+a.translated)
# class BoyerMooreMatcher:
#     def __init__(self,keyword,folder):
#         self.source = MatchWithBoyerMoore(keyword,folder)
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
        

# # a =MatchWithBoyerMoore("terkonfirmasi positif",os.path.curdir)
# # print(a.files)
# # print(a.content)
# # a.solve()
# # b = BoyerMooreMatcher("meninggal dunia",os.path.curdir)
# # print(b.getDictionaryOfNumber())
# # print(b.time())
