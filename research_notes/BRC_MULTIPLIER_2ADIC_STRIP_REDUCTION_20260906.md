# BRC Multiplier 2-adic Strip Reduction — Round 8

Status: `PROVED EXACT STRIP NORMALIZATION / COMPLETE UNIVERSAL 2-ADIC CLASSIFICATION / CLASSICAL CONGRUENCE CONTENT / NO LEHMAN IMPROVEMENT CLAIM`
Date: `2026-09-06`
Parents: `t0.brc_admissible_multiplier_scan`, `t0.brc_multiplier_vertical_wheel`

## 1. Question

After opening the two-dimensional `(m,t)` search, can an entire multiplier strip be removed rather than merely sieving individual t positions?

For odd N, yes for one exact 2-adic family.

## 2. Complete universal classification

Let `C=mN` with N odd.

### Case A: `m == 2 (mod 4)`

Then `C == 2 (mod 4)`. Integer squares are only 0 or 1 modulo 4, so no difference of two squares is 2 modulo 4.

Thus the strip is impossible.

### Case B: `m == 4 (mod 8)`

Then `C == 4 (mod 8)`. If `x^2-y^2=C`, examination of square residues modulo 8 forces x and y both even. Put `x=2X`, `y=2Y`. Then

`X^2-Y^2=(m/4)N`.

So every hit on the m strip is a square-scaled hit on the parent strip m/4.

### Case C: m odd or 8|m

No universal factor-two reduction is forced.

- For odd C, the identity `C=((C+1)/2)^2-((C-1)/2)^2` gives an opposite-parity representation.
- For 8|C, writing `C=8a` gives `C=(2a+1)^2-(2a-1)^2`, an odd/odd representation.

Therefore the previous two cases are the complete universal 2-adic classification.

## 3. Exact bounded-window offset law

Suppose m==4 mod8 and a square hit occurs at

`x=ceil(sqrt(mN))+t`.

Write m=4h. After dividing x,y by 2, the parent x-coordinate is X=x/2. Let

`a=ceil(sqrt(hN))`, `b=ceil(2sqrt(hN))`.

Since `b` is either `2a` or `2a-1`,

`t = 2(X-a)` or `2(X-a)+1`.

Hence the parent vertical offset is exactly

`T_parent=floor(t/2)`.

Consequences:

- in a common finite window `0<=t<T`, every child hit maps inside the same parent window;
- more generally the child strip is safely covered whenever the parent window contains all offsets through `floor((T_child-1)/2)`.

The gcd factor witness is preserved because N is odd:

`gcd(x±y,N)=gcd(2(X±Y),N)=gcd(X±Y,N)`.

## 4. m<=100 reduction

Among the first 100 positive multipliers:

- 25 are impossible (`m==2 mod4`);
- 13 more are redundant-by-four (`m==4 mod8`):
  `4,12,20,28,36,44,52,60,68,76,84,92,100`;
- 62 remain 2-adically primitive for this universal test.

Thus the BRC rectangle normalization is

`100 raw strips -> 75 difference-of-squares admissible strips -> 62 universally nonredundant 2-adic strips`.

For a common vertical horizon this reduces strip area by exactly 13/75 = 17.333...% relative to the Round-6 admissible grid.

Finite Python probes of the already-wheel-sieved rectangle showed additional wall-clock gains of roughly 1.1x..1.2x in representative 512..2048-bit / t=100000 runs; those timings are implementation diagnostics only.

## 5. Relation to classical Lehman congruences

This is not a new Lehman factoring theorem. Lehman's original `x^2-y^2=4kN` inner loop already imposes parity/mod-4 congruences and uses step 4 for odd k rather than the even-k step 2. The present strip normalization is the same elementary 2-adic content expressed in the project's arbitrary-multiplier BRC coordinates.

So the value here is **canonicalization and no-duplicate-work discipline inside the BRC tool**, not a claim that classical Lehman missed these congruences.

## 6. Executable certificate

`src/enterprise_math/brc_multiplier_strip_reduction.py` exposes:

- `multiplier_strip_class(m)`;
- `strip_reduced_multipliers(max_multiplier)`;
- `reduce_square_hit_to_parent(N,m,t)`;
- `two_adic_strip_counts(max_multiplier)`.

The reduction witness reconstructs both source and parent differences of squares and certifies `parent_t=floor(t/2)`.

## 7. Validation

Repository tests cover:

- exact counts 25 / 13 / 62 through m<=100;
- bounded exhaustion of the impossible class;
- bounded exhaustion of square hits on every redundant m<=100 and exact mapping to m/4;
- offset-halving and x/y-halving identities;
- representative class boundaries.

Independent exploratory enumeration mapped thousands of small-domain hits with no exception to the halving law.

## 8. Next frontier

This closes the **universal 2-adic strip-pruning** question. No further entire-strip deletion can follow only from forced powers of two, because the primitive counter-representations above exist for the remaining classes.

To shrink the rectangle further one needs information beyond fixed 2-adic type: a finite-horizon theorem, cross-multiplier factor-ratio certificate, or a growing modular/sieve structure. Fixed residue wheels continue to give only point/offset pruning and cannot by themselves change the classical search exponent.
