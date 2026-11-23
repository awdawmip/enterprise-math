from fractions import Fraction as F
from math import floor,lcm
from itertools import combinations_with_replacement as C,product
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form
import hashlib,json,argparse
P,CAP,N=13,2331,12
W=[P*r-1 for r in range(1,P)]
def lattice(atom=None):
    x=[0]*N; A=[[int(i==j) for j in range(N)] for i in range(N)]
    for k in range(1,7):
        mod=P**k;h=[pow(r,-k,mod) for r in range(1,P)]
        v=[sum(a*b for a,b in zip(row,h))%mod for row in A]
        piv=next(i for i,y in enumerate(v) if y%P);inv=pow(v[piv],-1,mod);old=A[piv]
        if atom:
            q,r=atom;target=(-pow(P*q+r,-k,mod)-sum(a*b for a,b in zip(x,h)))%mod
            factor=target*inv%mod;x=[a+factor*b for a,b in zip(x,old)]
        A=[[mod*a for a in row] if i==piv else [a-(v[i]*inv%mod)*b for a,b in zip(row,old)] for i,row in enumerate(A)]
    if atom:
        q,r=atom
        assert all((sum(t*pow(j,-k,P**k) for j,t in enumerate(x,1))+pow(P*q+r,-k,P**k))%(P**k)==0 for k in range(1,7))
    return x,A
M=Matrix(lattice()[1]);assert abs(M.det())==P**21
Rw=(hermite_normal_form(M.T).T*Matrix.diag(*W)).lll(delta=F(3,4));U=Rw*Matrix.diag(*(F(1,w) for w in W));assert all(x.q==1 for x in U)
UI=U.inv();G=Rw*Rw.T
mu=[[F(0)]*N for _ in range(N)];D=[]
for i in range(N):
    for j in range(i):mu[i][j]=(F(int(G[i,j]))-sum(mu[i][t]*mu[j][t]*D[t] for t in range(j)))/D[j]
    D.append(F(int(G[i,i]))-sum(mu[i][j]**2*D[j] for j in range(i)))
dmin=min(D);assert dmin>2*CAP**2
Urows=[[int(U[j,t]) for t in range(N)] for j in range(N)]
atoms={(q,r):lattice((q,r))[0] for q in range(1,4) for r in range(1,P)}
c_atom={a:[F(x) for x in Matrix(1,N,v)*UI] for a,v in atoms.items()}
g_atom={a:[c[i]+sum(c[j]*mu[j][i] for j in range(i+1,N)) for i in range(N)] for a,c in c_atom.items()}
L=[lcm(*(v[i].denominator for v in g_atom.values()),*(mu[j][i].denominator for j in range(i+1,N))) for i in range(N)]
mg=[[int(mu[j][i]*L[i]) for j in range(N)] for i in range(N)];ig={a:tuple(int(g[i]*L[i]) for i in range(N)) for a,g in g_atom.items()}
coef=[D[i]/L[i]**2 for i in range(N)];S=lcm(*(c.denominator for c in coef));K=[int(c*S) for c in coef];assert all(F(K[i],S)==D[i]/L[i]**2 for i in range(N))
def mass(roster):return sum(P*(P*q+r)-1 for q,r in roster)
def data(roster):return mass(roster),tuple(sum(ig[a][i] for a in roster) for i in range(N)),frozenset(roster)
positives=[((3,r),) for r in range(1,13)]+[((1,r),(2,s)) for r,s in product(range(1,13),repeat=2)]+[tuple((1,r) for r in v) for v in C(range(1,13),3)]
negatives=[((1,c),)+tuple((2,r) for r in v) for c in range(1,13) for v in C(range(1,13),3)]
assert len(positives)==520 and len(negatives)==4368
pd=[data(p) for p in positives]
def witness(pos,neg,n,radius):
    u=[sum(atoms[a][t] for a in pos)-sum(atoms[a][t] for a in neg)+sum(n[j]*Urows[j][t] for j in range(N)) for t in range(N)]
    masses=[mass(pos)+sum(w*max(0,x) for w,x in zip(W,u)),mass(neg)+sum(w*max(0,-x) for w,x in zip(W,u))]
    residues=[(sum(x*pow(r,-k,P**k) for r,x in enumerate(u,1))+sum(pow(P*q+r,-k,P**k) for q,r in pos)-sum(pow(P*q+r,-k,P**k) for q,r in neg))%(P**k) for k in range(1,7)]
    assert residues==[0]*6 and sum((w*x)**2 for w,x in zip(W,u))<=radius
    return dict(pos=pos,neg=neg,u=u,masses=masses,radius_sq=radius,budget_valid=max(masses)<=CAP,modular_residues=residues)
