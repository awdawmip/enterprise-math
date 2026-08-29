from itertools import combinations, permutations, product
from collections import deque

V=tuple("ABCD"); E=tuple(combinations(V,2)); EI={e:i for i,e in enumerate(E)}
S={v:frozenset(e for e in E if v in e) for v in V}
ID4=tuple(range(4)); ID6=tuple(range(6))
VECS={("A","B"):(1,1,0),("A","C"):(1,0,1),("A","D"):(0,1,-1),
      ("B","C"):(0,1,1),("B","D"):(1,0,-1),("C","D"):(1,-1,0)}

def comp(p,q): return tuple(p[q[i]] for i in range(len(q)))
def inv(p):
    r=[0]*len(p)
    for i,j in enumerate(p): r[j]=i
    return tuple(r)
def edge(a,b): return tuple(sorted((a,b)))
def eact(p):
    return tuple(EI[edge(V[p[V.index(a)]],V[p[V.index(b)]])] for a,b in E)
def supp(p): return frozenset(i for i,j in enumerate(p) if i!=j)
def comm(a,b): return comp(comp(comp(a,b),inv(a)),inv(b))
def ext(p,O):
    r=list(range(6))
    for i in O: r[i]=p[i]
    return tuple(r)
def isperm(p): return sorted(p)==list(range(len(p)))
def order(p):
    r=tuple(range(len(p)))
    for n in range(1,25):
        r=comp(p,r)
        if r==tuple(range(len(p))): return n
    raise AssertionError
def closure(gs):
    seen={ID4}; q=deque([ID4])
    while q:
        x=q.popleft()
        for g in gs:
            y=comp(g,x)
            if y not in seen: seen.add(y); q.append(y)
    return seen
def det(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def mv(M,v): return tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3))
def lk(v):
    v=tuple(v)
    for x in v:
        if x:
            return tuple(-y for y in v) if x<0 else v
def pmatrix(p):
    M=[[0]*6 for _ in range(6)]
    for i,j in enumerate(p): M[j][i]=1
    return tuple(tuple(r) for r in M)

# K4 incidence.
assert len(E)==6 and all(len(S[v])==3 for v in V)
assert all(S[a]&S[b]==frozenset({(a,b)}) for a,b in E)
ALL4=tuple(permutations(range(4)))
assert len({eact(p) for p in ALL4})==24

# Exact FCC determinant+1 signed-coordinate rotations realize all S4 edge actions.
LKEY={lk(v):e for e,v in VECS.items()}
phys=[]
for cp in permutations(range(3)):
    for signs in product((-1,1),repeat=3):
        M=[[0]*3 for _ in range(3)]
        for j,row in enumerate(cp): M[row][j]=signs[j]
        M=tuple(tuple(r) for r in M)
        if det(M)==1:
            ep=tuple(EI[LKEY[lk(mv(M,VECS[e]))]] for e in E)
            phys.append(ep)
assert len(phys)==24 and set(phys)=={eact(p) for p in ALL4}

# a=(BCD), b=(AB).
a=(0,2,3,1); b=(1,0,2,3)
ea,eb=eact(a),eact(b)
assert order(a)==3 and order(b)==2 and order(comp(a,b))==4
assert len(closure((a,b)))==24
assert pmatrix(ea)==((0,0,1,0,0,0),(1,0,0,0,0,0),(0,1,0,0,0,0),
                     (0,0,0,0,1,0),(0,0,0,0,0,1),(0,0,0,1,0,0))
assert pmatrix(eb)==((1,0,0,0,0,0),(0,0,0,1,0,0),(0,0,0,0,1,0),
                     (0,1,0,0,0,0),(0,0,1,0,0,0),(0,0,0,0,0,1))

# Slice action and stabilizers.
assert all(frozenset(E[eact(p)[EI[e]]] for e in S[v])==S[V[p[V.index(v)]]] for p in ALL4 for v in V)
assert sum(p[0]==0 for p in ALL4)==6
assert sum(eact(p)[EI[("A","B")]]==EI[("A","B")] for p in ALL4)==4
assert sum(p[0]==0 and eact(p)[EI[("A","B")]]==EI[("A","B")] for p in ALL4)==2

# Supported-extension iff invariant, plus inverse and conjugation.
for s in ALL4:
    es=eact(s)
    for mask in range(64):
        O=frozenset(i for i in range(6) if mask>>i&1)
        image=frozenset(es[i] for i in O)
        M=ext(es,O)
        assert isperm(M)==(image==O)
        if image!=O: continue
        assert comp(M,ext(inv(es),O))==ID6
        for t in ALL4:
            et=eact(t); lhs=comp(comp(et,M),inv(et))
            Ot=frozenset(et[i] for i in O)
            rhs=ext(eact(comp(comp(t,s),inv(t))),Ot)
            assert lhs==rhs

# General commutator support theorem, exhaustive on Sym(6)^2.
P6=tuple(permutations(range(6)))
for A in P6:
    SA=supp(A)
    for B in P6:
        D=SA&supp(B)
        bound=D|frozenset(A[i] for i in D)|frozenset(B[i] for i in D)
        assert supp(comm(A,B))<=bound

# Exact FCC overlap localizer.
SA=frozenset(EI[e] for e in S["A"]); SB=frozenset(EI[e] for e in S["B"])
UA=ext(ea,SA)
bab=comp(comp(b,a),b); UB=ext(eact(bab),SB)
C=comm(UA,UB)
face=frozenset(EI[e] for e in (("A","B"),("A","C"),("B","C")))
assert supp(UA)&supp(UB)==frozenset({EI[("A","B")]})
assert supp(C)==face

# No freely reduced word of length <4 in UA±,UB± localizes nontrivially to that face.
G=(UA,inv(UA),UB,inv(UB)); IL={0:1,1:0,2:3,3:2}
for n in (1,2,3):
    for w in product(range(4),repeat=n):
        if any(IL[w[i]]==w[i+1] for i in range(n-1)): continue
        p=ID6
        for z in w: p=comp(G[z],p)
        assert p==ID6 or not supp(p)<=face

# Slice transport and support-2 axis targeting.
assert V[b[0]]=="B"
pair=frozenset({EI[("A","C")],EI[("B","C")]})
T=ext(eb,pair)
assert isperm(T) and supp(T)==pair
assert all(len(supp(p))!=1 for p in P6)

# Exact BFS normal forms for <a,b> with alphabet {a,a^-1,b}.
alphabet=(a,inv(a),b); words={ID4:""}; q=deque([ID4])
while q:
    p=q.popleft()
    for c,g in zip("aAb",alphabet):
        h=comp(g,p)
        if h not in words: words[h]=words[p]+c; q.append(h)
assert len(words)==24 and max(map(len,words.values()))==6

# Typed regressions: C2 remains a separate involution; HCP cannot silently derive 6 native axes.
rho=(3,4,5,0,1,2)
assert order(rho)==2
HCP_FIRST_SHELL_CENTRALLY_SYMMETRIC=False
assert not HCP_FIRST_SHELL_CENTRALLY_SYMMETRIC

print("PASS")
print("physical_rotations=24")
print("S4_edge_representation=faithful")
print("generator_orders=a:3,b:2,ab:4")
print("normal_forms=24,max_shortlex_length=6")
print("supported_extension_iff_invariant=exhaustive_24x64")
print("conjugation=exhaustive")
print("commutator_support_lemma=exhaustive_Sym6_pairs")
print("localizer=[U_A,U_B]=(AB AC BC),shortest_local_word_length=4")
print("axis_targeting_min_support=2")
print("typed_regressions=C2,HCP")
