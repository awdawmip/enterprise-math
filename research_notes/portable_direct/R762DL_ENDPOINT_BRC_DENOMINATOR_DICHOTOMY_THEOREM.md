# R762DL — Exact arithmetic dichotomy for endpoint BRC seed compression in the paired-triad area walk

Date: 2026-11-18. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Historical own researcher: EM-X6-3050F6; SID MCP-4b2d70a97f594366a7c94a0f8b45df38. Mathematical review: NOT_REVIEWED.

## Provenance, frozen substrate, and scope

Scientific inputs are unchanged: taskbook research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md at e3f42efac29a2da2d95be391f3231a664e2fade0; P000 V5 at a72226e2430ffa4786321ac86e7f0c599d5f0389; R762DI paired three-axis, six-step signed native X6 Cell-return candidate paths at c70993410d204fa9468f9755465d2002dfe36f6d; R762DD path-area cocycle; R762DJ/DK at fbd9a7cec4720528be9e7eee510770448d6a43e5. The full ambient native spatial basis remains six-dimensional with separate time; this paper works inside the explicitly fixed three-axis supported path family embedded in X6. The paths are candidates, not licensed primitive TRIADIC_CLOSURE_E balance events.

Each six-step block consists of two permutations of three nonzero signed axes with opposite total signed axis counts. It has 36 distinct *named* paths, each with positive integer BRC mass one. The ordered oriented area increment is even; let u=A/2 be its exact integer triple in this fixed support. Within the declared final-area readout, path name is pushed forward through the map to u; the raw name and order remain available in the original source population and must be retained whenever a future legal observer can distinguish them.

## Theorem — exact criterion for strict equal-seed endpoint compression

Fix any physical area modulus q>=2 and a positive block horizon k>=1. Set g0=gcd(q,2) and Q=q/g0. The reachable area group H_q=(2 Z/q Z)^3 is canonically identified with (Z/Q Z)^3 by the map u -> 2u mod q.

Let c_{Q,k}(r) be the number of the 36^k equally weighted *named* k-block paths whose final normalized area is r in (Z/Q Z)^3. Include zero counts when taking the gcd. Define

    G_Q(k) = gcd_{r in (Z/QZ)^3} c_{Q,k}(r);
    M_q(k) = 36^k / G_Q(k).

Then M_q(k) is the minimum number of equal-probability deterministic initial BRC seeds reproducing *only* the exact final-area probability distribution.

The complete arithmetic compression criterion is:

(A) If Q=1, G_Q(k)=36^k and M_q(k)=1.

(B) If Q>=2 is not a power of 2 or a power of 3, then for EVERY k>=1,

    G_Q(k)=1,  M_q(k)=36^k.

(C) If Q=p^a for p in {2,3}, a>=1, then G_Q(k) is a power of p and

    G_Q(k)>1  if and only if  2k>=Q.

More precisely, for all k>=1,

    p^{floor(2k/Q)} divides G_Q(k).

Thus, for this fixed positive-branch population, exact final-readout BRC compression occurs at some finite horizon if and only if Q=1 or Q is a pure power of 2 or 3. For Q=p^a the first strictly compressed horizon is k=ceil(Q/2); the exact higher p-adic exponent of G_Q(k) for arbitrary a,k is left open here.

## Exact group-ring representation

Set B={(0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1)}. This is the image of the six orientation vectors s in the prior R762DK support S under b=(s+1)/2, coordinatewise. For two independent six-way named choices b,b' in B, the normalized area is u=b+b'-(1,1,1). Define

    P(X,Y,Z) = 1+X+Z+XY+YZ+XYZ.

Work in the integral commutative group ring

    R_Q = Z[X^{±1},Y^{±1},Z^{±1}]/(X^Q-1,Y^Q-1,Z^Q-1).

Then the exact coefficient table of normalized final areas after k blocks is

    F_{Q,k}=(XYZ)^(-k) P(X,Y,Z)^{2k} in R_Q.

This is an identity of positive *named-branch* path counts, proved by expanding the six choices of each half-block in their preserved order and grouping the 36^k resulting names by the explicitly declared endpoint observer. It invokes neither classic geometric angle arithmetic nor unverified signed-force cancellation. Consequently the coefficients of F_{Q,k} sum to 36^k, and G_Q(k) divides 36^k. Only the primes 2 and 3 can divide G_Q(k).

A deterministic equal-seed model with M initial seed labels has outcome masses n_r/M for integers n_r. The requirements n_r/M=c_{Q,k}(r)/36^k are equivalent to 36^k dividing M*c_{Q,k}(r) for every r. Their common minimal positive solution is M=36^k/G_Q(k), establishing the stated optimality within the exact final-area observer language.

## Proof of the prime-power dichotomy

