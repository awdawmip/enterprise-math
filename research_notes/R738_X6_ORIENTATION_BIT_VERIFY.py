"""R738 reproducible exact finite BRC coordinate-carrier certificate. Python 3 stdlib."""
from collections import Counter,defaultdict
from itertools import permutations,combinations,product

AX=(0,1,2)

def parity(a):
    return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))

def word(pattern,q,axes=AX):
    seen={i:0 for i in axes}; out=[]
    for i in pattern:
        s=q[axes.index(i)]*(-1 if seen[i] else 1)
        seen[i]+=1;out.append((i,s))
    assert all(v==2 for v in seen.values())
    return tuple(out)

def obs(w):
    a=tuple(sorted(set(i for i,s in w))); x={i:0 for i in a}
    q={};first=[];j={pair:0 for pair in combinations(a,2)}
    for i,s in w:
        if i not in q:q[i]=s;first.append(i)
        for u,v in j:
            if i==v:j[u,v]+=x[u]*s
        x[i]+=s
    assert all(v==0 for v in x.values())
    return tuple(q[i] for i in a),tuple(j[p] for p in combinations(a,2)),parity([a.index(i) for i in first])

# Each selected native axis occurs twice, in opposite signs. No adjacent inverse.
patterns=sorted(set(permutations((0,0,1,1,2,2))))
nb=[p for p in patterns if all(p[k]!=p[k-1] for k in range(1,6))]
assert len(patterns)==90 and len(nb)==30
reps=[''.join(map(str,p)) for p in nb if tuple(dict.fromkeys(p))==AX]
assert reps==['010212','012012','012021','012102','012120']
allfibers=defaultdict(list)
for q in product((-1,1),repeat=3):
    f=defaultdict(list)
    for p in nb:
        w=word(p,q);Q,J,eps=obs(w)
        assert Q==q
        f[J].append((w,eps));allfibers[(Q,J)].append((w,eps))
    assert len(f)==24 and Counter(map(len,f.values()))=={1:18,2:6}
    assert all(len({z for w,z in fs})==len(fs) for fs in f.values())
assert len(allfibers)==192 and Counter(map(len,allfibers.values()))=={1:144,2:48}
assert len({(Q,J,z) for (Q,J),fs in allfibers.items() for w,z in fs})==240

# Exact S6 orientation-line transport with source and destination three-axis charts.
checks=0
for axes in combinations(range(6),3):
    for rep in reps:
        w=word(tuple(axes[int(c)] for c in rep),(1,1,1),axes)
        oldeps=obs(w)[2]
        for g in permutations(range(6)):
            mapped=tuple((g[i],s) for i,s in w)
            dest=sorted(g[i] for i in axes)
            twist=parity([dest.index(g[i]) for i in axes])
            assert obs(mapped)[2]==twist*oldeps
            checks+=1
assert checks==72000

# A genuinely invariant single-bit/scalar observer cannot split the
# double fiber swapped by the axis relabeling 1 <-> 2.
a=word((0,1,2,0,2,1),(1,1,1))
b=word((0,2,1,0,1,2),(1,1,1))
assert obs(a)[:2]==obs(b)[:2] and obs(a)[2]!=obs(b)[2]
assert tuple((2 if i==1 else 1 if i==2 else i,s) for i,s in a)==b
print('R738_X6_ORIENTATION_BIT_EXACT_PASS',len(nb)*8,len(allfibers),checks)
