# D25/LIFT GH-20 and GH-21 — source-faithful second-digit Gauss transport and Hensel repair

2026-10-28 | Author-side portable mathematical research. Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Not a native Source checkpoint or official Research-Activity registration.

Parent task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Mother objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION remains OPEN. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

## Setup

Let p=8m+3 >= 11 be prime, 0<=r<=m. In Z_(p) define

a_r = (-m)_r^2 / ((2m+2)_r r!),
c_r = (3/8)_r^2 / ((5/4)_r r!),
nu_r = sum_{j=0}^{r-1} [2/(8j+3)+1/(4j+5)], nu_0=0.

F_m(z)=sum_{r=0}^m a_r z^r, G_m(z)=(16z d/dz+5)F_m(z);
hatF_p(z)=sum c_r z^r, K_p(z)=sum c_r nu_r z^r;
hatG_p=(16z d/dz+5)hatF_p, K_G,p=(16z d/dz+5)K_p.

All denominators above are units at p on the declared finite rank interval. The two F/G channels are retained separately. The correction K_p here is not the original GH-5 S-source correction or the Hasse B0.

## GH-20 — exact product and p^2 first variation

For each 0<=r<=m there is the rational identity

a_r/c_r = product_{j=0}^{r-1} ((1-p/(8j+3))^2/(1+p/(4j+5))).

Consequently a_r = c_r (1-p nu_r) (mod p^2), for the entire rank interval, and

**F_m(z) = hatF_p(z) - p K_p(z) (mod p^2),**
**G_m(z) = hatG_p(z) - p K_G,p(z) (mod p^2)**

for every z in Z_(p), with the same fixed truncation. Proof: -m=3/8-p/8 and 2m+2=5/4+p/4. The ratios of individual Pochhammer factors yield the exact product. Since all factors are p-units, expand (1-px)^2/(1+py)=1-p(2x+y) mod p^2, multiply across the finite set, and sum with weights 1 or (16r+5). No boundary/source term is deleted.

If a channel C in {F,G} has C_m(9)=0 mod p, define q_C=C_m(9)/p (mod p), hatq_C=hatC_p(9)/p (mod p) and K_C=K_p or K_G,p. Both divided residuals are well-defined, and **q_C=hatq_C-K_C(9) (mod p)**. This is a genuinely retained p-adic source moment, not a proof of the first-digit root or the original JT2 target.

## GH-21 — unique conditional p^2 root in the proper channel

Let C be either F_m or G_m, suppose C(9)=0 mod p and C'(9) != 0 mod p. Set q_C=C(9)/p (mod p), d_C=C'(9) (mod p), and u_C=-q_C/d_C (mod p). Then

**C(9+p u_C)=0 (mod p^2), and u_C is the unique solution mod p.**

Proof: finite polynomial Taylor expansion C(9+pu)=C(9)+pu C'(9) mod p^2; division by p yields the unique linear equation q_C+u d_C=0 mod p. GH-18 supplies the conditional derivative nonvanishing at z=9 (not one of the exceptional points 0,1,5). No assertion is made that the relevant F/G first-digit zeros exist for *every* prime.

This Hensel shift concerns an **auxiliary parameter**. It does not change the original S/W input z=9, produce an automatic supercongruence at the fixed parameter, or establish native Heartbeat World X6 dynamics. GH-17's factorization of the GH-16 Laurent obstruction into F_m G_m is only proved mod p, not automatically mod p^2.

## Exact certificates and finite verification

At p=19, m=2: F_2(z)=(z^2+14z+21)/21. Thus F_2(9)=76/7=19*4/7, q_F=6 mod 19, F_2'(9)=32/21=16 mod 19, u_F=2, and F_2(47)=8*19^2/21. At p=11, m=1: G_1(z)=5+21z/4, G_1(9)=209/4=11*19/4, q_G=2, G_1'(9)=21/4=8 mod 11, u_G=8, and G_1(97)=11^2*17/4.

Additional certificates (p, m, channel, q, derivative mod p, u, root mod p^2):
(43,5,F,5,9,9,396); (59,7,G,14,3,15,894);
(67,8,F,10,10,66,4431); (139,17,F,11,79,72,10017).

An independently executed Python standard-library exact checker validated GH-20 coefficientwise at every r and both retained moments for **all 310 primes 11<=p<10000 with p=3 mod 8**; checked the GH-19 integer-binomial representation for p<1500 and exact original rational evaluations at p=11,19,43. For all 310 sampled primes, the corresponding branch (F for p=19 mod 24; G for p=11 mod 24) vanished mod p and the shifted root was re-evaluated as exactly zero mod p^2. Every sampled fixed-parameter divided quotient q_C was nonzero. These sample patterns are *finite computational observations*, not universal proofs.

## Scope and continuation

BRC-compatible source/observer information: (p,m,r,z), coefficients a_r/c_r, variation nu_r, separate F/G moment, derivative, divided residual, and actual parameter shift. Preserve original W/S/Hasse labels, six Hasse ports, finite endpoints, positive infinity and original GH-15/16 Laurent corrections. Scalar rank and p-adic precision are not X6 spatial axes, and no native six-dimensional readout bridge is asserted. No native p=373 run was performed.

Unfinished: prove or refute for all target primes the original fixed-argument first-digit root F_m(9)=0 (p=19 mod24) or G_m(9)=0 (p=11 mod24), e.g. with a genuine prime-dependent finite-field/CM or WZ certificate. The exact integral GH-19 input is B_m=[t^m](1+t)^{3m+1}(1+9t)^m and B_m=0 mod p iff F_m(9)=0 mod p. If the root is proved, use the GH-20 correction and GH-21's quantified first lift to build a source-preserving next-digit bridge, and separately compute the actual p^2 correction to GH-17's Clausen factorization; do not conflate it with the original LIFT target.

Native formal acceptance, H0/B0, [X]U mod p^2, Frobenius eta/kappa, native p=373 and independent Driver review remain OPEN.

Execution-control: gateway status 0.6.11 had research_authority_granted=false, executor_binding_configured=false; no current winning claim, authorized open, Source durable checkpoint or Research-Activity admission was established. Historical self recovery https://github.com/awdawmip/kimi-query-bridge/issues/6622, continuation https://github.com/awdawmip/kimi-query-bridge/issues/6623, control issue https://github.com/awdawmip/enterprise-math/issues/1558. Do not borrow any former or maintenance session. Earlier GH-17 through GH-19 have a separate portable ZIP and unclosed remote synchronization debt; this new GitHub note does not silently publish them.