Fix a candidate prime p in {2,3}. Suppose Q has a divisor d>=2 relatively prime to p. Reducing exponents modulo d maps R_Q onto R_d; then reduce integer coefficients modulo p. Over the algebraic closure of the finite field F_p, the polynomials X^d-1, Y^d-1 and Z^d-1 have no repeated roots because p does not divide d. Their joint quotient ring is therefore a finite product of fields and has no nonzero nilpotents. The six distinct monomials of P, all with exponents 0 or 1 in each coordinate, remain distinct modulo every d>=2. Hence P is nonzero in that reduced quotient and P^{2k} is nonzero there for EVERY k>=1. Thus G_Q(k) is not divisible by p.

If Q>=2 is neither a pure 2-power nor a pure 3-power, it has for each p in {2,3} a divisor d>=2 relatively prime to p (take a prime divisor different from p; when p does not divide Q take d=Q). By the preceding paragraph neither 2 nor 3 divides G_Q(k), so G_Q(k)=1. This proves (B).

Now let Q=p^a, p in {2,3}. In the characteristic-p group ring, Frobenius gives

    P^Q = sum_{b in B} X^{Q*b1}Y^{Q*b2}Z^{Q*b3} = 6 = 0.

Thus in the *integral* group ring P^Q has all coefficients divisible by p. Writing 2k=Q*t+r with 0<=r<Q shows that the coefficients of P^{2k} (and of its monomial translate F_{Q,k}) are all divisible by p^t. In particular, 2k>=Q implies p divides G_Q(k).

Conversely, suppose 2k<Q. For p=2, specialize Y=Z=1. The image of P is 3(1+X), reducing to (X-1) in F_2[X]/(X^Q-1). With Q a power of 2, X^Q-1=(X-1)^Q in characteristic 2, so (X-1)^{2k} is nonzero for 2k<Q. Hence P^{2k} cannot be zero in the full characteristic-2 group ring and 2 does not divide G_Q(k).

For p=3, specialize Z=1. The characteristic-3 image is 2(X-1)(Y-1). With Q a power of 3, the quotient by X^Q-1 and Y^Q-1 is F_3[a,b]/(a^Q,b^Q) for a=X-1 and b=Y-1. The monomial (ab)^{2k} remains nonzero for 2k<Q. Thus P^{2k} is nonzero modulo 3 and 3 does not divide G_Q(k). For either pure p-power, the other prime in {2,3} is relatively prime to Q and is excluded by the first paragraph. Therefore G_Q(k) is a pure p-power, with p-divisibility occurring at precisely 2k>=Q. This proves (C). Statement (A) is immediate from the one-element group. QED.

## Examples, interpretation, and BRC retention boundary

The physical modulus q must first be converted to Q=q/gcd(q,2). This makes otherwise similar-looking moduli behave very differently:

| q | Q | First block horizon with strict final-area seed compression | Exact conclusion |
|---:|---:|---:|---|
| 2 | 1 | 1 | Every final area identical; M=1 |
| 3 | 3 | 2 | G_3(k)=3^{2k-2}, as in R762DJ |
| 4 | 2 | 1 | G_2(k)=2^{2k-1}, as in R762DJ |
| 6 | 3 | 2 | Same normalized observer as Q=3 |
| 8 | 4 | 2 | 2 divides G_4(k) exactly when k>=2 |
| 10 | 5 | Never | M=36^k for every k |
| 12 | 6 | Never | M=36^k for every k |
| 16 | 8 | 4 | 2 divides G_8(k) exactly when k>=4 |
| 18 | 9 | 5 | 3 divides G_9(k) exactly when k>=5 |
| 30 | 15 | Never | M=36^k for every k |

Even if a fixed-modulus endpoint law converges toward uniformity (R762DK), its *exact* rational denominators may retain the complete 36^k seed cost for all horizons. This is a sharp separation between mixing and exact equal-seed compression, not a statement about continuous random-number resources or approximate compression.

All conclusions concern the declared final modular area marginal of the fixed candidate six-step block population, and all individual names, sign paths and intermediate areas still exist in the uncompressed BRC representation. An enlarged observer reading trajectories, provenance, actual licensed events or interactions needs its own exact descent certificate before any state erasure. No TRIADIC_CLOSURE_E primitive license or physical BRC phase realization is asserted.

## Author verification and next scientific frontier

The companion R762DL_VERIFY.js reproduces 36 named one-block choices, computes exact BigInt endpoint distributions for normalized Q={2,3,4,5,6,7,8,9,10,12,16,18,25}, checks all total masses, gcd criterion, prime-factor restriction and p-adic lower bounds, and independently compares direct 36-way convolution against the coefficient table of P^{2k}(XYZ)^{-k} for Q={2,3,4,5,6,7,9}, k=1..4. Results and full configuration coverage are recorded in R762DL_EVIDENCE.json. These finite tests are author checks; the general theorem above is the symbolic proof. Mathematical independent review: NOT_REVIEWED.

Next: source-verify exact native TRIADIC_CLOSURE_E signed Cell/Link/Port event permission and V17/V29/V39 transport. If real licensed future events allow this block family, test whether they observe only final area or also intermediate area, path names or full 15-pair bivector. A further arithmetic direction within the existing candidate model is to calculate the exact exponent v_p(G_Q(k)) for Q=p^a, with the above guaranteed onset and lower bound as a reusable starting point.
