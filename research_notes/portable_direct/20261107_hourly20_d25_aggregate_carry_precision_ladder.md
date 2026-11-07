# D25: aggregate Clausen carry precision ladder and universal digit 5
2026-11-07. TASK_RESEARCH author-side mathematical evidence, PROVED ALGEBRA + EXECUTED EXACT FINITE CHECKS; UNREVIEWED / NOT_ADMITTED. This is not a native Source checkpoint, Result, accepted theorem or current claim.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7. Immutable scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
Research logical lane: chatgpt-research-hourly-enterprise-math-20260923; maintenance lane chatgpt-hourly-enterprise-math-20260921 is excluded.

## Objects and observer
For p>3 prime, p≡13 or 19 (mod24), define p-integral Gauss coefficients
f_i=(1/6)_i(1/3)_i/(i!)^2, g_i=(1/8)_i(3/8)_i/(i!)^2, 0≤i<p.
Let F_p(z)=Σ_{i<p}f_i z^i, G_p(z)=Σ_{i<p}g_i z^i.
The aggregated *unprojected* Clausen carry is C_F(z)=Π_{deg≥p}(F_p(z)^2), C_G(z)=Π_{deg≥p}(G_p(z)^2), with Cauchy convolution performed BEFORE projection. Degrees below mean degrees of the polynomial reduced mod p^q (not the degree of a scalar value after z=1/2 or z=1/9). Argument rescaling by 2 and 9 preserves the p-adic coefficient valuations. Labelled individual ports (i,j) and their sum at fixed degree are different observers.

## Theorem A: 216 Gauss-square aggregate has a sharp order-2 top
For p=6m+1, m≥1,
C_F≡0 (mod p²);
deg(C_F mod p³)=p−1+m=7m;
[z^{7m}]C_F=2 f_m f_{p−1} (mod p³), v_p(2f_m f_{p−1})=2.
Proof. Since denominators are units and numerator p-factors first occur at indices m (from 1/6) and 2m (from 1/3), v_p(f_i)=0,1,2 for i≤m, m<i≤2m, 2m<i<p. Products of total valuation 0 or 1 have degrees ≤2m or ≤3m, both below p; products 1+1 have degree ≤4m<p. Thus every carry coefficient is divisible by p². The only valuation-two products possibly above degree 4m are 0+2 (max degree m+p−1=7m). At the maximal degree exactly two ordered pairs, (m,p−1) and (p−1,m), survive and their sum is 2f_m f_{p−1}; as p>2 this is nonzero mod p³. QED.

## Theorem B: 2304 Gauss-square has a three-digit support ladder when p≡5 mod8
Define r=(5p−1)/8, s=(7p−3)/8; 0<r<s<p. Then
deg(C_G mod p)=2r=(5p−1)/4, leading coefficient g_r², valuation 0;
deg(C_G mod p²)=r+s=(3p−1)/2, leading coefficient 2g_r g_s, valuation 1;
deg(C_G mod p³)=2s=(7p−3)/4, leading coefficient g_s², valuation 2.
All coefficients and degrees above are at their respective precision, and all three degrees are ≥p.
Proof. The numerator p-factor in (1/8)_i appears at zero-based index r, as 5p/8; in (3/8)_i it appears at index s, as 7p/8. Therefore v_p(g_i)=0,1,2 on i≤r, r<i≤s, s<i<p. Valuation-zero products have maximum degree 2r, with unique (r,r) endpoint. Valuation-at-most-one products reach maximum r+s with exactly the two ordered ports (r,s),(s,r) of valuation 1. For valuation-at-most-two products, the possible top-degree values are 2s from 1+1 and r+p−1 from 0+2. Since 2s−(r+p−1)=(p+3)/8>0, the only highest surviving endpoint is (s,s), of valuation 2. Thus cancellation at every claimed top coefficient is impossible. QED.

## Theorem B2: normalized middle carry digit is universally 5
For EVERY prime p≡5 mod8,
[z^{r+s}]C_G / p = 2g_r (g_s/p) ≡ 5 (mod p).
Here the coefficient is p-divisible, so its quotient is p-integral.
Proof. Mod p, 1/8≡−r and 3/8≡−s, so g_r≡binom(s,r). There is exactly one p-factor in the first Pochhammer numerator of g_s, at r, namely 5p/8. Removing that factor yields
g_s/p ≡ (5/8)(−1)^{r+s} r!(s−r−1)!/s! (mod p).
Since r+s=(3p−1)/2 is odd and s−r=(p−1)/4≡−1/4 (mod p),
2g_r(g_s/p) ≡ (5/4)(−1)/(−1/4)=5 (mod p). QED.
Let U0=[z^{2r}]C_G mod p, U1=([z^{r+s}]C_G/p) mod p, U2=([z^{2s}]C_G/p²) mod p. Then
U1=5 (mod p), and 4U0U2=U1²=25 (mod p).
This exact rank-one certificate recovers universal information that disappears when the high-degree product is simply truncated.

