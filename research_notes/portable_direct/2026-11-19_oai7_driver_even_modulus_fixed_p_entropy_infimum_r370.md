# OAI7 r370 — Fixed-modulus entropy infimum with positive sharp-support samplers

Date: 2026-11-19. Driver-side author research / internal verification, extending the explicitly scoped even-modulus construction r368 and entropy identity r369. Shared-context derivation: **not** an independent Native Result review or a formal result intake. The odd prime-29 fixed-profile problem is unchanged.

## Theorem (exact fixed-`p` entropy infimum; nonattainment)

Fix **any even integer** `p=2r+2>=4` and `d>=1+ceil(log2(p/2))`. Consider the r368 unit-generator-gap double-star family with `m=p-1` pairwise translation-inequivalent ordered profiles, exactly two strictly positive translation atoms per profile, `S=2(p-1)=m+p-1`, exactly uniform residue marginals in all `d` coordinates, positive rational weights with integer profile numerators of common denominator `N` and `gcd(N,p)=1`. If `Y` denotes the entire ordered output, then

```
                inf H_2(Y) = log_2(p),
```

where the infimum is taken over all such samplers and is **not attained** by any sampler in this strictly positive, pairwise translation-inequivalent family. Thus for each fixed admissible `(p,d)` and each `epsilon>0` there is a genuine fully positive sampler with `H_2(Y)<log_2(p)+epsilon`; no increase in coordinates or support is needed.

This strengthens r369's `p -> infinity` asymptotic entropy bound in a different direction: the redundancy may be driven to zero **at fixed modulus and fixed minimal coordinate count**, by allowing a larger integer mass denominator.

## Exact parameter family

Keep the r368 shapes and their two atoms:
- `W_C=(0,...,0)` with translations `0,1`;
- `W_{A_j}=(0,b_j)` with translations `0,2j`;
- `W_{B_j}=(0,-b_j)` with translations `1,2j+1`, for `j=1,...,r`;
- `b_1,...,b_r` are distinct nonzero binary words in `{0,1}^{d-1}`.

For **each integer `M>=1`**, put
```
N = p*M - 1,                 gcd(N,p)=1,
q = 1/(p*N),                Q = (2*M-1)/(2*N).
```
Use masses `(Q,Q)` for `C`, `(q,1/p)` for every `A_j`, and `(q,1/p)` for every `B_j` (in the translation order above). Profile masses are precisely

```
mass(C) = (2M-1)/N,
mass(A_j) = mass(B_j) = M/N.
```

They are positive integer numerators over `N` and sum to one:
`(2M-1)+2rM=pM-1=N`. The first coordinate has each outer leaf residue `2,...,p-1` of mass `1/p`; the two hubs each have
`Q+r*q = ((2M-1)p+2r)/(2pN) = 1/p`.

For every subsequent coordinate, each binary bit `b_j[i]` either leaves the two corresponding connections stationary or exchanges **equal weights `q` between hub residues `0,1`** and **equal weights `1/p` between leaf residues `2j,2j+1`**. Therefore every residue remains exactly `1/p` in every coordinate. The shapes remain translation-inequivalent and `Y` distinguishes all `2(p-1)` positive atoms, exactly as in r368.

## Exact entropy identity and infimum

At either hub of `Y_1`, the conditional law of the compatible atoms is
```
pi_0 = p*Q = 1-r/N,
pi_1 = ... = pi_r = p*q = 1/N,
delta = r/N.
```
At the `p-2` outer leaves, the atom is determined by `Y_1`. Injectivity and the chain rule give the **exact identity**

```
H_2(Y) = log_2(p)
       + (2/p) [ h_2(delta) + delta*log_2(r) ],
delta = r/(p*M-1),
h_2(t)=-t log_2(t)-(1-t)log_2(1-t).
```

For fixed `p`, `delta -> 0` as `M -> infinity`, hence the overhead tends to zero. Exact uniformity of `Y_1` supplies the general lower bound `H_2(Y)>=log_2(p)`. For each finite `M`, hub conditional laws have at least two positive entries, so the overhead is strictly positive. More generally, the declared family has `2(p-1)>p` distinct positive output atoms, so no strictly positive sampler with pairwise inequivalent profiles can attain the `log_2(p)` equality case, which would require `Y` to be determined by uniform `Y_1`.

When `r=1` use `log_2(1)=0`; all conclusions remain valid at `p=4`. Larger permitted `d` are obtained by appending zero coordinates.

## Reproducibility (exact rational structural checks; floating entropy illustration)

```python
from fractions import Fraction as F
from math import gcd, log2

def verify(p, M):
    assert p >= 4 and p % 2 == 0 and M >= 1
    r = (p-2)//2
    d = 1 + r.bit_length()
    N = p*M - 1
    assert gcd(N,p) == 1
    q, Q = F(1,p*N), F(2*M-1,2*N)
    shapes = [(0,)*d]
    atoms = [(0,0,Q),(0,1,Q)]
    for j in range(1,r+1):
        b = tuple((j>>k)&1 for k in range(d-1))
        shapes.extend([(0,)+b, (0,)+tuple(-v for v in b)])
        atoms.extend([
          (2*j-1,0,q), (2*j-1,2*j,F(1,p)),
          (2*j,1,q),   (2*j,2*j+1,F(1,p))
        ])
    assert len(shapes)==p-1 and len(atoms)==2*(p-1)
    assert len({tuple(v%p for v in w) for w in shapes})==p-1
    assert sum((a[2] for a in atoms),F()) == 1
    Y = [tuple((t+v)%p for v in shapes[x]) for x,t,_ in atoms]
    assert len(set(Y)) == len(Y)
    for i in range(d):
        hist = [sum((a[2] for a in atoms
                     if (a[1]+shapes[a[0]][i])%p==v),F())
                for v in range(p)]
        assert hist == [F(1,p)]*p
    H = -sum(float(z)*log2(float(z)) for _,_,z in atoms)
    delta = r/N
    binary = -delta*log2(delta)-(1-delta)*log2(1-delta)
    expected = log2(p)+(2/p)*(binary+delta*log2(r))
    assert abs(H-expected)<1e-10
    return d, N, H-log2(p)

for p,M in [(4,1),(4,20),(30,1),(30,10),(30,1000),
            (100,100000),(150,1000)]:
    print(p,M,verify(p,M))
```

Illustration for `p=30,d=5`: `M=10` yields `N=299` and excess about `0.03006763423` bits; `M=1000` yields `N=29999` and excess about `0.00050759424` bits. These floating illustrations are not the proof of the exact claims.

## Lineage and boundary

- r368: https://github.com/awdawmip/enterprise-math/blob/6f8f6b04bcee2c628accc73a2cc3bf297327ff2d/research_notes/portable_direct/2026-11-19_oai7_driver_unit_gap_double_star_binary_threshold_r368.md
- r369: https://github.com/awdawmip/enterprise-math/blob/8004b37c3d027e08dad75542c3542040f0c400a7/research_notes/portable_direct/2026-11-19_oai7_driver_entropy_sharp_double_star_r369.md
- Original OAI7 Task `RS-OAI7-028-C-20261007-6F2A81`, publication `TP2-96FAC49786245691AE19`, preserved original researcher `EM-EMF6D046-5A2844`.
- This is one new **author-side mathematical subunit**, not a frozen Native Result, independent review, official task completion, parent objective closure, or transfer into the fixed prime-29/source-gated OAI7 theorem.
