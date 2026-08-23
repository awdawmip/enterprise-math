# CBRC F3R2 — Survivor Membership Predicate Driver Review

Status: `DRIVER_ACCEPTED / F3_F3R_CLOSURE`
Date: `2026-08-23`
Driver-ID: `EM-DVR-CBRC-F0-7C3A21`
Task-ID: `RS-CBRC-F3R2-SURVIVOR-MEMBERSHIP-PREDICATE-COMPLETION`
Accepted owner branch: `research/cbrc-f3r2-survivor-membership-predicate-completion`
Accepted owner head: `bb020ddc567bfc8b0a240bf3df0fd83ae7e1ad6d`
Taskbook source: `f4a98e4c0f9f8669f75e44ee1ef979236334b48a`

## 1. Driver verdict

`ACCEPTED`.

Hard target:

`BALANCED_MIXING_SURVIVOR_MEMBERSHIP_PREDICATE_CLASSIFIED = ACCEPTED`.

F3/F3R/F3R2 is now mathematically closed at the issued scope.

## 2. Accepted exact membership theorem

For a full two-slot additive automorphism on the accepted current carrier,

`M=(A,B,D)`

with

`A=[[a,b],[c,d]] in M_2(Z)`, `B in M_2(F3)`, `D in M_2(F3)`,

the exact survivor predicate is

`SURVIVOR(A,B,D)` iff

1. `det(A)=+1 or -1`;
2. `det(D)!=0 mod 3`;
3. `gcd(|a|,|d|)>1`;
4. `gcd(|b|,|c|)>1`.

There is no additional restriction on `B`.

Inside the ambient automorphism class this reduces to two Euclidean gcd tests.

Consequences accepted:

- membership depends only on the free block `A`;
- every surviving free block has exactly `81*48=3888` torsion/cross lifts;
- every nonsurviving free block has zero lifts;
- no torsion-sensitive-only operator survivor exists;
- the support-splitting union `union_{p!=r} S_{p,r}` is exactly the full free survivor set;
- there are no survivors outside all support-splitting strata.

## 3. Necessity audit

The decisive new proof is not tautological cone nonemptiness.

Every full admissible scalar `q` is reduced by the torsion-min envelope

`f(n)=min_{t in F3} q(n,t)`

to a torsion-blind free scalar satisfying the full free conservation identity and balanced values.

This kills the possibility that `(B,D)` rescues a bad free block.

Mixed differences of the free conservation identity, together with the inverse matrix, give four exact zero mixed-difference annihilators. Their Laurent-polynomial gcd is

`(T^g-1)(T^h-1)`

with

`g=gcd(|a|,|d|)`, `h=gcd(|b|,|c|)`.

Unimodularity implies `gcd(g,h)=1`. Evenness removes the repeated-root linear mode, forcing period `g*h`.

If `g=1`, balance forces the contradiction `f(c)=f(0)=0` versus `f(c)=1/2`. If `h=1`, the analogous contradiction is `f(a)=0` versus `f(a)=1/2`.

Hence `g>1` and `h>1` are necessary.

## 4. Sufficiency audit

If `g>1` and `h>1`, choose primes `p|g`, `r|h`. They are distinct.

Then `A mod p` is anti-diagonal monomial and `A mod r` is diagonal monomial. The accepted F3R support-splitting theorem supplies the explicit conserved balanced witness

`q_{p,r}(n,t)=1/2*(1_{p does not divide n}+1_{r does not divide n})`.

Because this witness ignores torsion, arbitrary `B` and invertible `D` preserve it.

Thus the gcd condition is also sufficient.

## 5. Second-column closure

For a fixed primitive admissible first column `(a,c)^T`, determinant sign `eps`, and one Bezout completion `(b0,d0)`, every completion is

`b=b0+k a`, `d=d0+k c`.

Successful completions are exactly the finite union of CRT progressions over prime pairs `p|a`, `r|c`:

`k in union_{p|a,r|c}(k_{p,r}+pr Z)`.

Therefore F3R's second-column gap is fully closed: not every unimodular completion survives, every admissible first column has infinitely many surviving completions, and there are no exceptional survivors outside these arithmetic progressions.

## 6. Decision-procedure acceptance

The final membership algorithm is finite and exact:

1. test `det(A)=+-1`;
2. test `D` invertible mod 3;
3. compute `gcd(|a|,|d|)`;
4. compute `gcd(|b|,|c|)`;
5. accept iff both gcds exceed one.

No scalar search, prime factorization, finite-box GL2 scan, downstream algebra, or numerical optimization is needed for membership.

Factorization is needed only if an explicit support-splitting witness or complete CRT stratum list is requested.

## 7. Evidence audit

Accepted checker:

`scripts/cbrc_f3r2_validate_survivor_membership.py`

Deterministic digest:

`5df55db542c5027adbd5ad1e3f9c9278b0cf1275a8e9ba6cf74be4c340f5696c`.

Manifest reports:

- theorem/enumeration mismatches: `0`;
- bounded GL2 regression: `1768` unimodular matrices;
- theorem-predicted survivors: `96`;
- admissible-first-column but nonsurviving examples: `800`;
- second-column CRT comparisons: `33184`;
- torsion-affine bijection checks: `34992`;
- all generated artifacts committed.

The bounded enumeration is accepted only as regression evidence; arbitrary-integer completeness rests on the theorem above.

## 8. Source / target-leak audit

`TARGET_LEAK_AUDIT_PASS` accepted.

No R063/R064/R065/FQ mathematics, downstream coherent-BRC/wave research, external quantum/wave theory, complex/quadratic selector, square norm, Hadamard/Fourier selector, or physical splitter target was used.

## 9. Scope boundary

This acceptance closes the F3/F3R survivor-membership program. It does **not** promote any mixing matrix or scalar law to Foundation truth.

The accepted result actually strengthens the underdetermination conclusion:

- the survivor set is exactly decidable;
- it is still infinite and contains infinitely many physically inequivalent mixing classes;
- the issued F3 axioms still do not select one quantitative scalar geometry.

Any further attempt to obtain a nondegenerate wave-like scalar must therefore introduce or derive an additional regularity principle.

## 10. Next Driver gate

Do not open downstream wave comparison yet.

The next forward question should test a target-independent nondegeneracy condition rather than select a familiar algebra:

`GLOBAL_ZERO_SEPARATION: z != 0 => q(z)>0`.

This condition was not an F3 premise. It must be treated as a new candidate regularity axiom and classified/falsified independently.

Recommended next stage:

`CBRC F4 — Positive-Separation Balanced Mixing Forward Classification`.

---

Driver closure:

`F3_EXISTENCE + F3R_STRICT_UNDERDETERMINATION + F3R2_EXACT_MEMBERSHIP = ACCEPTED_AND_CLOSED_AT_ISSUED_SCOPE`.
