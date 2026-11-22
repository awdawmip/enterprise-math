# R5 scalar partition: first exact period contraction at threshold 37

Date: 2026-11-22. Status: **AUTHOR_EXACT_PROOF / EXACT_FINITE_FIELD_CERTIFICATE / NOT_REVIEWED**. This is independent portable research; no Task CLAIM/RUN, native Result or review is asserted.

## Frozen problem

The scientific model remains pinned to \`awdawmip/enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15\`. Prices are all integers 214,...,314, and a configuration is a vector \`a_p >= 0\` with total cost \`N = sum p*a_p\`. For fixed \`m >= 1\`, failure \`E_i\` means \`sum_{p in S_i} a_p < m\` for the five sets:

* S0 = {214,215,216,217,218}
* S1 = {214,216,217,218,219,220,221}
* S2 = {215,216,217,218,219,220,221}
* S3 = {223,...,290}
* S4 = {296,...,312}

Let \`F_m(q)=sum_N f_m(N)q^N=R_m(q)/D(q)\`, where \`f_m(N)\` counts configurations satisfying at least one failure and \`D(q)=prod_{p=214}^{314}(1-q^p)\`. The numerator uses the **exact joint constraints** for overlapping S0,S1,S2; it is not an independence approximation. Write \`M_m(O_m(N))\` for the least common coefficient period of terms of polynomial degree >=2 in the quasipolynomial \`f_m(N)\`.

## Theorem (first contraction, complete finite prefix)

Set

\`L=229746052653717600\`.

Then, in this fixed five-event scalar model,

\`\`\`
For every integer 1 <= m <= 36:
    M_m(O_m(N)) = L.
At m=37:
    M_37(O_37(N)) = L/43 = 5342931457063200.
\`\`\`

Thus 37 is the **first positive integer threshold** at which this precision's strict minimum period contracts. No claim is made here for m >= 38.

## Proof: global upper bound

At a primitive d-th root of unity, the denominator's pole order is the number \`n_d\` of multiples of d in [214,314]. Only poles of order >=3 can contribute terms of degree >=2. Exact integer enumeration yields 40 candidate orders:

\`1..32, 33,34,36,37,38,39,43,44\` (written distinctly: 1 through 34, then 36,37,38,39,43,44).

Their least common multiple is exactly L. Thus \`M_m(O_m(N))|L\` for every m >=1, without assumptions about prior author notes.

## Proof: exact finite-field witnesses for 1 <= m <= 37

A genuinely independent algorithm evaluates \`R_m\` and its Euler derivative \`DR_m=q*dR_m/dq\` at a **primitive d-th root in a finite field**, rather than computing the earlier cyclotomic integer vectors. For each witness order in

\`W={7,9,11,13,17,19,23,25,27,29,31,32,37,43}\`,

choose a rational prime \`P_d > 10000\` satisfying \`P_d == 1 (mod d)\`, and a certified root \`w_d\` of exact multiplicative order d in \`F_{P_d}\`. For every input threshold, compute the complete pair

\`(R_m(w_d), DR_m(w_d)) (mod P_d)\`.

Three disjoint price blocks split the failure-union numerator **without losing intra-core overlaps**:

\`R_m=1-(1-A_m)(1-B_m)(1-C_m)\`.

Here \`A_m\` is the seven-term exact inclusion-exclusion numerator of E0/E1/E2 on the 8-price core, while B and C are the single-event numerators on S3 and S4. The core intersection is enumerated by a DP indexed by each selected event's actual multiplicity counter; all constrained counts are between 0 and m-1. Values and Euler derivatives are propagated together with the exact jet product rule. Each S3/S4 finite generating polynomial is computed by complete-homogeneous-polynomial recurrence with unbounded multiplicities truncated at m-1.

Why a modular witness proves a complex pole: \`R_m(q)\` has **integer polynomial coefficients**, and \`w_d\` is a root of \`Phi_d\` modulo a prime \`P_d\` not dividing d. If \`R_m(w_d) !=0\`, then \`Phi_d\` cannot divide \`R_m\` over Q, so the complex numerator is nonzero at every primitive d-th root. If \`R_m(w_d)=0\` but \`DR_m(w_d)!=0\`, then \`Phi_d^2\` cannot divide \`R_m\`, so any zero at a complex primitive d-th root is at most simple. Therefore a valid **degree >=2 witness** is:

* \`n_d >=3\` and \`R_m(w_d) != 0\`; or
* \`n_d >=4\` and \`DR_m(w_d) != 0\`.

The routine proves every prime/root order and calculates these quantities by exact integer residues, so no floating-point or probabilistic zero test is used. For all 36 thresholds \`m=1..36\`, **all 14 witness orders pass**. Their lcm is L, matching the independent global upper bound. This proves every one of the first 36 equalities. At m=37, the 13 witness orders other than 43 pass; their lcm is L/43. The displayed 37th-threshold residues and verification program are in the companion files.

## Proof: remove the 43 component exactly at m=37

The vanishing cannot be concluded solely from observing zero modulo one finite-field prime. We use an exact cyclotomic identity, also appearing in the parent proof \`r5_root43_allthreshold_phase_20261122/RESEARCH.md\`, reproduced here to make the load-bearing step explicit.

At primitive order 43, only 215, 258, 301 among the prices are multiples of 43. Each event except E1 contains one of these multiples, so every inclusion-exclusion term except singleton I={1} has an explicit vanishing factor. Hence

\`R_m(zeta)=P_1(zeta)*Q_m(zeta)\`,

with nonzero \`P_1(zeta)=prod_{p in S1}(1-zeta^p)\`, and

\`sum_{m>=1} Q_m(zeta)t^{m-1}
 = 1/[(1-t)*prod_{a in {42,1,2,3,4,5,6}}(1-zeta^a*t)]\`.

The eight denominator factors are distinct factors of \`1-t^43\`. Therefore this generating function equals \`B(t)/(1-t^43)\` with **polynomial degree B=35**, so \`Q_37(zeta)=Q_38(zeta)=...=Q_43(zeta)=0\`. The denominator D has a triple zero at the primitive 43rd root; the numerator zero reduces it to a pole of order at most two at m=37, removing all degree >=2 contributions of primitive order 43. No other candidate d with n_d>=3 is divisible by 43. Thus the universal upper period for m=37 divides L/43. The independent 13 modular witnesses give its matching lower bound, proving the exact m=37 value.

## Evidence and scope

All 37*14 = **518 pairs** were recomputed by the local Python 3 exact-modular evaluator (frozen sets, no external packages). The 36 first thresholds have 14/14 witnesses; m=37 has 13/14 (order 43 intentionally absent). The full local exact output digest is

\`sha256(R5_O1_MODULAR_CERTIFICATE.json) = 2ae805b37e1022de3c72e75e944a7be028b66c19048309f08939c5ba722a39ef\`

for a canonical, sorted-keys, indented JSON encoding used during the run. The companion verifier regenerates the complete table rather than treating this digest as a proof. This is an **author-side finite computation accompanied by a correctness argument** and a self-contained analytic 43-cancellation proof; no independent reviewer has accepted it.

A sample \`m=37\` certificate at d=43 uses field P=10321, primitive root w=3215 and returns \`R=0, DR=6843\` mod 10321; the zero in this single reduction is a diagnostic, not the complex-vanishing proof. In contrast, at d=37 the field is P=10139, root w=1802, with \`R=1888, DR=9411\`. All 13 lower-bound witnesses have explicit modular residue rows in CERTIFICATE_SUMMARY.md.

## Source, method and next question

Read current account rules and the project's current normative context, and preserve P000/ACTIVE worldview as declared premises. The scalar partition model is a frozen **derived test model**, not the complete native X6 geometry. This work uses signed inclusion-exclusion, typed event membership, and exact residue/jet observers. It cannot replace them by positive-only BRC aggregate mass without losing cancellation information. Existing core overlap DP and the previously derived 43 root filter were reused at their exact interfaces; the finite-field evaluation is a distinct verification route.

The parent frontier is \`enterprise-math@c9329abecc9963667647a2774b351a33c0456b0a\`; this note refines the finite range and proves the first exact contraction. The next useful question is the **next contraction after 37**: test 38..43 with the same modular witness code and the exact 43 periodicity, then investigate 29, 32 and 37 prime-power phase functions to classify the period for arbitrary m. Keep the Activity association and any formal Task/result authorization separately scoped.
