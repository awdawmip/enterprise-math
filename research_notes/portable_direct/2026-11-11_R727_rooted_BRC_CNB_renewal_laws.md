# R727 — Exact positive BRC renewal laws for the two sharp 15-arc CNB carrier classes

Date: 2026-11-11 (Asia/Shanghai). Independent author-side continuation of R723, R725, R726. Task context: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`; frozen scientific pin: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` (P000 V5). Input classification: R725 at `a9ba60cab51fc98e4b39f73e5d0eda7f49c51bb3`; reversal duality: R726 at `5ef47c8c33d09925c1d69119509cb6e0fbf904a1`.

**Scope:** Exact *positive rooted source-distinct cyclic nonbacktracking* (CNB) walk multiplicities in the derived five-axis V17 ordered-slot-triad model. A walk length is not a physical heartbeat time; the abstract triads are not full native Cell states. These are not original V29 Link/Port execution histories without a further typed realization. Mathematical proof and finite integer certificate are supplied; independent review is pending.

## Carrier and positive BRC observer

The ten vertices are 3-subsets of labels `01234`; sixty directed Johnson-neighbor arcs replace one axis. Root is `012` and the initial ordered frame is `012`. A history is an ordered directed closed walk `v_0=012,...,v_m=012` with cyclic nonbacktracking `v_(i-1) != v_(i+1)` at every index, including the closing seam. Positive histories remain source-distinct. The V17 slot-replacement law gives an S3 holonomy; the observer considered here **sums the positive counts over all six final holonomies**, and therefore does not claim to recover individual holonomy counts.

Select the two R725 canonical fifteen-arc masks under lexicographic ordering of all sixty arcs:

- Type A, orbits 1 and reverse 2: `211733226574`.
- Type B, orbits 3 and reverse 4: `5363347296468`.

The previous R726 theorem proves that reversal and root-preserving relabeling preserve this positive total within each type. Let `a_m,b_m` count their respective positive rooted histories.

## Theorem R727-A: exact rational generating functions

For each selected arc set E, construct the **15-state nonbacktracking arc operator**

`B_E[e,f] = 1` exactly when `head(e)=tail(f)` and `tail(e)!=head(f)`; otherwise zero.

Let `P_R` be the diagonal indicator of arcs leaving root `R=012`. A based closed m-step walk in this arc graph is in bijection with a rooted m-arc CNB history, including the seam restriction. Hence for all integers `m>=1`:

`a_m=tr(P_R B_A^m)`, `b_m=tr(P_R B_B^m)`.

Define the polynomials

`D_A(x)=1-3x^3-7x^4-8x^5-4x^6`,

`D_B(x)=1-3x^3-7x^4-8x^5-5x^6-x^7`.

Then, as **exact rational formal power series**,

`SUM_(m>=0) tr(P_R B_A^m)x^m = 2 + 1/D_A(x)`,

`SUM_(m>=0) tr(P_R B_B^m)x^m = 1 + 1/D_B(x)`.

The `m=0` terms on the left are the root outdegrees (3 and 2). Consequently, for **every m>=1**,

`a_m=[x^m]1/D_A(x)` and `b_m=[x^m]1/D_B(x)`.

### Proof, including an exact finite certificate

Integer Newton identities applied to traces of powers of the explicitly constructed 15x15 BRC arc matrices give

`charpoly(B_A;t)=t^9(t^6-3t^3-7t^2-8t-4)`,

`charpoly(B_B;t)=t^8(t^7-3t^4-7t^3-8t^2-5t-1)`.

Thus their determinants `det(I-xB)` are precisely `D_A,D_B`. By the adjugate formula, `det(I-xB)tr(P_R(I-xB)^(-1))` is a polynomial of degree <=14. Its complete coefficients are therefore determined by the exact traces for powers `m=0..14`, since `D(0)=1`. Convolution gives for A:

`(3,0,0,-6,-14,-16,-8,0,0,0,0,0,0,0,0)=coeff(2D_A+1)`;

and for B:

`(2,0,0,-3,-7,-8,-5,-1,0,0,0,0,0,0,0)=coeff(D_B+1)`.

