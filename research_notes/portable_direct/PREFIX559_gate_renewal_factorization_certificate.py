#!/usr/bin/env python3
"""PREFIX-559: native X6-BRC one-gate renewal coefficient factorization.
Pinned science: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Pure native BRC action weights from published PREFIX550; no classical propagator.
"""
from __future__ import annotations
from collections import Counter
import hashlib, json, time
from pathlib import Path
import PREFIX550_shared_gauge_compact_certificate as x

P=1000000007
ROOTS=(x.ZERO_ROOT,)+x.ROOTS
QSET=((2,3,5,7,11,13),(19,23,29,31,37,41))
Z=(0,)*6

def edges(root):
    no=[[] for _ in range(96)];gate=[[] for _ in range(96)]
    for i in range(96):
        for act in x.A:
            j,w=x.edge(i,act,root)
            (gate if w[-1] else no)[i].append((j,w[:6]))
    assert sum(map(len,no))==573 and sum(map(len,gate))==3
    assert all(j==9 for row in gate for j,_ in row)
    return no,gate

def num_weight(m,q):
    a=1
    for e,v in zip(m,q):a=a*pow(v,e,P)%P
    return a

def numeric_data(root,q):
    no,gate=edges(root)
    N=[[(j,num_weight(w,q)) for j,w in row] for row in no]
    u=[sum(num_weight(w,q) for j,w in row)%P for row in gate]
    return N,u

def step(N,v):
    return [sum(w*v[j] for j,w in row)%P for row in N]

def conv(a,b,D):
    c=[0]*(D+1)
    for i,aa in enumerate(a[:D+1]):
        if aa:
            for j,bb in enumerate(b[:D+1-i]):
                if bb:c[i+j]=(c[i+j]+aa*bb)%P
    return c

def propagate(N,u,D):
    U=[[1]*96];A=[u[:]]
    for _ in range(D):
        U.append(step(N,U[-1]));A.append(step(N,A[-1]))
    return U,A

def direct(N,u,D):
    K=(D+3)//4
    F=[[[1]*96]+[[0]*96 for _ in range(K)]]
    for d in range(1,D+1):
        prev=F[-1];cur=[]
        for k in range(K+1):
            col=step(N,prev[k]);g=prev[k-1][9] if k else 0
            if g:col=[(v+g*w)%P for v,w in zip(col,u)]
            cur.append(col)
        F.append(cur)
    return F

def renewal_predict(U,A,common_kernel,D):
    K=(D+3)//4
    B=[v[9] for v in U]
    H=[[1]+[0]*D]
    for k in range(1,K):H.append(conv(H[-1],common_kernel,D))
    result={}
    for k in range(1,K+1):
        C=conv(H[k-1],B,D)
        for i in range(96):
            for d in range(k,D+1):
                s=sum(A[n][i]*C[d-k-n] for n in range(d-k+1))%P
                result[(d,k,i)]=s
    return result

def addexp(a,b):return tuple(i+j for i,j in zip(a,b))

def symbol_step(no,v):
    out=[Counter() for _ in range(96)]
    for i,row in enumerate(no):
        for j,w in row:
            for m,n in v[j].items():out[i][addexp(m,w)]+=n
    return out

def poly_convolve(a,b,D):
    out=[Counter() for _ in range(D+1)]
    for i,aa in enumerate(a[:D+1]):
        if not aa:continue
        for j,bb in enumerate(b[:D+1-i]):
            if not bb:continue
            for m,n in aa.items():
                for h,v in bb.items():out[i+j][addexp(m,h)]+=n*v
    return out

