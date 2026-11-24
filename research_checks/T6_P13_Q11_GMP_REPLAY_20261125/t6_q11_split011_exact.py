#!/usr/bin/env python3
# Adaptation of frozen prior replay 949c4114b1882b37b60e4e7de05d7ce9933fb33b.
from fractions import Fraction as F
from math import floor, comb, lcm
from itertools import product, combinations_with_replacement, groupby
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form
from collections import Counter
import hashlib,json,time,sys
P,CAP,N=13,2331,12
W=[P*r-1 for r in range(1,P)]
H=[[pow(r,-k,P**k) for r in range(1,P)] for k in range(1,7)]
def solve(target):
    x=[0]*N; A=[[int(i==j) for j in range(N)] for i in range(N)]
    for k,h in enumerate(H,1):
        mod=P**k;t=(target[k-1]-sum(a*b for a,b in zip(x,h)))%mod
        v=[sum(a*b for a,b in zip(row,h))%mod for row in A]
        piv=next(i for i,y in enumerate(v) if y%P);inv=pow(v[piv],-1,mod);old=A[piv]
        x=[a+(t*inv%mod)*b for a,b in zip(x,old)]
        A=[[mod*a for a in row] if i==piv else [a-(v[i]*inv%mod)*b for a,b in zip(row,old)] for i,row in enumerate(A)]
    assert all((sum(a*b for a,b in zip(x,h))-target[k-1])%P**k==0 for k,h in enumerate(H,1))
    return x,A
_,A=solve([0]*6);M=Matrix(A);assert abs(M.det())==P**21
Rw=(hermite_normal_form(M.T).T*Matrix.diag(*W)).lll(delta=F(3,4))
U=Rw*Matrix.diag(*(F(1,w) for w in W));assert all(x.q==1 for x in U)
assert abs(U.det())==P**21
assert all(sum(int(U[j,t])*h[t] for t in range(N))%P**k==0 for j in range(N) for k,h in enumerate(H,1))
UI=U.inv();G=Rw*Rw.T
mu=[[F(0)]*N for _ in range(N)];D=[]
for i in range(N):
    for j in range(i):mu[i][j]=(F(int(G[i,j]))-sum(mu[i][t]*mu[j][t]*D[t] for t in range(j)))/D[j]
    D.append(F(int(G[i,i]))-sum(mu[i][j]**2*D[j] for j in range(i)))
dmin=min(D);assert dmin>2*CAP**2
Urows=[[int(U[j,t]) for t in range(N)] for j in range(N)]
# Positive target corresponds to subtracting the negative vertical roster.
C0={(q,r):[F(x) for x in Matrix(1,N,solve([pow(P*q+r,-k,P**k) for k in range(1,7)])[0])*UI] for q in range(1,12) for r in range(1,13)}
C0={k:[x-floor(x) for x in v] for k,v in C0.items()}
B=lcm(*(x.denominator for v in C0.values() for x in v)); C={a:[int(x*B) for x in v] for a,v in C0.items()}
# Exact scaling: center = (L_i*c_i + sum_j M_ji*z_j)/(B*L_i)
L=[lcm(*(mu[j][i].denominator for j in range(i+1,N))) for i in range(N)]
MM=[[int(mu[j][i]*L[i]) for j in range(i+1,N)] for i in range(N)]
K=[D[i]/(B*L[i])**2 for i in range(N)];Q=lcm(*(x.denominator for x in K));T=[int(x*Q) for x in K]
def patterns(total,length,low=1):
    if length==0:
        if total==0:yield ()
        return
    for q in range(low,total+1):
        for t in patterns(total-q,length-1,q):yield (q,)+t
def rosters(pat):
    groups=[len(tuple(g)) for _,g in groupby(pat)]
    for blocks in product(*(combinations_with_replacement(range(1,P),k) for k in groups)):
        yield tuple(zip(pat,(r for b in blocks for r in b)))
