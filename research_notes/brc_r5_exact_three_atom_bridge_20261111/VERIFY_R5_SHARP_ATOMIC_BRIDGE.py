#!/usr/bin/env python3
"""Exact R5 C->B and A->B atom witnesses (standard-library Fraction).
Frozen object: R5 7-ratio P/Q-BRC Blackwell fiber, prior commit
9708a8b5ba1870bb423577c50144c1acfa7606dd.
This is a constructive verification, not a two-atom A->B no-go proof.
"""
from fractions import Fraction as F
R=(2,10,15,20,25,30,38)
S=(1,2,3,5)
ARCS=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7)
           if j not in (0,6) or i==j)
E0=tuple(map(F,(
 '219346331/10192753200,7664319/135903376,2813871/16987922,'
 '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,393042/8493961,196521/33975844,'
 '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,5251441/33975844,166713611/1274094150,'
 '2500147/33975844,393042/8493961,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,7664319/135903376,451274777/3397584400').split(',')))
assert len(ARCS)==len(E0)==30 and min(E0)>0
V=tuple((i,j) for j in S for i in range(7))
ix={e:k for k,e in enumerate(V)}
A=[[int(ii==i) for ii,jj in V] for i in range(7)]
A += [[int(jj==j) for ii,jj in V] for j in S]
A += [[R[ii]*int(jj==j) for ii,jj in V] for j in S]
b=[sum((z for (ii,j),z in zip(ARCS,E0) if ii==i and j in S),F(0))
   for i in range(7)]
b += [sum((z for (ii,j),z in zip(ARCS,E0) if j==source),F(0)) for source in S]
b += [sum((R[ii]*z for (ii,j),z in zip(ARCS,E0) if j==source),F(0))
      for source in S]
assert len(A)==len(b)==15
MA,MC,MB={1,3,4,6},{2,3,4,6},{2,3,4,5}
def transfer(string):
    v=tuple(map(F,string.split(',')))
    assert len(v)==28
    return v
def atom(other,row):
    h=[F(0)]*28
    assert len(row)==3 and other in (1,2,5)
    for target,value in row.items():
        h[ix[(target,3)]]=F(value)
        h[ix[(target,other)]]=-F(value)
    assert all(sum(A[r][k]*h[k] for k in range(28))==0 for r in range(15))
    return h
def step(v,h,t):
    assert t>0
    return tuple(x+t*y for x,y in zip(v,h))
def check(v,mask):
    assert min(v)>=0 and len(v)==28
    assert all(sum(A[r][k]*v[k] for k in range(28))==b[r] for r in range(15))
    assert {i for i in range(7) if v[ix[(i,3)]]>0}==mask
    return sum(z>0 for z in v)
XC=transfer('61299435/951323632,1523703/9707384,0,0,256989/16987922,3431559/237830908,0,'
            '0,4519983/67951688,0,0,0,0,982605/67951688,'
            '0,0,1460251/8493961,377644447/2548188300,643933/8493961,0,226755/8493961,'
            '4429281/475661816,0,0,0,0,5850279/118915454,4429281/135903376')
HCB=atom(5,{2:F(-8,15),5:F(23,15),6:-1})
tCB=F('226755/8493961')
YC=step(XC,HCB,tCB)
print('C_TO_B_ONE_ATOM',check(XC,MC),check(YC,MB),'t=',tCB)
XA=transfer('10022571/135903376,1383455/16987922,1544855/16987922,0,0,0,5863/1213423,'
            '0,0,196521/2426846,0,0,0,0,'
            '0,33585773/237830908,0,377644447/2548188300,643933/8493961,0,13650395/237830908,'
            '0,196521/237830908,0,0,256989/16987922,2161731/33975844,10959825/951323632')
