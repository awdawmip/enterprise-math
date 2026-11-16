#!/usr/bin/env python3
"""R607: exact native signed-X6 path-composition and joint residual test.
Only integer combinatorics. No physical heartbeat or R462 K/J operator is executed.
"""
from itertools import product

DIM=6
PAIRS=tuple((i,j) for i in range(DIM) for j in range(i+1,DIM))
LETTERS=tuple((i,s) for i in range(DIM) for s in (-1,1))
ZERO_D=(0,)*DIM
ZERO_A=(0,)*len(PAIRS)

def step(letter):
    i,s=letter
    v=[0]*DIM
    v[i]=s
    return tuple(v),ZERO_A

def wedge(v,w):
    return tuple(v[i]*w[j]-v[j]*w[i] for i,j in PAIRS)

def mul(x,y):
    d,a=x; e,b=y
    return (tuple(d[i]+e[i] for i in range(DIM)),
            tuple(a[t]+b[t]+q for t,q in enumerate(wedge(d,e))))

def direct(word):
    vs=[step(letter)[0] for letter in word]
    d=tuple(sum(v[i] for v in vs) for i in range(DIM))
    a=tuple(sum(v[i]*w[j]-v[j]*w[i] for n,v in enumerate(vs) for w in vs[n+1:])
            for i,j in PAIRS)
    return d,a

def eval_word(word):
    result=(ZERO_D,ZERO_A)
    for letter in word:
        result=mul(result,step(letter))
    return result

def base_path(d):
    return tuple((i,1 if d[i]>0 else -1) for i in range(DIM) for _ in range(abs(d[i])))

def loop(i,j,positive=True):
    if positive:
        return ((i,1),(j,1),(i,-1),(j,-1))
    return ((j,1),(i,1),(j,-1),(i,-1))

def lift(d,a):
    assert len(d)==DIM and len(a)==len(PAIRS)
    assert all((a[t]-d[i]*d[j])%2==0 for t,(i,j) in enumerate(PAIRS))
    word=list(base_path(d))
    b=eval_word(word)[1]
    for t,(i,j) in enumerate(PAIRS):
        n=(a[t]-b[t])//2
        word.extend(loop(i,j,n>0)*abs(n))
    return tuple(word)

checked=0
for length in range(5):
    for word in product(LETTERS,repeat=length):
        d,a=direct(word)
        assert eval_word(word)==(d,a)
        assert all((a[t]-d[i]*d[j])%2==0 for t,(i,j) in enumerate(PAIRS))
        # Inverse is reverse ordered native signed steps.
        inv=tuple((i,-s) for i,s in reversed(word))
        assert mul((d,a),eval_word(inv))==(ZERO_D,ZERO_A)
        checked+=1

for t,(i,j) in enumerate(PAIRS):
    for sign in (1,-1):
        d,a=eval_word(loop(i,j,sign==1))
        assert d==ZERO_D
        assert all(x==(sign*2 if n==t else 0) for n,x in enumerate(a))

# Exhaust an explicit 729-point endpoint grid; test each canonical carrier and
# three independent generators at each endpoint (positive and negative).
endpoints=0
lifts=0
for d in product((-1,0,1),repeat=DIM):
    b=eval_word(base_path(d))[1]
    assert eval_word(lift(d,b))==(d,b)
    lifts+=1
    for t in range(3):
        for s in (-1,1):
            target=list(b);target[t]+=2*s
            assert eval_word(lift(d,tuple(target)))==(d,tuple(target))
            lifts+=1
    endpoints+=1

# Minimal 2-step displacement collision: endpoint same but A12 differs.
p=((0,1),(1,1));q=((1,1),(0,1))
dp,ap=eval_word(p);dq,aq=eval_word(q)
assert dp==dq and ap[0]==1 and aq[0]==-1
# Exact prefix/suffix stability of distinguishability for all |u|,|v|<=2.
shortwords=[()] + [(x,) for x in LETTERS] + list(product(LETTERS,repeat=2))
context_tests=0
for left in shortwords:
    for right in shortwords:
        lp=eval_word(left+p+right)
        lq=eval_word(left+q+right)
        assert lp[0]==lq[0] and lp[1][0]-lq[1][0]==2
        context_tests+=1

print('R607_WORDS_DIRECT_AND_COMPOSITION_PASS',checked)
print('R607_PARITY_AND_INVERSES_PASS',checked)
print('R607_COMMUTATOR_BASIS_PASS',len(PAIRS)*2)
print('R607_REACHABLE_ENDPOINTS_AND_LIFTS_PASS',endpoints,lifts)
print('R607_TWO_SIDED_CONTEXT_WITNESS_PASS',context_tests)
print('R607_ALL_EXACT_CERTIFICATES_PASS')
