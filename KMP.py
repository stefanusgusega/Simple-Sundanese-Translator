from nltk import tokenize
import os
import re


class MatchWithKMP:
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
    def borderFunction(self):
        # fail = [0 for i in range(self.keyword.__len__())]
        # m = self.keyword.__len__()
        # j = 0
        # i = 1
        # while (i < m) :
        #     if (self.keyword[j] == self.keyword[i]): # j+1 chars match
        #         fail[i] = j+1
        #         i+=1
        #         j += 1
        #     elif (j > 0): # j follows matching prefix
        #         j = fail[j-1]
        #     else:
        #         fail[i] = 0
        #         i += 1
        # return fail
        fail = [[] for i in range (self.kalimat.__len__())]
        ctr = 0
        for word in self.kalimat:
            arr = [0 for i in range (word.__len__())]
            m = word.__len__()
            j = 0
            i = 1
            while (i < m):
                if (word[j] == word[i]):
                    arr[i] = j+1
                    i += 1
                    j += 1
                elif (j > 0):
                    j = arr[j-1]
                else:
                    arr[i] = 0
                    i += 1
            fail[ctr] = arr
            ctr += 1
        return fail
    def solve(self): # returns index where pattern starts
        # for c in self.content:
        #     temp_res = []
        #     for c1 in c:
        #         temp_ress = []
        #         for c2 in c1:
        #             n = c2.__len__()
        #             m = self.keyword.__len__()
        #             fail = self.borderFunction()
        #             i = 0
        #             j = 0
        #             found = False
        #             while (i < n and not found):
        #                 if (self.keyword[j] == c2[i]):
        #                     if (j == m-1):
        #                         temp_ress.append(i-m+1)
        #                         found = True
        #                     i += 1
        #                     j += 1
        #                 elif (j > 0):
        #                     j = fail[j-1]
        #                 else:
        #                     i += 1
        #             if (not found):
        #                 # return -1
        #                 temp_ress.append(-1)
        #         temp_res.append(temp_ress)
        #     self.res.append(temp_res)
        if (self.indokesunda):
            ctr = 0
            for word in self.kalimat:
                n = self.dictindosunda.__len__()
                m = word.__len__()
                fail = self.borderFunction()
                i = 0
                j = 0
                found = False
                while (i < n and not found):
                    if (j > m-1):
                        j = fail[ctr][j-1]
                    if (word[j] == self.dictindosunda[i]):
                        if (j == m-1 and (self.dictindosunda[i-m]=='\n' or i==0) and self.dictindosunda[i-m+1+word.__len__()+1]=='='):
                            result = ""
                            it = i-m+1 + word.__len__() + 3
                            while (self.dictindosunda[it] != '\n'):
                                result += self.dictindosunda[it]
                                it += 1
                            if (word == "saya" or word == "kamu"):
                                result += " teh"
                            found = True
                            ctr += 1
                            self.res.append(result)
                        i += 1
                        j += 1
                    elif (j > 0):
                        j = fail[ctr][j-1]
                    else:
                        i += 1
                if (not found):
                    self.res.append(word)
        else:
            ctr = 0
            for word in self.kalimat:
                n = self.dictsundaindo.__len__()
                m = word.__len__()
                fail = self.borderFunction()
                i = 0
                j = 0
                found = False
                while (i < n and not found):
                    # print(str(j)+" "+str(i)+' '+str(m-1))
                    # print(self.dictsundaindo[i-m])
                    # print(word[j])
                    # print(self.dictsundaindo[i-m+1+word.__len__()+1])
                    if (j > m-1):
                        j = fail[ctr][j-1]
                    if (word[j] == self.dictsundaindo[i]):
                        if (j == m-1 and (self.dictsundaindo[i-m]=='\n' or i-m+1==0) and self.dictsundaindo[i-m+1+word.__len__()+1]=='='):
                            result = ""
                            it = i-m+1 + word.__len__() + 3
                            while (self.dictsundaindo[it] != '\n'):
                                result += self.dictsundaindo[it]
                                it += 1
                            ctr += 1
                            found = True
                            self.res.append(result)
                        i += 1
                        j += 1
                    elif (j > 0):
                        j = fail[ctr][j-1]
                    else:
                        i += 1
                if (not found):
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
#         a = MatchWithKMP(tobetranslated,True)
#         a.solve()
#         print("Sunda : "+a.translated)
#     elif (no == 2):
#         print("Sunda - Indonesia")
#         print("Sunda :",end=' ')
#         tobetranslated = str(input())   
#         a = MatchWithKMP(tobetranslated,False)
#         a.solve()
#         print("Indonesia : "+a.translated)
    
# class KMPMatcher:
#     def __init__(self,keyword,folder):
#         self.source = MatchWithKMP(keyword,folder)
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
# # a = MatchWithKMP("terkonfirmasi positif",os.path.curdir)
# # print(a.content)
# # a.solve()
# # print(a.res)
# c = KMPMatcher("terkonfirmasi positif",os.path.curdir)
# print(os.path.curdir)
# print(c.getNumber())
# # coba = "Laman Pusat Informasi dan Koordinasi COVID-19 Jabar (Pikobar) pada Sabtu (11/4/2020) pukul 18.43 WIB, mencatat terdapat 421 orang yang terkonfirmasi positif COVID-19.".lower()
# # print(c.num[coba])
# # c.time()
# # b = "23 orang"
# # print(re.search(r'\d+',b))