def search(pos,neg,pdata,ndata,rational=False):
    cp,gp,_=pdata;cn,gn,_=ndata
    if max(cp,cn)>CAP:return True,0,[]
    radius=(CAP-cp)**2+(CAP-cn)**2;assert radius<dmin
    g=[a-b for a,b in zip(gp,gn)];n=[0]*N;nodes=0;leaves=[]
    if rational:c=[sum(c_atom[a][i] for a in pos)-sum(c_atom[a][i] for a in neg) for i in range(N)]
    def descend(i,left):
        nonlocal nodes
        if i<0:leaves.append(witness(pos,neg,n,radius));return
        nodes+=1
        if rational:
            center=c[i]+sum((c[j]+n[j])*mu[j][i] for j in range(i+1,N));near=floor(-center);scale=1
        else:
            center=g[i]+sum(n[j]*mg[i][j] for j in range(i+1,N));near=(-center)//L[i];scale=L[i]
        for ni in (near,near+1):
            delta=center+ni*scale;cost=(D[i] if rational else K[i])*delta*delta
            if cost<=left:n[i]=ni;descend(i-1,left-cost)
    descend(N-1,F(radius) if rational else radius*S);return False,nodes,leaves
def replay(start,end):
    assert 0<=start<end<=len(negatives)
    st=dict(negative_rosters=0,positive_rosters=520,raw_signed_pairs=0,common_named_atom_canceled=0,vertical_original_mass_excess=0,gs_searches=0,gs_nodes=0,relaxed_sphere_witnesses=0,both_original_side_mass_valid=0)
    rh=hashlib.sha256();ph=hashlib.sha256();ws=[];reg=0
    for ni in range(start,end):
        neg=negatives[ni];nd=data(neg);st['negative_rosters']+=1;rh.update((repr(neg)+'\n').encode('ascii'))
        for pi,(pos,pdata) in enumerate(zip(positives,pd)):
            st['raw_signed_pairs']+=1;ph.update((repr((ni,pi,pos,neg))+'\n').encode('ascii'))
            if pdata[2]&nd[2]:st['common_named_atom_canceled']+=1;continue
            skip,nodes,leaves=search(pos,neg,pdata,nd)
            if ((ni-start)%97==0 and pi%31==0) or leaves:assert (skip,nodes,leaves)==search(pos,neg,pdata,nd,True);reg+=1
            if skip:st['vertical_original_mass_excess']+=1;continue
            st['gs_searches']+=1;st['gs_nodes']+=nodes;st['relaxed_sphere_witnesses']+=len(leaves);st['both_original_side_mass_valid']+=sum(int(w['budget_valid']) for w in leaves)
            for w in leaves:w.update(negative_roster_index=ni,positive_roster_index=pi);ws.append(w)
    assert st['raw_signed_pairs']==520*(end-start)==st['common_named_atom_canceled']+st['vertical_original_mass_excess']+st['gs_searches']
    return dict(schema='EM_T6_P13_Q10_SPLIT3_7_NEG1222_AUTHOR_EXACT_SLICE_V1',frozen_science='awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca',kernel_source='awdawmip/enterprise-math@de78443d23578a66d3ae79f2a045e4be8e756c50:research_checks/T6_P13_Q10_SPLIT2_8_NEG11111111_SLICE_REPLAY_20261123_2300.py',signed_split=[3,7],negative_q_pattern=[1,2,2,2],positive_q_patterns=[[3],[1,2],[1,1,1]],interval=[start,end],total_negative_rosters=4368,source_order='negative q1 outer then q2 CWR(12,3); positive q3 single, q1q2 product, q1^3 CWR',budget_each_side=CAP,lattice_index='13^21',gs_min_sq=str(dmin),integer_cost_scale=str(S),reference_rational_pair_comparisons=reg,stats=st,negative_roster_sha256=rh.hexdigest(),pair_digest_sha256=ph.hexdigest(),witnesses=ws,status='AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--start',type=int,required=True);p.add_argument('--end',type=int,required=True);p.add_argument('--output',required=True);a=p.parse_args();r=replay(a.start,a.end);open(a.output,'w').write(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps(r,sort_keys=True))
