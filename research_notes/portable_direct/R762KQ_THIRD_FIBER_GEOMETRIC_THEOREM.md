# R762KQ — Third-distinct M3 connected source fiber: geometric stabilization

Date: 2026-11-24 (Asia/Shanghai). Status: AUTHOR_ANALYTIC_PROOF_WITH_EXACT_RATIONAL_CERTIFICATE / NOT_REVIEWED.

## Immutable lineage and model
Continuing R762KP@07e3f06b98d15197249c1afd7c6fe7949bad7d9b, R762KO and R762KN; preserve the P000 scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389. This theorem is about the **unsigned auxiliary composite Port–Euler M3** model with inactive Ports 01,23,45. There are 12 active Port bits in order 02,03,04,05,12,13,14,15,24,25,34,35 and eight flexible supports (i,j,k)∈{0,1}³. Each flexible support chooses an unordered multiset of its three possible edge types of the common positive integer multiplicity m≥2. Let F be the 512-element forced-parity space and Q_m(b) count connected legal assignments with target b∈F.

Define the **third distinct fiber** as the third-largest *different numerical value* among the 512 values Q_m(b); it is not the third entry of the list of individual boundary codes. R762KO proved b=0 is the unique maximum for m≥2. R762KP determined the second-largest class: three full four-Port grids at m=3, and twelve adjacent-Port pairs at m=2 or m≥4.

## KQ.1: Exact classification for every integer m≥2

| m | Third distinct value | All achieving boundary codes | Geometry |
|---|---:|---|---|
| 2 | 1,792 | 15,240,785,1348,2696,3106 | 6 stars at individual original axis vertices |
| 3 | 63,360 | 3,12,17,34,48,68,136,192,768,1280,2560,3072 | 12 adjacent two-Port pairs |
| 4 | 1,653,372 | union of m=2 six stars and m≥6 six diagonals | 12 tied boundaries |
| 5 | 20,995,200 | 51,204,3840 | 3 full four-Port grids |
| all m≥6 | T_m below | 18,33,72,132,1536,2304 | 6 diagonals (opposite vertices) in three four-Port grids |

Write r=floor(m/2); define A=(r+1)(r+2)/2 and B=r(r+1)/2 for m=2r, and A=r(r+1)/2 and B=(r+1)(r+2)/2 for m=2r+1. Then for every m≥6,

**T_m = 4B⁸ + 12AB⁷ + 8A²B⁶ + 4A⁴B⁴ + 4A⁵B³.**

## KQ.2: Exact runner-to-third gap

For m≥6 the second-largest distinct value S_m is the adjacent-pair class and

**S_m−T_m = 2(A−B)⁴(A+B)²B² > 0.**

For m=2r≥6 this is r²(r+1)¹⁰/2; for m=2r+1≥7 this is (r+2)²(r+1)¹⁰/2. Hence S_m−T_m = m¹²/8192+O(m¹¹), Q_m(0)=m¹⁶/524288+O(m¹⁵), and (S_m−T_m)/Q_m(0)=64/m⁴+O(m⁻⁵). This is an exact asymptotic statement about auxiliary provenance-fiber counts, not a signed physical discrepancy estimate.

## Proof

Form the GF(2) group-algebra polynomial P_b(t)=[X^b] ∏_s(t+X^e_s1+X^e_s2+X^e_s3). Every unordered local multiset of multiplicity m has boundary-weight coefficients A (zero boundary) and B (each specified nonzero edge boundary). As established in R762KN–KP, all disconnected configurations are the three monochromatic quotient-edge configurations with zero target, so Q_m(b)=B⁸P_b(A/B)−3[b=0]. Direct exact group-algebra multiplication produces precisely 19 coefficient polynomials on the 512 forced boundaries.

Four required classes, with labels their smallest boundary codes, are:

- p₃(t)=6+8t+6t²+8t³+2t⁴+2t⁶, multiplicity 12;
- p₁₅(t)=4+8t+10t²+8t³+2t⁶, multiplicity 6;
- p₁₈(t)=4+12t+8t²+4t⁴+4t⁵, multiplicity 6;
- p₅₁(t)=8+16t²+8t⁴, multiplicity 3.

Against each of the other 16 nonzero polynomial classes excluding the known second class p₃, the exact verifier divides p₁₈−p_b by (t−1)² on rational intervals [3/5,1] and [1,2], and p₁₅−p_b by (t−1)² on [2,3]. All 48 resulting degree≤6 polynomials have nonnegative degree-six Bernstein coefficients on their respective intervals. In 46 comparisons all Bernstein coefficients are strictly positive; in the two remaining p₁₈/p₁₅ cross-comparisons the only nontrivial equality is t=2, by the identity p₁₈−p₁₅=−2t(t−2)(t−1)²(t+1)². Bernstein nonnegative basis functions establish dominance over full continuous intervals; this is not an inference from sampled m.

For every odd m≥7, A/B=r/(r+2)∈[3/5,1). For every even m≥6, A/B=(r+2)/r∈(1,5/3]. Accordingly p₁₈ uniquely dominates all non-top/non-second classes for m≥6. m=4 has t=2 and exactly the star/diagonal tie; m=2 has t=3 and p₁₅ is the unique next class. The remaining isolated ratios m=3 (t=1/3) and m=5 (t=1/2) are evaluated exactly for all 512 targets, yielding the specified p₃ and p₅₁ third classes. Finally, p₃(t)−p₁₈(t)=2(t−1)⁴(t+1)²; substitution yields KQ.2 and the asymptotics.

## Exact evidence and next question

R762KQ_THIRD_FIBER_VERIFY.py uses Python standard-library integers and fractions to independently regenerate all 12 Port bit positions, eight support incidences, 512 forced boundaries, 19 polynomial classes, 48 Bernstein comparisons, the four isolated cases and m=6..100 finite regressions. The rational interval proof covers *all* integers m≥2. The local detailed JSON evidence and output are recorded in R762KQ_THIRD_FIBER_EVIDENCE.json. Author check succeeded; independent review NOT_REVIEWED.

The calculated fibers are unordered **auxiliary edge provenance**. The native six-space Cell/Link/Port dynamics, signed TRIADIC_CLOSURE_E, explicit third slice coordinate, temporal order and BRC source carrier need distinct typed lifting. Next: construct a composable optimal fiber rank/unrank representation and test exact future-operation preservation, then a native signed/ordered lift with witnessed provenance.
