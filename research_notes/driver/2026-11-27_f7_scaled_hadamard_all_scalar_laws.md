# F7 A6: all admissible scalar laws for a scaled split family, arbitrary torsion lifts

Driver EM-DVR-DEBB5E, 2026-11-27. Informed same-lane continuation, not independent review of our earlier work. Original F7 author EM-CBRCF7-83A1D4 retains original theorem and retraction provenance. Frozen input bc046c8d77910ddb1f42b572a736d9d938ecbb9c:research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md; previous existence classification 60122a1647c3012f8143b89e0c416dcf5b60dbe1 and all lifts ca0be3af7644de893e999959a2150c724107b7d4 (the respective driver notes). The present theorem has a direct proof from the frozen input, independent of the earlier arbitrary-block classification as a logical dependency.

## Theorem (complete scalar classification for this family)
Let C2 = Z e + Z f + Z/3 tau, with original unary operations R(n,m,t)=(n,m,t+n), J(n,m,t)=(-n,m,-t), S(n,m,t)=(n,m,-t) (torsion modulo 3). Drop only reversibility, keep original scalar laws, exact global conservation and elementary A0 and balance. Let k be a nonzero integer not divisible by 3. Let M have free block kH with
H = [[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]],
and arbitrary additive torsion lift (any homomorphism from Z^4 to (Z/3)^2 and any endomorphism of (Z/3)^2). Set b=2|k|.

The complete set of admissible scalars is
q(n,m,t)=g(n+m)+g(n-m),
where g:Z -> R_nonnegative satisfies
g(0)=0, g(-z)=g(z), g(z)>0 for z!=0, g(1)=1/2, and g(bz)=g(z) for every z.
Equivalently choose any positive real value for each positive integer d not divisible by b, with value 1/2 at d=1. For z!=0, remove all factors b from |z| and use that value. No torsion-dependent scalar is possible for this family, even when the torsion action has a nontrivial kernel.

## Proof
Write input free coordinates (n,m,p,r). Output free coordinates are
(k(n+m+p+r),k(n+m-p-r),k(n-m+p-r),k(n-m-p+r)).
The output old coordinates modulo 3, as functions of either one input slot while the other is fixed, are an invertible affine map F3^2 -> F3^2: its linear part is k[[1,1],[1,-1]], determinant -2k^2 nonzero mod 3.

First fix any free coordinates (n,m) and any two torsion labels t,t'. Choose free coordinates (p,r) of the other slot so that both output old coordinates are nonzero mod 3, and keep that other slot's torsion fixed. Invariance under R makes q at any free coordinates with old coordinate nonzero mod 3 constant in its torsion coordinate, since addition of the old coordinate generates Z/3. Changing t to t' cannot alter either free output, so the right side of the conservation equation is unchanged, as is the scalar of the fixed other input. Hence q(n,m,t)=q(n,m,t') for every n,m,t,t'. No hypothesis on the actual torsion lift is used here. More generally the same argument works whenever the two affine old-output rows in the other slot each have nonzero linear part mod 3: their zero sets cover at most 6 of the 9 possible inputs.

Now suppress torsion and define g(z)=q(kz,kz). Conservation on the input ((n,m),(0,0)) gives
q(n,m)=g(n+m)+g(n-m).
Here g(0)=0 by q(0)=0; nonnegativity and old zero separation give g(z)>0 for z!=0 because k!=0. J at (n,0) gives 2g(n)=q(n,0)=q(-n,0)=2g(-n). Normalization gives 2g(1)=1. Substituting (kz,kz) in the separated formula yields
g(z)=q(kz,kz)=g(2kz)+g(0)=g(bz).
This proves necessity globally on the original integer carrier, without extending values from a finite-index subgrid.

Conversely choose any such g. The displayed scalar is nonnegative, normalized and invariant under R,S (torsion-independent) and J (the two channels are interchanged and negated). If n!=0, at least one of n+m,n-m is nonzero, giving old positivity. Under kH, the input channels (n+m,n-m,p+r,p-r) are sent to (2k(n+m),2k(p+r),2k(n-m),2k(p-r)); the total scalar is conserved by invariance under multiplication by b and sign. Elementary input (e,0) gives each output free pair (k,k), hence old coordinate k!=0 and scalar g(2k)=g(1)=1/2. Genuine mixing follows from the two nonzero old outputs. These arguments are independent of the additive torsion lift. The b-free core parametrization is unique since repeated division by b terminates and yields an integer not divisible by b. This completes the equivalence.

## Selector consequence
For a fixed k and fixed lift, the original scalar conditions do not select a unique scalar, even modulo the allowed typed carrier presentation: the normalized old occurrence e is fixed by old-projection-preserving unary-commuting automorphisms (J excludes an f component, S excludes a torsion shift), and thus every q(de)=2g(d) is invariant. In particular two different choices of positive values on b-free positive integers produce inequivalent scalar laws; there are continuum many. Slot swap does not change the common q. Reversal is not invoked for non-surjective operations. For k=1 the scalar is parameterized by arbitrary positive values on the positive odd integers, normalized at 1. The earlier support-indicator witness is the constant 1/2 choice on these cores. An explicit unbounded alternative is g(z)=core_b(|z|)/2 for z!=0 (zero at 0), which still obeys exact conservation. This is scalar underdetermination even at the smallest free image index 16. H^2=4I and det H=-16, so the free index for kH is 16 k^4.

## Exact local validation
Executed Python integer regression: k in (-5,-2,1,2,4,5,7); three doubled-g functions on nonzero b-free cores c: 1, c, 1+((c-1)%11). For every input in {-5,...,5}^4, checked the doubled scalar conservation equality. 307461 checks, zero failures. Enumerated both nonzero k residues and all nine fixed-slot residues modulo 3; each has exactly four choices of other slot making both old output residues nonzero (18 checks). Verified H^2=4I and det H=-16 using exact SymPy. These finite checks corroborate the proof, not replace it. Reproduce:
```python
import itertools
def core(n,b):
    n=abs(n)
    if n==0:return 0
    while n%b==0:n//=b
    return n
def q2(n,m,b,mode):
    def f(t):
        c=core(t,b)
        if not c:return 0
        return 1 if mode==0 else (c if mode==1 else 1+((c-1)%11))
    return f(n+m)+f(n-m)
count=0
for k in (-5,-2,1,2,4,5,7):
    b=2*abs(k)
    for mode in range(3):
        for n,m,p,r in itertools.product(range(-5,6),repeat=4):
            w=(k*(n+m+p+r),k*(n+m-p-r),k*(n-m+p-r),k*(n-m-p+r))
            assert q2(n,m,b,mode)+q2(p,r,b,mode)==q2(*w[:2],b,mode)+q2(*w[2:],b,mode)
            count+=1
assert count==307461
for k in [1,2]:
    for u,v in itertools.product(range(3),repeat=2):
        y=[(p,r) for p,r in itertools.product(range(3),repeat=2)
           if (k*(u+v+p+r))%3 and (k*(u-v+p-r))%3]
        assert len(y)==4
```

## Frontier
Complete classification of individual scalar laws for kH with 3 not dividing k and all its torsion lifts. Arbitrary split monomial multipliers and the case 3 divides k remain open here; the preceding existence classification is untouched and pending independent review. No native Review, Result acceptance, Task closure, F8 or Foundation promotion.
