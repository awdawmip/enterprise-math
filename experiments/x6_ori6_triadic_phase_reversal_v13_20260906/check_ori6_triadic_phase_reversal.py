#!/usr/bin/env python3
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, product

N=6
ID=tuple(range(1,N+1))
ZERO=(0,)*N


def compose(g,h):
    """Signed permutation g after h; entries are +/- 1-based axis images."""
    out=[]
    for x in h:
        s=1 if x>0 else -1
        y=g[abs(x)-1]
        out.append(s*y)
    return tuple(out)


def power(g,n):
    out=ID
    for _ in range(n): out=compose(g,out)
    return out


def inverse(g):
    out=[None]*N
    for i,y in enumerate(g):
        s=1 if y>0 else -1
        out[abs(y)-1]=s*(i+1)
    return tuple(out)


def act(g,z):
    out=[0]*N
    for i,c in enumerate(z):
        if not c: continue
        y=g[i]
        out[abs(y)-1]+=(1 if y>0 else -1)*c
    return tuple(out)


def unit(i,s=1):
    z=[0]*N; z[i]=s; return tuple(z)


def l1(a,b):
    return sum(abs(x-y) for x,y in zip(a,b))


def perm_parity(g):
    p=[abs(x)-1 for x in g]
    inv=sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))
    return inv%2


def determinant_sign(g):
    prod=-1 if perm_parity(g) else 1
    for x in g: prod*=1 if x>0 else -1
    return prod


def pointed_event(i,j,k,beta):
    g=list(ID)
    g[i]=beta*(j+1)
    g[j]=beta*(i+1)
    g[k]=-(k+1)
    return tuple(g)


def q_twist(cycle,alpha):
    g=list(ID)
    for r,i in enumerate(cycle):
        j=cycle[(r+1)%3]
        g[i]=alpha[r]*(j+1)
    return tuple(g)


def canonical_cycle(t):
    t=tuple(t)
    return min(t[i:]+t[:i] for i in range(3))


def shortest_midpoints_len2(a,b):
    assert l1(a,b)==2
    mids=set()
    for i in range(N):
        for s in (-1,1):
            m=list(a); m[i]+=s; m=tuple(m)
            if l1(a,m)==1 and l1(m,b)==1:
                mids.add(m)
    return frozenset(mids)


def signed_cycle_type(g):
    p=[abs(x)-1 for x in g]
    eps=[1 if x>0 else -1 for x in g]
    seen=[False]*N; pos=[]; neg=[]
    for i in range(N):
        if seen[i]: continue
        cur=i; ell=0; hol=1
        while not seen[cur]:
            seen[cur]=True; ell+=1; hol*=eps[cur]; cur=p[cur]
        (pos if hol==1 else neg).append(ell)
    return tuple(sorted(pos,reverse=True)),tuple(sorted(neg,reverse=True))


# 60 pointed triads x two common-node signed involutions = 120 distinct odd frames.
contexts=[]; events=set()
for k in range(N):
    rest=[i for i in range(N) if i!=k]
    for i,j in combinations(rest,2):
        for beta in (-1,1):
            o=pointed_event(i,j,k,beta)
            contexts.append((i,j,k,beta,o)); events.add(o)
            assert power(o,2)==ID
            assert perm_parity(o)==1
            assert determinant_sign(o)==1
assert len(contexts)==120 and len(events)==120

# Exact pointed-triad ansatz classification.
ansatz=[]
i,j,k=0,1,2
for a,b,c in product((-1,1),repeat=3):
    g=list(ID); g[i]=a*(j+1); g[j]=b*(i+1); g[k]=c*(k+1); g=tuple(g)
    involution=(power(g,2)==ID)
    moves=tuple(l1(unit(t),act(g,unit(t))) for t in (i,j,k))
    synchronous=(moves==(2,2,2))
    ansatz.append((a,b,c,involution,synchronous))
assert {(a,b,c) for a,b,c,inv,sync in ansatz if inv and sync}=={(-1,-1,-1),(1,1,-1)}

# Unique common pivot for every distinct event x every signed input triad.
triadic_cases=0
for i,j,k,beta,o in contexts:
    for signs in product((-1,1),repeat=3):
        starts=(unit(i,signs[0]),unit(j,signs[1]),unit(k,signs[2]))
        targets=tuple(act(o,a) for a in starts)
        mids=tuple(shortest_midpoints_len2(a,b) for a,b in zip(starts,targets))
        assert tuple(len(x) for x in mids)==(2,2,1)
        assert set(mids[0]) & set(mids[1]) & set(mids[2]) == {ZERO}
        triadic_cases+=1
assert triadic_cases==960

