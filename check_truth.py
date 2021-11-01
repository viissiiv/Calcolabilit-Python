import random

def build_var(prop_var):
    prop_var_copy = [var for var in prop_var] #copia di prop_var
    
    #costruisco la lista delle variabili proposizionali e delle loro negazioni
    pv = [0] + [var for var in prop_var_copy] 
    prop_var_copy.reverse()
    pv += [not var for var in prop_var_copy]
    return pv

def check_truth(prop_var, file_path):
    with open(file_path, 'r') as input:
        lines = input.readlines()
    l = [line.split() for line in lines]

    for row in range(len(l)): #aggiorno l modificando le stringhe lette in input in interi
        for col in range(len(l[row])):
            l[row][col] = int(l[row][col])

    num_var = l[0][0] #Il primo elemento della prima riga di l mi da il numero di variabili proposizionali da considerare
    #vorrei usarla per un controllo sull'input
    num_clauses = l[0][1] #Il secondo elemento della prima riga di l mi da il numero di clausole da verificare
    
    pv = build_var(prop_var)

    #controllo che le clausole siano soddisfatte dall'assegnamento di verità
    v = [False for _ in range(num_clauses)] 
    for clause in range(num_clauses):
        #lista contenente i valori di verità delle variabili proposizionali che appaiono nella clausola
        or_clause = [pv[l[clause+1][index]]  for index in range(len(l[clause + 1]))] 
        if True in or_clause: v[clause] = True
    
    if False in v: 
        print(f"L'assegnamento di verità {prop_var} non soddisfa le clausole")
    else: 
        print(f"L'assegnamento di verità {prop_var} soddisfa le clausole")


prop_var = [random.choice([True, False]) for i in range(10)]
#prop_var = [False, True, True, False, True, True, True, True, False, True]
check_truth(prop_var, 'testo_var.txt')
