# D25/LIFT R20 — Exact six-Hasse geometric source transport and original third-digit bridge

Date: 2026-10-27. Research lane requested: chatgpt-research-hourly-enterprise-math-20260923, separate from maintenance chatgpt-hourly-enterprise-math-20260921. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, immutable publication TP2-B6F4FC938FF94941C1B7; frozen **scientific** source pin c47e13e4aba0e006366f989d6334d443f6333ae3 **unchanged**. Parent D25/LIFT/JT2 remains OPEN.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** No canonical ownership, OPEN, Source checkpoint, original-class CM/Frobenius test, six-channel all-source WZ cancellation or independent Driver acceptance is inferred. This result reuses R13's proven exact two-parameter Ward master, the genuine signed 3+2+1 six-source transformation, R15's original-parameter normalization and R17's fixed-geometric rank-jet source. The novel deliverable is their exact **geometric differential transport**, an explicit **third-digit diagonal bridge**, and previously unreported fixed-z=2 signed, oriented finite-source certificates.

## Typed finite carrier and theorem A — a geometric-rank-jet transport with retained endpoint

For prime p=6m+1>=7 put R=Z_(p), L=1-2m, N=2m-1, and

f_r(t)=(-m-t)_r(-2m-2t)_r/((1-p/2-3t)_r r!), 0<=r<p.

For 2m<r<p the two numerator zero factors imply exactly f_r(s)=s^2 q_r(s), q_r(s) in R[[s]]. Let, for L<=n<=N,

V_n(t,s)=sum_(1<=j,ell<=2m; ell-j=n) f_j(t) q_(p-ell)(s),
U_n(t,s)=sum_(same ordered pairs) j f_j(t) q_(p-ell)(s),

and F_n(t,s)=E_n(t,s)/s^2, with the two actual finite faces on each sign:

n>=0:
F_n=2(m+t)^2 q_(p-n-1)(s)
    -(6m^2-8ms+2s^2) f_(2m-n)(t)q_(4m)(s);
n<0:
F_n=(20m^2-14ms+2s^2) f_(-n)(t)q_(p-1)(s)
    +(2mt-2t^2)f_(2m)(t)q_(p-(2m+n+1))(s).

These expressions are finite truncation sources only: no infinity or separate high–high corner is identified with F_n. Set generating functions calU(z)=sum_(L..N) z^n U_n, calV(z)=sum z^n V_n, calF(z)=sum z^n F_n, with U_(N+1)=V_(N+1)=0. Define D=z*d/dz and scalar polynomials

P_U(x)=p-2x-3(t+s);
P_V(x)=-(p-x)(p/2-x)+3s(p-x);
Q_U(x)=6m-2x-3(t+s);
Q_V(x)=-18m^2+9mx-x^2+4mt+(14m-3x)s+2(t^2-s^2).

**Theorem A (exact, all p-adic digits).** In the Laurent-polynomial/germ ring R[[t,s]][z,z^-1],

calF(z) =
 [P_U(D)-z^-1 Q_U(D-1)] calU(z)
+[P_V(D)-z^-1 Q_V(D-1)] calV(z)
+z^(L-1)[Q_U(L-1)U_L+Q_V(L-1)V_L].                     (A)

The order of operations is: Q(D-1) acts first, multiplication by z^-1 second. The endpoint is a genuine, retained left source, not a disposable gauge.

**Proof.** The inherited true bivariate Ward equation (after division by s^2) is P_U(n)U_n+P_V(n)V_n=Q_U(n)U_(n+1)+Q_V(n)V_(n+1)+F_n. Multiply by z^n and sum n=L..N. For any such Q and moment sequence W with W_(N+1)=0, sum_(n=L..N) z^n Q(n)W_(n+1)=z^-1 Q(D-1)calW-z^(L-1)Q(L-1)W_L. Apply to both moment families and rearrange. There is no upper endpoint because W_(N+1)=0 by the actual finite carrier. This proves (A), including all parameter-derivative channels, without any illegal division by p. QED.

