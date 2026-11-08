# PREFIX-602-R2 — Native X6-BRC mixed-source Krylov theorem and complete two-source census

Date: 2026-11-08. Author-side exact research, independent review pending. Scientific input frozen at awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Continues PREFIX-599/601 from immutable research commit 8ae854a05c0fb8b4c3821293ae25187437f01923, without repinning the source. P000/ACTIVE worldview are unchanged.

## Model / provenance / scope

Keep the original 48 native X6-BRC phases, 96 bit-ports, 576 typed actions, the four STAR triples (1,3,6),(1,4,5),(2,3,5),(2,4,6), and the original gate target phase g=4. At the established zero-axis boundary with six weights (1,1,1,1,0,0), use the *post-first-step* 48-phase nonnegative tail operator Q(z) from PREFIX-599, with row i and three original successor phases N(i):

- If absolute final native axis of phase i is 5 or 6, row i is zero.
- If i=g, Q(i,j)=1 for j in N(i).
- Otherwise Q(i,j)=2 for j in N(i), j not g; where g is in N(i), Q(i,g)=z+3.

Gate z is real nonnegative; this is a typed discrete BRC tail, not a general non-BRC numerical propagator. The source vectors e_j are right-source phase basis probes, and the observer is the full 48-component vector Q(z)^n v at every n>=0. Mapping a general probe to a nonnegative original 96-port initial state requires the previously proved encoding image test and is not presumed.

Let mu_v(t) be the *least-degree monic annihilator* of v under Q(z). Write s=4z+12.

## Theorem 1 — exact mixed-source recurrence changes for all nonnegative gate z

For every real z>=0, define these four NONNEGATIVE source mixtures:

| v | Individual source degrees (z≠1) | mu_v(t), z≠1 | degree | mu_v(t), z=1 |
|---|---|---|---|---|
| e0+e36 | 5+5 | t(t-2)(t+2) | 3 | same, degree 3 |
| e0+e18 | 5+5 | t(t-2)(t²+4) | 4 | same, degree 4 |
| e0+e4 | 5+5 | t(t⁴-16)(t⁴-s) | 9 | t(t⁴-16), degree 5 |
| e8+e11 | 10+10 | t²(t-2)(t²+4)(t⁴-s) | 9 | t²(t-2)(t²+4), degree 5 |

The native phase indices are zero-based in the frozen STAR ordering. Thus a nonnegative sum can have lower or higher recurrence order than its individual summands. The general lcm(mu_u,mu_v) only bounds mu_(u+v) from above; cancellations in common primary components determine whether equality holds.

## Proof / reproducible exact certificates

The accompanying executable reconstructs Q(z) with entries in Z[z], and for each pair checks all 48 entries of mu_v(Q(z))v = 0 *symbolically*. For the four sources respectively, it extracts an exact full-rank minor from the 48×d Krylov matrix [v,Qv,...,Q^(d-1)v]. The four determinants are:

1. e0+e36, d=3: -8.
2. e0+e18, d=4: 64.
3. e0+e4, d=9: 8388608 (z-1)^4 (z+3)^4.
4. e8+e11, d=9: -4194304 (z-1)^4 (z+3)(z²+10z+37).

All four are nonzero for their claimed gate ranges: z+3>0 and z²+10z+37=(z+5)²+12>0. Each upper annihilator and nonzero lower Krylov minor therefore establish the exact minimal degree. At z=1, explicit exact rank checks and special-annihilator checks give degrees 3,4,5,5. In particular, a pair of individually sharp degree-10 sources can collapse to degree 9 throughout every nonunit nonnegative gate value, while a pair of degree-5 sources can expand to degree 9.

## Theorem 2 — complete finite fixed-gate equal-weight pair census

For every unordered pair 0<=i<j<48, form v=e_i+e_j: there are exactly C(48,2)=1128 such inputs. The script computes exact rational ranks of their first m Krylov columns at the fixed integer gates z=1 (m=6) and z=2 (m=10). These m values are the established sharp matrix minimal polynomial degrees; the checker additionally verifies their matrix annihilator identities.

| sharp recurrence degree | z=1: number of pairs | z=2: number of pairs |
|---|---:|---:|
| 1 | 120 | 120 |
| 3 | 7 | 6 |
| 4 | 30 | 20 |
| 5 | 387 | 326 |
| 6 | 584 | 228 |
| 8 | 0 | 16 |
| 9 | 0 | 80 |
| 10 | 0 | 332 |
| **Total** | **1128** | **1128** |

The checker uses integer fraction-free Gaussian elimination with gcd normalization, preserving exact rank over Q. This is a complete finite two-gate classification, not an interpolation claim for other gates. Symbolic results in Theorem 1 have the separately established all-z scope. Representative ranks were cross-checked using SymPy's independent exact rational rank routine.

## Scientific use and next problem

For stationary rational z and a chosen v, the sharp degree d permits t^n mod mu_v(t) fast-jump propagation using only d native typed tail iterates to recover the whole 48-phase observer. This gives exact order reductions for the constructed families. Complete 96-port original input encoding, polynomial preprocessing, bit-growth, and full endpoint decoding remain part of the end-to-end algorithm evaluation. No physical time or heartbeat acceleration is claimed.

**Next:** derive a parameter-uniform primary-component/projector rule that classifies *all* 1128 pair sums as a function of z, identifying exceptional gate curves without separate ad-hoc minors; then determine which useful mixtures are nonnegative-reachable from native 96-port inputs and compare full reuse/encoding/decoding costs.

Evidence files: PREFIX602_R2_mixed_source_exact_checker.py (source), PREFIX602_R2_mixed_source_exact_results.json (all four symbolic lower-minor/pivot certificates and both exhaustive rational census outputs). Execution performed with SymPy exact polynomial/integer arithmetic; no pi/trigonometric/exp/Taylor fallback. Result status: AUTHOR_SIDE_EXACT_CHECKED; not Native Result or Driver acceptance.
