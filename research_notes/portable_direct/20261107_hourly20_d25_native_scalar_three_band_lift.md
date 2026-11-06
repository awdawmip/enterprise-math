# D25 / D=-24: exact three-valuation-band LIFT correction and prime-field tail formula

Date: 2026-11-07 (Asia/Hong_Kong). Status: AUTHOR-SIDE PROVED ALGEBRA / EXACT FINITE VERIFICATION / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. This result uses the **actual frozen scalar G_p h interface**, not the separate D25 auxiliary tangent observer. Logical Research lane: chatgpt-research-hourly-enterprise-math-20260923; exclude maintenance lane chatgpt-hourly-enterprise-math-20260921. Existing accepted parent: research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md. The accepted UR/JT0 first digit is an input, not reproved here.

## Exact source and theorem

Let p=6m+1 be a prime (p>=7), in the localization Z_(p). Define

B_0=1,   B_{k+1}=B_k (6k+1)(3k+1)/[36(k+1)^2],  0<=k<p-1,
g=sum_{k=0}^{p-1} B_k,  h=sum_{k=0}^{p-1}(12k+1)B_k,
G=g/p, Delta=(Gh-1)/p mod p.

For target p mod24 in {13,19}, the pinned parent proves g in p Z_(p) and Gh=1 mod p. Write three **label-preserving** bands

I0={0,...,m}; I1={m+1,...,2m}; I2={2m+1,...,p-1}.
g_i=sum_{k in Ii} B_k; h_i=sum_{k in Ii}(12k+1)B_k.

THEOREM A (exact valuations): for every index k in Ii, v_p(B_k)=i. Hence g1,h1 in p Z_(p), g2,h2 in p^2 Z_(p). In the target classes g0 is also in p Z_(p). Define p-integral

U=(g0+g1)/p, H=h0, V=h1/p, W=g2/p^2.

Then the frozen LIFT observable has the **source-separated exact formula**

Delta = K + M + Z (mod p),
K=(UH-1)/p (mod p), M=UV (mod p), Z=WH (mod p).

The first quotient K is integral by accepted first-digit UR: UH=Gh mod p. Therefore the original LIFT claim is equivalent, with its original R_p unchanged, to

K+M+Z = R_p (mod p),  for all target primes p mod24 in {13,19}.

The precision budget is explicit: U and H require mod p^2, V and W only mod p; h2 can be omitted modulo p^2, but g2 must be retained after the division of g by p. All signed weighted k-source ports, two target residue classes and quotient order are preserved.

Proof of valuations: for r>=0, 6r+1=p+6(r-m) and 3r+1=p+3(r-2m). For r in [0,p-2], the first numerator has precisely the one p-factor at r=m, and the second at r=2m. Denominators 36(r+1)^2 are units. Thus v_p(B_k)=0,1,2 on I0,I1,I2. Consequently g=g0+g1+p^2W=p(U+pW) and h=H+pV+h2 with h2 in p^2 Z_(p). Multiply G*h=(U+pW)(H+pV) mod p^2 and divide (Gh-1) by p. QED.

THEOREM B (prime-field closed leading coefficients): Define f! in F_p for 0<=f<p. In each band let b_k=B_k/p^i mod p for k in Ii. Then

I0, 0<=k<=m:
 b_k = m!(2m)! / [2^k (m-k)! (2m-k)! (k!)^2] (mod p).

I1, m<k<=2m:
 b_k = (-1)^(m+k) m!(2m)!(k-m-1)! /
       [6*2^k (2m-k)! (k!)^2] (mod p).

I2, 2m<k<p:
 b_k = (-1)^m m!(2m)!(k-m-1)!(k-2m-1)! /
       [18*2^k (k!)^2] (mod p).

Proof: expand the finite product for B_k. Remove the factor 6m+1=p at r=m and, where present, the factor 3(2m)+1=p at r=2m. For all remaining factors reduce 6r+1 to 6(r-m) and 3r+1 to 3(r-2m) mod p. The two signed factorial intervals and powers 6,3 divided by 36^k give the displayed formulas. All denominators are p-units (k<p). QED.

In particular, the exact mod-p values V and W can be calculated purely in F_p:

V = sum_{k=m+1}^{2m}(12k+1)b_k (mod p),
W = sum_{k=2m+1}^{p-1} b_k (mod p).

The low-band leading formula is binom(m,k)binom(2m,k)2^(-k), explicitly connecting g0 mod p to the already accepted terminating CM/Hesse interface. The upper-band formula isolates a **new source-relevant divided p^2 tail observer** instead of erasing it by mod-p truncation.

## Exact computational evidence

The companion executable d25_lift_three_band_minimal_verified_20261107.py used integer modular recurrence modulo p^3, separately evaluated all three factorial formulas at every k, and independently recomputed the full G*h scalar. For all 166 target primes p<5000: the three-band formula, each B_k valuation and its finite-field leading coefficient passed. For all six target primes p<=90 a second implementation using exact Python Fraction B_k recurrence independently reproduced Delta. In 165 of 166 tested target primes the upper-tail contribution Z is nonzero (the zero instance within this range is p=157).

 Selected rows (p : K, M, Z, Delta), all in F_p:
 13 : 3, 1, 9, 0.
 19 : 10, 15, 6, 12.
 37 : 15, 23, 10, 11.
 43 : 7, 5, 3, 15.
 109 : 108, 98, 62, 50.
 157 : 77, 5, 0, 82.
 373 : 2, 370, 197, 196.

At p=13, omitting Z gives 4 instead of the correct Delta=0; at p=19 it gives 6 instead of 12. Thus the previously tempting third-band truncation is explicitly falsified for the divided LIFT observer. The finite checks do not establish LIFT=R_p; no R_p comparison has been made in this new author-side unit.

## BRC applicability and frontier

Typed carrier: rational B_k with labelled index k, two special p-factors, exact p-adic valuation, and weighted h port. Observer: divide g by p, multiply by h, divide (Gh-1) by p, then reduce modulo p. Future operation: compare this exact Delta with frozen R_p / Phi_xx/Frobenius observers. Resolution COMPOSE_APPLIED with the existing D24 finite-sum scalar interface; the three bands are exact provenance-preserving subcarriers and do not assert an X6 native experiment.

New minimal next action: retrieve exact Source definition and pinned computation of R_p, insert it into K+M+Z-R_p, and seek a symbolic cancellation or an exact counterexample in the two target classes. The separate auxiliary D25 tangent lambda_p cannot be substituted for Delta without a proved map. Mother Delta_p=R_p mod p remains OPEN.

## Control boundary

Native em_status in this run rejected at preflight with BACKEND_IDENTITY_OR_VERSION_MISMATCH; operation_sent=false. Current own Researcher identity, protected staging, claim/run and native checkpoint remain unverified. Historical original pending requests em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 were not reissued. Existing support owner path: enterprise-math#1558. This note and checker are author-side portable evidence only, not a source-authenticated checkpoint, Result or independent review.
