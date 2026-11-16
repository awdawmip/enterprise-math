"""Pure auxiliary finite-algebra comparison, based on the sourced V38 packets."""
import hashlib
import importlib.util
import itertools
import sys
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

src = Path(sys.argv[1])
buf = src.read_bytes()
assert hashlib.sha1(b"blob "+str(len(buf)).encode()+b"\0"+buf).hexdigest() == "328c328d76e5766261f590afa710671b0a81f0cb"
spec = importlib.util.spec_from_file_location("v38",src)
v38 = importlib.util.module_from_spec(spec)
with redirect_stdout(StringIO()):
    spec.loader.exec_module(v38)

def perm_product(g,h):
    return tuple(g[i] for i in h)

def subgroup(identity, generators, product):
    seen = {identity}
    active = [identity]
    while active:
        word = active.pop()
        for gen in generators:
            out = product(word,gen)
            if out not in seen:
                seen.add(out)
                active.append(out)
    return seen

def affine(g,h):
    x,y,k = g
    u,v,j = h
    for _ in range(k):
        u,v = -v,u
    return ((x+u)%3,(y+v)%3,(k+j)%4)

def cycle(n, xs):
    v = list(range(n))
    for i,j in zip(xs,xs[1:]+xs[:1]):
        v[i]=j
    return tuple(v)

X,Y = (0,0,1),(2,1,1)
A,B = affine(X,X),affine(Y,Y)
old = subgroup((0,0,0), [A,B], affine)
new = subgroup((0,0,0), [X,Y], affine)
assert (len(old),len(new)) == (6,36)
assert [sum(affine(g,g)==t for g in new) for t in (A,B)] == [2,2]
assert all(affine(affine(a,b),c) == affine(a,affine(b,c))
           for a,b,c in itertools.product(new,repeat=3))

# Actual three transport slots use zero-based labels.
ra = (1,3,2,4)
rb = (0,3,1,4)
xp,yp = cycle(5,ra),cycle(5,rb)
ap,bp = perm_product(xp,xp),perm_product(yp,yp)
assert ap[:3] == v38.hol(v38.A) and bp[:3] == v38.hol(v38.B)
assert ap[3:] == bp[3:] == (4,3)
assert len(subgroup(tuple(range(5)),[ap,bp],perm_product)) == 6
for n in (3,4):
    permutations = itertools.permutations(range(n))
    possible = {perm_product(h,h) for h in permutations}
    assert not any(g[:3] == ap[:3] for g in possible)

# V38 family readout, path order equals reverse composition for forward maps.
s3 = list(itertools.permutations(range(3)))
identity = tuple(range(3))
def inv(g):
    return tuple(g.index(i) for i in identity)

def signatures(gs,k):
    out=[]
    for length in range(1,k+1):
        for word in itertools.product(gs,repeat=length):
            val=identity
            for g in word:
                val=perm_product(g,val)
            out.append(sum(v==i for i,v in enumerate(val)))
    return tuple(out)
def orbit(gs):
    return min(tuple(perm_product(q,perm_product(g,inv(q))) for g in gs) for q in s3)
for k in (3,4):
    sig2,sig3,orbits = set(),{},set()
    for tup in itertools.product(s3,repeat=k):
        sig2.add(signatures(tup,2))
        key=signatures(tup,3)
        canonical=orbit(tup)
        orbits.add(canonical)
        assert sig3.setdefault(key,canonical) == canonical
    print(k,len(sig2),len(sig3),len(orbits))
C=v38.seq_hol((v38.A,v38.B,v38.Ai,v38.Bi))
base=(v38.hol(v38.A),v38.hol(v38.B))
assert signatures(base+(C,),2)==signatures(base+(inv(C),),2)
assert signatures(base+(C,),3)!=signatures(base+(inv(C),),3)
print("Group of order 36, five-slot roots and sharp three-packet observation: PASS")
