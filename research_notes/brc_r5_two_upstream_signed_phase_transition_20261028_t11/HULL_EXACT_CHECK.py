"""Exact rational finite-hull membership certificates for the d=1/10 R5 sample.
SciPy floating LP is used ONLY to suggest sparse supports; final equality and
nonnegativity are verified exactly with SymPy rational linear algebra.
Run: python3 HULL_EXACT_CHECK.py (with VERIFY.py in the same directory).
"""
from fractions import Fraction as F
from itertools import product
import json
import numpy as np
from scipy.optimize import linprog
from sympy import Matrix
from VERIFY import tree,obs,P,Q,C

def vectors(rows,compressed):
    data=set()
    for roots in product((P,Q,C),repeat=2):
        choices=([(x,x) for x in (P,Q,C)] if compressed else product((P,Q,C),repeat=2))
        for cs in choices:
            for side in product((P,Q),repeat=2):
                for bits in product((P,Q),repeat=3 if compressed else 6):
                    data.add(obs(rows,roots,cs,side,tuple(bits)*2 if compressed else bits))
    return sorted(data)

def main():
    rows=tree(F(3,4),F(1,10),F(1,4),F(1,8))
    Fset=vectors(rows,False)
    Lset=vectors(rows,True)
    print("candidate d=1/10: full distinct",len(Fset),"LR distinct",len(Lset),flush=True)
    assert len(Fset)==380 and len(Lset)==120
    M=Matrix([[F(1)]*len(Lset)]+[[v[i] for v in Lset] for i in range(4)])
    Mf=np.array(M.tolist(),dtype=float)
    certs=[]
    lookup={v:i for i,v in enumerate(Lset)}
    for idx,vec in enumerate(Fset):
        target=[F(1)]+list(vec)
        if vec in lookup:
            indices=[lookup[vec]]
            weights=[F(1)]
        else:
            lp=linprog(np.zeros(len(Lset)),A_eq=Mf,b_eq=np.array(target,dtype=float),
                       bounds=(0,None),method="highs",
                       options={"primal_feasibility_tolerance":1e-9,"dual_feasibility_tolerance":1e-9})
            if not lp.success:raise RuntimeError((idx,lp.message))
            indices=[j for j,x in enumerate(lp.x) if x>1e-9]
            A=M[:,indices]
            sol,params=A.gauss_jordan_solve(Matrix(target))
            sol=sol.subs({x:0 for x in params})
            weights=[F(x) for x in sol]
            assert all(w>=0 for w in weights) and A*sol==Matrix(target)
        certs.append({"indices":indices,"weights":[str(w) for w in weights]})
        if idx and idx%100==0:print("confirmed",idx,flush=True)
    assert len(certs)==len(Fset)
    print("ALL 380 FULL POINTS HAVE EXACT RATIONAL LR CARATHEODORY CERTIFICATES",flush=True)
    print("max support",max(len(z["indices"]) for z in certs),
          "max denominator",max(F(w).denominator for z in certs for w in z["weights"]),flush=True)
    out={"model":{"theta":"3/4","d":"1/10","a":"1/4","b":"1/8"},
         "full_vectors":[[str(x) for x in v] for v in Fset],
         "lr_vectors":[[str(x) for x in v] for v in Lset],
         "certificates":certs}
    with open("EXACT_HULL_CERTIFICATES.json","w",encoding="utf-8") as f:
        json.dump(out,f,separators=(",",":"))
    print("witness saved EXACT_HULL_CERTIFICATES.json",flush=True)

if __name__=="__main__":main()
