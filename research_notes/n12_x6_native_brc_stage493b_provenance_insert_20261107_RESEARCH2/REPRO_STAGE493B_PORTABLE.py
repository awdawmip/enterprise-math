"""Stage493-B independent standard-library replay (exact integers)."""
from collections import Counter,defaultdict
from itertools import product
D='ABCDEFGHIJKL'; alphabet='ABGH'
P='ABGABA'; W='GH'
V={a: tuple((1 if i==j else 0) for j in range(6)) for i,a in enumerate(D[:6])}
V.update({a:tuple((-1 if i==j else 0) for j in range(6)) for i,a in enumerate(D[6:])})
E=tuple(a+b for a in D for b in D)

def q(h): return P+W+'A'+h+'A'
def obs(t):
    counts=Counter(t[i:i+2] for i in range(len(t)-1))
    return (len(t),tuple(sum(V[c][i] for c in t) for i in range(6)),tuple(counts[e] for e in E))
def put(t,j,z): return t[:j-1]+z+t[j-1:]
def setj(t,j,z): return t[:j-1]+z+t[j:]
def tri(t,j): return t[j-2:j+1]
def ibl(t): return put(t,len(t),'C')
def diff(a,b):
    aa,bb=Counter(a[i:i+2] for i in range(len(a)-1)),Counter(b[i:i+2] for i in range(len(b)-1))
    return {e:aa[e]-bb[e] for e in E if aa[e]!=bb[e]}

# Exact two-step distinguishing witness, even though the original site-11 triple matches.
a,b=q('AAAABAA'),q('AAABAAA')
assert obs(a)==obs(b) and tri(a,11)==tri(b,11)=='AAA'
assert all(obs(setj(a,11,z))==obs(setj(b,11,z)) for z in D)
ai,bi=ibl(a),ibl(b)
assert obs(ai)==obs(bi) and tri(ai,12)=='AAA' and tri(bi,12)=='AAB'
as_,bs=setj(ai,12,'I'),setj(bi,12,'I')
assert diff(as_,bs)=={'AA':-1,'AB':1,'IA':1,'IB':-1}

# Exact signed interaction for one insertion followed by edit of its right neighbor.
nonzero=0
for a,b,c,z,x in product(alphabet,repeat=5):
    old=a+b+c; ins=a+z+b+c; both=a+z+x+c
    expected=Counter()
    for e,n in [(a+b,-1),(b+c,-1),(a+z,1),(z+x,1),(x+c,1)]: expected[e]+=n
    assert diff(both,old)=={e:n for e,n in expected.items() if n}
    inter=Counter()
    for e,n in [(z+x,1),(z+b,-1),(a+x,-1),(a+b,1)]:inter[e]+=n
    nonzero+=any(inter.values())
assert nonzero==576

# H in alphabet^7: compare base fibers, triples, and ALL twelve replacement responses.
groups=defaultdict(list)
for h in map(''.join,product(alphabet,repeat=7)):
    t=q(h);u=ibl(t)
    groups[(obs(t),obs(u),tri(u,12))].append(h)
base=set();response_to_triple={}
for (s,t,trip),histories in groups.items():
    base.add((s,t))
    u=ibl(q(histories[0]))
    response=tuple(obs(setj(u,12,z)) for z in D)
    key=(s,t,response)
    assert key not in response_to_triple or response_to_triple[key]==trip
    response_to_triple[key]=trip
    if len(histories)>1:
        u2=ibl(q(histories[-1]))
        assert tuple(obs(setj(u2,12,z)) for z in D)==response
assert len(groups)==14752 and len(response_to_triple)==14752
assert len(base)==5219 and sum(map(len,groups.values()))==16384
print('WITNESS initial-observer equal, initial triple AAA, INSERT-before-last(C) equal, then SET_FROM_END(6,I) distinguishes')
print('WITNESS signed-edge difference',diff(as_,bs))
print('LOCAL_INTERACTION verified_cases=1024 nonzero=576')
print('FINITE_CENSUS 4^7=16384 base_fibers=5219 refined_classes=14752 full_12_response_classes=14752')
print('EXACT integers; all assertions passed')
