from fractions import Fraction as F
from math import floor, comb, lcm
from itertools import product, combinations_with_replacement
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form
import hashlib,json,argparse,time
P,CAP,N=13,2331,12
W=[P*r-1 for r in range(1,P)]
H=[[pow(r,-k,P**k) for r in range(1,P)] for k in range(1,7)]
A=[[int(i==j) for j in range(N)] for i in range(N)]
# Same exact saturation as immutable kernel; retain elimination stages for particular vectors.
stages=[]
for k,h in enumerate(H,1):
    mod=P**k
    v=[sum(a*b for a,b in zip(row,h))%mod for row in A]
    piv=next(i for i,x in enumerate(v) if x%P);inv=pow(v[piv],-1,mod);old=A[piv]
    stages.append((mod,h,inv,old))
    A=[[mod*a for a in row] if i==piv else [a-(v[i]*inv%mod)*b for a,b in zip(row,old)] for i,row in enumerate(A)]
M=Matrix(A);assert abs(M.det())==P**21
Rw=(hermite_normal_form(M.T).T*Matrix.diag(*W)).lll(delta=F(3,4))
U=Rw*Matrix.diag(*(F(1,w) for w in W));assert all(x.q==1 for x in U)
UI=U.inv();G=Rw*Rw.T
mu=[[F(0)]*N for _ in range(N)];D=[]
for i in range(N):
    for j in range(i):mu[i][j]=(F(int(G[i,j]))-sum(mu[i][t]*mu[j][t]*D[t] for t in range(j)))/D[j]
    D.append(F(int(G[i,i]))-sum(mu[i][j]**2*D[j] for j in range(i)))
dmin=min(D);assert dmin>2*CAP**2
Urows=[[int(U[j,t]) for t in range(N)] for j in range(N)]
def particular(q,r):
    x=[0]*N
    for k,(mod,h,inv,old) in enumerate(stages,1):
        target=(-pow(P*q+r,-k,mod)-sum(a*b for a,b in zip(x,h)))%mod
        x=[a+target*inv%mod*b for a,b in zip(x,old)]
    assert all((sum(t*h for t,h in zip(x,H[k-1]))+pow(P*q+r,-k,P**k))%(P**k)==0 for k in range(1,7))
    return x
