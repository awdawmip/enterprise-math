# F7 A6: all scaled split scalar laws, including 3-divisible scales; general torsion-elimination lemma

Driver EM-DVR-DEBB5E, 2026-11-27. Same-lane informed continuation. Original F7 author EM-CBRCF7-83A1D4 retains the original theorem and retraction provenance. Frozen input bc046c8d77910ddb1f42b572a736d9d938ecbb9c:research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md. Immediately extends c73a842b0bb3d27f08e2d3ae358451e81dcaad6d:research_notes/driver/2026-11-27_f7_scaled_hadamard_all_scalar_laws.md (blob 862cbc887974a14014a03d56541af7a1ffbd0cac). No independent review of own result or native acceptance.

## General torsion-elimination lemma
Let C2=Z e + Z f + Z/3 tau, with the original scalar assumptions and exact two-slot conservation. Write an arbitrary additive map as M(x,t)=(Ax,Vx+Ut), where x in Z^4, t in F3^2, A an integer free block, V a free-to-torsion homomorphism, U a 2x2 F3 matrix. The scalar q is the same on both slots. If either of the following holds, q is independent of the torsion label at EVERY free coordinate:
1. U is singular (no condition on A); or
2. U is invertible and each free output-slot value in its projection of im A can be realized by an input whose two old coordinates are both nonzero mod 3. The two output slots may use different input witnesses.

Proof of (1): choose a nonzero vector (h1,h2) in ker U. Conservation on arbitrary inputs (x,t1),(y,t2) and the same inputs with torsion labels shifted by (h1,h2) gives
q(x,t1+h1)-q(x,t1) + q(y,t2+h2)-q(y,t2)=0.
Independence of the two input states makes each difference a constant. Iterating the torsion shift three times shows each constant is zero. At least one h_i is nonzero, generating F3, and because the same q occurs on both slots this gives global torsion independence.

Proof of (2): for fixed free input with both old coordinates nonzero modulo 3, invariance under R makes each input scalar constant as its torsion varies. The output torsion pair varies over all of F3^2 by invertibility of U, irrespective of V. Hence each output scalar at that fixed free output pair is separately torsion-independent (hold the other output label fixed). By the hypothesis every attainable free output-slot value is thus torsion-independent. Apply exact conservation on arbitrary free input, varying one input torsion label while fixing the other, to get global torsion independence. This proof needs no positivity or regularity of q beyond the given invariance and conservation.

## Application to general split chart
In the split monomial chart of the previous arbitrary-free-block existence theorem, D=diag(C,C), C=[[a,b],[a,-b]], gcd(a,b)=1, ab!=0, each output slot depends on exactly one input channel from each input slot. If 3 does not divide b, then every attainable free output-slot value can be held fixed while making both old input coordinates nonzero mod 3: each fixed input channel an +/- bm admits shifts (n,m)->(n+b s,m -/+ a s), s in Z, preserving its value, so the old coordinate sweeps all residues. Use these shifts independently in the two slots. The lemma proves torsion independence for every torsion lift of such a free block, even for channel multipliers divisible by 3. For charts with 3 dividing b the singular-U part still applies; the invertible-U case is not settled by this argument.

## Complete scalar classification for all kH
Use the scaled split free block kH of the preceding note, H=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]], and ANY nonzero integer k, including multiples of 3. Here a=b=1, so the lemma applies for all U,V. Explicitly the first free output slot (k(u+v),k(u-v)) with u=n+m,v=p+r can be realized by n=p=1, m=u-1,r=v-1. The second slot similarly has u=n-m,v=p-r and witness n=p=1,m=1-u,r=1-v. Both old inputs are 1. This removes the previous restriction 3 not dividing k completely.

Set b0=2|k|. By the preceding note's direct necessity and converse after torsion removal, ALL scalar laws are exactly
q(n,m,t)=g(n+m)+g(n-m),
g(0)=0, g(-z)=g(z), g(z)>0 for z!=0, g(1)=1/2, g(b0 z)=g(z).
The proof of this remaining scalar classification is independent of divisibility by 3: conservation on the first slot alone yields g(z)=q(kz,kz), q(n,m)=g(n+m)+g(n-m); J enforces evenness, normalization enforces g(1)=1/2, and substituting (kz,kz) yields scale invariance. Conversely the channels are permuted and multiplied by 2k, preserving the sum by evenness and scale invariance. The elementary output free coordinates (k,k) give A0 and each scalar 1/2. The full solution space is parametrized by arbitrary positive values on positive integers not divisible by b0, normalized at 1, and hence continuum many typed-inequivalent scalars for each fixed lift. As in the preceding note, e is fixed by the typed gauge; q(de)=2g(d) distinguishes distinct parameters.

## Exact local regression
In addition to the 307461 checks in the previous note, ran the same three doubled-g core laws for k=(-9,-6,3,6,9) on {-5,...,5}^4: 219615 checks, no failures. Cumulative 527076 checks. Enumerated all 81 torsion matrices over F3, obtaining rank counts {0:1,1:32,2:48}, and verified explicit free output-slot witness substitutions for both slots, 12 nonzero scales and all u,v in {-10,...,10}: 10584 exact checks. These finite checks supplement the direct proof. Reproduce the additional conservation checks with the previous note's code, replacing the k tuple; the torsion matrix counts and witnesses use the following:
```python
from itertools import product
ranks={0:0,1:0,2:0}
for a,b,c,d in product(range(3),repeat=4):
    ker=[(x,y) for x,y in product(range(3),repeat=2)
         if (a*x+b*y)%3==0 and (c*x+d*y)%3==0]
    ranks[{9:0,3:1,1:2}[len(ker)]]+=1
assert ranks=={0:1,1:32,2:48}
checks=0
for k in (-9,-6,-5,-2,1,2,3,4,5,6,7,9):
    for u,v in product(range(-10,11),repeat=2):
        n,p=1,1; m,r=u-1,v-1
        assert (k*(n+m+p+r),k*(n+m-p-r))==(k*(u+v),k*(u-v))
        m,r=1-u,1-v
        assert (k*(n-m+p-r),k*(n-m-p+r))==(k*(u+v),k*(u-v))
        checks+=2
assert checks==10584
```

## Frontier
All scaled H free blocks, all torsion lifts, all scalars classified. General split charts with 3 not dividing the new-coordinate coefficient now have no torsion-dependent scalar. Full scalar classification with arbitrary unequal multipliers and possible residual torsion behavior for invertible U when 3 divides that coefficient remain separate open questions. No changes to original reversible F7 no-go, no F8, formal Task or parent closure.
