#!/usr/bin/env python3
"""R176 exact standalone audit of the proposed native Affine/EffectHistogram bridge.

Matches the public interface laws of enterprise_math.brc_transport.Affine.then,
EffectHistogram.alternatives/then; no claim of importing installed native module.
All arithmetic is integer/Fraction. This is a finite reference checker.
"""
from fractions import Fraction as Q
from itertools import product
from collections import defaultdict
import json

D=2 # first two axes of the native six-axis signed primitive alphabet; algebra is for general d>=1
DIRS=[(1,0),(-1,0),(0,1),(0,-1)]
# All self-maps of {0,1}; order matters, multiplication means FIRST left THEN right.
M=list(product(range(2),repeat=2))
UNIT=(0,1)
mi={m:i for i,m in enumerate(M)}
N=2*D+len(M)
ZERO=(0,)*D

def mul(a,b):return (b[a[0]],b[a[1]])
def plus(a,b):return tuple(x+y for x,y in zip(a,b))

def summary(word):
    pos=ZERO; cum=ZERO
    for v in word:
        pos=plus(pos,v)
        cum=plus(cum,pos)
    return len(word),pos,cum

def identity_matrix(n):return tuple(tuple(Q(i==j) for j in range(n)) for i in range(n))
def affine(m,word):
    n,disp,prefix=summary(word)
    a=[list(r) for r in identity_matrix(N)]
    for k in range(D):a[D+k][k]=Q(n)
    for i in range(len(M)):
        for j in range(len(M)):a[2*D+i][2*D+j]=Q(0)
    for u in M:a[2*D+mi[mul(u,m)]][2*D+mi[u]]=Q(1)
    b=tuple(map(Q, disp+prefix+(0,)*len(M)))
    return (tuple(map(tuple,a)),b)

def matmul(a,b):
    return tuple(tuple(sum((x*b[k][j] for k,x in enumerate(row)),Q(0)) for j in range(len(b[0]))) for row in a)
def matvec(a,v):return tuple(sum((x*y for x,y in zip(row,v)),Q(0)) for row in a)
def then(a,b):
    # self THEN later -> linear=later.linear @ self.linear
    ap,bp=a; aq,bq=b
    return (matmul(aq,ap), plus(matvec(aq,bp),bq))
def initial():return (Q(0),)*(2*D)+tuple(Q(x==UNIT) for x in M)
def act(a,x):return plus(matvec(a[0],x),a[1])
def extract(a):
    matrix,b=a
    n=matrix[D][0]
    assert n.denominator==1 and n>=0
    disp=tuple(int(x) for x in b[:D]); prefix=tuple(int(x) for x in b[D:2*D])
    # R_m sends the unit-basis column to m-basis column.
    col=[matrix[2*D+i][2*D+mi[UNIT]] for i in range(len(M))]
    assert col.count(Q(1))==1 and col.count(Q(0))==len(M)-1
    return M[col.index(Q(1))],int(n),disp,prefix

# a family is a list of (start_port, end_port, positive_weight, label, word, count).
def raw_serial(a,b):
    return [(i,k,u*v,mul(m,n),p+q,c*d)
            for i,j,u,m,p,c in a for j2,k,v,n,q,d in b if j==j2]

def histogram(family):
    h=defaultdict(int)
    for i,j,w,m,word,c in family:
        assert w>0 and c>=0
        if c:h[i,j,Q(w),affine(m,word)]+=c
    return dict(h)

def hist_serial(h,g):
    z=defaultdict(int)
    for (i,j,u,alpha),c in h.items():
        for (j2,k,v,beta),d in g.items():
            if j==j2:z[i,k,u*v,then(alpha,beta)]+=c*d
    return {k:v for k,v in z.items() if v}

def moments_hist(h):
    r=defaultdict(lambda: [Q(0),Q(0),[Q(0)]*D,[Q(0)]*D])
    for (i,j,w,a),count in h.items():
        m,n,dis,pre=extract(a)
        t=r[i,j,m];wc=w*count
        t[0]+=wc;t[1]+=wc*n
        for k in range(D):t[2][k]+=wc*dis[k];t[3][k]+=wc*pre[k]
    return {k:(v[0],v[1],tuple(v[2]),tuple(v[3])) for k,v in r.items() if any([v[0],v[1],*v[2],*v[3]])}

def moments_raw(h):
    r=defaultdict(lambda:[Q(0),Q(0),[Q(0)]*D,[Q(0)]*D])
    for i,j,w,m,p,c in h:
        n,dis,pre=summary(p)
        t=r[i,j,m];wc=Q(w)*c
        t[0]+=wc;t[1]+=wc*n
        for k in range(D):t[2][k]+=wc*dis[k];t[3][k]+=wc*pre[k]
    return {k:(v[0],v[1],tuple(v[2]),tuple(v[3])) for k,v in r.items() if any([v[0],v[1],*v[2],*v[3]])}

