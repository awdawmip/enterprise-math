# D25/LIFT R21 — Genuine fixed-2 six-Hasse finite faces: exact moment telescope and signed residues

Date 2026-10-27. Research logical lane chatgpt-research-hourly-enterprise-math-20260923 (not maintenance). Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** No native task checkpoint, Result, original-class experiment or independent review.

## Existing inputs, new question

Consume R13's authentic four-cutoff bivariate Green–Ward master, the prior exact signed six-Hasse 3+2+1 observer and diagonal information-loss proof, R15's original parameter bridge and positive-rank complement, R17's distinct rank-jet geometric observer, and R20's triangular cutoff Smith forms, without recrediting them. What are the actual **six separately labelled** finite-face source coefficients at **fixed geometric rank weight z=2**, with both rank orientations preserved? Can all of them be obtained from an exact finite rank-moment identity retaining the real leftmost boundary?

Let prime p=6m+1>=7, R=Z_(p), L=1-2m and N=2m-1. Reuse f_r(z)=(-m-z)_r(-2m-2z)_r/((1-p/2-3z)_r r!), 0<=r<p. Every reflected high index 2m<r<p has exact factor f_r(s)=s^2 q_r(s), q_r(0) a p-unit. On genuine ordered pairs 1<=j,ell<=2m with ell-j=n put

V_n(t,s)=SUM f_j(t) q_(p-ell)(s);
U_n(t,s)=SUM j f_j(t) q_(p-ell)(s);
F_n(t,s)=E_n(t,s)/s^2,

where the sum is restricted to ell-j=n and E_n is exactly R13's four-origin genuine finite face. U_(N+1)=V_(N+1)=0 by the real cutoff. All are regular germs; their [1,t,s,t²,ts,s²] coefficients are the six original Hasse source labels (0,2),(1,2),(0,3),(2,2),(1,3),(0,4), not the original parameter evaluation at theta=-p/6.

## New exact theorem: fixed-2 six-channel moment transport

For any integer k define the original bivariate master polynomials

alpha_k=p-2k-3(t+s),
beta_k=-(p-k)(p/2-k)+3s(p-k),
gamma_k=6m-2k-3(t+s),
delta_k=-18m²+9mk-k²+4mt+(14m-3k)s+2(t²-s²).

For the **actual full finite-face rank source** G_2(t,s)=SUM_(k=L..N) 2^k F_k(t,s), we have an identity of rational germs in the p-local ring:

**G_2 = SUM_(k=L..N) 2^k [(alpha_k-gamma_(k-1)/2) U_k + (beta_k-delta_(k-1)/2) V_k] + 2^(L-1)[gamma_(L-1)U_L+delta_(L-1)V_L].** (T)

The interior U coefficient simplifies exactly to 3m-k-(3/2)(t+s); the V coefficient is a quadratic rank polynomial. All four genuine finite cutoff origins contribute to F; the final term in (T) retains the true left boundary. Neither positive infinity nor ordered high/high is identified with a finite face.

**Proof:** Normalize R13's exact source master by s² using the proven two numerator zeros in every reflected factor, including the true edge faces. Its exact rank relation is F_k=alpha_k U_k+beta_k V_k-gamma_k U_(k+1)-delta_k V_(k+1). Multiply by 2^k and sum on the actual finite interval. Shift the last two sums by index k+1. Their internal coefficients are 2^(k-1)gamma_(k-1) and 2^(k-1)delta_(k-1). The terminal U_(N+1)=V_(N+1)=0 is a genuine absent pair population; restoring the missing lower-end k=L coefficient produces exactly the last term of (T). This is exact over R[[t,s]], not merely a finite-field pattern, and requires no division by p. Taking all six Hasse coefficients gives six legitimate source-to-moment identities. QED.

## New genuine fixed-2 source certificates

For six-vector v=(a,b,c,d,e,f), the established signed 3+2+1 readout is (S0,S1,S2;A0,A1,B)=(a,b+c,d+e+f;b-c,2(d-f),2(d-e+f)). Exact modular computation *directly from the four genuine E edge origins*, independent of the moment-side expression (T), gives:

| p | n<=0 cutoff six-vector | n>0 complement six-vector | total G_2 six-vector | total signed (3+2+1) |
|---:|---|---|---|---|
| 13 | (6,4,8,0,2,0) | (12,5,3,2,1,0) | **(5,9,11,2,3,0)** | **(5,7,5;11,4,11)** |
| 733 | (438,226,351,322,392,167) | (344,718,385,223,587,18) | **(49,211,3,545,246,185)** | **(49,214,243;208,720,235)** |

For further provenance at p=733, the four *true* finite edge origins, aggregated within their own sign branch and weighted by 2^k, are:

- nonnegative-rank first shift: (577,406,498,248,621,322)
- nonnegative-rank second shift: (207,490,238,550,358,596)
- strictly negative-rank first shift: (731,48,0,520,0,0)
- strictly negative-rank second shift: (0,0,0,693,0,0)

Their sum is the displayed full six-vector modulo 733. The E formula branches at n>=0 versus n<0, while the Clausen lower cutoff includes n=0 and the complement is n>0; these partitions are not confused. In particular, fixed-2 authentic **finite-face** transverse residues (208,720,235) are all nonzero mod733. This does **not** establish noncancellation of the complete J/E/infinity/high-high/original-class objective.

## Executed author evidence and precise frontier

Companion Python standard-library file 20261027_hourly_d25_signed_fixed2_ward_face_r21_check.py. **Actually executed PASS** for p=7,13,19,31,37,43,733: original rational Pochhammer recurrence converted to exact mod-p polynomial jets through degree four; real reflected s² factor; all six separate E-source jets from the four edge origins; independently built ordered V/U moment jets and each rank master identity; full fixed-2 telescope (T); and the previously established p=13 individual real edge rows F_-3,F_0,F_1. The general identity is proved algebraically; the listed residues are finite, author-checked, not native CM or independent Driver experiments.

**BRC COMPOSE_APPLIED:** preserve ordered (j,ell), genuine edge origin and sign, six Hasse labels, fixed geometric weight, and residual transverse coordinates. Diagonal and scalar totals are deliberately restricted observer ports, not proof of safe compression under later cross-source operations. These rank indices are not native X6 axes; P000 and ACTIVE residual-fidelity worldview remain unchanged.

**Next smallest science:** now combine (T) with the six separately labelled genuine J coupling, original scalar cutoff and positive/infinity Z^+, and independent ordered high/high H_p. Decide an authentic cross-source WZ syzygy at fixed z=2, or publish a source-labelled nonzero residual. Same-original-class H0/B0, [X]U mod p², normalized Frobenius eta, kappa, Delta_p-R_p, native experiment and independent review remain OPEN. D25/LIFT/JT2 mother objective OPEN.

**Control:** direct em_status 0.6.11 reports research_authority_granted=false. The fresh exact continuation researchhourly-20261027-0325-continuation-r20 failed INVALID_ARGUMENT/CONTROL_QUOTA. Last verified own recovery #6567 had no pending/authorized run/unopened claim/unpublished uploads, retaining two neutral staging archives; successful read-only continuation #6568 preserved historical SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED and execution_authorized=false. Existing control support enterprise-math#1558 owns the transition/CAS fix. Do not infer CLAIM/open/native publication/freeze/admission from this portable GitHub file.