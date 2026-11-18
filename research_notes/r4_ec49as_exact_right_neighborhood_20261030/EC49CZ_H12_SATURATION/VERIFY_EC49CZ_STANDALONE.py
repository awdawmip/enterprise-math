#!/usr/bin/env python3
"""Exact h=12 signed-X6 positive BRC certificate replay (169 minors). Stdlib only."""
import base64,json,lzma,random,sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
P=1000003;H=12;N=32
OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3)}
W=((2,3,3,2,1,1),(3,2,3,2,1,1))
def endpoint(path):
    z=[0]*6
    for x in path:
        assert type(x)==int and 1<=abs(x)<=6
        z[abs(x)-1]+=1 if x>0 else -1
    return tuple(z)
def tag(path):
    A=any(a==1 and b==2 for a,b in zip(path,path[1:]))
    B=any(a==2 and b==1 for a,b in zip(path,path[1:]))
    return 2*int(A)+int(B)
def weights(path):
    a=b=1
    for x in path:
        if x>0: a*=W[0][x-1]; b*=W[1][x-1]
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
    a,b=divmod(q,3)
    return 2*int(a==2)+int(b==2)
def qrank(rows):
    piv={}
    for row in rows:
        x=list(map(Fraction,row))
        for k,v in sorted(piv.items()):
            if x[k]:
                t=x[k]; x=[a-t*b for a,b in zip(x,v)]
        k=next((i for i,t in enumerate(x) if t),None)
        if k is not None: piv[k]=[v/x[k] for v in x]
    return len(piv)
def det(M):
    n=len(M); assert all(len(r)==n for r in M)
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
        for lab in range(4):
            groups[(-x,-y)].append(tuple(int(final(T[q])==lab) for q in range(9)))
    ranks={xy:qrank(rows) for xy,rows in groups.items()}
    assert len(level)==788 and len(all_signatures)==866 and exact==2658
    assert len(ranks)==169 and sum(ranks.values())*3==2892
    return ranks
def boundary_path(u,v,label,variant):
    assert u>0 and v>0 and u+v==H and 0<=label<4 and variant in (0,1,2)
    A=[1]*(2*u);B=[2]*(2*v)
    one1=[1,-1] if variant==1 else []
    one2=[2,-2] if variant==2 else []
    filler=[3,-3]*(4-(variant!=0))
    if label==0:s=A+one1+filler+B+one2
    elif label==1:s=B[:-1]+one2+B[-1:]+A+one1+filler
    elif label==2:s=A[:-1]+one1+A[-1:]+B+one2+filler
    else:s=A[:-2]+one1+A[-2:-1]+B[:-1]+[1,2]+one2+filler
    assert len(s)==N
    return tuple(s)
def replay(block):
    u,v=block['t'][0]//2,block['t'][1]//2
    if block.get('f')==1:
        assert u>0 and v>0 and u+v==H
        return [boundary_path(u,v,label,variant) for label in range(4) for variant in (0,1,2)]
    indices=block['i']
    assert len(indices)==len(set(indices)) and all(i>=0 for i in indices)
    rng=random.Random(block['seed']);wanted=set(indices);found={}
    distributions=((30,30,14,11,8,7),(46,46,3,3,1,1),(12,12,28,20,14,14))
    for i in range(max(indices,default=-1)+1):
        base=([1] if u>=0 else [-1])*(2*abs(u))+[2]*(2*v)
        path=base[:]
        for _ in range((N-len(base))//2):
            ax=rng.choices((1,2,3,4,5,6),weights=distributions[(i//307)%3],k=1)[0]
            path.extend((ax,-ax))
        rng.shuffle(path)
        if i in wanted:found[i]=tuple(path)
    return [found[i] for i in indices]+[tuple(p) for p in block.get('r',[])]
def verify(name):
    raw=lzma.decompress(base64.b64decode(Path(name).read_text().strip(),validate=True))
    cert=json.loads(raw)
    assert cert['schema']=='EC49CZ_H12_REPLAY_V1'
    assert (cert['h'],cert['n'],cert['p'])==(H,N,P)
    upper=formal()
    assert cert['upper_exact']==2658 and cert['upper_cumulative']==2892
    total=0;moduli=[];targets=set()
    for b in cert['blocks']:
        target=(b['t'][0],b['t'][1],0,0,0,0)
        assert b['t'][0]%2==0 and b['t'][1]%2==0 and b['t'][1]>=0
        assert target[:2] not in targets;targets.add(target[:2])
        rows=b['w'];r=upper[target[:2]]
        assert len(rows)==r and r==(4 if abs(target[0]//2)+target[1]//2==H else 6)
        suffix=[];T=[]
        for op,lab in rows:
            assert 1<=len(op)<=H and lab in range(4)
            suff=tuple(x for y in op for x in OPS[y])
            assert endpoint(suff)==tuple(-x for x in target)
            suffix.append((suff,lab))
            T.append(tuple(int(final(transform(suff)[q])==lab) for q in range(9)))
        assert qrank(T)==r
        paths=replay(b);assert len(paths)==3*r
        assert all(len(p)==N and endpoint(p)==target for p in paths)
        M=[]
        for suff,lab in suffix:
            triple=[weights(p+suff) if tag(p+suff)==lab else (0,0,0) for p in paths]
            for j in range(3):M.append([x[j] for x in triple])
        d=det(M);assert d and d==b['d'],(target,d,b['d'])
        moduli.append(d);total+=len(paths)
    assert len(targets)==169 and total==2892
    return {'status':'PASS','n':N,'h':H,'fibers':169,'real_paths':total,'nonzero_minors':169,
            'formal_exact':2658,'formal_cumulative':2892,'signatures_exact':788,
            'signatures_cumulative':866,'min_mod_p':min(moduli),'max_mod_p':max(moduli)}
if __name__=='__main__':
    print(json.dumps(verify(sys.argv[1] if len(sys.argv)>1 else 'EC49CZ_REPLAY_CERT.json.xz.b64'),sort_keys=True))
