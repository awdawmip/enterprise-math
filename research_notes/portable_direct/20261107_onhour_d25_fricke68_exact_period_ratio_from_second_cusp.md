# D25 — Exact 216/2304 infinite-period ratio via the second cusp of X_0(6)

Date: 2026-11-07. Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, TP2-B6F4FC938FF94941C1B7, immutable scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Immediate prerequisite: `20261107_onhour_d25_fricke68_explicit_two_leg_and_common_special_fiber.md` at commit 7f5107ce41724bbcf5efdc47c2f58d8649bf4ace. Status: AUTHOR_SIDE_PROVED / SYMBOLICALLY_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Theorem: an exact algebraic two-leg hypergeometric transformation

Let
[
z(t)=rac{108t^2(t+9)(t+8)^2}{(t+12)^6},qquad
w(t)=rac{256t^3(t+8)(t+9)^3}{(t^2+36t+216)^4}.
]
For the principal real Gauss solutions and every real 0<=t<12+12sqrt(3),
[
oxed{{}_2F_1(	frac16,	frac13;1;z(t))
=sqrt{	frac32},rac{t+12}{sqrt{t^2+36t+216}},
{}_2F_1(	frac18,	frac38;1;w(t)).}	ag{1}
]
Both z(t),w(t) lie in [0,1) on this interval.

**Proof.** The preceding note proves the exact transformed Gauss operator equality: with d=6t/((t+12)(t^2+36t+216)), P_A,P_B and Q_A,Q_B denoting the two equations after substitution of z,w,
[
(P_B-P_A)/2=d,qquad Q_B=d'+d^2+P_A d+Q_A.
]
Hence multiplication by (widetilde G(t)=sqrt{3/2}(t+12)/sqrt{t^2+36t+216}) maps any solution of the B equation to a solution of the A equation, where (widetilde G'/widetilde G=d).

At the **second cusp t=0**, z(t)=t^2/48+O(t^3), w(t)=t^3/1458+O(t^4), and (widetilde G(0)=1). The two sides are therefore holomorphic solutions of the same pulled-back Fuchsian equation with value 1. Near t=0, the coefficient of the first derivative is (1/t+O(1)), while the coefficient of Y has at worst a simple pole, so the indicial equation is (r^2=0). A Frobenius recurrence shows that a holomorphic solution is uniquely determined by its constant term; its second independent solution has a logarithmic germ. Thus both sides coincide near t=0. Algebraic continuation along the positive interval before the first z=1 point proves (1) for all stated t. This proof bypasses the elliptic crossing needed when the germ is normalized instead at t=infinity.

Equivalently, the Clausen identity (2F1(a,b;a+b+1/2;x))^2 = 3F2(2a,2b,a+b;2a+2b,a+b+1/2;x) yields the exact third-order transformation
[
oxed{
{}_3F_2(	frac12,	frac13,	frac23;1,1;z(t))
=rac{3(t+12)^2}{2(t^2+36t+216)}
{}_3F_2(	frac14,	frac12,	frac34;1,1;w(t)).
}	ag{2}
]
The pair of arguments is connected by the explicitly constructed two-legged modular correspondence, rather than a one-legged rational substitution.

## Corollary: the previously numerically observed period ratio is exact

Set (t_*=6sqrt2), which belongs to (0,12+12sqrt3). The exact polynomial-gcd certificate gives (z(t_*)=1/2), (w(t_*)=1/9), while
[
rac{3(t_*+12)^2}{2(t_*^2+36t_*+216)}=rac{3sqrt2}{4}.
]
Using the coefficient identities
[
rac{inom{2k}{k}^2inom{3k}{k}}{216^k}
=rac{(rac12)_k(rac13)_k(rac23)_k}{(k!)^3}Big(rac12Big)^k,
]
[
rac{inom{2k}{k}^2inom{4k}{2k}}{2304^k}
=rac{(rac14)_k(rac12)_k(rac34)_k}{(k!)^3}Big(rac19Big)^k
]
and the absolutely convergent series gives the **proved real equality**
[
oxed{
sum_{k=0}^inftyrac{inom{2k}{k}^2inom{3k}{k}}{216^k}
=rac{3sqrt2}{4}
sum_{k=0}^inftyrac{inom{2k}{k}^2inom{4k}{2k}}{2304^k}.
}	ag{3}
]
The old 110-digit rational-interval observation at `4020b5d8be7d1bfb8f9673d65f2331407609c476` is now *consumed as prior empirical evidence*; the proof above is independent of that finite precision.

## BRC provenance / next open mathematical unit

The exact comparison requires preserving the cusp port (t=0 versus t=infinity), normalization of the Gauss solution, leg A/B and branch of the square root. This is a COMPOSE_APPLIED use of provenance-retaining observer semantics: quotienting both legs to mere numerical arguments z,w before the cusp choice loses the connection scalar. No alteration to P000 or the frozen task input occurs.

The infinite-period equality (3) is analytic, not a finite truncated congruence. The mother D25 target still needs the fourth-digit p-adic relation (2V_p-W_p-p(rac{-3}{p})=0mod p^4) (conjectural) or another route to (W_p=pmod p^3) on 13,19 mod 24, plus the original-class p373 native H0/B0/Frobenius independent experiment (#1559). **Next exact action:** derive the rational first-jet of (2) in the joint parameter at the special fiber, then identify the extra boundary/Frobenius defect when a finite sum replaces an infinite period. Compare with the existing `p^4 signed tails`, `R_p=K_p` bridge and `mu_19/mu_373` as *tests*, not as assumed theorems.

Source native status at this run: BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false, current Site CONFIGURED_NOT_LIVE_VERIFIED; original request `onhour11-20261106-1400-exact-research-lane-continuation` remains unresolved and unresent. Fixed research lane `chatgpt-research-onhour-enterprise-math-20260923`; Researcher session/claim/run not verified, REGISTER_PENDING/SYNC_DEBT; independent Source admission pending.
