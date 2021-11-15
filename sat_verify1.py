from itertools import product
import random


def build_var(prop_var):
    prop_var_copy = [var for var in prop_var] #copia di prop_var
    
    #costruisco la lista contenente le variabili proposizionali date in input e delle loro negazioni
    pv = [0] + [var for var in prop_var_copy] 
    prop_var_copy.reverse()
    prop_var_copy = [not var for var in prop_var_copy]
    pv += prop_var_copy
    return pv


def check_truth(prop_var, T, num_clauses):
    pv = build_var(prop_var)

    #controllo che le clausole siano soddisfatte dall'assegnamento di verità
    v = [0 for _ in range(num_clauses)] 
    for clause in range(num_clauses):
        #lista contenente i valori di verità delle variabili proposizionali che appaiono nella clausola
        or_clause = [pv[T[clause + 1][i]]  for i in range(len(T[clause + 1]))] 
        if 1 in or_clause: v[clause] = 1
    
    if 0 in v: 
        flag = 0 #L'assegnamento di verità non soddisfa le clausole
    else: 
        flag = 1 #L'assegnamento di verità soddisfa le clausole
    
    return flag

        
def sat_verify(file_path):
    with open(file_path, 'r') as input_text:
        lines = input_text.readlines()
    T = [line.split() for line in lines]
    
    for row in range(len(T)): #aggiorno T modificando le stringhe lette in input in interi
        for col in range(len(T[row])):
            T[row][col] = int(T[row][col])

    num_var = T[0][0] #Il primo elemento della prima riga di l mi da il numero di variabili proposizionali da considerare
    num_clauses = T[0][1] #Il secondo elemento della prima riga di l mi da il numero di clausole da verificare
    
    count = 0
    max_count = 10 # massimo numero di test che voglio effettuare costruendo casulamente l'assegnamento di verità
    while count < max_count:
        prop_var = [random.choice([1, 0]) for i in range(num_var)]
        count += 1
        if check_truth(prop_var, T, num_clauses) == 1:
            print(f"""Un assegnamento di verita che soddisfa le clausole è il seguente:
{prop_var}""")
            print(f"Il numero di test effettuati è: {count}")  
            break
    
    if count == max_count: # dopo un numero fissato di test cerco un assegnamento di verità che soddisfa le clausole costruendoli tutti 
        all_prop_var = list(product(range(2), repeat=num_var)) # lista contenente tutte le possibili combinazioni di vettori binari di lunghezza num_var
        t = False
        for i in range(len(all_prop_var)):
            if check_truth(all_prop_var[i], T, num_clauses) == 1:
                t = True
                break
        if t: 
            print(f"""Un assegnamento di verita che soddisfa le clausole è il seguente:
{all_prop_var[i]}""")
        else:
            print("Non esiste un assegnamento di verita che soddisfa le clausole")        


sat_verify('testo_var.txt')
