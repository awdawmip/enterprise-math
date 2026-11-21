from fractions import Fraction as Q
from itertools import combinations
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog

G = [20,20,20,-100,140,-100]
coeff = [1,-4,6,-4,1]

def problem(n,a,b,sgn):
    k=n-4
    H=np.zeros((k,n),dtype=int)
    for i in range(k): H[i,i:i+5]=coeff
    U=np.array([G[(a+i)%6] for i in range(k)])
    V=np.array([G[(b+i)%6] for i in range(k)])
    # h, alpha, beta, offset, t
    E=np.column_stack([H,-U,sgn*V,-np.ones(k),np.zeros(k)])
    C=np.zeros(n+4);C[-1]=1
    I=np.zeros((2*n,n+4))
    for i in range(n):
        I[2*i,i]=1;I[2*i+1,i]=-1
        I[2*i,-1]=I[2*i+1,-1]=-1
    bounds=[(None,None)]*n+[(1,None),(1,None),(None,None),(0,None)]
    res=linprog(C,A_ub=I,b_ub=np.zeros(2*n),A_eq=E,b_eq=np.zeros(k),bounds=bounds,method='highs')
    assert res.success,res.message
    rat=lambda x:Q(float(x)).limit_denominator(10**7)
    x=list(map(rat,res.x))
    y=list(map(rat,res.eqlin.marginals))
    h=x[:n]; alpha,beta,offset,t=x[n:]
    dot=lambda u,v:sum(aa*bb for aa,bb in zip(u,v))
    Hcols=[list(H[:,j]) for j in range(n)]
    assert all(dot(H[i],h)==alpha*U[i]-sgn*beta*V[i]+offset for i in range(k))
    assert alpha>=1 and beta>=1 and max(map(abs,h))<=t
    assert sum(y)==0
    assert sum(abs(dot(col,y)) for col in Hcols)<=1
    assert dot(y,U)>=0 and sgn*dot(y,V)<=0
    lower=dot(y,U)-sgn*dot(y,V)
    assert lower==t,(n,a,b,sgn,t,lower,res.eqlin.marginals)
    return {'n':n,'a':a,'b':b,'relative_sign':sgn,'distance':str(t),'radius':str(t/2),'primal':[str(v) for v in x],'dual':[str(v) for v in y]}

if __name__ == '__main__':
    out=[problem(n,a,b,s) for n in (7,8) for a,b in combinations(range(6),2) for s in (1,-1)]
    Path(__file__).with_name('certificates.json').write_text(json.dumps(out,indent=2)+'\n')
    for n in (7,8):
        for positive in (True,False):
            group=[r for r in out if r['n']==n and (not positive or r['relative_sign']==1)]
            m=min(Q(r['distance']) for r in group)
            print(n,'positive' if positive else 'signed','distance',m,'radius',m/2)
            for row in group:
                if Q(row['distance'])==m: print(row)
