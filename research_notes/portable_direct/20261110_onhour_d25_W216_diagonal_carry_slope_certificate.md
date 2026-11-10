# D25/W216 — exact finite diagonal Frobenius carry witnesses

Date: 2026-11-10, Research-onhour lane. Status: **AUTHOR_SIDE / EXACT FINITE COMPUTATION / UNREVIEWED / NOT_ADMITTED / NATIVE H0/B0 NOT_RUN**.

Parent Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; **frozen scientific Source** `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged). Research conversation `chatgpt-research-onhour-enterprise-math-20260923` is separate from maintenance.

## 1. Original signed observer and discriminating question

Use the original, unmodified W216 coefficients
[
A_k=rac{inom{2k}{k}^{2}inom{3k}{k}}{216^k}, quad
W_n=sum_{k=0}^{n-1}(6k+1)A_k,quad
chi_p=egin{cases}1&pequiv1mod3,\-1&pequiv2mod3.end{cases}
]
Put (W_1=1). For (rge1), let
[
D_{p,r}=W_{p^r}-chi_ppW_{p^{r-1}},qquad
E_{p,r}=D_{p,r}/p^{3r}.
]
The quotient is a (p)-local integer at each finite tested input (verified in exact modular arithmetic). The prior author-side note proves two **counterexamples** to the overstrong assertion (E_{p,r}equiv E_{p,1}pmod{p^2}), with (p=13,19,r=2). Its new open conjecture was that the (p^2) observer stabilizes from (r=2).

The new test asks a different, more discriminating question: does the *newly exposed leading digit* at each transition have a scale-independent value? Precisely, is
[
E_{p,r+1}-E_{p,r}stackrel{?}{equiv}delta_p p^rpmod{p^{r+1}},
quad
delta_p=(E_{p,2}-E_{p,1})/pmod p?
]
This is a **candidate**, not a universal theorem.

## 2. Two-path exact finite certificates

Every table entry (E_{p,r}) is reduced modulo (p^d), with (d=5) for (p=13,19) and (d=3) for (p=37,43,61,67). All (D_{p,r}) were independently checked divisible by (p^{3r}) before division. The displayed (delta_p) is the exact observed quotient ((E_{p,r+1}-E_{p,r})/p^rmod p) at **each listed transition**.

| p | target p mod24 | precision d | (E_{p,1},E_{p,2},ldots,E_{p,R}pmod{p^d}) | R | (delta_p) | verified transitions |
|---:|---:|---:|---|---:|---:|---|
| 13 | 13 | 5 | 300777, 331470, 146077, 335019, 192214 | 5 | 8 | r=1,2,3,4 |
| 19 | 19 | 5 | 726059, 572843, 2024063, 2360154, 1317586 | 5 | 11 | r=1,2,3,4 |
| 37 | 13 | 3 | 45714, 32357, 44678 | 3 | 9 | r=1,2 |
| 43 | 19 | 3 | 34548, 8834, 16230 | 3 | 4 | r=1,2 |
| 61 | 13 | 3 | 115724, 132682, 32215 | 3 | 34 | r=1,2 |
| 67 | 19 | 3 | 30875, 265442, 40992 | 3 | 17 | r=1,2 |

**Finite exact statement:** For precisely these 16 ((p,r)) transitions, the congruence (E_{p,r+1}-E_{p,r}equivdelta_p p^rpmod{p^{r+1}}) holds; all six (delta_p) are nonzero. The valuation of each tested transition difference is therefore **exactly** (r). For p=13 and p=19 there are now 5 independently reconstructed power-scale terms reaching (13^5=371293) and (19^5=2476099), at (p^{20}) arithmetic precision. This extension is not a proof for arbitrary prime or arbitrary r.

An immediate *finite consequence* is stabilization (E_{p,r+1}equiv E_{p,r}pmod{p^r}) on these transitions, but the stronger displayed digit (delta_p) is the actual additional observation. Neither the (delta_p) nor the complete value (E_{p,r}pmod{p^{r+1}}) can be reconstructed from the previously published mod-p and mod-p² summaries alone.

## 3. Independent exact constructions and BRC observer

The checked script `d25_w216_carry_diagonal_20261110.py` uses two separately implemented original-coefficient paths:

1. Forward hypergeometric step `A[k+1]/A[k]=(2k+1)(3k+1)(3k+2)/(36(k+1)^3)` with per-step (p)-valuations and unit inverses.
2. Independently evolving (p)-unit factorial values of (k!, (2k)!, (3k)!), reconstructing `A_k=(2k)!(3k)!/(k!)^5/216^k`; denominator inversions use units only.

The two complete scale-residue arrays agreed in all 22 ((p,r)) cases (5+5+3+3+3+3). No floating point or non-unit inverse occurs. The second construction is not a native divided-power H0/B0 algorithm.

**BRC: COMPOSE_APPLIED.** Retained carrier ((p,r,k,v_p(A_k),u_p(A_k),6k+1,D_{p,r},E_{p,r}mod p^d)); operations: signed sum then (r)-transition then selected precision projection. The mod-p projection erases the nonzero scale-step digits; even mod-p² erases the r=2→3 and later leading transition digits. This explicitly records *which* information is lost and *when* it matters. It does not claim the W216 ring operator is the native six-axis coordinate dynamics.

## 4. Exact native and mathematical outstanding items

The original LIFT mother goal remains (Delta_p-R_pequiv0pmod p) for **both** target residue classes. The highest native evidence debt is still the **same-original-class** H0/B0 divided-power (p=373) object ([X]Umod139129), its actual module rank, source Frobenius semilinear direction, normalization (eta), odd signed (kappa), and independently replicated original (Delta_p-R_p) mapping. Existing support issue #1559 is OPEN and has no assigned executor at this read. These W216 computations are neither the native benchmark nor a surrogate passing that gate.

The next mathematical action is **not another unbounded prime scan**: derive or refute an explicit (p)-adic transfer bound for the difference (E_{p,r+1}-E_{p,r}), with the sharper digit condition as a separate target; prioritize the exceptional-factor p-block jets. A native authorized executor must separately materialize original H0/B0 inputs/outputs under the frozen pin, then submit them for independent review.

## 5. Control/source provenance and publication boundaries

Use the current Source continuation instead of resetting identity. Original request `onhour11-20261110-1936-exact-source` returned `SUCCEEDED` (source as-of `ee1d5709918327b02ba1920a9d62ae10d16179d6`); newest exact continuation request `onhour11-20261110-1957-exact-continuation` returned `SUCCEEDED` on current control Source `abf7c03205b83f96b114747e2fc326dbc3615cdb`. Research own `recovery_status` returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`; historical service-issued session `MCP-5378d3819d8947bda9049c9428493e2d` is not a private capability recoverable in this client. This note does not claim new native CLAIM, open run, Source checkpoint, formal Result or review. Maintenance conversation was not used for identity operations. GitHub author-side publication, if committed, is a distinct durability surface and remains **UNREVIEWED / NOT_ADMITTED**.