def moments_product(a,b):
    out=defaultdict(lambda:[Q(0),Q(0),[Q(0)]*D,[Q(0)]*D])
    for (i,j,m),(A,L,B,C) in a.items():
        for (j2,k,n),(a,l,bb,cc) in b.items():
            if j!=j2:continue
            z=out[i,k,mul(m,n)]
            z[0]+=A*a;z[1]+=L*a+A*l
            for h in range(D):
                z[2][h]+=B[h]*a+A*bb[h]
                z[3][h]+=C[h]*a+A*cc[h]+B[h]*l
    return {k:(v[0],v[1],tuple(v[2]),tuple(v[3])) for k,v in out.items() if any([v[0],v[1],*v[2],*v[3]])}

def optional_native_probe():
    """When executed in the EM repository, exercise its actual imported classes."""
    try:
        from enterprise_math.brc_transport import Affine, EffectHistogram
    except ImportError:
        return {"native_module_imported": False, "native_cases": 0}
    samples=[(),((1,0),),((1,0),(-1,0)),((0,-1),(0,1),(1,0))]
    checked=0
    for m,n in product(M,repeat=2):
        for p in samples:
            for q in samples:
                aa=affine(m,p); bb=affine(n,q)
                left=EffectHistogram.from_terms(N,[(Q(2,3),Affine(*aa),2)])
                right=EffectHistogram.from_terms(N,[(Q(3,5),Affine(*bb),3)])
                got=left.then(right)
                exp=Affine(*affine(mul(m,n),p+q))
                assert got.entries==((Q(2,5),exp,6),)
                assert left.alternatives(left).entries==((Q(2,3),Affine(*aa),4),)
                checked+=1
    return {"native_module_imported": True, "native_cases": checked}

def exhaust():
    checks={'associativity_monoid':0,'path_action':0,'composition_label':0,'raw_vs_hist_serial':0,'moment_vs_serial':0,'moment_vs_raw':0,'origin_alias_witness':0,'signed_formal':0}
    for a,b,c in product(M,repeat=3):
        assert mul(mul(a,b),c)==mul(a,mul(b,c));checks['associativity_monoid']+=1
    words=[()]+[(x,) for x in DIRS]+list(product(DIRS,repeat=2))
    for p,q in product(words,repeat=2):
        lhs=then(affine(UNIT,p),affine(UNIT,q))
        assert lhs==affine(UNIT,p+q)
        checks['path_action']+=1
    for a,b in product(M,repeat=2):
        for p,q in [((),()),(((1,0),),()),(((1,0),),((-1,0),))]:
            assert then(affine(a,p),affine(b,q))==affine(mul(a,b),p+q)
            checks['composition_label']+=1
    assert mul(M[0],M[-1])!=mul(M[-1],M[0]) # noncommutative
    # Positive rational-weight families, 2-port, varying labels, axis directions and multiplicities.
    samples=[]
    for k in range(12):
        samples.append([(0,1,Q(1+k%3,1+(k%2)),M[k%4],words[(k*3)%len(words)],1+(k%2)),
                        (1,0,Q(1+(k%4),3),M[(k+1)%4],words[(k*5+1)%len(words)],2),
                        (0,0,Q(2+k%3,5),M[(k+2)%4],words[(k*2+2)%len(words)],1)])
    for F,G in product(samples,repeat=2):
        lhs=histogram(raw_serial(F,G));rhs=hist_serial(histogram(F),histogram(G))
        assert lhs==rhs;checks['raw_vs_hist_serial']+=1
        assert moments_raw(raw_serial(F,G))==moments_hist(rhs);checks['moment_vs_raw']+=1
        assert moments_hist(rhs)==moments_product(moments_hist(histogram(F)),moments_hist(histogram(G)))
        checks['moment_vs_serial']+=1
    # One-point evaluate at zero conflates empty walk and a nonempty null-prefix-integral walk.
    loop=((1,0),(-1,0),(-1,0),(1,0))
    assert summary(loop)==(4,(0,0),(0,0))
    a=affine(UNIT,());b=affine(UNIT,loop)
    assert act(a,initial())==act(b,initial())
    assert a!=b
    lead=affine(UNIT,((1,0),))
    assert act(then(lead,a),initial())!=act(then(lead,b),initial())
    checks['origin_alias_witness']=1
    # Signed formal completion: positive and negative parts remain distinct in the native positive carrier.
    p=[(0,0,Q(1),UNIT,((1,0),),1)]
    q=[(0,0,Q(1),UNIT,((-1,0),),1)]
    x=moments_hist(histogram(p));y=moments_hist(histogram(q))
    assert x!=y and moments_hist(histogram(p+q))!=x
    checks['signed_formal']=1
    return checks

if __name__=='__main__':
    counts=exhaust()
    native=optional_native_probe()
    print(json.dumps({'status':'R176_EXACT_BRIDGE_PASS','arithmetic':'Fraction', 'ambient_axes':6,
      'tested_axes':2,'monoid':'full transformations on two elements (4, noncommutative)',
      'model':'independent exact reference for native Affine/EffectHistogram interface laws',
      **native,'checks':counts},indent=2))
