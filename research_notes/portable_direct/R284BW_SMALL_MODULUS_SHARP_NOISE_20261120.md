# R284BW — A 35-bit exact single-read star-Port code with sharp radius 59/2

Date: 2026-11-20 (Asia/Shanghai). Research type: independent portable auxiliary algebraic result. Status: AUTHOR_PROVED / EXACT_EXHAUSTIVE_CHECK_PASSED / NOT_REVIEWED.

## Frozen provenance and exact model

Scientific predecessor: R284BV at immutable commit `630117e9b8e3fc7be964b4e5cb16e99c6917f43e`, path `research_notes/portable_direct/R284BV_RADIX_SEPARATED_DOUBLE_FROZEN_SHARP_NOISE_DECODER_20261120.md`, Git blob `d0bf424fc0b3a0d822755ece17ba2388143d4884`. Its earlier R284BU constant-cofactor formula is reused. The research changes only the finite-field encoder and decoder for the same frozen 4×4 star-Port observation. No new native X6/BRC observation or formal Task CLAIM is asserted.

Take all `C in {1,2}^{4x4}` (65,536 matrices), with fixed `d1=6,d2=13`. The observation before reduction is

```
F_C = det(diag(d0,6,13,d3) - C - z1 E01 - z2 E02 - z3 E03).
```

Read the residue modulo the explicit prime
```
p=34359738337  (35 bits)
d0=2905293013, d3=27976265365,
z1=618143958, z2=12373935123, z3=32899103541.
```
Noise is real circular additive measurement error with radius `rho`, i.e. a received point on the circle of circumference `p` lies within arc-distance `rho` of the true residue. Closed error balls are assumed.

## Exact finite theorem

**Theorem R284BW-1.** For the fixed controls above, the minimum circular distance between any two distinct matrix residues is **exactly 59**. Consequently, nearest-neighbor decoding uniquely recovers every one of the 65,536 matrices from one 35-bit residue subject to arbitrary adversarial circular error whenever `0 <= rho < 59/2`; the largest correctable integral error magnitude is 29.

Furthermore, with `d1=6,d2=13` frozen, *no choice* of other star-Port controls or prime modulus guarantees worst-case recovery of the entire matrix family for `rho >= 59/2`. Thus `rho < 59/2` is the sharp existence threshold for this fixed pair.

The construction gives a **35-bit communication versus finite-table decoding** tradeoff; it does not inherit R284BV's table-free radix decoder. A sorted residue-to-matrix table of 65,536 entries (or on-demand complete enumeration) is a valid decoder.

## Algebra and proof of the upper noise obstruction

Write rows of `C` as
```
[a,b1,b2,b3]
[u1,A11,x,y]
[u2,w,A22,z]
[u3,g,h,r].
```
Let `T=6-A11,S=13-A22,U=T*S-x*w`,
`p1=S*u1+x*u2,p2=T*u2+w*u1`, and `q3=U*u3+p1*g+p2*h`.
For every choice of the free controls, the only dependence on `b3=C03` is `-b3*q3`. The R284BU extremal cofactor theorem gives
```
min_C q3 = 6*13-(6+13) = 59.
```
The same lower and upper values 59 and 196 are independently established by the exhaustive checker in this finite model. There are two matrices differing only by a unit in `b3` whose integer observations differ by exactly 59 for every free-control choice. After reduction modulo any prime their circular distance is at most 59. If `2*rho >= 59`, their closed circular error balls overlap; uniform unique decoding is impossible. The exhibited pair is also retained below.

## Sufficient direction: reproducible finite certificate

For `U,V,p1,p2,q1,q2,q3,J,K` use the exact formulas in the companion standard-library checker, independently cross-checked against a direct 24-permutation Leibniz determinant. It evaluates the stated controls for **all** `2^16` row-major matrices, reduces modulo the asserted prime, sorts all 65,536 residues, and checks every consecutive difference including the cyclic wrap from maximum back to minimum plus `p`.

The exact result is
```
p is prime (trial division up to floor(sqrt(p))).
Number of matrices:              65536
Distinct nonconstant signatures: 32768
Each signature fibre:            exactly 2, differing only at C03
q3 range:                       [59,196]
Minimum cyclic distance:        59
Number of cyclic gaps equal 59: 64
Independent direct determinants: 256
Nearest-neighbor tests:          196608 (all C, errors -29/0/+29)
```
The lexicographic row-major list of 65,536 unsigned 64-bit big-endian residues has SHA-256
`91cd91d431cdf4557a5db891e0fd97559e6fba6a9bee10a6351a03797059cc44`.

One minimum-gap adjacent pair has residue `676834187` for
`(1,2,1,2, 1,2,2,1, 1,2,2,2, 1,1,1,1)`,
and `676834246` for
`(1,2,1,1, 1,2,2,1, 1,2,2,2, 1,1,1,1)`.
Its only difference is `C03`, so the upper bound is visibly attained.

These exact finite checks certify all 65,536 candidate residues, rather than relying on a random-sampling argument or a claimed global algebraic injectivity theorem. The 256 independent determinant checks are an additional implementation crosscheck, not a substitute for the complete coefficient-based census. The observed minimum circular separation of 59 proves robustness to **every real** error radius strictly below 29.5, including untested noninteger errors.

## Comparison, representation tradeoff, and next open work

R284BV's symbolic general-H and table-free deterministic construction used a sufficient modulus bound of approximately 833 bits for its explicit H=2 example, accommodating integral noise up to 227,082,239. R284BW supplies a different H=2 instantiation with a 35-bit modulus and a 65,536-entry decoder table, accommodating integral noise up to 29. These are different noise requirements and decoding costs, not a same-specification bit-length comparison. The counting lower bound for a circle code with 65,536 centers and minimum separation 59 is `p >= 65536*59=3866624` (22 bits). Our explicit witness leaves a gap from 35 to that 22-bit packing bound. No optimality claim is made for 35 bits.

The `32768` two-element fibres at the *nonconstant-signature* level retain the distinguished directed edge `C03`; the constant-slot value resolves the fibre at this observer and error horizon. This is a scope-typed residual-retention certificate, not a native X6 embedding, physical-time observation, or general lossless state compression.

Useful next question: find a prime with fewer than 35 bits and an explicit complete-distance certificate for this fixed `d1,d2` pair, or replace the 65,536 lookup with a much smaller algebraic decoder while retaining the 35-bit channel. General-H and higher-dimensional versions remain open. Search controls were found computationally and then fixed; the published verification is independent of their discovery randomness.

Contributor provenance: prior portable scientific line historically labelled `EM-DIRECT-E6B1DD`. Current native Researcher/SID is not authenticated by this GitHub artifact. Formal CLAIM, Activity association, independent Review, and Result promotion are not asserted.
