"""Stage491-B portable exact oracle; Python 3 stdlib, no external I/O."""
from collections import Counter, defaultdict
from itertools import product
D, S, T, W = 'ABCDEFGHIJKL', 'ABGH', 'ABGABA', 'GH'

def Q(h): return T+W+'A'+h+'A'
def E(q): return tuple(sorted(Counter(zip(q,q[1:])).items()))
def V(q):
    z=[0]*6
    for a in q:
        i=D.index(a); z[i%6] += 1 if i<6 else -1
    return tuple(z)
def O(q): return len(q),V(q),E(q)
def tau(q,j): return q[j-2:j+1]
def base(q): return E(q),q[-2]
def key(q,d=5,b=1):
    n=len(q); return base(q),tuple(tau(q,n+t-d) for t in range(b+1))
def edited(q,pre,z,d=5):
    q+=pre; j=len(q)-d
    assert 1<j<len(q)
    return O(q[:j-1]+z+q[j:])
def scan(u):
    groups=defaultdict(list)
    for w in product(S,repeat=u):
        h=''.join(w);groups[key(Q(h))].append(h)
    return groups

x,y=Q('AAAABA'),Q('AAABAA')
assert base(x)==base(y) and O(x)==O(y)
assert all(tau(x,j)==tau(y,j) for j in (10,11))
assert edited(x,'','I')==edited(y,'','I')
assert O(x+'C')==O(y+'C')
assert edited(x,'C','I')!=edited(y,'C','I')
g6=scan(6);g7=scan(7)
assert (len(g6),len(g7))==(4096,15952)
nontrivial=[g for g in g7.values() if len(g)>1]
assert len(nontrivial)==432
checks=0
for g in nontrivial:
    for h in g[1:]:
        for pre in ('','C'):
            for z in D:
                assert edited(Q(g[0]),pre,z)==edited(Q(h),pre,z)
                checks+=1
assert checks==10368
# Complete coupled Q trace: APPEND any of 12, POP<=1, moving SET<=1.
# POP before SET forbids subsequent SET in this bounded subgrammar.
a,b=map(Q,nontrivial[0][:2]); stack=[(a,b,0,0,0,False)]; seen=set()
while stack:
    a,b,p,ap,s,locked=stack.pop(); t=(a,b,p,ap,s,locked)
    if t in seen: continue
    seen.add(t);assert O(a)==O(b)
    if ap<1:
        for z in D: stack.append((a+z,b+z,p,ap+1,s,locked))
    if p<1 and len(a)>1:
        stack.append((a[:-1],b[:-1],p+1,ap,s,locked or s==0))
    if s==0 and not locked:
        j=len(a)-5
        if 1<j<len(a):
            for z in D:stack.append((a[:j-1]+z+a[j:],b[:j-1]+z+b[j:],p,ap,1,locked))
assert len(seen)==481
print('PASS; u6 classes=4096/4096; u7 classes=15952/16384; nontrivial classes=432; SET comparisons=10368; Q paired trace states=481')
print('strict witness: H1=AAAABA H2=AAABAA; APPEND(C), SET(end-5,I) distinguishes; zero-append SET does not')
