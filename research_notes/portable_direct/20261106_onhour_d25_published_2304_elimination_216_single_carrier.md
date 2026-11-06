# D25 — published 2304 half-truncation theorem removes the 2304 side of the third-digit proof

Date: 2026-11-06. TASK_RESEARCH, author-side targeted prior-art intake and strict algebraic reduction; source class = **external published theorem + inherited frozen scalar interface + exact finite regression**. **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0**.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`. Immutable publication `TP2-B6F4FC938FF94941C1B7`; scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923` (not the maintenance conversation). Prior author-side highest frontier: bottom 216 two-jet and three exact nonzero jet endpoint identities, `research_notes/portable_direct/20261106_onhour_d25_bottom_216_jet_endpoint_telescope.md`, commit `3b5a162a9f8e6279630e4617f6bef540b02c7e8d`. Consume; do not reprove or recredit.

## 1. Verified primary literature and coefficient match

Victor J. W. Guo and Wadim Zudilin, *A q-microscope for supercongruences*, Advances in Mathematics **346** (2019), 329–358, DOI **10.1016/j.aim.2019.02.008**, arXiv **1803.01830** (abstract explicitly states both truncations). Primary manuscript: https://arxiv.org/abs/1803.01830 ; publication DOI: https://doi.org/10.1016/j.aim.2019.02.008 . Relation to this task: **ADOPT** previously published exact 2304 half-truncation theorem, **COMBINE** with frozen Enterprise Math scalar interface and already checked 216-shell identities. This author does **not** claim originality of Guo–Zudilin's theorem.

Define, for every prime p>3:
[
a_n=rac{(2n)!(3n)!}{216^n(n!)^5}
=rac{inom{2n}{n}^{2}inom{3n}{n}}{216^n},quad
b_k=rac{(4k)!}{2304^k(k!)^4}
=rac{inom{4k}{2k}inom{2k}{k}^2}{2^{8k}3^{2k}},
]
[
W_p=sum_{n=0}^{p-1}(6n+1)a_n,qquad
V_h=sum_{k=0}^{h}(8k+1)b_k,quad h=(p-1)/2.
]
Since `2^(8k)3^(2k)=2304^k`, the Guo–Zudilin half truncation `S((p-1)/2)` is **exactly** this frozen `V_h`, term-by-term, in `Z_(p)`. Their published theorem gives
[
oxed{V_hequiv pleft(rac{-3}{p}ight)pmod{p^3}qquad(p>3).}
]
For both frozen classes `p mod 24 in {13,19}`, `p mod 3=1`, hence the quadratic character `(-3/p)=+1`. Therefore
[
oxed{V_hequiv ppmod{p^3}quad(pequiv13,19pmod{24}).}	ag{GZ}
]

## 2. Strict reduction of the exact remaining third digit

Inherited source-aligned author-side scalar reduction (from the original immutable D25 task/source notes) is:
[
(W_p-p)/p^2equivDelta_p-R_ppmod p
]
on the two target residue classes, with the accepted first-digit premise `p² | (W_p-p)`. The earlier finite-transport author interface also asks for `W_p-V_h=0 mod p³`. Insert (GZ) into the *same* original-sum observer:
[
oxed{
W_p-V_hequiv0pmod{p^3}
 LongleftrightarrowW_p-pequiv0pmod{p^3}
 LongleftrightarrowDelta_p-R_pequiv0pmod p.}
	ag{E}
]
The last equivalence is **conditional on the inherited precisely matched scalar bridge and first-digit divisibility**; it makes no claim about native fixed H0/B0 Frobenius identification. This is a strict reduction to a **single original 216 hypergeometric carrier**, not an assertion of its unresolved congruence.