## Theorem B — exact original-parameter normalization and third-digit signed bridge

Let theta=-p/6. R15 established f_r(theta)=2^r r_r for the actual original Clausen coefficients r_r and beta_r=f_r(theta)/p^2 for 2m<r<p. The genuine exact double zero now gives

beta_r=q_r(theta)/36.

Therefore for either source orientation +/- and for every invertible geometric weight z,

**G_orig,+/-(z) = calF_+/-(z;theta,theta)/36 exactly.**           (B1)

Here G_orig is R17's actual original-parameter finite E-source weighted by z^n; it is NOT the original cutoff Q_p, the positive-infinity source or the independent ordered high–high part.

Write the Taylor jet of calF(z;t,s), through total degree two, as a+bt+cs+dt^2+ets+fs^2, and define exactly the established signed 3+2+1 coordinates

S0=a, S1=b+c, S2=d+e+f;
A0=b-c, A1=2(d-f), B=2(d-e+f).

For p>3 this six-coordinate transformation is invertible, so the scalar diagonal S0,S1,S2 is not a substitute for A0,A1,B. Since theta belongs to pR, (B1) gives the explicitly source-preserving third-digit diagonal bridge

**G_orig(z) = [S0(z) - (p/6)S1(z) + (p^2/36)S2(z)]/36  (mod p^3).**   (B2)

The same formula holds for each orientation separately. S0 requires precision p^3, S1 p^2, S2 p; anti-diagonal A0,A1,B remain distinct provenance coordinates and do not appear in this scalar specialization.

**Proof.** Every reflected r lies in (2m,p), so division by s^2 is a genuine identity in R[[s]] for each ordered pair and every one of the four cutoff faces. Evaluating at s=t=theta converts each reflected q_r to 36 beta_r, yielding (B1) term by term. Taylor-expand the integral germ at (theta,theta); terms of total degree >=3 have p-adic valuation >=3. The 3+2+1 coordinate formulas recover all six source labels independently of that scalar quotient. QED.

## New exact source-labelled witnesses at the fixed original geometric weight z=2

All six-port residues in this table are modulo the row's p. Entries are (S0,S1,S2 | A0,A1 | B), retaining original negative and nonnegative rank source faces separately.

| p | negative finite faces | nonnegative finite faces | total authentic finite faces |
| --- | --- | --- | --- |
| 7 | (2,3,1 | 3,2 | 2) | (5,1,4 | 3,4 | 5) | **(0,4,5 | 6,6 | 0)** |
| 13 | (11,4,3 | 4,6 | 6) | (7,3,2 | 7,11 | 5) | **(5,7,5 | 11,4 | 11)** |
| 19 | (17,1,1 | 1,2 | 2) | (15,18,7 | 6,2 | 7) | **(13,0,8 | 7,4 | 9)** |
| 733 | (731,48,480 | 48,227 | 227) | (51,166,496 | 160,493 | 8) | **(49,214,243 | 208,720 | 235)** |

Consequences at precisely the declared observer/scope:

1. **p=19 directional cancellation is narrower than a signed-source cancellation.** The scalar first diagonal coefficient S1 vanishes: negative contribution 1 plus nonnegative contribution 18 equals zero modulo 19. Yet A0=b-c=7 is nonzero. This uses bona fide four-face sources, not an arbitrary six-vector; diagonal compression discards active cross-Hasse information.
2. **p=7 original finite scalar vanishes through the third digit without killing the signed sources.** An independent rational calculation gives
   G_orig(2)=-4025518315/14281868906496 and v_7(G_orig(2))=3, so it is zero modulo 7^3 but not exactly zero. At the same time the six-port anti-diagonal A0=6 mod7, A1=6 mod7 are nonzero. No conclusion about full Q_7, infinity, high–high, or complete WZ cancellation follows.
