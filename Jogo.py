import random
import copy

class Problema:
    """docstring for [object Object]."""
    Solucao=[[0,1,2],[3,4,5],[6,7,None]]
    nPassosTreinamento=10
    Status=[]
    debug=True

    def __init__(self):
        for a in self.Solucao:
            self.Status.append([])
            for b in a:
                self.Status[-1].append(b)

    def TestaVitoria(self):
        return self.Status == self.Solucao

    def Joga(self, J):
        #1 para cima, 2 para direita, 3 para baixo, 4 para esquerda
        i=0;
        ret=1;
        if(self.debug):
            print "---------------------- \nAntes"
            for i in range(0, len(self.Status)):
                print self.Status[i]
        for a in range(0,len(self.Status)):
            tmp= self.Status[a]
            i=a if None in tmp else i
        j=self.Status[i].index(None)
        if J==1:
            if i==0:
                ret= -1;
            else:
                tmp=self.Status[i-1][j]
                self.Status[i-1][j]=self.Status[i][j]
                self.Status[i][j]=tmp
        elif J==2:
            if j==0:
                ret= -1;
            else:
                tmp=self.Status[i][j-1]
                self.Status[i][j-1]=self.Status[i][j]
                self.Status[i][j]=tmp
        elif J==3:
            if i==len(self.Status)-1:
                ret= -1;
            else:
                tmp=self.Status[i+1][j]
                self.Status[i+1][j]=self.Status[i][j]
                self.Status[i][j]=tmp
        elif J==4:
            if j==len(self.Status[0])-1:
                ret= -1;
            else:
                tmp=self.Status[i][j+1]
                self.Status[i][j+1]=self.Status[i][j]
                self.Status[i][j]=tmp
        if(self.debug and ret>0):
            print "depois, Passo " +str(J)
            for i in range(0, len(self.Status)):
                print self.Status[i]
            print "Possibilidades "+str(self.Possibilidades())
        return ret

    def Possibilidades(self):
        i=0
        for a in range(0,len(self.Status)):
            tmp= self.Status[a]
            i=a if None in tmp else i
        j=self.Status[i].index(None)
        tmp=[1,2,3,4]
        if i==0:
            if j>0:
                if j<len(self.Status[0])-1:
                    tmp=[2,3,4]
                else:
                    tmp=[2,3]
            else:
                tmp=[3,4]
        elif i==len(self.Status)-1:
            if j>0:
                if j<len(self.Status[0])-1:
                    tmp=[1,2,4]
                else:
                    tmp=[2,1]
            else:
                tmp=[1,4]
        elif j==0:
            tmp=[1,3,4]
        elif j==len(self.Status[0])-1:
            tmp=[1,2,3]
        else:
            tmp=[1,2,3,4]

        return tmp

    def embaralha(self):
        for i in range(0,self.nPassosTreinamento):
            tmp =self.Joga(random.randint(1, 4))
