#in this function, we create a dictionary
#where the key is the degree and the value is the nodes

import copy

def get_degree_list(graphe):
    """create degree distribution"""

    #D{ key : dégré, valeur : [liste de sommets ayant ce degré]}
    D={}

    #if the current degree hasnt been checked
    #we create a new key under the current degree
    #otherwise we append the new node into the list
    for i in graphe.keys():
        try:
            D[len(graphe[i])].append(i)

        except KeyError:
            D[len(graphe[i])]=[i]

    #dictionary is sorted by key instead of value in ascending order
    D=dict(sorted(D.items()))

    return D

# ---------------------

def Degenerescence(graphe,ordering=False,degeneracy=False):
    """ ".
    """

    subset=copy.deepcopy(graphe)

    #k is the ultimate degeneracy
    k=0

    #denote L as the checked list
    L=[]

    #denote output as the storage of vertices in 1-core to k-core
    output={}

    #degree distribution



    D=get_degree_list(subset)
    print("D =" + str(D))



    #initialize
    for i in range(1,max(D.keys())+1):
        output[i]=[]


    #we initialize the current degree i to 0
    #because we want to keep track of 1-core to k-core
    i=0

    while D:

        #denote i as the minimum degree in the current graph
        i=list(D.keys())[0]
        #print(i)

        #k denotes the degeneracy
        k=max(k,i)


        #pick a random vertex with the minimum degree
        v=D[i].pop(0)


        #checked and removed
        L.append(v)
       # print(L)

        del subset[v]


        # subset.remove(v)
        output[k].append(v)
        #print("output iteration=" + str(output))

        for som in subset.values():
            if v in som:
               # print(som)
                som.remove(v)



        #update the degree list
        D=get_degree_list(subset)




    #start from -2 to 0
    for ind in sorted(output.keys(),reverse=True)[1:]:

        #remove empty k-core
        if not output[ind+1]:
            del output[ind+1]

        #add vertices from high order core to low order core
        else:
            output[ind]+=output[ind+1]

    #output depends on the requirement
    if ordering:
        return L
    elif degeneracy:
        return k
    else:
        return output



###### Main #############
"""
G = {
        1: [2,3,4],
        2: [1,3,4,5],
        3: [1,2,4],
        4: [1,2,3,5,6],
        5: [2,4,7],
        6: [4],
        7: [5]
    }

#D = get_degree_list(G)
#print(D)

D = Degenerescence(G,True,False)
print(D)

"""