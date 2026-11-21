"""X6 C12 / S6 stabilizer and fiber reflection checks (integer exact)."""
import itertools, json
E=[]
for k in range(6):
    a=[0]*6; a[k%3]=1 if k<3 else -1; E.append(tuple(a))
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
V=[v for k in range(6) for v in (E[k],add(E[k],E[(k+1)%6]))]
assert len(set(V))==12
assert all(sum(abs(y-x) for x,y in zip(V[q],V[(q+1)%12]))==1 for q in range(12))
stab=[]
for p in itertools.permutations(range(6)):
    W=[]
    for v in V:
        z=[0]*6
        for i,x in enumerate(v):z[p[i]]=x
        W.append(tuple(z))
    if set(W)==set(V):
        f=tuple(V.index(w) for w in W)
        assert f in (tuple(range(12)),tuple((4-q)%12 for q in range(12)))
        stab.append(f)
assert len(stab)==12 and stab.count(tuple(range(12)))==6
assert stab.count(tuple((4-q)%12 for q in range(12)))==6
pairs=sorted({tuple(sorted((q,(3-q)%12))) for q in range(12)})
assert len(pairs)==6 and (5,10) in pairs
cases=[]; checks=0
for N in (6,12,24,48,96):
    for theta in (1,-1):
        seen=set()
        for a in range(N):
            w=[0]*12; w[5]=a; w[10]=(-theta*a)%N
            for q in range(12):
                assert (theta*w[q]+w[(3-q)%12])%N==0; checks+=1
            H=sum(w)%N
            assert H==(a-theta*a)%N; checks+=1
            seen.add(H)
        assert seen=={(a-theta*a)%N for a in range(N)}; checks+=1
        cases.append({'N':N,'theta':theta,'image_size':len(seen),'H6_possible':(6%N in seen)})
w=[0]*12; w[5]=w[10]=3
assert sum(w[:6])==sum(w[6:])==3 and sum(w)==6
assert all(w[q]==w[(3-q)%12] for q in range(12))
assert any(w[q]!=w[(q+2)%12] for q in range(12))
print(json.dumps({'S6_checked':720,'stabilizer':12,'induced_identity':6,'induced_reflection':6,
 'reflection_on_vertices':'4-q mod 12','reflection_on_edges':'3-q mod 12',
 'holonomy_image':'Im(id-theta)','unit232_macroshift_image':'6 Im(id-theta)',
 'congruence_assertions':checks,'cases':cases,'witness':{'w5':3,'w10':3,'H':6,'halfturns':[3,3]},
 'mismatches':0},indent=2))
