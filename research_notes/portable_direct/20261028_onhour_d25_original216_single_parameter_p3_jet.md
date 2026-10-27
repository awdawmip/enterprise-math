# D25 / SECOND-DIGIT-LIFT — one-parameter original weighted216 third-digit jet with four exact bands

Date: 2026-10-28 Asia/Hong_Kong. Actual Research logical lane `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance). Parent `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Classification: **AUTHOR-SIDE / EXACT ALL-p≡1 mod6 JET IDENTITY PROVED / 11 EXECUTED EXACT CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Original all-target third-digit zero and native H0/B0 benchmark remain OPEN.

## 1. Exact original 216 object and its integer-parameter interpolation

For a prime p=6m+1>3, let `(a)_n=∏_{j=0}^{n-1}(a+j)`, `(a)_0=1`, in the p-local coefficient ring. The original signed finite sum is

[
W_p=sum_{n=0}^{p-1}(6n+1)
 rac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3}
=sum_{n=0}^{p-1}(6n+1)rac{inom{2n}{n}^2inom{3n}{n}}{216^n}.
]

Define the *one-parameter exact original-class deformation*

[
Phi_m(s)=sum_{n=0}^{p-1}(6n+1)
 rac{(-3m+s/2)_n(-2m+s/3)_n(-4m+2s/3)_n}
 {2^n(n!)^3}.
	ag{J0}
]

Since `p=6m+1`, the three parameters at `s=p` are **exactly** `1/2,1/3,2/3`, respectively; hence `Phi_m(p)=W_p` as an exact p-local rational identity, before any reduction. For every n<p, `2^n(n!)^3` and the rationals' factors 2,3 are p-units. There is no singular denominator or change of target/cutoff.

Write the coefficientwise formal expansion

[
Phi_m(s)=J_0+sJ_1+s^2J_2+s^3(cdots)
]
in (mathbb Z_{(p)}[[s]]), where `J0=Phi_m(0)`, `J1=[s]Phi_m`, `J2=[s²]Phi_m` (`J2=Phi_m''(0)/2`). **Theorem, all primes p≡1 mod6:**

[
oxed{W_pequiv J_0+pJ_1+p^2J_2pmod{p^3}.}	ag{J1}
]

**Proof:** Substitute s=p and collect by powers. All coefficients are p-integral; every term of s³ or greater is p³-divisible. No unproved hypergeometric identity enters: (J1) is exact finite-coefficient Taylor arithmetic of an exactly matching original interpolation. QED.

## 2. Exact p³ cutoff with provenance-preserving four bands

For `n≤2m` no one of the three terminating parameters crosses its zero at s=0. For `2m<n≤3m`, `(-2m+s/3)_n` contributes exactly one factor s. For `3m<n≤4m`, also `(-3m+s/2)_n` contributes one s, so the term is divisible by s². For `4m<n≤6m=p-1`, the third factor `(-4m+2s/3)_n` makes the product divisible by s³. Consequently the **formal** valuation bands are

| Original n-band | smallest forced power of s | contributes to p³ jet |
|---|---:|---|
| 0..2m | s⁰ | J0,J1,J2 |
| 2m+1..3m | s¹ | J1,J2 |
| 3m+1..4m | s² | J2 only |
| 4m+1..6m | s³ | none modulo p³ |

This is an exact **observer-scoped reduction**, not elimination of the p² high band or an original operator identification. The high band's p² coefficient **equals the original weighted216 reflection Theta_p** established in the immediately preceding onhour research checkpoint (project commit `321f9240503f7c462a2f722b1da1ff96b950abcb`) because the individual summands equal the original w_n at s=p and start at s². Therefore the two independently calculated high-band digit interfaces have a rigorously proved relation.

The original frozen Clausen cutoff observer `R_p` remains distinct. In particular at p=373, `Theta_373=266` whereas `R_373=196`. Retain signed original weights, the s-factor origin of each band and the original signed `Q/R` when transporting back to the Source target.

## 3. Concrete all-target-prime reduction (OPEN zero obligation)

Consume only already accepted first-digit UR `W_p≡p (mod p²)` for the two frozen target classes `p≡13,19 (mod24)`; it ensures divisibility of `J0+pJ1-p` by p² in the p-local ring (J1). Thus the original **third-digit** test is exactly