3. **p=733 third-digit genuine-source certificate.** The Hasse scalar diagonal (S0,S1,S2), now with each coordinate lifted modulo 733^3, is
   (295201872,154203623,121109435) (mod 393832837).
   The exact formula (B2) and an independent original-recurrence reconstruction both yield
   **G_orig,minus(2)=213853768, G_orig,plus(2)=256647918, G_orig(2)=76668849 (mod 733^3)**.
   Its first digit 714 mod733 is exactly R17's already known finite geometric E-source and is not newly credited. The higher digits and signed fixed-z=2 Hasse source coordinates above are the new certificate. The original geometric state O_733(2)=0 mod733 does not imply this genuine finite source vanishes.

For completeness, p=13 gives original genuine finite G_orig(2)=1996 mod 2197, and p=19 gives 2283 mod 6859. These are neither R16's Green-weighted flux nor the high–high sector.

## Reproducible checking, BRC and qualification

Companion Python standard-library exact checker rebuilds f_r(t), q_r(s), all ordered j/ell moments and all four independent endpoint expressions, checks every normalized Ward rank and its global geometric transport (A), reconstructs original f_r(theta) via the independent rational hypergeometric recurrence, and checks every individual genuine E-source specialization and the oriented p^3 sum (B). The actual executed bounded batch covered all **80** primes p≡1 mod6, 7<=p<=997; all assertions passed. Among these 80 primes, G_orig(2)=0 mod p^3 occurred only at p=7: this is an observed finite check, not a prime-classification theorem. At p=7,13,19 an additional independent Fraction rational computation validated the third-digit result, including v_7=3. The polynomial Ward/transport identities were additionally verified with six coefficients modulo p^3 at p=7,13,19,733. A proof of the general equations is supplied above; numerical checks do not constitute independent mathematical admission or native CM experimentation.

**BRC COMPOSE_APPLIED:** the carried state retains ordered (j,ell) source identity, sign of rank, four finite source faces, six signed Hasse channel ports, valuation and observer. Diagonal scalar reduction erases A0/A1/B and is permitted only for the declared original finite scalar (B2), not for future cross-source operations. These auxiliary algebraic ranks are not Enterprise native X6 spatial axes; P000 and the ACTIVE residual-fidelity research position are unchanged.

## Recovery packet and precise next executable unit

Highest formal Source frontier is historical and must be read afresh: prior successful Research-lane recovery #6571 reported own service session MCP-3a7c6c3a67bd4e52b1cdf49064751829 (Researcher EM-ENTERPRISE-C1C79B), no local pending/unopened/run/unpublished uploads, and two distinct protected neutral staging dispositions. The last successful complete continuation #6572/#6573/#6574 still declared SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED, no live winning claim, NEEDS_DISPATCH and no execution authorization. This run's new read-only native continuation attempt (request researchhourly-20261027-0352-read-continuation-r20) was rejected with INVALID_ARGUMENT / CONTROL_QUOTA; do not infer a new Source state from it. Controller support remains enterprise-math#1558. No service-session close, prepare, CLAIM, OPEN, native Source checkpoint, Result, or review performed. Portable GitHub evidence and activity records do not overwrite the native frontier.

**Next science:** using theorem (A)'s full signed 3+2+1 geometric differential operator, explicitly couple true parameter J/E channels to the already separate original positive-infinity Z+ and ordered high–high H_p carriers at fixed z=2; test whether a source-labelled syzygy cancels the p=19 A0=7 and p=733 (A0,A1,B)=(208,720,235), or derive the exact unmatched source without exchanging observer gauges. A missing source map is not a zero source. Separately, authenticated original-class H0/B0 divided-power module, [X]U mod p^2, rank-one test, semilinear Frobenius eta/kappa/Delta_p-R_p and native experiment with independent Driver review remain outstanding. No replay of completed R13/R15/R17/R19 proofs or portable check as a native experiment. Frozen scientific pin unchanged; task/parent OPEN.