For `p=6m+1`, consume the existing valuation slicing `W_p=B_p+pM_p^*+p²U_p (mod p³)`, where `B_p=sum_{n=0}^{2m}(6n+1)a_n`. The open proof becomes
[
oxed{(B_p-p)/p+M_p^*+pU_pequiv0pmod{p^2}.}	ag{F}
]
Equivalently, reuse the proved bottom two-jet
`B_p=A_0-pA_1+(p²/2)A_2 (mod p³)` and the one-seed pair contribution:
[
oxed{
rac{A_0-p}{p}-A_1+rac p2A_2+
sum_{j=0}^{m-1}
left[(3p-2-6j)u_j+
rac{p(6j+4)}{36(3m-j)^3u_j}ight]equiv0pmod{p^2}.}
	ag{F'}
]
Here `u_j=a_{3m-j}/p` in `Z_(p)/p²`; the inverses and divisions are made in the p-local ring before reduction. The quotient `(A_0-p)/p` is p-integral by inherited first-digit theorem. All BRC observer labels (216 source, p, n/j, valuation shell, signed weights, zero/first/second jets, p-adic carry) persist. **The published theorem removes the original 2304 right-side boundary from the OPEN cancellation equation only at modulus p³ and within the frozen target classes**; the original V_h remains available as independently sourced evidence.

## 3. Exact finite regression, adversarial p^4 scope test

Executed the separate integer modular program
`d25_onhour_20261106_published_2304_single_carrier_check.py` (author-side reproducible attachment). For each of the **166 primes 5<=p<=997**, evaluated the two ORIGINAL sums in `Z/p^4Z`, using the exact invertible recurrences
[
a_{n+1}/a_n=(2n+1)(3n+1)(3n+2)/(36(n+1)^3),
]
[
b_{k+1}/b_k=(4k+1)(2k+1)(4k+3)/(288(k+1)^3).
]
For p<=23 an independently coded direct factorial/binomial formula matched each recurrence. Asserted `W_p == p*chi (mod p³)`, `V_h == p*chi (mod p³)`, and `W_p==V_h (mod p³)`; **166/166 passed (45 target primes), assertion failures 0**. This is finite confirmation, not proof of the still-open 216 statement.

Deliberate stronger-scope test: the coefficient `(W_p-V_h)/p³ (mod p)` is **nonzero** for p=13 (7), p=19 (9), p=373 (94). Thus the easy replacement of a p³ observer by p⁴ equality **fails on those exact inputs**. At p=13 the separate p³ coefficients of `W_p-p` and `V_h-p` are 9 and 2; at p=19 they are 12 and 3; at p=373 they are 228 and 134. This is a precise counterexample to the over-strong *mod-p⁴ equality*, not to the frozen mod-p³ LIFT target. Retain the higher p-adic digit if future operations require it.

## 4. Research choice, status, and exact next action

The formal Task hard target `Delta_p=R_p (mod p)` remains **OPEN**. After eliminating the independently proven V_h side, concentrate on the **single 216 carrier's cubic-digit telescoper**: derive a source-compatible WZ/parameter-jet identity for `(1+6 theta)F_m(z;t)|_{z=1,t=p}`, matching the already exact triangular three-jet boundary and the middle/upper one-seed complementary shell. Look first for a certificate producing the necessary p² vanishing of (F') at p=13,19, and then a proof uniform in both target classes. Avoid a further 2304 tail calculation unless a new observer actually demands it. The previously proved nonzero derivative endpoints must be kept.

BRC application: **COMPOSE_APPLIED**, population all original 216 n-indices and original 2304 k-indices, labelled prime-class and signed coefficient, with theorem-based quotient `V_h -> p` valid under the precise final mod-p³ observer and operation horizon. It is not a claim of information-lossless equivalence for mod-p⁴, native X6, Frobenius, or independent experimental operator. The fixed **p=373 native H0/B0 divided-power [X]U mod139129, rank, semilinear F/eta, kappa, odd Hesse/Green, and independent replication** remains **NOT_EXECUTED**, tracked in existing GitHub Issue #1559 (OPEN, no executor as of this run).

Source: previous request `d25-onhour-20261106-0701-recovery-read` was `SUCCEEDED/execution_authorized=false`. New exact read `d25-onhour-20261106-0805-exact-lane-read` was `QUEUED` at the last observation; retain original request id and reconcile later. No authenticated own CLAIM/open/run/Result from this note. Client scoped checkpoint is separate. Publication of this author-side note is not Source admission or independent review.