def symbolic_check(root,D=8):
    no,gate=edges(root)
    u=[Counter() for _ in range(96)]
    for i,row in enumerate(gate):
        for j,w in row:u[i][w]+=1
    U=[[Counter({Z:1}) for _ in range(96)]]
    A=[[dict(c) for c in u]]
    for _ in range(D):
        U.append(symbol_step(no,U[-1]));A.append(symbol_step(no,A[-1]))
    K=[A[n][9] for n in range(D+1)]
    B=[U[n][9] for n in range(D+1)]
    maxk=(D+3)//4
    H=[[Counter({Z:1})]+[Counter() for _ in range(D)]]
    for k in range(1,maxk):H.append(poly_convolve(H[-1],K,D))
    counts=0;nonzero=0
    F=[[Counter({Z:1}) for _ in range(96)]]+[[Counter() for _ in range(96)] for _ in range(maxk)]
    for d in range(D+1):
        for k in range(1,maxk+1):
            C=poly_convolve(H[k-1],B,D-k)
            for i in range(96):
                got=Counter()
                for n in range(d-k+1):
                    for m,v in A[n][i].items():
                        for h,w in C[d-k-n].items():got[addexp(m,h)]+=v*w
                assert +got==+F[k][i],(root,d,k,i)
                counts+=1;nonzero+=len(+got)
        if d<D:
            nxt=[symbol_step(no,F[k]) for k in range(maxk+1)]
            for k in range(1,maxk+1):
                for i,row in enumerate(gate):
                    for j,w in row:
                        for m,n in F[k-1][9].items():nxt[k][i][addexp(m,w)]+=n
            F=nxt
    return {'root':list(root),'D':D,'exact_polynomial_equalities':counts,'nonzero_gate_terms_compared':nonzero}

def main():
    D=32;all_num=0;root_counts=[];kernels=[]
    start=time.perf_counter()
    for q in QSET:
        kref=None
        for root in ROOTS:
            N,u=numeric_data(root,q)
            U,A=propagate(N,u,D)
            kap=[v[9] for v in A]
            if kref is None:kref=kap
            assert kap==kref,(root,q)
            pred=renewal_predict(U,A,kref,D)
            direct_dp=direct(N,u,D)
            for (d,k,i),v in pred.items():
                assert v==direct_dp[d][k][i],(root,q,d,k,i)
                all_num+=1
            for d in range(D+1):
                for i in range(96):assert U[d][i]==direct_dp[d][0][i]
            root_counts.append({'root':list(root),'q':list(q),'depth':D})
        kernels.append({'q':list(q),'kappa_coefficients_0_to_9':kref[:10]})
    exact=[symbolic_check(x.ZERO_ROOT,8),symbolic_check(x.ROOTS[0],8)]
    from PREFIX558_universal_gate_kernel_certificate import symbolic_kappa
    K=symbolic_kappa(x.ZERO_ROOT,17)
    sym=[]
    for s in range(3,18,2):
        row=K[s]
        assert all(m[0]>=1 and m[2]>=1 for m in row)
        symmetry=all(row.get(m[:4]+(m[5],m[4]),0)==v for m,v in row.items())
        sym.append({'s':s,'monomials':len(row),'native_path_count':sum(row.values()),'q5_q6_swap_symmetric':symmetry})
    elapsed=round(time.perf_counter()-start,3)
    result={'status':'ALL_CHECKS_PASS','scope':'fixed four-STAR native X6 BRC action graph',
            'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
            'native_ports':96,'native_actions':576,'gate_edges':3,'common_gate_destination':9,
            'renewal_formula':'[z^k]F_i(t,z)=t^k A_i(t) kappa(t)^(k-1) B(t), k>=1',
            'proof':'formal resolvent + rank-one gate decomposition',
            'numerical_exact_mod_prime':P,'specializations':[list(i) for i in QSET],
            'root_cases':len(ROOTS),'depth_inclusive':D,'numeric_equalities':all_num,
            'symbolic_exact_checks':exact,'kernel_odd_coefficients_3_to_17':sym,
            'candidate_symmetry':'q5<->q6 established computationally for s<=17 only',
            'elapsed_seconds':elapsed}
    Path('PREFIX559_EXACT_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','numeric_equalities','symbolic_exact_checks','kernel_odd_coefficients_3_to_17','elapsed_seconds')},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
