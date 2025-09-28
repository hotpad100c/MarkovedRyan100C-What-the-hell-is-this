import random
class model:
    def __init__(self):
        pass
    def train(self,datas:list[str]):
        datas=[i.replace('\n','') for i in datas]
        ct=2
        self.forward={'\n':1}
        self.backward={1:'\n'}
        for i in datas:
            for j in i:
                if j not in self.forward:
                    self.forward[j]=ct
                    self.backward[ct]=j
                    ct+=1
        self.l=ct
        self.p=[[0 for j in range(ct)] for i in range(ct)]
        for i in datas:
            for j in range(len(i)):
                if j==0:
                    if len(i)>1:
                        self.p[self.forward[i[j]]][self.forward[i[j+1]]]+=1
                    self.p[0][self.forward[i[j]]]+=1
                if j==len(i)-1:
                    self.p[self.forward[i[j]]][1]+=1
                if j!=0 and j!=len(i)-1:
                    self.p[self.forward[i[j]]][self.forward[i[j+1]]]+=1
    def run(self):
        cur=0
        s=""
        while cur!=1:
            cur=random.choices([i for i in range(self.l)],self.p[cur])[0]
            s+=self.backward[cur]
            print(self.backward[cur],end='')
        return s
