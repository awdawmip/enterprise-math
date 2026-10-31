#!/usr/bin/env python3
"""Exact h=10 signed-X6 BRC certificate replay. Python 3 standard library only.
Random.Random reconstructs fixed literal witnesses; proof is 121 exact nonzero minors.
"""
import base64, json, lzma, random, sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
P=1000003; H=10; N=28
OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3)}
W=((2,3,3,2,1,1),(3,2,3,2,1,1))
def endpoint(path):
    a=[0]*6
    for x in path:
        assert isinstance(x,int) and 1<=abs(x)<=6
        a[abs(x)-1]+=1 if x>0 else -1
    return tuple(a)
def tag(path):
    A=any(a==1 and b==2 for a,b in zip(path,path[1:]))
    B=any(a==2 and b==1 for a,b in zip(path,path[1:]))
    return 2*int(A)+int(B)
def weights(path):
    a=b=1
    for x in path:
        if x>0:a*=W[0][x-1];b*=W[1][x-1]
    return (a,b,1)
def next_state(q,x):
    a,b=divmod(q,3)
    a=2 if a==2 or (a==1 and x==2) else int(x==1)
    b=2 if b==2 or (b==1 and x==1) else int(x==2)
    return 3*a+b
def transform(path):
    T=tuple(range(9))
    for x in path:T=tuple(next_state(q,x) for q in T)
    return T
def final(q):
    a,b=divmod(q,3);return 2*int(a==2)+int(b==2)
def qrank(rows):
    piv={}
    for row in rows:
        x=list(map(Fraction,row))
        for k,v in sorted(piv.items()):
            if x[k]:
                t=x[k];x=[a-t*b for a,b in zip(x,v)]
        k=next((i for i,t in enumerate(x) if t),None)
        if k is not None:piv[k]=[v/x[k] for v in x]
    return len(piv)
def det(M):
    n=len(M);assert all(len(r)==n for r in M)
    A=[[x%P for x in row] for row in M];d=1
    for j in range(n):
        k=next((i for i in range(j,n) if A[i][j]),None)
        if k is None:return 0
        if k!=j:A[j],A[k]=A[k],A[j];d=-d
        x=A[j][j];d=d*x%P;inv=pow(x,-1,P)
        for i in range(j+1,n):
            t=A[i][j]*inv%P
            if t:
                for z in range(j+1,n):A[i][z]=(A[i][z]-t*A[j][z])%P
                A[i][j]=0
    return d%P
def formal():
    moves={k:(endpoint(v),transform(v)) for k,v in OPS.items()}
    level={(0,0,tuple(range(9)))};all_signatures=set();exact=None
    for depth in range(1,H+1):
        level={(x+delta[0],y+delta[1],tuple(Tmove[q] for q in T))
               for x,y,T in level for delta,Tmove in moves.values()}
        all_signatures |= level
        if depth==H:
            exact=3*sum(qrank([tuple(int(final(T[q])==lab) for q in range(9))
                       for X,Y,T in level if (X,Y)==(x,y) for lab in range(4)])
                       for x,y in {(X,Y) for X,Y,_ in level})
    groups=defaultdict(list)
    for x,y,T in all_signatures:
        for lab in range(4):groups[(-x,-y)].append(tuple(int(final(T[q])==lab) for q in range(9)))
    ranks={xy:qrank(rows) for xy,rows in groups.items()}
    assert len(level)==547 and len(all_signatures)==602 and exact==1887
    assert len(ranks)==121 and sum(ranks.values())*3==2052
    return ranks
def replay(block):
    target=tuple(block['target']);u,v=target[0]//2,target[1]//2
    rng=random.Random(block['seed']);indices=block['indices'];wanted=set(indices)
    assert len(indices)==len(wanted) and all(i>=0 for i in indices)
    found={}
    for i in range(max(indices,default=-1)+1):
        base=([1] if u>=0 else [-1])*(2*abs(u))+[2]*(2*v)
        path=base[:]
        distributions=((30,30,14,11,8,7),(46,46,3,3,1,1),(12,12,28,20,14,14))
        for _ in range((N-len(base))//2):
            x=rng.choices((1,2,3,4,5,6),weights=distributions[(i//307)%3],k=1)[0]
            path.extend((x,-x))
        rng.shuffle(path)
        if i in wanted:found[i]=path
    return [tuple(found[i]) for i in indices]+[tuple(p) for p in block['rare_paths']]
def verify(name):
    raw=lzma.decompress(base64.b64decode(Path(name).read_text().strip(),validate=True))
    cert=json.loads(raw)
    assert cert['schema']=='EC49CX_H10_REPLAY_CERT_V1'
    assert (cert['h'],cert['n'],cert['p'])==(H,N,P)
    upper=formal();ranks=0;moduli=[];targets=set()
    for b in cert['blocks']:
        target=tuple(b['target']);assert target[2:]==(0,0,0,0)
        assert target[:2] not in targets;targets.add(target[:2])
        rows=b['selected_suffix_rows'];r=upper[target[:2]]
        assert len(rows)==r and r==(4 if abs(target[0]//2)+target[1]//2==H else 6)
        S=[];T=[]
        for op,lab in rows:
            assert 1<=len(op)<=H and lab in range(4)
            suff=tuple(x for y in op for x in OPS[y]);assert endpoint(suff)==tuple(-x for x in target)
            S.append((suff,lab))
            T.append(tuple(int(final(transform(suff)[q])==lab) for q in range(9)))
        assert qrank(T)==r
        paths=replay(b);assert len(paths)==3*r
        assert all(len(p)==N and endpoint(p)==target for p in paths)
        M=[]
        for suff,lab in S:
            triple=[weights(p+suff) if tag(p+suff)==lab else (0,0,0) for p in paths]
            for j in range(3):M.append([x[j] for x in triple])
        d=det(M);assert d and d==b['minor_mod_p']
        moduli.append(d);ranks+=len(paths)
    assert len(targets)==121 and ranks==2052
    assert cert['cumulative_formal']==2052 and cert['exact_formal']==1887
    return {'status':'PASS','n':N,'h':H,'fibers':121,'real_paths':ranks,'nonzero_minors':121,
            'formal_exact':1887,'formal_cumulative':2052,'min_mod_p':min(moduli),'max_mod_p':max(moduli)}
if __name__=='__main__':print(json.dumps(verify(sys.argv[1] if len(sys.argv)>1 else 'EC49CX_REPLAY_CERT.json.xz.b64'),sort_keys=True))
