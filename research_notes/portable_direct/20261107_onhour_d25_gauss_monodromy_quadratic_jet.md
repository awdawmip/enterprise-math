# D25: Gauss-pullback monodromy obstruction and the first necessary quadratic jet (2026-11-07)

Status: AUTHOR_SIDE_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. This is NOT a Source Result, a native p=373 benchmark, or an independently reviewed theorem.
Research logical lane: `chatgpt-research-onhour-enterprise-math-20260923` (not the maintenance lane).
Mother task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, **unchanged frozen scientific pin** `c47e13e4aba0e006366f989d6334d443f6333ae3`.
Consumed author-side source: `20261107_onhour_d25_heun_period_gate_signed_jet.md` (commit `4020b5d8be7d1bfb8f9673d65f2331407609c476`), especially the period candidate, the p=19 scalar-transfer counterexample and the p=4 tail decomposition. No native experiment is claimed.

## Theorem A: no single rational pullback of the full Gauss equations, in either direction

Define
[
F_A(z)={}_2F_1(1/6,1/3;1;z),quad
F_B(w)={}_2F_1(1/8,3/8;1;w).
]
Their squares at (z=1/2) and (w=1/9) respectively give the unweighted 216 and 2304 periods by Clausen's identity.

**Statement.** There is no nonconstant rational function (phi) and nonzero algebraic scalar gauge (lambda) for which the entire rank-two Gauss differential equation of (F_A) becomes that of (F_B) (or conversely) under a one-legged pullback (z=phi(w)) and (Ymapstolambda Y). This statement concerns **equivalence of the full differential equations**, not a possible identity at the two specified arguments, not an arbitrary correspondence with two maps, and not a finite-sum mod-(p^4) congruence.

**Proof.** The Gauss equation (z(1-z)y''+[c-(a+b+1)z]y'-ab y=0) has local exponent differences
((1-c,c-a-b,b-a)) at (0,1,infty). For (F_A) these are ((0,1/2,1/6)); for (F_B) they are ((0,1/2,1/4)). Consequently, the finite projective local monodromy orders are (2,6) for (A), versus (2,4) for (B); the zero exponent-difference singularity has nontrivial unipotent/infinite projective monodromy in both cases.

Under a nonconstant rational pullback, local monodromy around a point of ramification index (e) is conjugate (up to a scalar) to the (e)-th power of the local monodromy at its image. Hence a finite projective local monodromy order of a pullback must divide the source equation's original finite order; a pullback of a regular point is projectively trivial. A pullback of (A) therefore cannot contain local projective monodromy of order (4), which (B) requires. A pullback of (B) cannot contain order (6), which (A) requires. Algebraic scalar gauges do not change projective monodromy. Both directions are impossible. QED.

**Constructive change of route.** A common *two-legged* orbifold covering (if one exists) can avoid this obstruction. The triangle-orbifold Euler characteristics are (chi_A=1/6+1/2-1=-1/3) and (chi_B=1/4+1/2-1=-1/4). For an unramified orbifold common cover with degrees (d_A,d_B), multiplicativity forces (d_Achi_A=d_Bchi_B), i.e. (4d_A=3d_B), hence ((d_A,d_B)=(3h,4h)). This is a **necessary conditional degree filter, not an existence or minimality proof**. A surviving order-two point over (A)'s order-six point requires ramification index (eequiv3pmod 6); over (B)'s order-four point it requires (eequiv2pmod4). Thus the next algebraic search is a two-legged Heun/modular correspondence, not another one-legged rational argument substitution.

## Theorem B: a unique non-base-field first jet is required at p=19 and p=373

Write
[
a_k=inom{2k}{k}^2inom{3k}{k}216^{-k},quad
b_k=inom{2k}{k}^2inom{4k}{2k}2304^{-k},
]
[
A_p=sum_{k<p}a_k,quad B_p=sum_{k<p}b_k,quad
D_{B,p}=sum_{k<p}k,b_k.
]
All finite sums are evaluated in (mathbb Z/p^3) with (p>3). For (p=19,373), (2) is a quadratic nonresidue. Set (E_p=mathbb F_p[s]/(s^2-2)) and (ho=3s/4). Since (A_p,B_pin p^2mathbb Z/p^3) and (D_{B,p}in p(mathbb Z/p^3)) with (D_{B,p}/p
e0mod p), the relation
[
 A_pequiv ho B_p+p,mu_p D_{B,p}pmod{p^3}
]
determines a **unique necessary coefficient** (mu_pin E_p):
[
 mu_p=rac{(A_p/p^2)-(3s/4)(B_p/p^2)}{D_{B,p}/p}pmod p.
]
Explicit independent binomial and recurrence calculations give the following exact modular data:

| p | (A_p mod p^3) | (B_pmod p^3) | (D_{B,p}mod p^3) | ((A_p/p^2,B_p/p^2,D_{B,p}/p)mod p) | necessary (mu_p) |
|---|---:|---:|---:|---|---|
| 19 | 2888 | 2527 | 3116 | (8,7,12) | (7+15s) |
| 373 | 9878159 | 28243187 | 35390986 | (71,203,140) | (195+274s) |

The coefficients of (s) are nonzero. **Thus no derivative-correction coefficient drawn solely from the base field (mathbb F_p) can repair the naive algebraic period scalar at this precision for these two primes.** An extension-valued correction is possible and uniquely prescribed by these data. This is a necessary coefficient, *not* a canonical/global Heun jet, proof of a p-adic transform, or a native Frobenius measurement.

All three numbers per prime were recomputed by two independent exact paths. The script `d25_two_leg_monodromy_jet_check_20261107.py` reproduces the table and also checks the existing fourth-digit **conjectural** signed residual at the discriminating (p=11,19,373), and the exact fifth-digit counterexample (p=11). These checks do not upgrade the universal conjecture.

## Relation to the frozen objective; BRC observer

The original goal remains (Delta_pequiv R_pmod p) for primes (pequiv13,19mod24), conditionally equivalent under the previously established bridge to (W_pequiv pmod p^3). The author-side candidate (2V_p-W_p-p(-3/p)equiv0mod p^4) remains unproved. The new results refine the **next route**: seek a two-legged correspondence and then retain the (k)-indexed 216/2304 coefficient streams, cutoff, denominator units, valuations, Gauss derivatives, Frobenius and Wilson carry as separate BRC observer coordinates until a verified readout. No native X6 equivalence is asserted.

Next discriminating action: seek explicit common Heun equations with two maps satisfying the ((3h,4h)) conditional degree filter; calculate the differentiated relation and compare its reduction with the required (7+15s) at 19 and (195+274s) at 373, while keeping the (p=11) fifth-digit failure. A failed candidate is a scoped witness, not a statement that the mother supercongruence cannot hold.

Source-lane status: original request `onhour11-20261106-1400-exact-research-lane-continuation` UNKNOWN_NOT_RESENT. Fresh gateway 2026-11-07 04:59 UTC reports CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false; request receipt and em_status return BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. No Source session/claim/run/Result is asserted, activity REGISTER_PENDING/SYNC_DEBT. Actual operator action remains dedicated Site-bound backend client + reviewed version + secure credentials, then original receipt/Source continuation before role writes. The separate native fixed p373 H0/B0 benchmark remains OPEN at issue #1559 and is NOT_EXECUTED by this note.

References: DLMF 15.10 (Gauss differential equation/local exponents); Bostan et al., *Ising n-fold integrals as diagonals of rational functions and integrality of series expansions* (J. Phys. A 46 (2013), 185202) as heuristic background; exact prior Enterprise Math notes and source pins above. Literature is not being cited as proving the new jet relation.