## Theorem C: 2304 Gauss-square has order-2 top for p≡3 mod8
Define r=(p−3)/8, s=(3p−1)/8. Then
C_G≡0 (mod p²);
deg(C_G mod p³)=p−1+r;
[z^{p−1+r}]C_G = 2g_r g_{p−1} (mod p³), valuation 2.
Proof. The first numerator p-factors occur at index r in 3/8 and index s in 1/8, so the unit/valuation-1/valuation-2 strata end at r,s,p−1. Total valuation <2 products have maximal degrees 2r and r+s=(p−1)/2 <p. The valuation-2 maxima are 2s and r+p−1; their difference (r+p−1)−2s=3(p−3)/8>0, hence unique top ordered ports (r,p−1),(p−1,r), summing without cancellation. QED.

## Secondary precise obstruction: no one-way rational scalar Gauss pullback
Let f(z)=2F1(1/6,1/3;1;z), g(z)=2F1(1/8,3/8;1;z). Their local exponent differences at (0,1,∞) are respectively {0,1/2,1/6} and {0,1/2,1/4}. Under any rational argument pullback of a full Fuchsian differential equation, a local exponent difference is multiplied by a positive integer ramification index; a nonzero rational scalar gauge leaves the difference unchanged. Over an ordinary base point it is an integer. Thus the full f-equation cannot yield a g-equation singularity with difference 1/4, and conversely the g-equation cannot yield f's 1/6. This excludes a single *rational scalar pullback of the complete second-order differential equation* in either direction, regardless of degree. It does not exclude two-leg/common-cover Heun transformations, non-scalar differential intertwiners, special-value identities, algebraic correspondences, or finite p-adic WZ summations. It does not invalidate the other research lane's separate analytic Heun candidate.

## Executed exact regression and representative witnesses
The companion Python stdlib script recursively computes all coefficients in Z/p³Z, constructs EVERY high-degree Cauchy coefficient, checks all first p-valuation strata, degree cutoffs, unique endpoint formulas and universal digit-5/rank-one identities. All 23 target primes 13≤p<500 PASSED. No float approximation and no native experiment.

p=13: A top degree 14, unit/p²=9; B degree ladder mod p,p²,p³ =16,19,22; U0,U1,U2=3,5,1.
p=19: A top 21, unit/p²=4; B vanishes mod p², top degree 20, unit/p²=15.
p=37: A top 42, unit/p²=22; B ladder 46,55,64; U0,U1,U2=33,5,10.
p=43: A top 49, unit/p²=7; B vanishes mod p², top degree 47, unit/p²=35.
p=109: A top 126, unit/p²=44; B ladder 136,163,190; U0,U1,U2=73,5,46.
p=373: A top 434, unit/p²=368; B ladder 466,559,652; U0,U1,U2=177,5,284.
The general proofs are not inferred from this finite test.

## Highest previous verified source frontier and continuation
Consume, do not repeat:
- research_notes/portable_direct/20261107_hourly20_d25_gauss_spectral_carry_bridge.md: previous individual-labelled-port minimum and Gauss spectral identity;
- research_notes/portable_direct/20261107_onhour_d25_heun_period_gate_signed_jet.md: separately authored fixed-band impossibility and p=19 scalar-truncation obstruction.
New result is the AGGREGATED noncancelling support, universal digit-5, rank-one relation, and one-way whole-equation pullback boundary.

The mother objective Δ_p−R_p=0 mod p, equivalently via pinned frozen bridge W_p=p mod p³ for p≡13,19 mod24, remains OPEN. These high-degree polynomial carry theorems are NOT a proof of the weighted finite-sum supercongruence. Next: attempt two-leg algebraic/Heun or finite-WZ transformation that includes the projection correction with digit 5 for p≡13 mod24 and order-p² top for p≡19 mod24; first evaluate p=13,19,37,43,109,373, preserving labelled ports and truncated derivative data.

Native status independently checked: em_status BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false; Site CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false. Protected session/claim/run/staging UNKNOWN_PRESERVE. Old exact requests em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 NOT RESENT. Activity REGISTER_PENDING; native checkpoint SYNC_DEBT. Control support awdawmip/enterprise-math#1558. This GitHub note is author-side evidence, not formal SOURCE publication.