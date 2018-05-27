import Jogo
import time
import copy


if __name__ == '__main__':
    debug=False
    Status=[]
    prob=Jogo.Problema()
    prob.debug=False
    prob.nPassosTreinamento=80
    nMax=prob.nPassosTreinamento
    print prob.TestaVitoria()
    prob.embaralha()
    print prob.TestaVitoria()
    Status.append([copy.copy(prob.Status)])

    print " #####################"
    print "Solucao:"
    for i in range(0, len(prob.Status)):
        print prob.Solucao[i]
    print "Jogo embaralhado com "+str(nMax)+" Iteracoes:"
    for i in range(0, len(prob.Status)):
        print prob.Status[i]

    print " #####################"
    c=0
    i=0
    fim=False

    apontador=[0]
    t=time.time()
    prob.debug=False
    while ~fim and i<=nMax:
        i=i+1
        t=time.time()
        Status.append([])
        for k in Status[-2]:
            prob.Status=copy.deepcopy(k)
            #print k
            #print "TESTE :"+str(prob.Possibilidades())
            for j in prob.Possibilidades():
                prob.Status=copy.deepcopy(k)
                prob.Joga(j)
                Status[-1].append(copy.deepcopy(prob.Status))
                c=c+1
                if(debug):
                    for p in range(0, len(prob.Status)):
                        print prob.Status[p]


                if prob.TestaVitoria():
                    print " =========\o/GANHO\o/========="
                    print prob.TestaVitoria()
                    print "Solucao:"
                    for i in range(0, len(prob.Status)):
                        print prob.Solucao[i]
                    print "Jogo:"
                    for i in range(0, len(prob.Status)):
                        print prob.Status[i]
                    fim=True
                    print " ============================="
                    break

        print "Tempo loop "+str(i)+":"+str(time.time()-t)
        if fim:
            break
    print str(c)+" Iteracoes"
    for i in range(0, len(prob.Status)):
        print prob.Status[i]

    print " --------------------------"
    for i in range(0, len(prob.Status)):
        print prob.Solucao[i]
