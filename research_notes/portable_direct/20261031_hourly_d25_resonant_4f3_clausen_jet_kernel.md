# D25/LIFT — resonant Clausen branch and sharp CM-jet observer boundary

2026-10-31 Asia/Hong_Kong. Research lane: chatgpt-research-hourly-enterprise-math-20260923, distinct from maintenance. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Original **scientific** Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 and P000 ACTIVE_LOCKED unchanged. External finite-field arithmetic; no native X6 projection.

## Consumed frontier

Prior same-lane report 20261031_hourly_d25_reversed_terminating_4f3_e2_bridge.md (EM e4da8741fc91c6b584de6a61a9c8cd6b7ae1ed66) already established, for p=6l+1 prime and theta=z d/dz,

H_l(z)=sum_{s=0}^{l-1} [(1)_s(1-l)_s(1+l)_s/(1-3l)_s^3] z^s,

L_l=theta(theta-3l)^3-z(theta+1)^2(theta+1-l)(theta+1+l),

L_l H_l=0,

I_p = K_l [(4+6theta)H_l]_{z=1/2} (mod p),
K_l=2^{3l}((3l-1)!)^2 / (36(4l)!(2l)!).

These are finite, explicitly bounded polynomial formulas; the bottom parameter 1-3l is a negative integer and must not be read as an unqualified infinite 4F3. The I_p certificate is for the original signed E.2 middle strip, not the total LIFT.

The separate onhour lane proved the original 216/E.2 decomposition
A_p-B_p = D0+D1+p^2 I_p (mod p^3)
and left **both** D0+D1=0 (mod p^2) and (D0+D1)/p^2+I_p=0 (mod p) open. Its own contributions are not recredited here.

## New theorem 1 — a genuine resonant solution and gauge intertwiner

Work in F_p[z], p=6l+1>=7. Define

G_l(z)=sum_{r=0}^l binom(l,r)binom(2l,r) z^r,

C_l(z)=sum_{r=0}^{2l} (1/2)_r(1/3)_r(2/3)_r/(r!)^3 z^r,

M=theta^3-z(theta+1/2)(theta+1/3)(theta+2/3).

Clausen's classical formal hypergeometric square identity, with a=-l,b=-2l, reduced coefficientwise in F_p up to degree<p, gives

**C_l(z)=G_l(z)^2 in F_p[z].**

Justification of reduction: a+b+1/2=-3l+1/2 =1 (mod p); 2a+2b=-6l=1 (mod p); top parameters 2a,2b,a+b reduce to 1/3,2/3,1/2. All bottom factorial factors are units in the degree range <p. The left terminates at degree l before squaring; the reduced right terminates at degree 2l, so both sides are polynomials of degree at most 2l. This reuses, and does not claim originality of, classical Clausen (DLMF 16.12.2).

**New gauge operator identity (mod p only):**
L_l(z^{3l} f)=z^{3l}(theta-1/2) M f for EVERY polynomial f in F_p[z].

Proof: replacing theta by theta+3l and using 3l=-1/2, 2l=-1/3, 4l=-2/3 (mod p) yields
(theta-1/2)theta^3 - z(theta+1/2)^2(theta+1/3)(theta+2/3).
The Ore relation (theta-1/2)z=z(theta+1/2) gives exactly (theta-1/2)M. The recurrence of C_l proves M C_l=0. Hence

**J_l(z)=z^{3l}C_l(z)=z^{3l}G_l(z)^2 and L_l J_l=0.**

J_l has nonzero coefficients at degrees 3l and 5l, all coefficients outside this interval zero; H_l is supported at degrees 0 through l-1. Distinct original branch identities and exponent supports are retained.

## New theorem 2 — COMPLETE low-degree polynomial kernel

**ker(L_l) on F_p[z]_{deg<p} = span_{F_p}{H_l, J_l}, dimension 2.**

Proof: the coefficient equation for F=sum_{n=0}^{p-1}f_n z^n is

n(n-3l)^3 f_n = n^2(n-l)(n+l) f_{n-1}, 1<=n<p.

At n=l the right side vanishes and left factor is a unit, forcing f_l=0 and then f_{l+1}=...=f_{3l-1}=0. The only singular left factor for 1<=n<p is at n=3l; its preceding coefficient already vanishes, so f_{3l} is a genuinely new free variable. For 3l<n<=5l, the recurrence transports that variable uniquely. At n=5l+1, n+l=p kills the right side, so f_{5l+1}=0 and all later coefficients below p vanish. The z^p equation imposes no extra constraint since both sides contain p. Exactly two free coefficients remain: f_0 and f_{3l}. They are realized independently by H_l and J_l. QED.

