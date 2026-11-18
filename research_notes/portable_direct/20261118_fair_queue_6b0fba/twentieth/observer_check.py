"""Native signed chart, rational closure certificates, and integral Krylov indices."""
import json
from fractions import Fraction as F
from itertools import combinations
from math import gcd
from functools import reduce


N = 13
O = (0,)*6
S = [O]+[tuple(int(c==i//2 or (i%2 and c==(i//2+1)%6)) for c in range(6))
         for i in range(12)]
FACES = [tuple(s[j] for s in S) for j in range(6)]
JOINTS = [tuple(s[j]*s[(j+1)%6] for s in S) for j in range(6)]
MASS = (1,)*N
OBS = {'m': MASS, **{f'x{i+1}':row for i,row in enumerate(FACES)},
       **{f'j{i+1}':row for i,row in enumerate(JOINTS)}}
MAPS = {'A':[0]+[1+(i+1)%12 for i in range(12)],
        'B':[0]+[1+(i-1)%12 for i in range(12)],
        'I':list(range(N)), 'R':[0]*N}


def pull(row, op):
    if isinstance(op,str):
        return tuple(row[i] for i in MAPS[op])
    a,b,d = op
    c=1-a-b-d
    return tuple(a*row[x]+b*row[y]+c*row[i]+d*row[0]
                 for i,(x,y) in enumerate(zip(MAPS['A'],MAPS['B'])))


def add(row, reduced, mod=None):
    v=[x%mod for x in row] if mod else list(map(F,row))
    for p,h in sorted(reduced.items()):
        if v[p]:
            c=v[p]
            v=[x-c*y for x,y in zip(v,h)]
            if mod: v=[x%mod for x in v]
    p=next((i for i,x in enumerate(v) if x),None)
    if p is None: return False
    reduced[p]=[x*pow(v[p],-1,mod)%mod for x in v] if mod else [x/v[p] for x in v]
    return True


def inverse(mat):
    n=len(mat)
    m=[list(map(F,row))+[F(i==j) for j in range(n)] for i,row in enumerate(mat)]
    for j in range(n):
        i=next(i for i in range(j,n) if m[i][j])
        m[i],m[j]=m[j],m[i]
        c=m[j][j]
        m[j]=[x/c for x in m[j]]
        for i in range(n):
            if i!=j and m[i][j]:
                c=m[i][j]
                m[i]=[x-c*y for x,y in zip(m[i],m[j])]
    return [row[n:] for row in m]


def sparse(mat):
    return [[i,j,str(v)] for i,row in enumerate(mat) for j,v in enumerate(row) if v]


def cert(keys, ops):
    reduced={}
    rows=[]
    labels=[]
    def save(label,row):
        if add(row,reduced):
            labels.append(label)
            rows.append(row)
    for k in keys: save(k,OBS[k])
    ranks=[len(rows)]
    lo=0
    while True:
        hi=len(rows)
        for i in range(lo,hi):
            for name,op in ops.items(): save(name+' '+labels[i],pull(rows[i],op))
        if hi==len(rows): break
        ranks.append(len(rows))
        lo=hi
    piv=sorted(reduced)
    inv=inverse([[row[p] for p in piv] for row in rows])
    def coords(row):
        c=[sum(row[p]*inv[j][i] for j,p in enumerate(piv)) for i in range(len(rows))]
        assert all(sum(h[q]*z for h,z in zip(rows,c))==row[q] for q in range(N))
        return c
    transition={s:sparse([coords(pull(h,op)) for h in rows]) for s,op in ops.items()}
    reconstruction=sparse([coords(OBS[k]) for k in keys])
    witnesses=[]
    for j in range(1,len(rows)):
        v=[F(0)]*N
        for i,p in enumerate(piv): v[p]=inv[i][j]
        assert sum(v)==0
        weight=sum(max(0,x) for x in v)
        gap=1/weight
        assert all(sum(v[q]*row[q] for q in range(N))==int(i==j)
                   for i,row in enumerate(rows))
        witnesses.append([j,str(gap)])
    classes={}
    for q in range(N): classes.setdefault(tuple(h[q] for h in rows),[]).append(q)
    return dict(keys=keys,basis_future_labels=labels,ranks=ranks,pivot_columns=piv,
                basis=sparse(rows),update=transition,readout=reconstruction,
                dual_at_pivots=sparse(inv),deletion_witness_gaps=witnesses,
                point_classes=list(classes.values()))


def modular(mask,regime):
    p=101
    keys=['m',*[f'x{i+1}' for i in range(6)],*[f'j{i+1}' for i in range(6) if mask>>i&1]]
    reduced={}
    gen=[]
    for k in keys:
        if add(OBS[k],reduced,p): gen.append(OBS[k])
    for row in gen:
        a,b=pull(row,'A'),pull(row,'B')
        if regime=='control': newer=[a,b]
        elif regime=='biased': newer=[tuple((2*x+y+z)%p for x,y,z in zip(a,b,row))]
        elif regime=='symmetric': newer=[tuple((x+y+z)%p for x,y,z in zip(a,b,row))]
        else: newer=[row]
        for h in newer:
            if add(h,reduced,p): gen.append(h)
    return len(gen)


def bareiss(mat):
    m=[list(row) for row in mat]
    sign=old=1
    for i in range(len(m)-1):
        z=next((j for j in range(i,len(m)) if m[j][i]),None)
        if z is None: return 0
        if z!=i:
            m[i],m[z]=m[z],m[i];sign=-sign
        for j in range(i+1,len(m)):
            for k in range(i+1,len(m)):
                n=m[j][k]*m[i][i]-m[j][i]*m[i][k]
                assert n%old==0
                m[j][k]=n//old
        old=m[i][i]
    return sign*m[-1][-1]


def integral_rows(a,b,c):
    # q=(z^12-1)/(z^2+z+1)=(z-1)(1+z^3+z^6+z^9), monic degree 10.
    q=[-1,1,0,-1,1,0,-1,1,0,-1,1]
    v=[1]+[0]*9
    table=[]
    for _ in range(10):
        table.append(v)
        fwd=[0]+v[:-1]
        fwd=[x-v[-1]*y for x,y in zip(fwd,q)]
        back=v[1:]+[0]
        back=[x+v[0]*y for x,y in zip(back,q[1:])]
        v=[a*x+b*y+c*z for x,y,z in zip(fwd,back,v)]
    return table


def integral_check():
    J=[i for i in range(12) if i not in (4,8)]
    pairs=[(i+j)%12 for i,j in combinations(J,2)]
    exps={d:pairs.count(i) for i in range(12) for d in [12//gcd(i,12)]}
    assert all(pairs.count(i)==exps[12//gcd(i,12)] for i in range(12))
    examples=[];total=0;red_count=0
    for a in range(6):
        for b in range(6):
            for c in (0,2):
                pol={1:a-b,2:a+b,3:a*a+a*b+b*b,4:a*a+b*b,
                     6:a*a-a*b+b*b,12:a**4-a*a*b*b+b**4}
                predicted=reduce(lambda x,y:x*y,(pol[d]**e for d,e in exps.items()),1)
                rows=integral_rows(a,b,c);det=bareiss(rows)
                assert abs(det)==abs(predicted)
                for p in (2,3,5,7,11,13,17,19,31,37):
                    basis={}
                    for x in rows: add(x,basis,p)
                    assert (len(basis)==10)==bool(det%p)
                    if p>3:
                        if a%p==0 and b%p==0: expect=1
                        elif not a%p or not b%p: expect=10
                        else:
                            t=a*pow(b,-1,p)%p
                            order=next((d for d in (1,2,3,4,6,12) if pow(t,d,p)==1),None)
                            expect=10-exps[order] if order else 10
                        assert len(basis)==expect
                    red_count+=1
                if c==0 and (a,b) in [(1,0),(2,1),(3,1),(1,1)]:
                    examples.append(dict(a=a,b=b,det_abs=abs(det)))
                total+=1
    return dict(exponents=exps,examples=examples,integer_determinants=total,modular_ranks=red_count)


def main():
    assert len(set(S))==13
    for i in range(12): assert sum(abs(x-y) for x,y in zip(S[1+i],S[1+(i+1)%12]))==1
    for k,data in enumerate(JOINTS): assert [i for i,x in enumerate(data) if x]==[2*k+2]
    models={'control':{name:name for name in MAPS},
            'biased':{'K':(F(2,5),F(1,5),F(1,5))},
            'symmetric':{'K':(F(1,3),F(1,3),F(1,6))},
            'idle':{'K':(F(0),F(0),F(1,3))},'reset':{'K':(F(0),F(0),F(1))}}
    axes=list(OBS)[1:7]
    menus={'x1':['m','x1'],'axes':['m',*axes],
           'axes+j1':['m',*axes,'j1'],'axes+j1+j4':['m',*axes,'j1','j4'],
           'axes+j1+j2':['m',*axes,'j1','j2'],'all':list(OBS)}
    certificates={}
    masks={}
    for regime,ops in models.items():
        certificates[regime]={s:cert(ks,ops) for s,ks in menus.items()}
        preds={}
        for m in range(64):
            js=[j for j in range(6) if m>>j&1]
            if regime in ('control','biased'): dim=13 if js else 11
            elif regime=='symmetric': dim=10 if not js else 11+len(set(j%3 for j in js)) if len(set(j%3 for j in js))<2 else 13
            else: dim=7+len(js)
            assert modular(m,regime)==dim
            preds[dim]=preds.get(dim,0)+1
        masks[regime]=preds
    pair=[tuple(int(i%3==v) for i in range(12)) for v in (0,1)]
    for j in range(12):
        assert sum(pair[0][i]*FACES[0][1+(i+j)%12] for i in range(12))==1
        assert sum(pair[1][i]*FACES[0][1+(i+j)%12] for i in range(12))==1
    return dict(states=S,index_order='0=o, i+1=r_i',models={k:{n:str(v) for n,v in ops.items()} for k,ops in models.items()},
                sparse_format='[zero-based row,zero-based column,rational value]',certificates=certificates,
                all_64_joint_masks_verified_at_prime_101=masks,integral=integral_check())


if __name__=='__main__':
    print(json.dumps(main(),sort_keys=True,separators=(',',':')))
