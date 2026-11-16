"""Exact independent-noise certification for three successive fourth differences.

For a rival to beat/tie the true phase, there must be an axis and sign on which
signed true error bounds all six signed rival errors. These six inequalities
are linear in the seven raw observations. For partially assigned samples,
the maximum of each inequality over the independent coordinate rectangle is
its exact endpoint sum. Prune whenever one such maximum is negative.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb,lcm
from pathlib import Path
import json

H = (455,-295,-25,185,-25,-295)
weights = (1,-4,6,-4,1)
rows = [tuple(weights[j-t] if 0<=j-t<5 else 0 for j in range(7)) for t in range(3)]
signatures = tuple(tuple(sum(row[j]*H[(a+j)%6] for j in range(7))//36 for row in rows) for a in range(6))
errors=tuple(product(range(-2,3),repeat=2))

def population(n):
    D=[1]
    for w in (1,1,1,2,3,6):
        D = [(D[i] if i<len(D) else 0)-(D[i-w] if w<=i<len(D)+w else 0) for i in range(len(D)+w)]
    C=[0]*(n+1);T=[0]*(n+1)
    for q in range(1,n+1):
        C[q]=(q==1)-sum(D[j]*C[q-j] for j in range(1,min(q,len(D))))
        T[q]=T[q-1]+C[q-1]
    return C,T
C,T=population(1450)

@lru_cache(None)
def data(q):
    S=18*q**4+54*q**3-345*q*q+2070*q-16315
    return sorted((Fraction(108*q**3*(T[q]+e)-S*(C[q]+d),108*(C[q]+d)),(e,d))
               for e,d in errors if C[q]+d>0)

def certify(r):
    a=r%6
    vals=[data(q) for q in range(r,r+7)]
    scale=lcm(*(z.denominator for vs in vals for z,_ in vs))
    zs=[[int(z*scale) for z,_ in vs] for vs in vals]
    lo=[v[0] for v in zs];hi=[v[-1] for v in zs]
    sig=signatures[a]
    lower=[];upper=[]
    for row,t in zip(rows,sig):
        low=sum(w*(lo[j] if w>=0 else hi[j]) for j,w in enumerate(row))
        high=sum(w*(hi[j] if w>=0 else lo[j]) for j,w in enumerate(row))
        lower.append(low-t*scale)
        upper.append(high-t*scale)
    if max(*upper,*[-x for x in lower])<60*scale:
        return None,0
    visits=0
    for b,R in enumerate(signatures):
        if b==a:continue
        for t,sign in product(range(3),(-1,1)):
            A=[];B=[]
            for k,u in product(range(3),(-1,1)):
                A.append(tuple(sign*x-u*y for x,y in zip(rows[t],rows[k])))
                B.append(scale*(u*R[k]-sign*sig[t]))
            # Each row is A*x+B>=0. Maximize independently over unassigned coordinates.
            # Tiebreak with spread, total coefficient size. Use integer arithmetic.
            order=sorted(range(7),key=lambda j:(hi[j]-lo[j])*sum(abs(row[j]) for row in A),reverse=True)
            U=[c+sum(w*(hi[j] if w>=0 else lo[j]) for j,w in enumerate(row)) for row,c in zip(A,B)]
            def solve(i,ups,chosen):
                nonlocal visits
                visits+=1
                if min(ups)<0:return
                if i==7:return chosen
                j=order[i]
                # If a row is near infeasible, try its maximizing endpoint first.
                limiting=min(range(6),key=ups.__getitem__)
                indices=range(len(zs[j])-1,-1,-1) if A[limiting][j]>=0 else range(len(zs[j]))
                for idx in indices:
                    x=zs[j][idx]
                    U1=[old+row[j]*(x-(hi[j] if row[j]>=0 else lo[j])) for old,row in zip(ups,A)]
                    if min(U1)<0:continue
                    ret=solve(i+1,U1,chosen+[(j,idx)])
                    if ret is not None:return ret
            sol=solve(0,U,[])
            if sol:
                ids=[i for _,i in sorted(sol)]
                qv=[vals[j][i][0] for j,i in enumerate(ids)]
                ov=[sum(w*x for w,x in zip(row,qv)) for row in rows]
                da=max(abs(x-y) for x,y in zip(ov,sig))
                db=max(abs(x-y) for x,y in zip(ov,R))
                assert db<=da
                return dict(r=r,true_phase=a,rival=b,errors=[vals[j][i][1] for j,i in enumerate(ids)],true_distance=str(da),rival_distance=str(db)),visits
    return None,visits

def check_tail():
    # C,T are branch polynomials of degrees at most 5,6. After multiplying
    # by 108(C+d), (3 +/- error) is a branch polynomial of degree <=9.
    # Positive initial value and nonnegative forward differences imply positivity
    # at every nonnegative integer. This gives 16*3<60 on the infinite tail.
    for q0 in range(1350,1356):
        for (e,d),sgn in product(errors,(-1,1)):
            def poly(t):
                q=q0+6*t
                S=18*q**4+54*q**3-345*q*q+2070*q-16315
                den=C[q]+d
                return 324*den+sgn*(108*q**3*(T[q]+e)-(S+3*H[q%6])*den)
            dif=[poly(t) for t in range(10)]
            coef=[]
            while dif:
                coef.append(dif[0]);dif=[v-u for u,v in zip(dif,dif[1:])]
            assert coef[0]>0 and min(coef[1:])>=0
            assert sum(c*comb(10,i) for i,c in enumerate(coef))==poly(10)

if __name__=='__main__':
    check_tail()
    total=pruned=0
    for r in range(1349,0,-1):
        w,n=certify(r)
        total+=n;pruned+=n==0
        if w:
            result=dict(threshold=r+1,witness=w,visited_interval_nodes=total,norm_pruned_r=pruned,tail_bound=3)
            print(result,flush=True);Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
            break
