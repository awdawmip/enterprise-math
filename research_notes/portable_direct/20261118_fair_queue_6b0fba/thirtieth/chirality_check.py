"""Integer checks for sampled Weyl labels, translated grids, finite jets and Dirac aliases.
Python 3.9+ with SymPy, no network. All spectral and rank assertions use exact arithmetic.
"""
import json
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb, gcd, prod

from sympy import Matrix


def grid(sizes):
    return product(*(range(n) for n in sizes))


def mul(A,v):
    return tuple(sum(x*y for x,y in zip(row,v)) for row in A)


def v2(n):
    return (n & -n).bit_length()-1


def smith_case(name, diagonal, left, right):
    A=left*Matrix.diag(*diagonal)*right
    assert abs(left.det())==abs(right.det())==1
    a=[[int(x) for x in row] for row in A.tolist()]
    ell=[sum(int(left[j,i]) for j in range(3))%2 for i in range(3)]
    t=1+min(v2(d) for b,d in zip(ell,diagonal) if b)
    orientation=1 if A.det()>0 else -1
    exponent=2*diagonal[-1]
    def labels(u,n):
        au=mul(a,u)
        if any(2*z%n for z in au):return None
        return tuple((2*z//n)%2 for z in au)
    # Enumerate the continuous kernel on a proven common denominator, independent of Smith columns.
    roots={}
    for x in grid([exponent]*3):
        z=labels(x,exponent)
        if z is not None: roots[x]=z
    det=prod(diagonal)
    assert Counter(roots.values())=={z:det for z in grid([2]*3)}
    mesh_cases=[]
    for n in range(1,17):
        count=prod(gcd(n,2*d) for d in diagonal)
        eligible=[i for i,d in enumerate(diagonal) if v2(n)>v2(d)]
        expected=set()
        for choice in grid([2]*len(eligible)):
            z=[0,0,0]
            for i,w in zip(eligible,choice):
                for j in range(3):z[j]+=w*int(left[j,i])
            expected.add(tuple(w%2 for w in z))
        bylabel=Counter()
        for u in grid([n]*3):
            z=labels(u,n)
            if z is not None:bylabel[z]+=1
        assert bylabel=={z:count//len(expected) for z in expected}
        charge=sum(orientation*(-1)**sum(z)*f for z,f in bylabel.items())
        assert charge==(orientation*count if v2(n)<t else 0)
        # Cosets are uniquely indexed by N*x (mod 1). Check every nonempty translate.
        cosets=defaultdict(Counter)
        for x,z in roots.items():
            cosets[tuple(n*u%exponent for u in x)][z]+=1
        assert len(cosets)==len(roots)//count
        for c in cosets.values():
            z0=next(iter(c))
            assert len(c)==len(expected) and sum(c.values())==count
            assert {tuple(a^b for a,b in zip(z,z0)) for z in c}==expected
        label_classes={tuple(sorted(c)) for c in cosets.values()}
        assert len(label_classes)==8//len(expected)
        refine=exponent//gcd(exponent,n)
        assert n*refine%exponent==0 and all(n*k%exponent for k in range(1,refine))
        if n in [2,4,6,8,12]:
            mesh_cases.append({"N":n,"sampled_zeros":count,"charge":charge,
                "labels_seen":len(expected),"twists_for_all_labels":len(label_classes),
                "twists_for_all_nodes":len(cosets)})
    return {"name":name,"A":a,"smith":list(diagonal),"orientation":orientation,
            "continuous_zeros":len(roots),"first_balanced_v2":t,"cases":mesh_cases}


def jet_rank(R,N,J):
    # Direct evaluation at the actual grid: sizes 1 and 2 have rational characters.
    freqs=list(product(*(range(-r,r+1) for r in R)))
    rows=[]
    for x in grid(N):
        for a in grid([J+1]*3):
            if sum(a)>J:continue
            rows.append([(-1 if sum(k[i]*x[i] for i in range(3) if N[i]==2)%2 else 1)*
                         prod(ki**ai for ki,ai in zip(k,a)) for k in freqs])
    rank=Matrix(rows).to_DM().rank()
    groups=defaultdict(list)
    for k in freqs:groups[tuple(ki%ni for ki,ni in zip(k,N))].append(k)
    predicted=0
    for members in groups.values():
        sizes=[len({k[i] for k in members}) for i in range(3)]
        predicted+=sum(sum(u)<=J for u in grid(sizes))
    assert rank==predicted
    return rank


def ranks():
    out=[]
    for R,N in [((1,1,1),(2,2,2)),((2,1,0),(2,2,1)),((3,0,0),(2,1,1)),
                ((1,1,1),(1,2,2))]:
        critical=sum(2*r//n for r,n in zip(R,N))
        rr=[jet_rank(R,N,j) for j in range(critical+1)]
        ncoef=prod(2*r+1 for r in R)
        assert rr[-1]==ncoef and ncoef-rr[-2]==prod((2*r)%n+1 for r,n in zip(R,N))
        out.append({"R":R,"N":N,"first_unique_jet":critical,"ranks_from_order_zero":rr})
    return out


def alias_case(n,L,s):
    # Up to a nonzero monomial and scalar, f-sin has polynomial factor
    # (z^2-1)(z^L-1)^(2s); enumerate physical derivatives by powers of frequencies.
    assert L%n==0 and L%2==0
    coeff=Counter()
    for j in range(2*s+1):
        c=(-1)**j*comb(2*s,j)
        coeff[L*(j-s)+1]+=c
        coeff[L*(j-s)-1]-=c
    for d in range(2*s):
        residues=Counter()
        for k,v in coeff.items():residues[k%n]+=v*k**d
        assert all(t==0 for t in residues.values())
    zeros=[F(0),F(1,2)]+[F(2*j+1,4*L) for j in range(2*L)]
    assert len(set(zeros))==2*(L+1)
    # sin(2*pi*x) at the new rational roots has the sign of which open half contains x.
    signs=[1,-1]
    for j,x in enumerate(zeros[2:]):
        signs.append(-(1 if x<F(1,2) else -1)*(-1)**j)
    assert Counter(signs)=={-1:L+1,1:L+1}
    # Wilson scalar at an unmodified nonorigin zero. Other coordinates contribute
    # either zero or two, so the minimal positive lift has the nearest angular root.
    nearest=min(min(x,1-x) for x in zeros if x)
    assert nearest==F(1,4*L)
    sampled=[x for x in zeros if (n*x).denominator==1]
    g=gcd(n,2)
    assert len(sampled)==g
    return {"N":n,"L":L,"s":s,"matched_sampled_jet_through":2*s-1,
            "extra_factor_roots":2*L,"closest_Wilson_lift_argument_turns":str(nearest),
            "Wilson_corner_multiplicities":[comb(4,j) for j in range(5)],
            "continuous_Weyl_zeros":4*len(zeros),
            "continuous_Euclidean_Dirac_zeros":8*len(zeros),"grid_Weyl_zeros":g**3,
            "grid_Euclidean_Dirac_zeros":g**4}


def main():
    eye=Matrix.eye(3)
    l=Matrix([[1,0,0],[1,1,0],[0,0,1]])
    v=Matrix([[1,1,0],[0,1,-1],[0,0,1]])
    perm=Matrix([[0,1,0],[1,0,0],[0,0,1]])
    tests=[("identity",(1,1,1),eye,eye),("diag122",(1,2,2),eye,eye),
           ("shear122",(1,2,2),l,eye),("mixed126",(1,2,6),l,v),
           ("orientation248",(2,4,8),perm*l,v),("oddparts139",(1,3,9),l,v)]
    cases=[smith_case(*test) for test in tests]
    # Exact independence of the four Euclidean gamma matrices, Clifford/anti-gamma5 semantics.
    from sympy import I, eye as identity, zeros, kronecker_product as tensor
    pauli=[Matrix([[0,1],[1,0]]),Matrix([[0,-I],[I,0]]),Matrix([[1,0],[0,-1]])]
    gamma=[tensor(pauli[0],v) for v in pauli]+[tensor(pauli[1],identity(2))]
    gamma5=gamma[0]*gamma[1]*gamma[2]*gamma[3]
    for i,x in enumerate(gamma):
        assert x*gamma5+gamma5*x==zeros(4)
        for j,y in enumerate(gamma):
            assert x*y+y*x==2*int(i==j)*identity(4)
    print(json.dumps({"smith_families":cases,"smith_grids_directly_checked":16*len(cases),
        "full_jet_rank_checks":ranks(),"exact_aliases":[alias_case(3,6,2),alias_case(5,20,3),
        alias_case(6,12,2)],"Euclidean_Clifford_relations":"verified"},indent=2))


if __name__=="__main__":
    main()
