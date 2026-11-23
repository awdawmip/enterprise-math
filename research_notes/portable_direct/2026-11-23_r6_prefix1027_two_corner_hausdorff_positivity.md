# PREFIX-1027 — Two-edge eventual Hausdorff positivity for the signed X6 BRC positive-port contrast

Date: 2026-11-23 (Asia/Shanghai). Scientific status: AUTHOR_EXACT_ANALYTIC_PROOF / EXTENDED_INTEGER_BRC_OBSERVER_CHECK / NOT_REVIEWED. Parent: PREFIX-1026. This research unit changes neither the immutable task inputs nor prior claims.

## Frozen object and purpose

Continue the P000 V5 scientific pin awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Candidate Stage46 signed twelve-direction BRC kernel W=J12-6I12, native X6, chosen Cell anchor, incoming -e1, bidirectionally blocked Link {0,e1}, exactly one negative outgoing step. Coherent signed amplitudes are combined in each joint Cell–terminal-port–grade fibre before square-mass observation. The exact integer Laurent observer and the three-A6-shift identity are inherited from PREFIX-1016/1018/1023/1026; no new native update is introduced.

Let a_m=Q^+_(m+4,1)-Q^+_(m+4,2), m>=1. The other five positive axes are symmetric. Let mu be the pushforward of six independent unit-circle Haar phases under L=|z1+...+z6|^2 in [0,36], so A6(r)=int y^r dmu. Let nu denote the **exact**, possibly signed functional of PREFIX-1026:

5nu[f]=-4 int y^2(y-36)^2 f'(y)dmu
       -2 int y(y-36)(17y-91) f(y)dmu
       +12 int(6-y){int_0^y (11+x)f(x)dx}dmu(y).

It has nu[y^m]=a_m for all m>=1. For nonnegative integers k put E_(m,k)=nu[y^m(36-y)^k], equal to the integer finite difference sum from PREFIX-1026.

## New Theorem A — fixed first index and arbitrarily late Hausdorff difference

Write rho(y) for the distribution density of L near y=0. It is continuous at zero with rho(0)>0. For **each fixed integer m>=1**, as k tends through the nonnegative integers to infinity,

E_(m,k) ~ (3024/5)rho(0) 36^(m+k+2) B(m+2,k+1)
        ~ (3024/5)rho(0) Gamma(m+2) 36^(m+k+2) k^(-m-2).

In particular E_(m,k)>0 for all sufficiently large k, for each fixed m. Both asymptotic equivalences are in the exact Laurent spectral observer; no native-heartbeat timing or physical-residual assertion is made.

### Proof of the density premise

The sum of two independent Haar unit-circle vectors has a planar radial density
q2(r)=1/(pi^2 r sqrt(4-r^2)) for 0<r<2, and zero outside. It is strictly positive on 0<r<2 and q2 belongs to L^(3/2)(R^2): its singularities at r=0 and r=2 are integrable to every exponent below 2. Young's convolution inequality gives q4=q2*q2 in L^3(R^2). Holder's inequality and translation continuity in L^3 show q6=q4*q2 is bounded and continuous on R^2. Since q2 and q4 are strictly positive on overlapping disks (away from the radial endpoints), q6(0)>0. Rotational invariance yields dmu(y)=rho(y)dy with rho(y)=pi q6(sqrt(y)), hence rho is continuous at zero and rho(0)>0. This is an exact regularity argument for the already established Laurent/Parseval observer; it does not generate an alternative native update or classical numerical comparison.

### Proof of the asymptotic

Set f(y)=y^m(36-y)^k, J_(p,q)=int y^p(36-y)^q dmu(y), and I_(p,q)=int_0^36 y^p(36-y)^q dy. Direct differentiation in the exact PREFIX-1026 functional gives

5E_(m,k)= -4m J_(m+1,k+2) +(4k+34)J_(m+2,k+1)
           -182 J_(m+1,k+1)
           +12 int_0^36 (11+x) f(x) H(x) dx,

where H(x)=int_[x,36](6-y)dmu(y). As A6(1)=6, int(6-y)dmu=0, so H(x)=-int_[0,x](6-y)dmu(y)=-6rho(0)x+o(x) when x decreases to zero.

