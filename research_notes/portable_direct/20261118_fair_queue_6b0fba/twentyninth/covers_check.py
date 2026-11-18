"""Central C2 extensions of the labelled four-point quotient, including all subgroup restrictions."""
import json
from collections import Counter, defaultdict
from itertools import permutations, product, combinations


def compose(p,q):
    return tuple(p[j] for j in q)


P=list(permutations(range(4)))
N={p:i for i,p in enumerate(P)}
M=[[N[compose(p,q)] for q in P] for p in P]
SIGN=[sum(p[i]>p[j] for i,j in combinations(range(4),2))%2 for p in P]


def perm_type(p):
    seen=set()
    parts=[]
    for j in range(4):
        if j not in seen:
            count=0
            while j not in seen:
                seen.add(j); count+=1; j=p[j]
            parts.append(count)
    return tuple(sorted(parts))


TYPES=[perm_type(p) for p in P]
LINES=((1,0),(0,1),(1,1),(1,2))


def mm(x,y):
    return tuple(sum(x[2*i+k]*y[2*k+j] for k in (0,1))%3
                 for i,j in product(range(2),repeat=2))


def neg(x):
    return tuple((-v)%3 for v in x)


def matperm(x):
    out=[]
    for a,b in LINES:
        c=(x[0]*a+x[1]*b)%3; d=(x[2]*a+x[3]*b)%3
        out.append(LINES.index((1,d*c%3) if c else (0,1)))
    return N[tuple(out)]


GL=[x for x in product(range(3),repeat=4) if (x[0]*x[3]-x[1]*x[2])%3]
REPS={matperm(x):min(x,neg(x)) for x in GL}
assert len(REPS)==24 and len(GL)==48
assert all(matperm(mm(x,y))==M[matperm(x)][matperm(y)] for x,y in product(GL,repeat=2))
TWIST=[[int(mm(REPS[g],REPS[h])!=REPS[M[g][h]]) for h in range(24)] for g in range(24)]
CLASSES=((0,0),(1,0),(0,1),(1,1))


