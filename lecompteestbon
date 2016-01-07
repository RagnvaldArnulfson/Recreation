def lecompteestbon(using,goal,return_first): #le bool return_first prend une valeur true si l'on souhaite arrêter l'algorithme \
                                             #dès qu'une possibilité est trouvée
                                             #dans le cas contraire, toutes le possibilités sont envisagées
    L=len(using)                              
    if L==1:
        return using
    solution=[]
    for i in range(0,L):
        for j in range(i+1,L):
            for op in "*+-":
                p=lecompteestbon(["("+str(using[i])+op+str(using[j])+")"]+[using[n] for n in range(0,L) if n!=i and n!=j],goal,return_first)
                for s in p:
                    if eval(s)==goal:
                        solution+=[s]
                        if return_first:
                            return [s]
    return solution
    

print(lecompteestbon([3,4,5,6],1,False))

print(lecompteestbon([1,2,3,4,5,6,7,8,9],2016,True))
