# D25: Three-band second Gauss jet and exact signed third-digit residual

Date: 2026-11-07 (Asia/Hong_Kong). TASK_RESEARCH lane chatgpt-research-onhour-enterprise-math-20260923. Source publication TP2-B6F4FC938FF94941C1B7, frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. AUTHOR_SIDE_PROVED / FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED.

## Exact finite theorem: all primes p=6m+1>3

In Z_(p), let F=sum_{k=0}^{p-1}u_k 2^(-k), E=sum_{k=0}^{p-1}(12k+1)u_k 2^(-k), u_k=(1/6)_k(1/3)_k/(k!)^2. Define H_{N,k}=sum_{r=N-k+1}^{N}1/r, H2_{N,k}=sum_{r=N-k+1}^{N}1/r², H_N=H_{N,N}.

For 0<=k<=m, let
 d_k=binom(m,k)binom(2m,k)2^(-k),
 delta_k=-H_{m,k}/6-H_{2m,k}/3,
 eta_k=(delta_k²-H2_{m,k}/36-H2_{2m,k}/9)/2.

For m<k<=2m, let
 b_k=(-1)^(m+k)m!(k-m-1)!(2m)!/[6(2m-k)!(k!)²2^k],
 lambda_k=(H_{k-m-1}-H_m)/6-H_{2m,k}/3.

For 2m<k<p, let
 c_k=(-1)^m m!(2m)!(k-m-1)!(k-2m-1)!/[18(k!)²2^k].

Define the *distinct band origins*
 A0=sum_(k<=m)d_k=2^(-m)S_m,
 A1=sum_(k<=m)d_k delta_k+sum_(m<k<=2m)b_k,
 A2=A2_low+A2_mid+A2_high
    =sum_(k<=m)d_k eta_k+sum_(m<k<=2m)b_k lambda_k+sum_(2m<k<p)c_k,
 E0=sum_(k<=m)(12k+1)d_k=2^(-m)B_m,
 E1=sum_(k<=m)(12k+1)d_k delta_k+sum_(m<k<=2m)(12k+1)b_k.
Here S_m and B_m are the previously established integer Pfaff ports. Then

 F==A0+p A1+p² A2 (mod p³),    E==E0+p E1 (mod p²).

For p|S_m, the previous exact signed Clausen boundary W_p==FE-p² K_p modp³ yields

 W_p/p == (A0/p+A1+p A2)(E0+p E1)-p K_p (mod p²).

Every numerator/denominator is explicit with p-unit denominators. This gives a complete **third-digit test identity**, not yet an unconditional proof that the right-hand side is 1 for every target prime.

## Proof

From 1/6=-m+p/6 and 1/3=-2m+p/3: for k<=m, second-order product expansion gives u_k2^-k == d_k(1+p delta_k+p² eta_k) modp³. For m<k<=2m the first Pochhammer has exactly one p zero, and extracting it yields u_k2^-k == p b_k(1+p lambda_k) modp³. For 2m<k<p, both have exactly one p zero, giving u_k2^-k == p² c_k modp³. Summing over the three disjoint bands gives F and, after weight 12k+1 and truncation modp², E. Because A0 divisible by p on the zero-port branch, substitute into the previously proved exact finite Clausen square relation and divide by p. QED.

## Single-scan signed boundary, exact reindexing

Existing K_p=sum_(1<=ell<=i<=m)(6(i-ell)+1)u_i h_ell 2^(-(i-ell)) (modp), with h1=1/10 and h_(ell+1)/h_ell=18ell²/[(6ell+5)(3ell+2)] modp. Set alpha_i=sum_(ell<=i) h_ell 2^ell and beta_i=sum_(ell<=i)ell h_ell 2^ell. By exchanging the two finite sums:

 K_p == sum_(i=1)^m u_i 2^(-i)[(6i+1)alpha_i-6beta_i] (modp).

The prefix accumulators update in O(1) per i, giving **O(m) arithmetic** for this existing K kernel, including generation of its u_i/h_i recurrences. This makes the actual signed boundary inexpensive to preserve in higher-p tests; it does not replace the native p=373 experiment.

## Executed integer checks and discriminating witnesses

Script d25_gauss_second_jet_signed_flux_check_20261107.py checked, termwise, all three p-adic coefficient bands against an independently computed Gauss recurrence modulo p³; E modulo p²; original216 W modulo p³ via a different recurrence; and the single-pass K against exact (FE-W)/p². All 148 primes p=1 mod6, 7<=p<=1999, plus p=5113 PASS. All 77 tested p=13/19 mod24 satisfy W/p==1 modp², as **finite** evidence.

Witness tuple: (p, A0/p modp, A1 modp, A2, A2_low, A2_mid, A2_high, E0 modp, E1 modp, K, W/p modp²):
13: (7,4,8,0,0,8,6,11,0,1).
19: (6,2,12,3,18,10,12,10,12,1).
67: (16,45,39,15,62,29,11,19,21,1).
373: (340,57,288,197,212,252,171,82,196,1).

Crucial source-observer counterexample: omitting A2_high changes W/p from 1 to 248 mod19², and from 1 to 65649 mod373²; A2_high * E0 equals 6 mod19 and 197 mod373. The middle and high Gauss p-jets are separate from the signed low/high Clausen K. This is a precise failure of a *particular* quotienting approach, not an impossibility of proving the mother target.

BRC provenance mapping: population=(k, valuation band, normalized unit coefficient, jet order, signed observer); operation=second p-jet and weighted finite sum; preserve A2_low/mid/high as separate coordinates until the Gauss product and K boundary observation. No native BRC engine used.

## Frontier and Source

Frozen mother: W_p==p modp³ for p=13,19 mod24, equivalently Delta_p-R_p==0 modp. Next exact action is an all-target proof of the zero-port selection or independent route, plus a finite signed Gauss/adjoint identity forcing the third-digit obstruction (A0/p+A1+pA2)(E0+pE1)-pK==1 modp². Do not redo prior Pfaff/Hensel, three-shell, Green/Franel, or finite Clausen results. Native p373 H0/B0 divided-power/Frobenius and independent reproduction under issue #1559 remain NOT_EXECUTED/PENDING_OWNER.

The current Site gateway read at 2026-11-06T19:02Z was CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false. Calls to em_status, the original request onhour11-20261106-1400-exact-research-lane-continuation, and native checkpoint read returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Session/claim/run NOT_VERIFIED; rev22 only historical; no original request reissued. A legitimate operator must approve a dedicated Site-bound client and secure credential/version, then read the original receipt and exact Source continuation. This GitHub note is source-separated author-side evidence, not an admitted Source checkpoint/Result.