H1=atom(1,{1:-23,2:28,6:-5})
H2=atom(2,{1:-23,2:28,6:-5})
t1,t2,t3=F('1544855/475661816'),F('196521/67951688'),tCB
W1=step(XA,H1,t1)
W2=step(W1,H2,t2)
YA=step(W2,HCB,t3)
checks=[check(z,mask) for z,mask in zip((XA,W1,W2,YA),(MA,MA|MC,MC,MB))]
print('A_TO_B_THREE_ATOMS',checks,'steps=',(t1,t2,t3))
print('SOURCE3_SUPPORT_SEQUENCE',[(1,3,4,6),(1,2,3,4,6),(2,3,4,6),(2,3,4,5)])
print('SOURCE3_INTERIOR_PEAK',5)
print('A_TO_B_ONE_ATOM_EXCLUDED_BY_FOUR_CHANGED_TARGETS',sorted(MA^MB))
print('A_TO_B_TWO_ATOM_MINIMALITY','UNRESOLVED')
print('PASS_EXACT_R5_C_B_ONE_ATOM_AND_A_B_THREE_ATOM_WITNESSES')

# -- R5 exact two-operation no-go; appended to the predecessor's exact
# -- three-operation rational witness / observer definition.
# Dataset: R5_TWO_ATOM_FARKAS_CERTIFICATES.json.gz.b64
import itertools, json, gzip, base64, sys

def candidate(old,new,third,compensator):
    assert len({old,new,third})==3
    z0,z1,z2=R[new]-R[third],R[third]-R[old],R[old]-R[new]
    if z0*z1>=0:return None
    vals=[F(v,-z0) for v in (z0,z1,z2)]
    assert vals[0]==-1 and vals[1]>0
    h=[F(0)]*28
    for i,z in zip((old,new,third),vals):
        h[ix[(i,3)]]=z
        h[ix[(i,compensator)]]=-z
    assert all(sum(row[k]*h[k] for k in range(28))==0 for row in A)
    return tuple(h)

def all_cases():
    D={}
    for old1,new1 in itertools.product((1,6),(2,5)):
        old2=next(iter({1,6}-{old1}))
        new2=next(iter({2,5}-{new1}))
        for third1,third2,j1,j2 in itertools.product((3,4,old2),(3,4,new1),(1,2,5),(1,2,5)):
            h1=candidate(old1,new1,third1,j1)
            h2=candidate(old2,new2,third2,j2)
            if h1 is not None and h2 is not None:
                D[('I',(old1,new1,third1,old2,new2,third2),j1,j2)]=(h1,h2)
    for new1 in (2,5):
        new2=next(iter({2,5}-{new1}))
        for old_a,old_b in itertools.combinations(sorted(MA),2):
            for j1,j2 in itertools.product((1,2,5),repeat=2):
                h1=candidate(old_a,new1,old_b,j1)
                if h1 is None:h1=candidate(old_b,new1,old_a,j1)
                h2=candidate(1,new2,6,j2)
                if h2 is None:h2=candidate(6,new2,1,j2)
                assert h1 is not None and h2 is not None
                D[('II',(old_a,new1,old_b,1,new2,6),j1,j2)]=(h1,h2)
    assert len(D)==270
    assert sum(k[0]=='I' for k in D)==162
    assert sum(k[0]=='II' for k in D)==108
    return D

def matrices(mode,hh):
    h1,h2=hh
    if mode=='s3':
        nv=9
        v1=[h1[ix[(i,3)]] for i in range(7)]
        v2=[h2[ix[(i,3)]] for i in range(7)]
        eq=[[F(1)]*7+[F(0),F(0)], [F(r) for r in R]+[F(0),F(0)]]
        rhs=[b[7+S.index(3)],b[11+S.index(3)]]
        for i in range(7):
            if i not in MA:
                row=[F(0)]*nv;row[i]=F(1);eq.append(row);rhs.append(F(0))
            if i not in MB:
                row=[F(0)]*nv;row[i]=F(1)
                row[7]=v1[i];row[8]=v2[i]
                eq.append(row);rhs.append(F(0))
        ub=[];bounds=[]
        for i in range(7):
            row=[F(0)]*nv;row[i]=-1;row[7]=-v1[i];ub.append(row);bounds.append(F(0))
            row=[F(0)]*nv;row[i]=-1;row[7]=-v1[i];row[8]=-v2[i];ub.append(row);bounds.append(F(0))
            for stage in (0,1,2):
                row=[F(0)]*nv;row[i]=1
                if stage>0:row[7]=v1[i]
                if stage>1:row[8]=v2[i]
                ub.append(row);bounds.append(b[i])
    else:
        assert mode=='full'
        nv=30
        eq=[[F(v) for v in row]+[F(0),F(0)] for row in A]
        rhs=list(b)
        for i in range(7):
            if i not in MA:
                row=[F(0)]*nv;row[ix[(i,3)]]=1;eq.append(row);rhs.append(F(0))
            if i not in MB:
                row=[F(0)]*nv;row[ix[(i,3)]]=1
                row[28]=h1[ix[(i,3)]]
                row[29]=h2[ix[(i,3)]]
                eq.append(row);rhs.append(F(0))
        ub=[];bounds=[]
        for i in range(28):
            row=[F(0)]*nv;row[i]=-1
            row[28]=-h1[i]
            ub.append(row);bounds.append(F(0))
            row=[F(0)]*nv;row[i]=-1;row[28]=-h1[i];row[29]=-h2[i]
            ub.append(row);bounds.append(F(0))
    return eq,rhs,ub,bounds

