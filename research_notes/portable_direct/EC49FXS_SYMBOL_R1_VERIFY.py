"""EC49FXS pinned Farey-CRT auxiliary symbol observer: exact integer verifier.
Run: python EC49FXS_SYMBOL_R1_VERIFY.py  (Python standard library only).
"""
from itertools import combinations
from collections import Counter
from random import Random
import json

C = [list(range(i,55,5)) for i in range(5)]
A_LOSS = [0,1,2,5,7,10,12,15,20,22,25,27,28,30,32,35,39,40,42,45,47,52]
A_GOOD = [0,2,5,10,12,13,17,19,20,22,25,27,30,32,35,36,40,42,45,47,50,52]

def solve(A):
    """Enumerate singleton-compatible physical-color groups, construct sharp layout."""
    A = set(A)
    assert all(any(x%5 == i for x in A) for i in range(5))
    T = {i:[x for x in C[i] if (2*x)%55 not in A] for i in range(5)}
    for k in range(5,-1,-1):
        for E in combinations(range(5),k):
            order = sorted(E,key=lambda i:len(T[i]))
            def search(j,groups):
                if j == len(order): return groups.copy()
                for x in T[order[j]]:
                    if all((x+y)%55 not in A for y in groups):
                        groups.append(x)
                        found = search(j+1,groups)
                        if found is not None: return found
                        groups.pop()
                return None
            picked = search(0,[])
            if picked is None: continue
            singles = dict(zip(order,picked))
            S = sorted(x for i in range(5) for x in
                       ([singles[i]] if i in singles else C[i][:2]))
            assert len(S) == 10-k and len(set(S)) == len(S)
            return len(S),S,singles,T
    raise AssertionError("The empty singleton assignment is always compatible")

def direct_rows(A,S):
    """Entire two-channel physical activation counts as ONE symbol."""
    worst = (len(S)+1,None,None,None)
    checked = 0
    for d in A:
        for i in range(5):
            for j in range(11):
                g = sum(1 for t in S if
                    ((t%5 == i and t%11 != j) or
                     ((d-t)%5 == i and (d-t)%11 != j)))
                checked += 1
                if g < worst[0]:worst = (g,d,i,j)
    return worst,checked

def histogram(A):
    return [sum(x%5 == i for x in A) for i in range(5)]

def singleton_layout_count(A):
    A=set(A)
    T=[[x for x in C[i] if (2*x)%55 not in A] for i in range(5)]
    def search(i,chosen):
        if i==5:return 1
        return sum(search(i+1,chosen+[x]) for x in T[i]
                   if all((x+y)%55 not in A for y in chosen))
    return search(0,[])

def main():
    report = {"scientific_pin":"BRC16943","model":"auxiliary Farey-CRT whole-activation symbol observer, r=1",
              "claim":"N1(A)=10-alpha(A), all five modulo-5 phase colors present",
              "witnesses":{},"row_checks":0}
    cases = [("loss",A_LOSS),("good",A_GOOD),
             ("full",list(range(55))),("one_each",list(range(5)))]
    for name,A in cases:
        n,S,singles,T=solve(A)
        worst,num=direct_rows(A,S)
        assert worst[0]>=1
        report["row_checks"]+=num
        report["witnesses"][name]={
          "phase_set":A,"histogram":histogram(A),"N1":n,"layout":S,
          "safe_groups":{str(i):T[i] for i in range(5)},
          "singleton_groups":{str(i):x for i,x in singles.items()},
          "minimum_row":worst,"all_singleton_layout_count":singleton_layout_count(A)}
    W=report["witnesses"]
    assert W["good"]["histogram"]==W["loss"]["histogram"]==[10,1,9,1,1]
    assert (W["good"]["N1"],W["loss"]["N1"],W["full"]["N1"],W["one_each"]["N1"])==(5,6,10,5)
    # Independent finite obstruction for A_loss: forced x0=25, x2=12.
    A=set(A_LOSS);T={int(i):v for i,v in W["loss"]["safe_groups"].items()}
    assert T[0]==[25] and [x for x in T[2] if (x+25)%55 not in A]==[12]
    assert T[1]==[36,46]
    for x1 in [36,46]:
        x3=[x for x in T[3] if all((x+y)%55 not in A for y in [25,12,x1])]
        x4=[x for x in T[4] if all((x+y)%55 not in A for y in [25,12,x1])]
        assert x3==[38] and x4==([] if x1==36 else [4])
    assert (38+4)%55 in A
    # 600 deterministic full-color sets; count exact integer CRT rows.
    rng=Random(20261123);counts=Counter();rows=0
    for q in range(600):
        A=[]
        for i in range(5):A.extend(rng.sample(C[i],1+rng.randrange(11)))
        n,S,_,_=solve(A)
        worst,c=direct_rows(A,S)
        assert worst[0]>=1,(q,n,S,worst)
        counts[n]+=1;rows+=c
    report["row_checks"]+=rows
    report["generated"]={"seed":20261123,"sets":600,"rows":rows,
                         "cost_distribution":dict(sorted(counts.items()))}
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
