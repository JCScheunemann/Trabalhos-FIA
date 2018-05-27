import Jogo
if __name__ == '__main__':
    nMax=1000
    prob=Jogo.Problema()
    tmp=prob.embaralha()

    for i in range(0, len(prob.Status)):
        print prob.Status[i]
    i=0
    Status=[prob.Status]
    Possibilidade=[prob.Possibilidades()]
    apontador=[0]
    while ~prob.TestaVitoria() or i>=nMax:
        i=i+1