This proves the claimed **unbounded** generating functions, not just a checked prefix. The verifier computes the Newton coefficients from integer power traces, checks the integer 225-entry Cayley–Hamilton identity for each matrix, checks the full numerator identity, and compares the original vertex-path recursion independently at lengths 3–8. QED.

### Corollary: positive weighted renewal

Set `u_0=v_0=1`, `u_m=a_m`, `v_m=b_m` for `m>=1`; all negative-index values are zero. Then, for every `m>=1`:

`u_m=3u_(m-3)+7u_(m-4)+8u_(m-5)+4u_(m-6)`;

`v_m=3v_(m-3)+7v_(m-4)+8v_(m-5)+5v_(m-6)+v_(m-7)`.

Equivalently the total counts equal the coefficients of weighted compositions with lengths/weights `{3:3,4:7,5:8,6:4}` and `{3:3,4:7,5:8,6:5,7:1}`. This **enumerative equivalence** does not assert a unique decomposition of physical executions into such blocks.

| m | a_m | b_m | gap |
|--:|--:|--:|--:|
| 3 | 3 | 3 | 0 |
| 4 | 7 | 7 | 0 |
| 5 | 8 | 8 | 0 |
| 6 | 13 | 14 | 1 |
| 7 | 42 | 43 | 1 |
| 8 | 97 | 97 | 0 |
| 9 | 163 | 169 | 6 |
| 10 | 309 | 329 | 20 |
| 11 | 721 | 751 | 30 |
| 12 | 1556 | 1608 | 52 |

The totals at m=4..12 reproduce the previous R726 S3-resolved counts summed over holonomy.

## Theorem R727-B: strict positive multiplicity dominance

Subtracting the two exact rational functions yields

`SUM_(m>=1) (b_m-a_m)x^m = (x^6+x^7)/(D_A(x)D_B(x))`.

Both reciprocal denominators have **nonnegative integer coefficients** as weighted compositions. Their product has positive coefficients at every degree n>=3, since every n>=3 is a sum of 3,4,5 (base n=3,4,5 and repeatedly add 3). Its coefficient at degree zero is 1, and at degrees 1,2 zero. Therefore, for `m>=3`:

**`b_m>=a_m`; equality holds exactly for m in {3,4,5,8}; strict inequality holds for m=6,7 and all m>=9.** QED.

Both classes realize all six Boolean S3 states at every length >=4 under R725, but have distinguishable exact positive BRC multiplicity. This is a concrete support-observer information loss example.

## Corollary R727-C: strictly different growth constants

Each `D=1-SUM_d w_d x^d` with `w_3,w_4,w_5>0` has exactly one smallest-modulus root `rho>0`: the positive root is unique and simple by strict monotonicity, and uniqueness on the circle follows by equality in the triangle inequality and gcd(3,4,5)=1. Hence the positive counts have exact asymptotic form

`a_m ~ C_A rho_A^(-m)`, `b_m ~ C_B rho_B^(-m)`, where

`C = 1/(SUM_d d*w_d*rho^d)>0`.

Since `D_B(x)=D_A(x)-x^6-x^7`, `0<rho_B<rho_A<1`; thus Type B has a strictly larger exponential growth constant. Exact integer sign checks show

`485450/1000000 < rho_A < 485451/1000000`,

`483131/1000000 < rho_B < 483132/1000000`.

These are count-growth laws, not inferred physical probabilities or energies.

## Reproduction, frontier and unproven bridge

The adjacent `R727_BRC_RENEWAL_VERIFY.py` uses Python standard library only, exact integer paths and matrices, explicit masks, Newton identities, Cayley–Hamilton and adjugate certificates; `R727_BRC_RENEWAL_RESULTS.json` records exact coefficients, tests and scope. Unbounded results follow the exact algebraic proof, not extrapolated finite checks. The native P000 six-axis force/balance axioms remain unchanged; the current combinatorial five-axis carrier is a derived research slice.

**Next discriminating units:** (1) lift the edge-state generating function to separately labeled S3 outcomes, identify minimal sufficient BRC observer state and possible asymptotic holonomy distributions; (2) for both orientation-free classes, provide original V29 Link/Port inventory/Cell/event-time witnesses for each allowed abstract arc or a sharp obstruction, then recompute the exact positive mass on the truly executable subgraph. Independent mathematical review and native Source Result admission remain pending.
