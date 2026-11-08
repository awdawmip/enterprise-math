#!/usr/bin/env python3
"""PREFIX-577-R2-GC: all-order gate-resolvent certificate on pinned native X6-BRC.
Run beside PREFIX565_positive_marginal_certificate.py and
PREFIX566_gate_quotient_certificate.py.
Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Exact integer/Fraction arithmetic, not a classical propagator or physical-time model.
"""
from collections import Counter, deque
from fractions import Fraction as F
from math import factorial, comb
import json
from PREFIX565_positive_marginal_certificate import SCIENCE_PIN, ZERO_ROOT, ROOTS, ACTIONS, edge
from PREFIX566_gate_quotient_certificate import marginal_gate_rows, weighted_quotient

PIN="f42f2906d77f24085c123f3ccfe9667d41caa96d"
Q=[248832,-34560,-4992,-416,-20,1]   # Q(w), ascending
N=[-62208,1728,48,20]                  # N(w), ascending

def mm(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]

def mul(a,b,n):
    v=[F(0)]*(n+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=n:v[i+j]+=x*y
    return v

def mult_int(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z

def trim(a):
    a=list(map(F,a))
    while len(a)>1 and not a[-1]:a.pop()
    return a

def divrem(a,b):
    a=trim(a);b=trim(b)
    assert b!=[0]
    o=[F(0)]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        i=len(a)-len(b);v=a[-1]/b[-1];o[i]=v
        for j,c in enumerate(b):a[i+j]-=v*c
        a=trim(a)
    return o,a

def gcd_degree(a,b):
    while trim(b)!=[0]:
        _,r=divrem(a,b);a,b=b,r
    return len(trim(a))-1

def generate_rates(max_order=8):
    # A(t)=t R(1+t) has a simple exact rational power-series expansion.
    k=max_order
    w=[F(36),F(72),F(36)]
    def compose(coeffs):
        power=[F(1)]+[F(0)]*k
        ans=[F(0)]*(k+1)
        for coeff in coeffs:
            ans=[ans[j]+coeff*power[j] for j in range(k+1)]
            power=mul(power,w,k)
        return ans
    a=compose(N);b=compose(Q)
    assert b[0]==0 and b[1]!=0
    b=b[1:]+[F(0)]
    A=[]
    for i in range(k+1):
        A.append((a[i]-sum(b[j]*A[i-j] for j in range(1,i+1)))/b[0])
    coeff=[F(0)]
    for m in range(1,k+1):
        power=[F(1)]+[F(0)]*(m-1)
        for _ in range(m):power=mul(power,A,m-1)
        coeff.append(power[m-1]/m)
    # Check the implicit rank-one equation through degree 8.
    lam=[F(1)]+coeff[1:]
    wl=[36*v for v in mul(lam,lam,k)]
    def subst(a):
        ans=[F(0)]*(k+1);power=[F(1)]+[F(0)]*k
        for c in a:
            ans=[ans[i]+c*power[i] for i in range(k+1)]
            power=mul(power,wl,k)
        return ans
    lhs,rhs=subst(Q),subst(N)
    assert lhs[0]==0
    assert all(lhs[i]==rhs[i-1] for i in range(1,k+1))
    delta=[F(0)]+[F(1,factorial(i)) for i in range(1,k+1)]
    l=[F(1)]+[F(0)]*k
    power=[F(1)]+[F(0)]*k
    for m in range(1,k+1):
        power=mul(power,delta,k)
        for i in range(k+1):l[i]+=coeff[m]*power[i]
    log=[F(0)]
    for m in range(1,k+1):
        log.append(l[m]-sum(F(i,m)*log[i]*l[m-i] for i in range(1,m)))
    rates=[log[i]*factorial(i) for i in range(1,k+1)]
    assert A[:4]==[F(1,192),F(-19,2304),F(79,27648),F(5801,331776)]
    assert rates[:4]==[F(1,192),F(1127,221184),F(206963,42467328),
                       F(434651857,97844723712)]
    return A,coeff[1:],rates

def independent_dp(rows,ids,depths=(0,1,2,5,10,20,40,80,128),order=8):
    # Forward integer BRC path DP for binomial(K,k), independent of resolvent.
    trans=[]
    for row in rows:
        c=Counter()
        for (j,a,b,mark),v in row.items():c[j,mark]+=v
        trans.append(c)
    sizes=Counter(ids)
    f=[[0]*(order+1) for _ in rows]
    for i in range(len(rows)):f[i][0]=sizes[i]
    snaps=[]
    S=[[0]*(order+1) for _ in range(order+1)];S[0][0]=1
    for m in range(1,order+1):
        for j in range(1,m+1):S[m][j]=j*S[m-1][j]+S[m-1][j-1]
    for depth in range(max(depths)+1):
        total=96*6**depth
        assert sum(x[0] for x in f)==total
        if depth in depths:
            aa=[F(sum(row[j] for row in f),total) for j in range(order+1)]
            M=[F(1)]
            for m in range(1,order+1):
                M.append(sum(F(factorial(j)*S[m][j])*aa[j] for j in range(1,m+1)))
            K=[F(0)]*(order+1)
            for m in range(1,order+1):
                K[m]=M[m]-sum(F(comb(m-1,j-1))*K[j]*M[m-j] for j in range(1,m))
            assert K[1]==F(depth,192)
            snaps.append({"depth":depth,"kappa5_per_depth":str(K[5]/depth) if depth else None,
                          "kappa6_per_depth":str(K[6]/depth) if depth else None,
                          "kappa8_per_depth":str(K[8]/depth) if depth else None})
        if depth==max(depths):break
        ff=[[0]*(order+1) for _ in rows]
        for i,row in enumerate(trans):
            for (j,mark),v in row.items():
                for k in range(order+1):
                    ff[j][k]+=v*(f[i][k]+(f[i][k-1] if mark and k else 0))
        f=ff
    return snaps

def main():
    assert SCIENCE_PIN==PIN and len(ROOTS)==9 and len(ACTIONS)==6
    native=sorted((i,j) for i in range(96) for act in ACTIONS
                  for j,w in [edge(i,act,ZERO_ROOT)] if w[6])
    assert native==[(7,9),(29,9),(31,9)]
    original=marginal_gate_rows(ZERO_ROOT)
    assert len(original)==96
    assert all(marginal_gate_rows(root)==original for root in ROOTS)
    ids,rows,growth=weighted_quotient(original)
    assert growth==[1,4,13,21,33,37] and len(rows)==37
    C=[[0]*37 for _ in rows];g=[0]*37;gate=[]
    for i,row in enumerate(rows):
        for (j,a,b,mark),v in row.items():
            C[i][j]+=v;g[i]+=mark*v
            if mark:gate.append((i,j,v,a,b))
    assert all(sum(row)==6 for row in C)
    assert sorted(gate)==[(4,5,1,0,0),(15,5,1,0,0),(17,5,1,0,0)]
    sizes=Counter(ids)
    assert sum(sizes.values())==96
    assert all(sum(sizes[i]*C[i][j] for i in range(37))==6*sizes[j]
               for j in range(37))
    color={0:0};todo=deque([0])
    while todo:
        i=todo.popleft()
        for j,v in enumerate(C[i]):
            if not v:continue
            if j in color:assert color[i]!=color[j]
            else:color[j]=1-color[i];todo.append(j)
    assert len(color)==37
    ix=[i for i in range(37) if color[i]==color[5]]
    iy=[i for i in range(37) if color[i]!=color[5]]
    assert (len(ix),len(iy))==(17,20)
    A=[[C[i][j] for j in iy] for i in ix]
    B=[[C[i][j] for j in ix] for i in iy]
    D=mm(A,B)
    b=[sum(A[i][j]*g[iy[j]] for j in range(20)) for i in range(17)]
    assert mult_int(mult_int([-36,1],[-4,1]),mult_int([12,1],[144,8,1]))==Q
    assert gcd_degree(Q,N)==0
    V=[[int(i==j) for j in range(17)] for i in range(17)]
    zero=[[0]*17 for _ in range(17)];m=[]
    for k in range(6):
        if k:V=mm(V,D)
        m.append(sum(V[ix.index(5)][j]*b[j] for j in range(17)))
        for i in range(17):
            for j in range(17):zero[i][j]+=Q[k]*V[i][j]
    assert all(v==0 for row in zero for v in row)
    assert m[:5]==[0,20,448,19008,604160]
    numerator=[sum(Q[r]*m[r-j-1] for r in range(j+1,6)) for j in range(5)]
    assert numerator==N+[0]
    Acoeff,lambdacoeff,kappa=generate_rates()
    assert kappa[4]==F(203828245435,56358560858112)
    assert kappa[5]==F(9969866857747,4809263859892224)
    assert kappa[6]<0 and kappa[7]<0
    dp=independent_dp(rows,ids)
    return {"status":"ALL_CHECKS_PASS","pin":PIN,"native_gate_edges":native,
            "quotient_growth":growth,"bipartition":[17,20],
            "N_coefficients_ascending":N,"Q_coefficients_ascending":Q,
            "D_matrix_17x17":D,"b_vector":b,"target_index":ix.index(5),
            "Q(D)_zero_entry_checks":289,"markov_parameters":m[:5],
            "exact_implicit_equation_checked_through":8,"coprime_N_Q":True,
            "Laurent":list(map(str,Acoeff[:4])),
            "lambda_coefficients_zminus1":list(map(str,lambdacoeff)),
            "asymptotic_cumulant_rates_1_to_8":list(map(str,kappa)),
            "independent_stationary_integer_DP":dp,
            "status_boundary":"AUTHOR_PROVED/EXACT_CHECKED/UNREVIEWED/NOT_ADMITTED"}

if __name__=="__main__":
    print(json.dumps(main(),ensure_ascii=False,indent=2))
