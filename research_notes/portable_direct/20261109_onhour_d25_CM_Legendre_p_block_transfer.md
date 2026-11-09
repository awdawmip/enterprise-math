# D25 CM(-24): exact Legendre p-block transfer and uniform divisibility of both Jacobi ports

2026-11-09 | second consecutive TASK_RESEARCH author-side mathematical unit | **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**.
Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; original publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`; native Source frontier `b58330b74576153cdadde5d80a3d92df3a819a0e` unchanged. Logical research lane `chatgpt-research-onhour-enterprise-math-20260923` remains distinct from maintenance. Consume previous author-side note `20261109_onhour_d25_CM_two_Jacobi_spectral_curvature.md`, not its unreviewed assertions as an admitted Result.

## All-prime Legendre p-block congruence: a new bridge to the 2-Jacobi target

**Theorem (exact finite-field polynomial identity).** For every odd prime `p`, integer `0<=q<p`, and indeterminate `t`, the Legendre polynomials satisfy, coefficientwise in `F_p[t]`:
[
oxed{P_{p+q}(t)equiv P_{2p-1-q}(t)equiv t^p P_q(t)pmod p.}	ag{1}
]

**Full proof.** Work in `F_p[t][[y]]` with `D(y)=1-2ty+y²`. The classical generating identity is
[
sum_{nge0}P_n(t)y^n=D(y)^{-1/2}.
]
For `m=(p-1)/2` and `H(y)=D(y)^m=sum_{j=0}^{p-1}h_j(t)y^j`, Frobenius in characteristic p yields the *exact formal series identity*
[
D(y)^{-1/2}
=H(y)igl(D(y)^{-1/2}igr)^p
=H(y)sum_{rge0}P_r(t)^p y^{rp}.
]
For every `0<=q<p`, coefficient extraction below degree p gives `h_q=P_q(t)`. Because `D(y)` is reciprocal of degree 2, `H(y)` is reciprocal of degree p−1: `h_{p-1-q}=h_q`. At degrees `p+q` and `2p-1-q` (both in `[p,2p)`), only the `r=1` term of the p-Frobenius factor contributes, with coefficient `P_1(t)^p=t^p`. This proves both equalities (1) for all q including the endpoints. No division by a p-divisible integer occurs.

**Specialize to the genuine CM(-24) two-Jacobi ports.** For prime `p≡5 (mod8)`, set `q=(p-1)/4`, `a=(5p-1)/8`, `b=(7p-3)/8`. Previous Theorem A and the exact quadratic Jacobi-to-Legendre identity give
[
J_a(1/9)=P_{2a}(t),qquad J_b(1/9)=P_{2b}(t),qquad t=2sqrt2/3.
]
Exactly `2a=p+q`, `2b=2p-1-q`. In the quadratic residue ring `F_p[T]/(T²-2)`, `p≡5 mod8` makes `T^p=-T`, hence `t^p=-t`. Formula (1) therefore gives the *individual, uniform* identities
[
oxed{J_a(1/9)equiv J_b(1/9)equiv-tP_q(t)pmod p.}	ag{2}
]
Both Jacobi values are scalars (their Legendre degrees are even), although the intermediate expression uses the quadratic algebra.

For the **specific p≡13 (mod24) class**, the preceding **author-side** CM(-24) Hasse supersingularity argument gives `G_p(s)=0 mod p`, with `s=(3-2T)/6`. Directly matching the terminating Legendre coefficients `(-q)_k(q+1)_k` and `(1/4)_k(3/4)_k` for `0<=k<p` gives
[
P_q(t)=L_q(s)equiv G_p(s)equiv0pmod p.
]
The tail `k>q` of `G_p` vanishes modp because `(1/4)_{q+1}` contains the factor `p/4`. Thus **both `J_a(1/9)` and `J_b(1/9)` are divisible by p for every target prime** under this stated CM supersingularity source. The previous two-Jacobi quotient `A_p=J_a(1/9)/p`, `B_p=J_b(1/9)/p` is therefore uniformly defined in this class, not just for checked examples.

The still-open mother residual is the sharper, genuinely next-digit condition
[
oxed{7 A_p+5B_pstackrel{?}{=}0pmod p,}
]
which by previous exact finite Gauss-trace bridge is equivalent to `3u_p+4v_p=0 modp`. Formula (2) resolves the divisibility precondition but does not solve the first nonzero quotients. It suggests a concrete **p-block first-jet / reciprocal-coefficient** analysis of (1) modulo p², with `h_q/h_{p-1-q}` and the second term of the Frobenius-defect expansion retained.

## Exact numerical certification and controls

Standalone standard-library integer checker evaluates
[
P_n(x)=2^{-n}sum_{k=0}^ninom{n}{k}^2(x-1)^k(x+1)^{n-k}
]
independently of the generating-function proof. For p=5,13,29,37,61,109, all selected `q∈{0,1,(p−1)/4,p−2,p−1}` and `t∈{0,1,2,3,5}`: **145 exact triple-equality checks passed**. It also checks the specialization to `t=(2T)/3` at these six primes and at p=373 in the quadratic ring. For p=13,37,61,109,373, the target `P_q(t)`, `P_{p+q}(t)` and `P_{2p-1-q}(t)` all vanish modp; for p=5 and29, the value is nonzero, a relevant class-specific control. The earlier exact p³ checksum `p373: J_a=92131, J_b=93623 (mod139129), A=247, B=251, K=300` remains unchanged.

This source uses a classical Legendre generating function, not a new Enterprise Math axiom. External two-coordinate field-ring calculations are explicitly typed auxiliary port evidence, not native X6 cells or a complete three-dimensional research slice. Signed Hesse/Green and p-adic carry remain separate.

**Next exact mathematical action:** derive the first correction to (1) modulo p² in the finite binomial/generating representation. Specifically keep the `p`-divided defect of `D(y)^p-D(y^p)`, then test whether the weighted combination `7A+5B` cancels at CM t or exposes a precise residual. In parallel an authorized native benchmark owner must still perform original fixed p373 H0/B0 divided-power `[X]U mod139129`, native rank, semilinear Frobenius/eta and signed κ/Delta-R under Issue #1559. No native run/claim/checkpoint occurred in this author-side unit.