def check_farkas(c,hh):
    eq,rhs,ub,bounds=matrices(c['mode'],hh)
    m,n=len(eq),len(eq[0]);k=len(ub)
    y=[F(0)]*m;lam=[F(0)]*k
    for i,v in c['equalities'].items():y[int(i)]=F(v)
    for i,v in c['inequalities'].items():lam[int(i)]=F(v)
    assert min(lam)>=0
    assert min(sum(eq[i][j]*y[i] for i in range(m))+
               sum(ub[i][j]*lam[i] for i in range(k)) for j in range(n))>=0
    gap=sum(rhs[i]*y[i] for i in range(m))+sum(bounds[i]*lam[i] for i in range(k))
    assert gap<0 and gap==F(c['gap'])
    return gap

def check_s3_triples():
    q=b[7+S.index(3)];m=b[11+S.index(3)]
    rejected=0
    for u,v,w in itertools.combinations(range(7),3):
        y0=F(m-R[w]*q,R[v]-R[w]);y1=F(R[w]-R[u],R[v]-R[w])
        z0=q-y0;z1=-1-y1
        lower=F(0);upper=b[u]
        for const,slope,cap in ((y0,y1,b[v]),(z0,z1,b[w])):
            if slope>0:
                lower=max(lower,-const/slope);upper=min(upper,(cap-const)/slope)
            elif slope<0:
                upper=min(upper,-const/slope);lower=max(lower,(cap-const)/slope)
            elif const<0 or const>cap:
                upper=lower-1
        assert lower>upper,(u,v,w)
        rejected+=1
    return rejected

def verify_dual_bundle(path):
    data=json.loads(gzip.decompress(base64.b64decode(open(path,encoding='ascii').read())))
    cases=all_cases()
    by_pattern={}
    for (kind,pattern,j1,j2),hh in cases.items():
        by_pattern.setdefault((kind,pattern),hh)
    assert len(by_pattern)==30
    seen=set();s3=set();full=set()
    for c in data['certificates']:
        kind=c['kind'];pat=tuple(c['pattern'])
        mode=c['mode'];j1=c['first_port'];j2=c['second_port']
        if mode=='s3':
            key=('s3',kind,pat)
            hh=by_pattern[(kind,pat)]
            s3.add((kind,pat))
        else:
            key=('full',kind,pat,j1,j2)
            hh=cases[(kind,pat,j1,j2)]
            full.add((kind,pat,j1,j2))
        assert key not in seen
        seen.add(key)
        check_farkas(c,hh)
    assert len(s3)==23 and len(full)==63 and len(seen)==86
    for kind,pat,j1,j2 in cases:
        assert (kind,pat) in s3 or (kind,pat,j1,j2) in full
    assert check_s3_triples()==35
    print('EXACT_S3_TRIPLES_EXCLUDED',35)
    print('COMPLETE_TWO_STEP_CLASSES I=18x9 II=12x9')
    print('EXACT_FARKAS_CERTIFICATES',len(s3),len(full))
    print('ALL_270_TWO_STEP_PORT_PATTERNS_EXCLUDED',True)
    print('EXACT_ATOMIC_DISTANCE_A_B_PEAK5',3)
    print('PASS_R5_EXACT_86_DUAL_CERTIFICATES_AND_SHARP_THREE_ATOM_BRIDGE')

if __name__=='__main__':
    verify_dual_bundle(sys.argv[1] if len(sys.argv)>1 else
      'R5_TWO_ATOM_FARKAS_CERTIFICATES.json.gz.b64')
