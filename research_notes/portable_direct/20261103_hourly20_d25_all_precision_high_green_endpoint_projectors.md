# D25 — Exact all-precision high-strip Green rank-three normal form and directed endpoint projectors

Date: 2026-11-03 (+08). TASK_RESEARCH **author-side portable mathematics**, UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING; not native Source checkpoint/Result/Claim. Logical lane: `chatgpt-research-hourly-enterprise-math-20260923` (not maintenance). Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; original frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Mother target for p mod24 in {13,19}: the original signed W_(p−1) equals p mod p³.

## Exact theorem A: all-order source-oriented rank-three quotient

Use the original factorial source, not a reciprocal surrogate:
[
b_k=rac{(2k)!(3k)!}{(k!)^5,216^k},quad
A(k)=(2k+1)(3k+1)(3k+2)=18k^3+27k^2+13k+2,quad
rac{b_{k+1}}{b_k}=rac{A(k)}{36(k+1)^3}.
]
For any prime p=6r+1≥7 define k_s=3r+1+s=(p+1)/2+s, 0≤s≤r, and Y_s=b_{k_s}/p² in Z_(p). Legendre valuations are 2 for 0≤s<r, and 3 for s=r. In the ring Z_(p)[s] define

[
oxed{mathscr D_pP(s)=rac{A(k_s)}{36}P(s+1)-k_s^3P(s).}
]

For every p-integral polynomial P, **exactly**, not merely modulo p²,
[
oxed{sum_{s=0}^{r-1}(mathscr D_pP)(s)Y_s
=k_r^3P(r)Y_r-k_0^3P(0)Y_0.}	ag{A}
]
Proof: the summand equals (k_s+1)^3P(s+1)Y_(s+1)-k_s^3P(s)Y_s by the original rational ratio. Summing telescopes.

For any N≥1 and R_N=Z/p^NZ, the operator raises the degree of any nonzero P of degree m by exactly 3, with leading coefficient multiplied by -1/2, a **unit** for p≥7: A(k_s)/36 has leading coefficient 1/2 while k_s³ has leading coefficient 1. Hence repeated leading-term elimination proves a unique decomposition for every W∈R_N[s]:
[
oxed{W=mathscr D_pP+d_0+d_1s+d_2s²,quad
R_N[s]=operatorname{im}mathscr D_poplus R_N{1,s,s²}.}	ag{B}
]
This holds also over Z_(p). Uniqueness works despite possible zero-divisor leading coefficients because multiplication by a unit is injective. Writing M_j=∑_(s=0)^(r-1) s^jY_s,
[
oxed{sum W(s)Y_s=d_0M_0+d_1M_1+d_2M_2
+k_r³P(r)Y_r-k_0³P(0)Y_0.}	ag{C}
]
For P=1, letting K_j=∑ k_s^jY_s, a concrete exact cubic certificate is
[
-18K_3+27K_2+13K_1+2K_0=36(k_r³Y_r-k_0³Y_0).
]
The **original signed high contribution** is
[
oxed{H_2(p)/p²=sum(6k_s+1)Y_s=(3p+4)M_0+6M_1.}	ag{D}
]

## Exact theorem B: independent original-source boundary ports

Since 0<r<p, the two p-integral linear polynomials
[
P_{m in}(s)=1-s/r,qquad P_{m out}(s)=s/r
]
satisfy opposite endpoint conditions. Their explicit degree-four polynomial weights are
[
W_{m out}(s)=rac{A(k_s)(s+1)/36-k_s³s}{r},qquad
W_{m in}(s)=A(k_s)/36-k_s³-W_{m out}(s).
]
Equation (A) gives two independent directed exact flux certificates:
[
oxed{sum W_{m in}(s)Y_s=-k_0³Y_0},quad
oxed{sum W_{m out}(s)Y_s=k_r³Y_r}.	ag{E}
]
They work at **every p-adic precision**, with no additional singular weight factor. These artificial projector weights are distinct from the signed weight (D); the latter's remaining interior moments must be matched by a genuine cross-band relation.

The earlier three-moment Gosper construction applies to original polynomial observers globally. This result explicitly specializes it to the original normalized high strip at **all p-adic orders**, and adds directed endpoint projectors. The prior rank-four Hensel theorem `5123cbd3...` is for the different rational observer W(s)Y_s/(2s+3) modulo p². These are different observer classes, not conflicting claims.

## Executed certificate and BRC preservation

The companion stdlib checker uses the original p-free factorial-unit arithmetic, verifies exact recurrence (A), both endpoint projectors (E), arbitrary high monomial weights degrees 3..10 by coefficientwise normal form, and the original signed observer (D), all modulo p⁴. A separate expanded local checker also cross-checks p≤37 against direct original integer binomial coefficients modulo p⁶. Actual execution passed **148 primes, 7≤p≤2000, p mod6=1; 22,952 oriented high-strip positions**. Samples (p, entrance mod p⁴, exit mod p⁴, H₂/p² mod p): (13,7295,25246,10), (19,21152,66291,9), (373,2860891407,11524594801,266). Finite regression is supplementary to the exact algebraic proof; independent formal review has not occurred.

BRC observer retains the original factorial source, oriented k_s, valuations, chosen precision, weight class, and *separately* typed entrance and exit; this polynomial rank concerns an auxiliary scalar observer, not P000's native six-dimensional space.

## Next executable mathematical unit / control boundary

Apply (E) at the original 2r/3r/4r cutoffs in a genuinely p-dependent **signed** low/middle/high Green–WZ ansatz. Preserve all physical signed interior moments from (D) and test exact remaining endpoint/residual equations at p=13,19,373 before asserting universal LIFT. Do not redo D24 first digit, previous original-four-source middle carry, or onhour block two-jet. Frozen mother congruence remains open. Gateway 0.6.11 at 2026-11-03 returns UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, active jobs 5/5. Historical #6637 read-only recovery and terminal failed #6638 remain unchanged; control support #1558. This is author-side research evidence, not a newly authorized native Research run or checkpoint.
