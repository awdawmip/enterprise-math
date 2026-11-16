# PREFIX-808 — Exact splitting criterion for the Reeve canonical-cover class-group sequence

Date: 2026-11-17. Status: author-side proved algebraic subunit in the pinned normal Reeve semigroup model; independent Native Result review remains open.

## Sources and precise scope

Original TU/Reeve observational model: **EM-DIRECT-4660FF**. The saturated semigroup, canonical cover and class-group calculations, and this follow-up: **EM-DVR-DEBB5E**.

- [Source class group at immutable commit c39db69](https://github.com/awdawmip/enterprise-math/blob/c39db69b566cd2c5a4d149939352feb45ce2a950/research_notes/driver/2026-11-17_prefix808_full_toric_divisor_class_group.md)
- [Target class group, toric pullback and explicit kernel at immutable commit 8c342dd](https://github.com/awdawmip/enterprise-math/blob/8c342dd2d8a65bc87ce06616f784efe52c333096/research_notes/driver/2026-11-17_prefix808_canonical_cover_class_group_and_toric_pullback.md)

Let K be any field, h >= 2, g=gcd(h,2), and r=h/g. In the notation of the cited sources, R_h is the normal invariant Reeve observation ring and C_h^can its finite normal canonical cover. Put a=(1,0,0,1), b=(0,1,1,0), and let D_i be the four coordinate toric height-one divisor classes.

The previously proved exact sequence is
```
0 --> <[N_g]> (isomorphic to Z/r) --> Cl(R_h) --> Cl(C_h^can) --> 0.
```
The term `N_g` is indexed modulo h, so N_2=N_0 when h=2.

## Theorem — splitting as an exact sequence of abelian groups

**For every field K and h >= 2, the above sequence splits if and only if 4 does not divide h.** Equivalently, it splits exactly when gcd(g,r)=1.

In particular:
- Every odd height splits; both source and target have the previously identified invariant factors.
- Every height h congruent to 2 mod 4 (including h=2) splits.
- For each height divisible by 4, this specific pullback exact sequence is non-split even in the category of abstract abelian groups.

This statement concerns a section of the induced homomorphism on Weil divisor class groups; it does not assert or require a section of the finite ring morphism.

## Proof with the actual toric map

Use the unimodular Z-basis (e0,e1,a,b) of Z^4 employed in the preceding class-group proof. The complete principal-divisor relations for Cl(R_h) are h times all four vectors and a-b. Eliminating a, the **actual pullback map**, not merely an abstract isomorphism, is
```
Cl(R_h)       = (Z/h)[e0] ⊕ (Z/h)[e1] ⊕ (Z/h)[b],
Cl(C_h^can)   = (Z/h)[e0']⊕ (Z/h)[e1']⊕ (Z/g)[b'],
pullback      = (id, id, reduction mod g).
```
Indeed the cover lattice adds the relations i*a+j*b whenever i+j is divisible by g. After a=b in the source, these are exactly the relation g*b=0 in the target. Because g divides h, the target's last factor is Z/g. Thus the kernel is g*(Z/h)[b], of order h/g=r, agreeing with <[N_g]>.

A section exists precisely when the cyclic quotient q: Z/h --> Z/g admits a section. For g=1, q has the zero target and the obvious section. For general g dividing h, a section must send the generator 1 mod g to an element x mod h such that
```
x = 1 (mod g),       g*x = 0 (mod h).
```
The second condition is equivalent to r dividing x. Such x exists if and only if r is invertible modulo g, i.e. gcd(r,g)=1. For the present g in {1,2}, this fails exactly if h is divisible by 4.

For the nontrivial split-even case h=2k with k odd, an explicit section of the last coordinate is
```
1 in Z/2  |-->  k*[b] in Z/(2k).
```
It has order 2 and reduces to the nonzero class modulo 2. For 4|h, every element of order dividing 2 in Z/h is 0 or (h/2)[b], both of which reduce to zero mod 2; therefore no section exists. QED.

## Exact checks, interpretation and boundaries

Direct enumeration of the two conditions on x for all h=2,...,20 agrees with the theorem: non-split values are 4,8,12,16,20. The proof is uniform and integer-exact, independent of these finite checks, the characteristic of K, and separability of the cover.

The decomposition of the **target group** into invariant factors remains valid at non-split heights; the non-split statement refers to the **pullback short exact sequence**, not to an inability to decompose the target as an abelian group. This distinction also separates the class-group extension from any other previously discussed module/category extension.

Completed author-side subunit only. Independent reviewer admission, native Source/Activity linkage, formal Task closure, and transfer to native X6 geometry have separate authorization and mathematical requirements.