[
oxed{
  mathcal J_p:=(J_0+pJ_1-p)/p^2+J_2equiv0pmod p,
  qquad pequiv13,19pmod{24}.
}	ag{J2}
]

From the already source-aligned original identity, its readout is `J_p=(W_p-p)/p²=Delta_p-R_p (modp)`. The new work proves this reduction and the p³ endpoint reconstruction; it **does not** establish `J_p=0` for all target primes. An allowable next proof route is exact terminating-product derivative/creative telescoping or a valid modular identity for the coupled J0,J1,J2, preserving the p² high-band term; another loop of finite prime fixtures cannot close it.

## 4. Actual executed independent BigInt certificate

The companion `d25_original216_single_parameter_p3_jet_guard_20261028.js` was actually executed (not merely written). It performs exact `BigInt` modular arithmetic in `(Z/p³)[s]/(s³)` using the independent three-parameter rising-factorial recurrence, compares against a second independent original integer-binom(2n,n)²binom(3n,n)/216^n sum for every `0≤n<p`, verifies the four bands, and checks 11 cases `p=7,13,19,31,37,43,61,67,73,211,373` (including 8 target class cases and 3 controls). All assertions passed. Status: `PASS_D25_ORIGINAL216_SINGLE_PARAMETER_P3_JET`. Target finite numerical equalities are regression fixtures only, not the all-prime zero proof.

At fixed native diagnostic p=373 (m=62, p²=139129, p³=51895117):

[
J_0=15521276mod p³,quad
J_1=47909mod p²,quad J_2=133mod p.
]

The J2 contributions split as `82 (n≤124) + 158 (125≤n≤186) +266 (187≤n≤248) =506≡133 (mod373)`. The high band `266` independently matches `Theta_373`, and `n≥249` contributes zero at p³ precision. The quotient `(J0+373*J1-373)/139129≡240 (mod373)`; `240+133=373≡0`. Direct original sum also gives `W_373≡373 (mod51895117)`. These are exact modular certificates, not the original native `[X]U` experiment.

## 5. BRC typing, disposition and exact continuation

Carrier `(p,m,n,6n+1,original signed w_n,three separate Pochhammer factors,s-derivative order,term cutoff,Source Q/R,operator provenance)`. Observer: precisely `W_p modp³`, and on the target classes the verified Source bridge to `Delta_p-R_p modp`. Allowed operations: exact p-local parameter interpolation, formal coefficient extraction, p-adic specialization and strict valuation-banded truncation. This algebraic one-variable deformation is an **external auxiliary arithmetic representation**, NOT a native six-dimensional Heartbeat X6 Cell coordinate, not a complete original Frobenius operator, and not an all-future-information sufficient quotient. Native six-dimensional P000 semantics and source pins are unchanged.

**Research frontier:** highest required original-class experiment at `awdawmip/enterprise-math#1559` (authorized original fixed p373 H0/B0 divided-power `[X]U mod139129`, module rank, semilinear Frobenius direction and eta, signed odd Green/Hesse, original kappa and Delta-R, independently reproducible Source-pinned raw output) is STILL `PENDING_OWNER / NOT_EXECUTED` as last observed in this run. Native support comment `#1559#issuecomment-6454959066` binds the companion p³ tail risk without asserting a native run. Do not substitute this finite scalar jet, and do not reopen frozen UR/CM0 or the completed auxiliary Cauchy proof.

**Source-side state:** This Research lane's historical `awdawmip/kimi-query-bridge#6575` recovery is a local ACTIVE session pointer, not a Source winning CLAIM; historical #6576 dispatch failed TimeoutExpired, not NO_DISPATCH. Gateway v0.6.11 Site at this run `research_authority_granted=false`, native active requests 5/5, and `em_control_result` did not recognize the original GitHub bridge request IDs. Therefore no native CLAIM/open/Source checkpoint/Result/review was made; `REGISTER_PENDING` and former three staging sources remain independent. Save any next protected operation to the same lawful stable Research conversation only, never maintenance. A future authorized Source continuation/claim is required for formal admission, and independent Driver review is required for science. Original hourly scheduler, enabled state and notification settings were not modified.
