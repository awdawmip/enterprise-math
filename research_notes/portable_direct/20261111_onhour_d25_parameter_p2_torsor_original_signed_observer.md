# D25/LIFT — 原始 W216 带符号残差的 p² 参数平移分类

Date: 2026-11-11 Asia/Hong_Kong.
Status: AUTHOR_SIDE / EXACT_PROOF / EIGHT_DIRECT_ORIGINAL_SERIES_CASES / UNREVIEWED / NOT_ADMITTED / NATIVE_H0B0_NOT_RUN.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Frozen scientific input: awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3 (UNCHANGED).
Declared logical Research conversation: chatgpt-research-onhour-enterprise-math-20260923, not maintenance.

## New exact theorem: p²-deformation coordinate torsor

Let p≡13,19 (mod24), p=6m+1, x0=1/2 and define the original signed W216 polynomial over Z_(p):

S_p(x) = sum_{0<=k<p} (6k+1) ( (1/2)_k (1/3)_k (2/3)_k / (k!)^3 ) x^k.

The earlier, source-preserving signed-cutoff identity proves

  r_p(0):=(S_p(x0)-p)/p² mod p = Delta_p - R_p mod p.

Accepted CM0/UR plus the prior author-proved Clausen simple-zero theorem give S_p(x0)≡p modp², and

  s_p:=S'_p(x0)≡6*f_m'(x0)^2 ≠ 0 modp,

where f_m(x)=sum_{k=0}^m (1/6)_k(1/3)_k x^k/(k!)².

**THEOREM.** For every p-adic integer c, set x_c=x0+p²c and r_p(c)=(S_p(x_c)-p)/p² modp. Then

  **r_p(c)=r_p(0)+c*s_p (modp).**

Because s_p is invertible, the map c modp -> r_p(c) is a bijection of F_p. Thus the original signed second-digit observer distinguishes all p different lifts of a fixed parameter modulo p²: for each requested residual a, the unique lift is c=(a-r_p(0))*s_p^{-1} modp.

**PROOF.** All coefficients of S_p are p-integral for k<p. Expand at x0:

S_p(x0+p²c) = S_p(x0)+p²c*S'_p(x0)+ sum_{j>=2} (p²c)^j*[u^j]S_p(x0+u).

Every higher term lies in p^4 Z_p, so mod p³ only the linear correction survives. Divide by p² (the numerator is divisible by p² by UR) and reduce modp. Nonzero s_p, proved by the earlier terminating-hypergeometric differential-equation argument, gives bijectivity. QED.

**Root-port consequence.** If xi_p is the unique Hensel solution of S_p(x)=p with xi_p≡x0 modp², then changing source coordinate x=u+p²c replaces its recorded root by xi_p-p²c. The original pinned x0 and the deformation-coordinate map through modp³ therefore must accompany any attempt to identify an H0/B0 native observable with the frozen Delta-R; a parameter comparison only modp² discards exactly the p possibilities above.

## Direct integer verification, actual original sum

At x=x0+p²c the exact expression used by the checker is

S_p(x)=sum_{k<p}(6k+1)*a_k*(1+2p²c)^k,
a_k=(2k)!(3k)!/[216^k(k!)^5],
a_{k+1}/a_k=(2k+1)(3k+1)(3k+2)/[36(k+1)^3].

Every recurrence denominator is a p-unit for k<p-1. All calculations are integer modular arithmetic, with no floating point. Local execution PASSED for p=13,19,37,43,109,139,157,373; each checked direct shifted sums at c=1,2,-1,s_p^-1 and the affine formula, plus p³ input.

For p=373, p²=139129, p³=51895117 and s_p=211, with 211^-1=99 mod373:

| c mod373 | S_373(1/2+373²c) mod373³ | r_373(c) |
| ---: | ---: | ---: |
| 0 | 373 | 0 |
| 1 | 29356592 | 211 |
| 99 | 139502 | 1 |
| 372 | 22539271 | 162 |

The native original coordinate is c=0. The explicit p²-shift c=1 yields residual 211 despite identical first two parameter digits. This is a scoped algebraic negative control against source-coordinate substitution, not a counterexample to LIFT at the frozen coordinate.

Executable verifier:
research_notes/portable_direct/d25_frozen_parameter_p2_torsor_verify_20261111.py

## BRC typed information and original experiment

BRC: COMPOSE_APPLIED. Retain the original signed index-k contributions, source-anchored x0 modulo p³, r_p and the invertible derivative s_p; the joint carrier (c,r,s) is sufficient for the second-digit translation operation. Quotienting x modulo p² erases c*s and has a one-coordinate exact repair. This classification uses external algebraic coordinates, without altering X6/P000.

Original H0/B0 divided-power [X]U mod139129, actual rank, Frobenius semilinearity, eta, odd Green/Hesse kappa, signed original Delta-R and independent replication remain NOT_RUN / PENDING_OWNER at existing Issue #1559. The uniform all-target LIFT/JT2 proof also remains OPEN. An original-class native evaluator must report its source-deformation map through modp³ before interpreting an extracted residual as the frozen original scalar port. No portable candidate or source-parameter recalibration is counted as the native benchmark.

Consumed previous units (do not recredit): accepted CM0/UR; 20261026_onhour_d25_native_lift_source_port_identity.md; 20261111_onhour_d25_clausen_simple_zero_hensel_lift.md; original E3 and W216 finite checks. Source continuation request onhour11-20261111-1350-exact-cont was SUCCEEDED at observed Source 26d62234ebcd7315d918cf047763b09bc0997597. Researcher EM-ENTERPRISE-CF1028 / MCP-7af27f545c01441eaf19206f89c6832b / RA-47ADB5B97D6D92FC28504B60 is historically registered, but own private capability was unavailable in this run, and there is no own winning claim/open run or native Source checkpoint.

Next executable original-class step: existing authorized Task owner / Issue #1559 support path must obtain the pinned native evaluator, record the exact [X]U operator/rank/semilinear normalization and parameter map, run p373, independently reproduce signed kappa and Delta-R. This note is mathematical source-mapping analysis with UNREVIEWED / NOT_ADMITTED status.