Therefore the fourth-order ODE plus normalization F(0)=1 does NOT uniquely select H_l. The original bounded degree/termination guard does select it. Do not promote an ODE-only numerical or formal connection to the original H.

## New theorem 3 — a sharp CM first-jet insufficiency witness

For the **frozen** p mod24 in {13,19}, consume the previously published (still independently unreviewed) CM/Hasse hypotheses

G_l(1/2)=0 and G_l'(1/2) != 0 (mod p).

For these hypotheses, J=z^{3l}G_l^2 has a DOUBLE root and

J_l(1/2)=J_l'(1/2)=0,
J_l''(1/2)=2^{1-3l}G_l'(1/2)^2
          =2^{-3l} hbar^2/18 !=0 (mod p),
hbar=6G_l'(1/2).

Thus the entire family H_l+lambda J_l satisfies the SAME 4F3 equation, same constant coefficient, same **value and first derivative** at z=1/2, and same declared signed scalar readout [(4+6theta)F]_{1/2}; its second derivative differs by lambda J_l''(1/2). This is a precise observed fiber contrast, not a general inverse-uniqueness claim.

Unconditionally, even without CM:
[(4+6theta)J_l]_{1/2}
=2^{-3l} sum_{r=0}^{2l}(6r+1)
  (1/2)_r(1/3)_r(2/3)_r / (2^r(r!)^3) (mod p).
The CM root annihilates this one scalar readout, NOT the entire resonant branch.

**BRC COMPOSE_APPLIED:** carrier retains p,l, original 216 coefficient source, branches H/J and polynomial degree, original signed weight, modulus/valuation, and the observer order. Permitted future operations are L4, theta, evaluation at z=1/2, first/second jets, and the original signed 4+6theta readout. The quotient dropping J is safe for this signed CM scalar, but unsafe for future second-derivative observers or reconstructing the full 4F3 solution. No classical finite-field formalism is retyped as native Enterprise six-axis evidence.

## Executed exact certificates

Actually ran the accompanying Python standard-library verifier d25_resonant_4f3_clausen_20261031.py, using only integer modular arithmetic. All 330 primes 7<=p<=5000, p=1 mod6 (including 166 frozen p mod24=13,19) passed 772620 coefficient checks of L4H=L4J=0 and M C=0. Independent coefficient-by-coefficient Gauss-square convolution was run for 46 primes; four-point polynomial comparisons ran for all 330; the CM root, simple derivative and second-derivative contrast were tested at all 166 frozen primes. Marker:

PASS_D25_RESONANT_4F3_CLAUSEN_JET_KERNEL_EXACT

At p=373 (l=62): G(1/2)=0, G'(1/2)=215, hbar=171,
J''(1/2)=54 nonzero, K_l=290,
[(4+6theta)H]_{1/2}=217, I_373=266.
At p=13: J''=11, I=10. At p=19: J''=11, I=9.
Finite checks do not prove the universal CM input or the open LIFT.
No Lean formalization, independent review or native H0/B0/Frobenius experiment occurred.

## Open original target and exact next action

A_p = sum_{n=0}^{p-1}(6n+1) binom(2n,n)^2 binom(3n,n) / 216^n
   ?= p (mod p^3), p mod24 in {13,19}, remains OPEN.

The separate original 216/E.2 bridge needs D0+D1=0 (mod p^2) and, only then, (D0+D1)/p^2 + I_p=0 (mod p). This gauge result cannot establish them. Next scientific unit: test whether the low/middle original-source difference D0+D1 can be connected by a **joint signed, source-faithful** finite WZ/CM relation to the gauge-invariant middle readout. Respect its first-digit divisibility, all prior 11 Euler-Clausen ports, and the source labels; do not determine an ODE solution from CM first-jet values alone. Preserve original fixed parameters, do not repeat ruled-out single-term Gosper.

Native H0/B0 divided-power, [X]U modp², rank, semilinear Frobenius/eta, odd signed Green/Hesse, kappa and original native p373 replication remain separately UNEXECUTED. Gateway 0.6.11 reports research_authority_granted=false, executor_binding_configured=false, active native control jobs 5/5 and control CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED. No callable recovery_status action on authenticated connector despite advertisement. Existing enterprise-math #1558 controls lawful recovery, #1559 native experiment. No new own session/CLAIM/OPEN/checkpoint/Result/review, no old protected session or maintenance identity modified. Formal research activity remains REGISTER_PENDING/SYNC_DEBT; this Git artifact is not native Source completed_units or mathematical admission.

Sources: earlier hourly 4F3 at EM e4da8741fc91c6b584de6a61a9c8cd6b7ae1ed66; onhour factorial inverse moment at EM 9aa17bb0c56a6f4cdd471a4ccaf99a5b7158df28; NIST DLMF §16.12.2, https://dlmf.nist.gov/16.12#E2.