c_atom={(q,r):[F(x) for x in Matrix(1,N,particular(q,r))*UI] for q in range(1,4) for r in range(1,P)}
positives=[((3,r),) for r in range(1,13)]+[((1,r),(2,s)) for r,s in product(range(1,13),repeat=2)]+[tuple((1,r) for r in v) for v in combinations_with_replacement(range(1,13),3)]
negatives=[((1,r),(1,s),(2,t),(3,u)) for r,s in combinations_with_replacement(range(1,13),2) for t,u in product(range(1,13),repeat=2)]
assert len(positives)==520 and len(negatives)==11232
# Compute using the same rational GS test; integer representation clears denominators exactly.
Q=lcm(*(x.denominator for v in c_atom.values() for x in v))
L=[lcm(Q,*(Q*mu[j][i].denominator for j in range(i+1,N))) for i in range(N)]
B=[[int(mu[j][i]*L[i]/Q) for j in range(N)] for i in range(N)]
DD=[D[i]/L[i]**2 for i in range(N)];K=lcm(*(x.denominator for x in DD));T=[int(x*K) for x in DD]
assert all(x>0 for x in T)
ci={a:tuple(int(x*Q) for x in v) for a,v in c_atom.items()}
def prepare(roster):return (sum(P*(P*q+r)-1 for q,r in roster),tuple(sum(ci[a][j] for a in roster) for j in range(N)),set(roster))
pp=list(map(prepare,positives));nn=list(map(prepare,negatives))
def pair_search(pos,neg,pa,na):
    cp,pc,_=pa;cn,nc,_=na
    if cp>CAP or cn>CAP:return (True,0,[])
    radius=(CAP-cp)**2+(CAP-cn)**2;assert radius<dmin
    c=[a-b for a,b in zip(pc,nc)];z=c[:];nodes=0;leaves=[]
    def descend(i,spent):
        nonlocal nodes
        if i<0:
            numer=[sum(z[j]*Urows[j][t] for j in range(N)) for t in range(N)]
            assert all(x%Q==0 for x in numer);u=[x//Q for x in numer]
            masses=[cp+sum(w*max(0,x) for w,x in zip(W,u)),cn+sum(w*max(0,-x) for w,x in zip(W,u))]
            residues=[(sum(x*h for x,h in zip(u,H[k-1]))+sum(pow(P*q+r,-k,P**k) for q,r in pos)-sum(pow(P*q+r,-k,P**k) for q,r in neg))%(P**k) for k in range(1,7)]
            assert residues==[0]*6
            leaves.append(dict(pos=pos,neg=neg,u=u,masses=masses,radius_sq=radius,budget_valid=max(masses)<=CAP,modular_residues=residues));return
        nodes+=1
        center=c[i]*(L[i]//Q)+sum(z[j]*B[i][j] for j in range(i+1,N))
        near=(-center)//L[i]
        for ni in (near,near+1):
            next_spent=spent+T[i]*(center+ni*L[i])**2
            if next_spent<=radius*K:
                z[i]=c[i]+ni*Q;descend(i-1,next_spent)
        z[i]=c[i]
    descend(N-1,0);return (False,nodes,leaves)
def replay(start,end):
    assert 0<=start<end<=len(negatives)
    st=dict(negative_rosters=0,positive_rosters=520,raw_signed_pairs=0,common_named_atom_canceled=0,vertical_original_mass_excess=0,gs_searches=0,gs_nodes=0,relaxed_sphere_witnesses=0,both_original_side_mass_valid=0)
    roster_sha=hashlib.sha256();pair_sha=hashlib.sha256();witnesses=[]
    for ni in range(start,end):
        neg=negatives[ni];na=nn[ni];st['negative_rosters']+=1;roster_sha.update((repr(neg)+'\n').encode('ascii'))
        for pi,pos in enumerate(positives):
            pa=pp[pi];st['raw_signed_pairs']+=1;pair_sha.update((repr((ni,pi,pos,neg))+'\n').encode('ascii'))
            if pa[2]&na[2]:st['common_named_atom_canceled']+=1;continue
            skip,nodes,leaves=pair_search(pos,neg,pa,na)
            if skip:st['vertical_original_mass_excess']+=1;continue
            st['gs_searches']+=1;st['gs_nodes']+=nodes;st['relaxed_sphere_witnesses']+=len(leaves);st['both_original_side_mass_valid']+=sum(int(v['budget_valid']) for v in leaves)
            for v in leaves:v.update(negative_roster_index=ni,positive_roster_index=pi);witnesses.append(v)
    assert st['raw_signed_pairs']==520*(end-start)==st['common_named_atom_canceled']+st['vertical_original_mass_excess']+st['gs_searches']
    return dict(frozen_science='awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca',signed_split=[3,7],negative_q_pattern=[1,1,2,3],interval=[start,end],total_negative_rosters=len(negatives),positive_q_patterns=[[3],[1,2],[1,1,1]],budget_each_side=CAP,lattice_index='13^21',gs_min_sq=str(dmin),stats=st,negative_roster_sha256=roster_sha.hexdigest(),pair_digest_sha256=pair_sha.hexdigest(),witnesses=witnesses,status='AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--start',type=int,required=True);p.add_argument('--end',type=int,required=True);p.add_argument('--output',required=True);a=p.parse_args();t=time.monotonic();r=replay(a.start,a.end);json.dump(r,open(a.output,'w'),indent=2);print(json.dumps(r));print('seconds',time.monotonic()-t)