For each fixed p>=0 and bounded integer shift s, density continuity gives
J_(p,k+s) ~ rho(0) I_(p,k+s) as k tends to infinity.
The normalized beta-integral measure concentrates at y=0; contributions from y>=epsilon have exponentially smaller weight, including the factors from differentiation. Let I=I_(m+1,k). The first three contributions divided by rho(0)I tend respectively to
-5184m, 5184(m+2), and -6552.
Here J_(m+2,k+1)/I ~ 36^2(m+2)/(m+k+3), hence its extra +34 term vanishes after division by I. The final Volterra term divided by rho(0)I tends to -792. The sum equals 3024, so
5E_(m,k) ~ 3024 rho(0) I.
Finally I=36^(m+k+2)B(m+2,k+1), and the standard factorial ratio gives its stated fixed-m asymptotic. The positive leading coefficient proves eventual positivity. QED.

## Theorem B — the complementary fixed-difference edge

The already proven full relative-phase expansion for the contrast (PREFIX-1025) has, for every K,
b_m:=a_m/36^m = CDelta m^(-7/2)(1+sum_(j=1)^K d_j/m^j+O_K(m^(-K-1))),
where CDelta=1530900/pi^(5/2)>0 is inherited symbolically, not evaluated numerically here. Taking sufficiently many expansion terms before applying each fixed order k of finite differences gives

E_(m,k)=36^(m+k)(-1)^k Delta_forward^k b_m
       ~ 36^(m+k) CDelta (7/2)_k m^(-7/2-k)

as m grows, for each fixed nonnegative integer k. Therefore E_(m,k)>0 for all sufficiently large m at every fixed k. The full expansion, rather than a leading equivalent alone, justifies the cancellation under k finite differences.

Together, the two edge theorems show that each fixed row and each fixed column of the infinite E-triangle is eventually strictly positive. The region where m,k both vary and grow remains the live simultaneous-positivity problem.

## New exact arithmetic evidence

A recurrence-based integer replication independently generates A6 from A6(0)=1, A6(1)=6, A6(2)=66 using the exact PREFIX-1018 third-order recurrence, checks its first eight collision counts, forms a_m by the PREFIX-1016 rational three-shift formula with exact integer divisibility, and iterates E_(m,k+1)=36E_(m,k)-E_(m+1,k).

First, a 240-triangle replay recovers the *exact* PREFIX-1026 digest ba12049d9510eabf3abef8326249de88d7edcfdf88f1d990d2539a51bae8afc8. Then a complete N=1200 triangle checks all 720600 pairs m>=1,k>=0,m+k<=1200, with no zero or negative witness. The ordered SHA-256 of the ASCII stream m,k,E followed by newline, ascending k then ascending m, is
b626fc2e4e12db5ce219ab6f5e69f0c0344f38d6fe63d189a768a935d888439e.

The exact checker and compact certificate are the companion files PREFIX1027_R6_HAUSDORFF_TWO_CORNER_CHECK.py and PREFIX1027_R6_EXACT_CERTIFICATE.json. The finite triangle is not used as a substitute for the two asymptotic proofs, and no all-(m,k) positivity or positive-measure theorem is claimed.

## Implications and next discriminating question

For any fixed m or k, E_(m,k) is eventually positive along the other coordinate. The unsolved question is uniform positivity when both indices grow (including proportional growth k/m and intermediate rates). A promising direct test is the sign of the signed functional's effective spectral density in the interior 0<y<36; a rigorous positive spectral representation would settle all m,k and the all-order Hankel conjecture. Alternatively a counterexample E_(m,k)<=0 would delimit this route. Keep the full Cell–port–grade signed BRC carrier for any claim about future native evolution.

The mother objective B_fix,odd(32) in {19,20} remains open. Original project author attribution: historical EM-DIRECT-FBEA5D, Activity RA-3FB2D033BE6048D8712FF056, SID MCP-45ad6d29cd534c1aad25595a72e3c532. These are provenance, not a present CLAIM or Reviewer identity.

## Exact source lineage

- PREFIX-1026: research_notes/portable_direct/2026-11-23_r6_prefix1026_hausdorff_spectral_transform.md and its published integer checker.
- PREFIX-1025: research_notes/portable_direct/2026-11-23_r6_prefix1025_contrast_hankel_jet_identity.md.
- PREFIX-1024 and PREFIX-1023: published fixed-order full asymptotic and original Laurent packet.
- PREFIX-1018: published third-order A6 recurrence and exact recurrence evidence.

Review status: NOT_REVIEWED; no new formal Result, independent Driver review, CLAIM/PROGRESS or P000 modification.