def tables(s,d):
    f=[[s*SIGN[g]*SIGN[h] ^ d*TWIST[g][h] for h in range(24)] for g in range(24)]
    mul=[[2*M[i//2][j//2]+((i%2)^(j%2)^f[i//2][j//2]) for j in range(48)]
         for i in range(48)]
    assert all(mul[mul[i][j]][k]==mul[i][mul[j][k]] for i,j,k in product(range(48),repeat=3))
    return f,mul


def order(mul,x):
    y=x; k=1
    while y!=0:
        y=mul[y][x];k+=1
        assert k<=len(mul)
    return k


def subgroup(mul,gens):
    seen={0}
    todo=[0]
    while todo:
        x=todo.pop()
        for y in gens:
            z=mul[x][y]
            if z not in seen:
                seen.add(z);todo.append(z)
    return frozenset(seen)


def all_subgroups():
    sub=frozenset([0])
    seen={sub}
    todo=[sub]
    while todo:
        h=todo.pop()
        for g in range(1,24):
            if g in h:
                continue
            k=subgroup(M,(*h,g))
            if k not in seen:
                seen.add(k);todo.append(k)
    return seen


def coboundary(H,f):
    """Gauss in F2: variables are the adjustments to one chosen lift for each h in H."""
    pivots={}
    for g,h in product(H,repeat=2):
        row=(1<<(g+1))^(1<<(h+1))^(1<<(M[g][h]+1))^f[g][h]
        while row>1:
            j=row.bit_length()
            if j not in pivots:
                pivots[j]=row
                break
            row^=pivots[j]
        if row==1:
            return False
    return True


def main():
    groups=all_subgroups()
    assert len(groups)==30
    classifier={}; mult={}
    A0=(1,1,0,1);B0=(0,1,1,0)
    a,b=matperm(A0),matperm(B0)
    assert P[a]==(0,2,3,1) and P[b]==(1,0,2,3)
    aij=[N[p] for p in ((1,0,2,3),(0,2,1,3),(0,1,3,2))]
    klein=subgroup(M,[aij[0],aij[2]])
    for s,d in CLASSES:
        f,mul=tables(s,d)
        classifier[s,d]=f
        lifts=lambda x:[2*x,2*x+1]
        power=lambda x,n: pow_in(mul,x,n)
        for x,p in enumerate(P):
            if TYPES[x] in ((1,1,2),(2,2),(4,)):
                e=4 if TYPES[x]==(4,) else 2
                bit=s if TYPES[x]==(1,1,2) else d
                assert {power(y,e) for y in lifts(x)}=={bit}
        braid_choices=0
        for x,y,z in product(*(lifts(i) for i in aij)):
            assert mul[x][z] == (mul[z][x]^d)
            if mul[mul[x][y]][x]==mul[mul[y][x]][y] and mul[mul[y][z]][y]==mul[mul[z][y]][z]:
                braid_choices+=1
                assert power(mul[x][y],3)==s
        assert braid_choices==2
        triangle=[]
        for aa,bb in product(lifts(a),lifts(b)):
            triangle.append([power(aa,3),power(bb,2),power(mul[aa][bb],4),len(subgroup(mul,[aa,bb]))])
        invs=sum(order(mul,i)==2 for i in range(48))
        k_invs=sum(order(mul,i)==2 for i in range(48) if i//2 in klein)
        mult[str((s,d))]={"element_orders":dict(Counter(order(mul,i) for i in range(48))),
                           "klein_involutions":k_invs,"global_involutions":invs,
                           "triangle_A3_B2_AB4_generated_order":sorted(triangle),
                           "strict_adjacent_braid_choices":braid_choices}
    restrictions=Counter()
    ranks=Counter()
    for H in groups:
        vanished=tuple((s,d) for s,d in CLASSES if coboundary(H,classifier[s,d]))
        rank={1:2,2:1,4:0}[len(vanished)]
        ranks[rank]+=1
        tr=sum(TYPES[g]==(1,1,2) for g in H)
        name={(1,0):"1",(2,0):"C2 double",(2,1):"C2 transposition",(3,0):"C3",
              (4,2):"V4 disjoint transpositions",(6,3):"S3",(8,2):"D8",(12,0):"A4",
              (24,6):"S4"}.get((len(H),tr))
        if name is None and len(H)==4:
            name="C4" if any(TYPES[g]==(4,) for g in H) else "V4 double transpositions"
        assert name is not None
        restrictions[(name,vanished)]+=1
    assert ranks=={0:5,1:18,2:7}
    # Scalar twist over F9 = F3[i], i^2=-1. Pair (t,x) encodes i^t x.
    encoded={(SIGN[matperm(g)],g) for g in GL}
    for t,g in encoded:
        assert ((-1)**t*(g[0]*g[3]-g[1]*g[2]))%3==1
        for u,h in encoded:
            j=matperm(g);k=matperm(h)
            prod=mm(g,h)
            if t*u:prod=neg(prod)
            assert (t^u,prod) in encoded
            scalar=(g!=REPS[j])^(h!=REPS[k])^classifier[1,1][j][k]
            assert prod==(neg(REPS[M[j][k]]) if scalar else REPS[M[j][k]])
    print(json.dumps({"quotient":len(P),"matrix_GL23":len(GL),"fibres":["I","-I"],
                      "models":mult,"subgroup_restriction_ranks":dict(ranks),
                      "subgroup_profiles":[{"type":k,"count":v,"restricts_to_split":z}
                              for (k,z),v in sorted(restrictions.items())],
                      "fourth_model_SL2_F9":len(encoded)},indent=2,sort_keys=True))


def pow_in(mul,x,n):
    y=0
    for _ in range(n):y=mul[y][x]
    return y


if __name__=="__main__":
    main()