# Four-twist gauge-covariant phase-reversal contexts.
twists=tuple(a for a in product((-1,1),repeat=3) if a[0]*a[1]*a[2]==-1)
cycles=tuple(sorted({canonical_cycle(p) for p in permutations(range(N),3)}))
assert len(twists)==4 and len(cycles)==40
associations=defaultdict(list)
for cyc in cycles:
    for alpha in twists:
        q=q_twist(cyc,alpha)
        assert power(q,3)==tuple(-(i+1) if i in cyc else i+1 for i in range(N))
        assert power(q,6)==ID
        for r in range(3):
            i=cyc[r]; j=cyc[(r+1)%3]; k=cyc[(r+2)%3]
            o=pointed_event(i,j,k,alpha[r])
            assert compose(compose(o,q),o)==power(q,5)
            associations[o].append((cyc,alpha,r))
assert len(associations)==120
assert Counter(len(v) for v in associations.values())=={4:120}

# Direct sign-gauge covariance of Q and O.
for alpha in twists:
    cyc=(0,1,2); q=q_twist(cyc,alpha)
    for eps in product((-1,1),repeat=3):
        gauge=list(ID)
        for r,i in enumerate(cyc): gauge[i]=eps[r]*(i+1)
        gauge=tuple(gauge)
        alpha2=tuple(eps[r]*eps[(r+1)%3]*alpha[r] for r in range(3))
        q2=q_twist(cyc,alpha2)
        assert compose(compose(gauge,q),gauge)==q2
        for r in range(3):
            i=cyc[r]; j=cyc[(r+1)%3]; k=cyc[(r+2)%3]
            o=pointed_event(i,j,k,alpha[r])
            o2=pointed_event(i,j,k,alpha2[r])
            assert compose(compose(gauge,o),gauge)==o2

# Complete B6 class and current-even conjugacy orbit.
rep=pointed_event(0,1,2,-1)
assert signed_cycle_type(rep)==((2,1,1,1),(1,))
B6=[]
for p in permutations(range(N)):
    for eps in product((-1,1),repeat=N):
        B6.append(tuple(eps[i]*(p[i]+1) for i in range(N)))
assert len(B6)==46080
centralizer=[g for g in B6 if compose(g,rep)==compose(rep,g)]
assert len(centralizer)==384
assert len(B6)//len(centralizer)==120
Rtriad=[g for g in B6 if perm_parity(g)==0]
assert len(Rtriad)==23040
even_orbit={compose(compose(h,rep),inverse(h)) for h in Rtriad}
assert even_orbit==events

# Primitive signed-direction phase partition: three 2-cycles plus six fixed directions.
signed_dirs=tuple(unit(i,s) for i in range(N) for s in (-1,1))
unseen=set(signed_dirs); lengths=[]
while unseen:
    x=next(iter(unseen)); orb=[]; y=x
    while y not in orb:
        orb.append(y); unseen.discard(y); y=act(rep,y)
    lengths.append(len(orb))
assert tuple(sorted(lengths,reverse=True))==(2,2,2,1,1,1,1,1,1)

# Canonical local D12 completion.
q=q_twist((0,1,2),(-1,-1,-1))
o=pointed_event(0,1,2,-1)
assert compose(compose(o,q),o)==power(q,5)
G={ID}; queue=deque([ID])
while queue:
    x=queue.popleft()
    for g in (q,o):
        y=compose(g,x)
        if y not in G:
            G.add(y); queue.append(y)
assert len(G)==12
pure_positive_kernel={g for g in G if tuple(abs(x) for x in g)==ID}
assert pure_positive_kernel=={ID,power(q,3)}
odd_involutions=[]; fully_participating=[]
for m in range(6):
    h=compose(power(q,m),o)
    assert power(h,2)==ID and perm_parity(h)==1
    moves=tuple(l1(unit(i),act(h,unit(i))) for i in (0,1,2))
    odd_involutions.append(h)
    if moves==(2,2,2): fully_participating.append(h)
assert len(set(odd_involutions))==6
assert len(set(fully_participating))==3

# Canonical frame factorization O = J_S P_ij.
P=list(ID); P[0]=2; P[1]=1; P=tuple(P)
J=power(q,3)
assert compose(J,P)==o

print('PASS_X6_ORI6_TRIADIC_PHASE_REVERSAL_V13')
print('pointed_triad_contexts',60)
print('distinct_odd_commonnode_frames',len(events))
print('signed_triad_path_cases',triadic_cases)
print('gauge_phase_reversal_contexts',sum(map(len,associations.values())))
print('contexts_per_distinct_odd_frame',4)
print('signed_cycle_type',signed_cycle_type(rep))
print('B6_centralizer_order',len(centralizer))
print('B6_and_Rtriad_conjugacy_class_size',len(events))
print('local_phase_reversal_group_order',len(G))
print('local_odd_involutions',len(odd_involutions))
print('triadic_commonnode_odd_involutions',len(fully_participating))
print('ori6_charge',1)
print('foundation_physical_admission_claimed',False)
