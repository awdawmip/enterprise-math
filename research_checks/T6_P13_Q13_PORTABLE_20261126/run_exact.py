from fractions import Fraction as F
from math import floor,comb,lcm
from itertools import combinations_with_replacement
from collections import Counter
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form
import json, pathlib, hashlib, subprocess, sys, time
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
C0={(q,r):[F(x) for x in Matrix(1,N,solve([pow(P*q+r,-k,P**k) for k in range(1,7)])[0])*UI] for q in range(1,14) for r in range(1,13)}
C0={k:[x-floor(x) for x in v] for k,v in C0.items()}
B=lcm(*(x.denominator for v in C0.values() for x in v)); C={a:[int(x*B) for x in v] for a,v in C0.items()};assert B==P**6
L=[lcm(*(mu[j][i].denominator for j in range(i+1,N))) for i in range(N)]
MM=[[int(mu[j][i]*L[i]) for j in range(i+1,N)] for i in range(N)]
K=[D[i]/(B*L[i])**2 for i in range(N)];Q=lcm(*(x.denominator for x in K));T=[int(x*Q) for x in K]
def patterns(total,low=1):
    if total==0:
        yield ();return
    for q in range(low,total+1):
        for tail in patterns(total-q,q):yield (q,)+tail
def feasible(pat,limit):
    def walk(rs,s):
        i=len(rs)
        if i==len(pat):yield tuple(zip(pat,rs));return
        lo=rs[-1] if i and pat[i]==pat[i-1] else 1
        hi=min(12,limit-s-(len(pat)-i-1))
        for a in range(lo,hi+1):yield from walk(rs+(a,),s+a)
    yield from walk((),0)
def count_dp(pat,limit):
    d=Counter({0:1});raw=1
    for m in Counter(pat).values():
        raw*=comb(11+m,m)
        g=Counter({(0,0):1})
        for t in range(1,13):
            h=Counter()
            for (k,s),v in g.items():
                for n in range(m-k+1):
                    if s+t*n<=limit:h[k+n,s+t*n]+=v
            g=h
        h=Counter()
        for s,v in d.items():
            for (k,t),n in g.items():
                if k==m and s+t<=limit:h[s+t]+=v*n
        d=h
    return raw,sum(d.values())
root=pathlib.Path(__file__).resolve().parent
params=root/'params.txt'
params.write_text('\n'.join(map(str,[B,Q]+L+T+[x for row in MM for x in row]+[x for a in sorted(C) for x in C[a]]))+'\n')
def runrow(pat):
    length=len(pat);limit=(CAP-169*12+length)//13
    nraw,n=count_dp(pat,limit);counts=Counter(pat);m=counts.get(1,0)
    no_common=comb(10+m,m)
    for q,k in counts.items():
        if q!=1:no_common*=comb(11+k,k)
    common=12*(nraw-no_common)
    # Exact independent enumeration of feasible rosters and common labels.
    seen=0;common_feasible=0
    for neg in feasible(pat,limit):
        seen+=1;common_feasible+=len({r for q,r in neg if q==1})
    assert seen==n
    ls=subprocess.check_output([str(root/'exact'),str(params),*map(str,pat)],text=True).splitlines()
    actual,cf,nodes,leaves=map(int,ls[-1].split()[1:]);assert ls[-1].startswith('R ') and actual==12*n and cf==common_feasible and len(ls)==leaves+1
    ws=[]
    for line in ls[:-1]:
        assert line.startswith('W ');a=list(map(int,line.split()[1:]));pos=((1,a[0]),);neg=tuple(zip(pat,a[1:1+length]));z=a[1+length:];assert len(z)==N
        u0=[sum(z[j]*Urows[j][t] for j in range(N)) for t in range(N)];assert all(x%B==0 for x in u0);u=[x//B for x in u0]
        cp=sum(P*(P*q+r)-1 for q,r in pos);cn=sum(P*(P*q+r)-1 for q,r in neg);assert max(cp,cn)<=CAP
        residues=[(sum(x*h for x,h in zip(u,H[k-1]))-sum(pow(P*q+r,-k,P**k) for q,r in neg)+sum(pow(P*q+r,-k,P**k) for q,r in pos))%(P**k) for k in range(1,7)];assert residues==[0]*6
        norm=sum((w*x)**2 for w,x in zip(W,u));radius=(CAP-cp)**2+(CAP-cn)**2;assert norm<=radius
        c=[(sum(C[a][j] for a in neg)-sum(C[a][j] for a in pos))%B for j in range(N)];assert all((a-b)%B==0 for a,b in zip(z,c))
        masses=[cp+sum(w*max(0,x) for w,x in zip(W,u)),cn+sum(w*max(0,-x) for w,x in zip(W,u))]
        ws.append(dict(pos=pos,neg=neg,z=z,u=u,residues=residues,norm_sq=norm,radius_sq=radius,masses=masses,budget_valid=max(masses)<=CAP))
    row=dict(pos_pattern=[1],neg_pattern=pat,raw=12*nraw,over=12*(nraw-n),search=12*n,common_included=common,common_feasible=common_feasible,nodes=nodes,leaves=leaves,valid=sum(w['budget_valid'] for w in ws),witnesses=ws)
    path=root/('row_'+'_'.join(map(str,pat))+'.json');tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(row,separators=(',',':'))+'\n');tmp.replace(path)
    print('ROW',pat,row['search'],nodes,leaves,row['valid'],flush=True)
    return row
if __name__=='__main__':
    print('Dmin',dmin,'Q bits',Q.bit_length(),'B',B,flush=True)
    if len(sys.argv)>1 and sys.argv[1]=='check':
        runrow((12,));sys.exit()
    from concurrent.futures import ThreadPoolExecutor
    pats=[p for l in range(6,13) for p in patterns(12) if len(p)==l]
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows=list(pool.map(runrow,pats))
    totals={k:sum(r[k] for r in rows) for k in ('raw','over','search','common_included','common_feasible','nodes','leaves','valid')}
    out=dict(schema='T6_P13_Q13_SPLIT1_12_AUTHOR_EXACT_INTEGER_V1',frozen_science='d84bd940cfb093cdc60e569f15cad58772a51dca',source_initializer_blob='1097ff3a84242ea2c9347912697205f9681d8448',prior_program_blob='6a1759de6d5420b0ce42d8085eca66659c4231d7',p=P,valuation=1,total_q=13,split=[1,12],budget=CAP,negative_lengths=list(range(6,13)),gs_min_sq=str(dmin),lattice_index='13^21',coset_denominator=B,U=Urows,rows=rows,totals=totals,program_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),kernel_sha256=hashlib.sha256((root/'exact.cpp').read_bytes()).hexdigest(),status='AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED',scope='Six mixed congruences and both independent budgets; H0 and lower prime completion not implied; no formal claim or protected progress.')
    (root/'T6_P13_Q13_SPLIT1_12_LEN6_12_CERT.json').write_text(json.dumps(out,separators=(',',':'))+'\n');print('TOTAL',totals,flush=True)
