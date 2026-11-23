# R5 — all-threshold 61-primary coefficient-period classification

2026-11-23 (Asia/Shanghai). **AUTHOR_EXACT_PROOF / FINITE_FIELD_NONZERO_WITNESS / NOT_REVIEWED.** Independent portable research; not a CLAIM/Result/Review or native X6/BRC theorem. Frozen scientific pin: awdawmip/enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15. Predecessor: https://github.com/awdawmip/enterprise-math/blob/21e5c3327e139130cbb8e19951a41a140ee30991/research_notes/portable_direct/r5_d41_allthreshold_mod82_20261123/RESEARCH.md

## Frozen input and theorem

For nonnegative multiplicities of prices 214..314 the failure supports are S0=214..218; S1={214,216,217,218,219,220,221}; S2={215,216,217,218,219,220,221}; S3=223..290; S4=296..312. Each event means its supported total multiplicity is less than integer m≥1. Let F_m(q)=R_m(q)/D(q) count their union, D(q)=∏_{p=214}^{314}(1-q^p). Let M_m^(≥1) be the strictly least common period of all quasipolynomial coefficient functions of degrees ≥1.

**Theorem.** For any primitive complex 61st root ζ and every positive integer m,

\[
R_m(\zeta)=0\iff m\bmod122\in\{0,118,119,120,121\}.
\]

Consequently,

\[
v_{61}(M_m^{(\ge1)})=\begin{cases}
0,&m\bmod122\in\{0,118,119,120,121\},\\
1,&\text{otherwise}.
\end{cases}
\]

## Exact overlapping-load derivation

Let A_m denote the normalized numerator of the overlapping union S0∨S1∨S2, and B_m,C_m the singleton normalized numerators of S3,S4. Boolean union of the three disjoint blocks gives R_m=A_m+B_m+C_m−A_mB_m−A_mC_m−B_mC_m+A_mB_mC_m. Every singleton normalized numerator equals a product of (1−q^p) on its support times a finite complete-homogeneous prefix sum. At any primitive ζ61, B_m=0 since 244∈S3 and 61|244; C_m=0 since 305∈S4 and 61|305. Thus R_m(ζ)=A_m(ζ).

Set a=a214, b=a215, c=a216+a217+a218, d=a219+a220+a221. The minimum of the three event loads is

\[
\min(a+b+c,a+c+d,b+c+d)=c+a+b+d-\max(a,b,d).
\]

Put α=ζ^214, β=ζ^215, γ_j=ζ^j for j=219,220,221; K=∏_{p=214}^{221}(1−ζ^p); H_c(t)=∏_{p=216}^{218}(1−tζ^p)^{-1}. Complete-homogeneous partial fractions give

\[
h_d(\gamma_{219},\gamma_{220},\gamma_{221})
=\sum_j\kappa_j\gamma_j^d,\quad
\kappa_j=\frac{\gamma_j^2}{\prod_{k\ne j}(\gamma_j-\gamma_k)}.
\]

For each permutation π=(top,middle,bottom) of (a,b,d), break ties with priority a,b,d. Let e1 be 1 if top has lower tie priority than middle and e2 be 1 if middle has lower tie priority than bottom; otherwise each is zero. Let (u1,u2,u3) denote (α,β,γ_j) arranged as π. Exact nonnegative gap variables give the cone generating function

\[
\sum_{a,b,d\in\operatorname{cone}(\pi)}
\alpha^a\beta^b\gamma_j^d\,t^{a+b+d-\max(a,b,d)}
=\frac{u_1^{e_1}(u_1u_2t)^{e_2}}
{(1-u_1)(1-u_1u_2t)(1-u_1u_2u_3t^2)}.
\]

Since a configuration of minimum load k contributes to all thresholds m≥k+1, its threshold generating function gains t/(1−t). Therefore

\[
G_A(t)=\sum_{m\ge0}A_m(\zeta)t^m
=\frac{Kt}{1-t}H_c(t)
\sum_{j=219}^{221}\kappa_j\sum_{\pi\in S_3}
\frac{u_1^{e_1}(u_1u_2t)^{e_2}}
{(1-u_1)(1-u_1u_2t)(1-u_1u_2u_3t^2)}.
\]

## All-threshold characteristic-zero zeros from poles and infinity degree

At primitive order 61 the possible t-poles (all distinct) are:

| Source | poles |
|---|---|
| threshold | ζ^0 |
| c-group | ζ^26, ζ^27, ζ^28 |
| top-pair | ζ^52, ζ^53, ζ^54, ζ^55, ζ^59 |
| three-variable | ±ζ^11, ±ζ^41, ±ζ^42 |

Each has multiplicity at most one: all positive root classes are distinct and three negative classes cannot collide with positive 61st roots since 61 is odd. Every pole is a 122nd root. Also 1−u1 and γ_j−γ_k never vanish. Hence

\[
G_A(t)=Q(t)/(1-t^{122}),\qquad Q(t)\in\mathbb Q(\zeta)[t].
\]

At infinity H_c=O(t^{-3}), t/(1−t)=O(1), and each cone factor is O(t^{e2−3}), e2≤1. Thus G_A=O(t^{-5}) and **deg Q≤117**. Coefficients A_m are strictly 122-periodic and vanish in characteristic zero for m mod122=118,119,120,121,0. This also supplies a shorter characteristic-zero explanation for the five overlapping-block zeros at order 41 (period 82, deg numerator ≤77); the complete order-41 union additionally uses its C-block result.

## Exact finite-field converse (117/117)

The accompanying verifier evaluates this same exact six-cone expression over F_367 with z=47, an element of exact multiplicative order 61. The prime 367 and order are checked. It evaluates 122 residues, checks a second period, checks the disjoint pole classes and independently checks the m=1 value against seven-term inclusion-exclusion of the original three sets. **Every m=1..117 has R_m(47)≠0 mod367**. The remaining residues 118..122 are zero, as already proved in characteristic zero by the degree argument.

Selected exact modular outputs: R1=202; R53=71; R61=149; R117=224; R123=202. SHA256 of the 122-row CSV beginning with the literal header m,R_mod367 followed by newline:

bf80fa3b6cdbd22db81b308789633e3b775920e895c8d301272f9cb7cec1b1aa

Nonzero reduction at one primitive order-61 root proves that the integral polynomial R_m is not divisible by Φ61 in characteristic zero, and hence it is nonzero at every primitive complex 61st root. Modular zeros are never used as characteristic-zero zero evidence.

## Exact coefficient-period conclusion

The only two multiples of 61 among prices 214..314 are 244 and 305, with gcd 61. No other root order divisible by 61 can have two denominator zero factors, hence only order 61 could contribute to positive-degree quasipolynomial coefficients. At primitive order 61 the denominator has a double zero. If R_m(ζ)≠0, the resulting double pole contributes an order-61 oscillation to the linear coefficient; if R_m(ζ)=0, the pole is at most simple and contributes no positive-degree term. Thus the stated exact 61-primary valuation follows.

## Verification status and next direction

Performed: exact modular arithmetic, primitive-root and primality checks, all 122 residues, second-period agreement, pole disjointness, and independent m=1 inclusion-exclusion. The characteristic-zero zero/period claims are algebraic proofs, while the finite field is only a nonvanishing witness. Independent review is **NOT_REVIEWED**. The signed overlapping joint load remains explicit (consistent with joint-relation/BRC observer preservation); no native X6 embedding is claimed.

Next: the same threshold-series and degree-at-infinity method for orders 47 and 59; determine whether colliding poles force polynomial-in-threshold coefficients. Preserve composite-order observation directions in the eventual complete M_m^(≥1) classification.