def search(neg):
    cn=sum(P*(P*q+r)-1 for q,r in neg)
    if cn>CAP:return True,0,[]
    radius=CAP**2+(CAP-cn)**2;assert radius<dmin;bound=radius*Q
    c=[sum(C[a][j] for a in neg)%B for j in range(N)];z=c[:];nodes=0;leaves=[]
    def descend(i,spent):
        nonlocal nodes
        if i<0:
            uu=[sum(z[j]*Urows[j][t] for j in range(N)) for t in range(N)]
            assert all(x%B==0 for x in uu);u=[x//B for x in uu]
            masses=[sum(w*max(0,x) for w,x in zip(W,u)),cn+sum(w*max(0,-x) for w,x in zip(W,u))]
            residues=[(sum(x*h for x,h in zip(u,H[k-1]))-sum(pow(P*q+r,-k,P**k) for q,r in neg))%(P**k) for k in range(1,7)]
            assert residues==[0]*6
            norm=sum((w*x)**2 for w,x in zip(W,u));assert norm<=radius and norm*Q==spent
            leaves.append(dict(neg=neg,u=u,masses=masses,residues=residues,norm_sq=norm,radius_sq=radius,budget_valid=max(masses)<=CAP));return
        nodes+=1;center=L[i]*c[i]+sum(a*b for a,b in zip(MM[i],z[i+1:]));den=B*L[i];near=(-center)//den
        for ni in (near,near+1):
            sp=spent+T[i]*(center+den*ni)**2
            if sp<=bound:
                z[i]=c[i]+B*ni;descend(i-1,sp)
        z[i]=c[i]
    descend(N-1,0);return False,nodes,leaves
# Independent direct coefficient DP for vertical mass cut.
def dp_count(pat):
    d={0:1}
    for m in Counter(pat).values():
        g=Counter(sum(rs) for rs in combinations_with_replacement(range(1,P),m));h=Counter()
        for a,b in d.items():
            for s,n in g.items():h[a+s]+=b*n
        d=h
    return sum(d.values()),sum(n for s,n in d.items() if P*P*11+P*s-len(pat)>CAP)
if __name__=='__main__':
    start=time.perf_counter();rows=[];witnesses=[];length=int(sys.argv[1]);lo=int(sys.argv[2]) if len(sys.argv)>2 else 0;hi=int(sys.argv[3]) if len(sys.argv)>3 else 1000
    for index,pat in enumerate(patterns(11,length)):
        if not lo<=index<hi:continue
        raw=over=nodes=leaves=valid=0;digest=hashlib.sha256()
        for neg in rosters(pat):
            raw+=1;digest.update((repr(neg)+'\n').encode('ascii'));skip,nd,ws=search(neg);over+=skip;nodes+=nd;leaves+=len(ws);valid+=sum(w['budget_valid'] for w in ws);witnesses.extend(ws)
        expected=1
        for m in Counter(pat).values():expected*=comb(11+m,m)
        assert raw==expected and (raw,over)==dp_count(pat)
        row=dict(index=index,pattern=pat,raw=raw,over=over,search=raw-over,nodes=nodes,leaves=leaves,valid=valid,roster_sha256=digest.hexdigest());rows.append(row);print(json.dumps(row),flush=True)
    out=dict(schema='T6_P13_Q11_SPLIT0_11_AUTHOR_EXACT_INTEGER_V1',frozen_science='d84bd940cfb093cdc60e569f15cad58772a51dca',source_replay='949c4114b1882b37b60e4e7de05d7ce9933fb33b',p=13,valuation=1,total_q=11,split=[0,11],budget=2331,length=length,pattern_range=[lo,min(hi,len(list(patterns(11,length))))],gs_min_sq=str(dmin),lattice_index='13^21',coset_denominator=B,energy_denominator=Q,rows=rows,witnesses=witnesses,totals={k:sum(r[k] for r in rows) for k in ('raw','over','search','nodes','leaves','valid')},elapsed_s=time.perf_counter()-start,status='AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED')
    with open(f'/mnt/data/t6_q11_len{length}_{lo}_{hi}.json','w') as f:json.dump(out,f,indent=2,sort_keys=True);f.write('\n')
    print('RESULT',json.dumps({k:v for k,v in out.items() if k!='rows'},separators=(',',':')),flush=True)
