"""PREFIX-471: exact integer support checker, positive-multiplicity X6 gate model.
Tests automaton Parikh image, independent composition-feasibility formula,
normal-state bijections, and ordered-word enumeration for n<=4.
"""
from collections import Counter
from math import comb

GATES = {'aa':(1,1), 'aA':(1,2), 'ab':(1,3), 'AB':(2,4),
         'aba':(1,3,1), 'aAa':(1,2,1), 'aaa':(1,1,1)}

def obs(c):
    y = tuple(c[1+2*i]-c[2+2*i] for i in range(5))
    p = tuple(min(c[1+2*i],c[2+2*i]) for i in range(5))
    return (c[0],)+y+(p[1]+2*p[3]+p[4],p[2]+p[4])

def norm(f,w):
    s,*tail=f
    y=tail[:5]; A,C=tail[5:]
    r=max(s-1,0); h=Counter(w)
    d=tuple(y[i]-r*(h[1+2*i]-h[2+2*i]) for i in range(5))
    L=tuple(max(0,r*h[1+2*i]-max(0,y[i]),
                   r*h[2+2*i]-max(0,-y[i])) for i in range(5))
    return (s,)+d+(A-L[1]-2*L[3]-L[4],C-L[2]-L[4])

def qstep(q,a,w):
    t=w[:q]+(a,)
    for j in range(len(w),0,-1):
        if t[-j:]==w[:j]: return j
    return 0

def layers(w,N):
    state={((0,)*11,0)}
    for n in range(N+1):
        yield state
        out=set()
        for c,q in state:
            for a in range(1,11):
                v=list(c);v[a]+=1;out.add((tuple(v),qstep(q,a,w)))
            if n==0 or q==len(w):
                v=list(c);v[0]+=1;out.add((tuple(v),0))
        state=out

def weak(n,width=11):
    if width==1:
        yield (n,)
    else:
        for a in range(n+1):
            for rest in weak(n-a,width-1):yield (a,)+rest

def K(n):
    if n<0:return 0
    num=(1,2,3,4,2)
    return sum(v*comb(n-j+7,7) for j,v in enumerate(num) if n>=j)

def B(n,k):
    return K(n)+sum(K(n-1-(k+1)*r) for r in range(n//(k+1)+1))

def ordered_counts(n,w):
    paths=[()]
    for _ in range(n):
        nxt=[]
        for p in paths:
            nxt.extend(p+(a,) for a in range(1,11))
            if not p or p[-len(w):]==w:
                nxt.append(p+(0,))
        paths=nxt
    return {tuple(p.count(i) for i in range(11)) for p in paths}

def verify():
    normals={}
    for name,w in GATES.items():
        h=Counter(w)
        seq=[]
        for n,states in enumerate(layers(w,7)):
            counts={c for c,q in states}
            feasible={c for c in weak(n) if c[0]==0 or
                      all(c[a]>=(c[0]-1)*v for a,v in h.items())}
            assert counts==feasible,(name,n,'Parikh')
            F={obs(c) for c in counts}
            Z={norm(f,w) for f in F}
            assert len(F)==len(Z)==B(n,len(w)),(name,n,'series')
            for c in counts:
                z=norm(obs(c),w)
                r=max(c[0]-1,0)
                d=z[1:6]
                rest=n-c[0]-r*len(w)-sum(map(abs,d))
                assert rest>=0 and rest%2==0
            if n<=4:
                assert ordered_counts(n,w)==counts,(name,n,'ordered')
            seq.append(Z)
        normals[name]=seq
        print('GATE',name,'k',len(w),'B7',len(seq[7]))
    for names in (('aa','aA','ab','AB'),('aba','aAa','aaa')):
        assert all(normals[t]==normals[names[0]] for t in names[1:])
        print('NORMAL_BIJECTION',names,'n=0..7 PASS')
    aa={obs(c) for c,q in list(layers(GATES['aa'],4))[4]}
    aA={obs(c) for c,q in list(layers(GATES['aA'],4))[4]}
    witness=(2,2,0,0,0,0,0,0)
    assert witness in aa and witness not in aA and len(aa)==len(aA)==933
    print('RAW_SUPPORT_DIFF',witness,'n4',len(aa),len(aA))
    for k in (2,3):
        print('COEFFICIENTS',k,','.join(str(B(n,k)) for n in range(11)))
    print('ALL_CHECKS_PASS')

if __name__=='__main__': verify()
