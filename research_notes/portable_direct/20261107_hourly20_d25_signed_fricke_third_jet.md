# D25: third-order weighted Fricke CM jet and branch-conjugate second logarithmic derivative

**Date:** 2026-11-07. **Status:** AUTHOR-SIDE PROVED ALGEBRA / 26 TARGET PRIMES EXACT CHECKED / UNREVIEWED / NOT_ADMITTED. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable scientific input c47e13e4aba0e006366f989d6334d443f6333ae3; publication TP2-B6F4FC938FF94941C1B7. Research lane chatgpt-research-hourly-enterprise-math-20260923; maintenance excluded.

Consumes the same-lane 20261107_hourly20_d25_weighted_low_degree_jet_bridge.md (fbe820347866f8b8f8ae6d48da534f0889203672) and 20261107_hourly20_d25_fricke_weighted_local_twojet.md (625a4d42db5e4b379f9e3f021b3ca5e983d948e0), plus independent onhour Fricke maps at 6ffcf3e8e7a2876fdd4e35ddd7b1ca4d35754e07. This note establishes a new **third-jet constraint**, not a second independent proof of those inputs.

## Theorem 1: both original weighted-polynomial third-jet ratios

Let p≡13 mod24 be prime, p=6m+1=8k+5. Define F_m(z)=Σ_(j≤m) binom(m,j)binom(2m,j)z^j, H_k(w)=Σ_(j≤k)binom(3k+1,j)binom(k,j)w^j and the original weighted degree-<p 3F2 polynomial observers P_A=(1+6θ)A_<p, P_B=(1+8θ)B_<p. Reuse A_<p=F_m², B_<p=(1-w)H_k². The previously proved CM0 and CM/Hasse results give F_m(1/2)=H_k(1/9)=0 with nonzero respective first derivatives.

The two Gauss equations at the CM zeros and their first derivatives give the **new third unweighted ratios**:

  F_m''(1/2)/F_m'(1/2)=-1,  F_m'''(1/2)/F_m'(1/2)=65/9;
  H_k''(1/9)/H_k'(1/9)=-117/16,  H_k'''(1/9)/H_k'(1/9)=72657/512.

Proof: modulo p both equations are
  z(1-z)F''+(1-3z/2)F'-(1/18)F=0,
  w(1-w)H''+(1-5w/2)H'-(35/64)H=0.
Evaluate at a zero, differentiate once and evaluate again. Denominators are p-units for p≡13 mod24.

Differentiating P_A=F²+12zFF' and P_B=(1-9w)H²+16w(1-w)HH' three times, substituting the preceding ratios, yields

  **P_A'''(1/2)/P_A'(1/2)=116/9**;
  **P_B'''(1/9)/P_B'(1/9)=29403/256**.

These are exact finite-field identities for every prime in the stated class, not a finite-data fit.

## Theorem 2: necessary signed Fricke third-jet scalar gauge

Use the independently established rational Fricke maps

 z(t)=108t²(t+9)(t+8)²/(t+12)^6,
 w(t)=256t³(t+8)(t+9)³/(t²+36t+216)^4,

and both common CM fibers T_±=±6sqrt(2)∈F_(p²), with z(T)=1/2 and w(T)=1/9. For a nonzero formal local scalar gauge gamma_±(t) satisfying

  P_A(z(t))=gamma_±(t) P_B(w(t))+O((t-T_±)^4),

the first two conditions from the prior 2-jet theorem are retained:

  gamma_±(T_±)=±(6561sqrt(2)/1024)(F_m'(1/2)/H_k'(1/9))²,
  ell_±=gamma_±'/gamma_±(T_±)=-5/4±11sqrt(2)/12.

A new **third-jet matching identity**, obtained by taking three derivatives of the product gamma P_B(w(t)) and dividing by nonzero first derivatives, forces

  **gamma_±''(T_±)/gamma_±(T_±)=65/9∓245sqrt(2)/48**,

equivalently

  **(log gamma_±)''(T_±)=191/48∓45sqrt(2)/16**.

Derivation: write R_X=(P_X∘x)''/(P_X∘x)' and S_X=(P_X∘x)'''/(P_X∘x)' with x=z or w. Chain rule gives R_A=(4/3)z'+z''/z', S_A=(116/9)z'^2+4z''+z'''/z', R_B=(-99/16)w'+w''/w', S_B=(29403/256)w'^2-297w''/16+w'''/w'. Then ell=(R_A-R_B)/2 and gamma''/gamma=[S_A-S_B-3ell R_B]/3. Direct substitution of both exact rational maps at t=±6sqrt2 gives the displayed values. The (formal) scalar gauge with these prescribed first three Taylor coefficients always matches through cubic order, since P_B∘w has a simple zero.

The two signed branches are exchanged by Fp² Frobenius and retain **new invariant traces/norms**:

  Tr(gamma''/gamma)=130/9; Norm(gamma''/gamma)=575/10368;
  Tr((log gamma)'')=191/24; Norm((log gamma)'')=31/2304.

The invariants are exactly scoped to the local weighted finite-field observation and do not assert a global period equality, p-adic transport, or native-X6 observer equivalence. The branch signs and individual Cauchy carry ports remain necessary data.

## Exact verification and next unfinished work

The accompanying Python program performs two independent checks: (i) reconstruct all original weighted 216 and 2304 3F2 coefficients modulo p and compute first/second/third derivatives directly for every p≡13(mod24), p<1200 (26 primes), checking the ratios above; (ii) evaluate rational Fricke derivatives up to third order at both t=±6sqrt2 in the quadratic field Fp², and check the claimed ell and gamma''/gamma. Execution PASS for all 26 primes and both signs. Witnesses (p; P_A',P_A'',P_A'''; P_B',P_B'',P_B'''):

  13: (6,8,8; 11,1,5);
  37: (23,6,21; 19,5,2);
  61: (29,59,1; 54,9,35);
  109: (99,23,77; 85,94,40);
  181: (179,118,115; 26,88,86);
  373: (211,157,150; 320,258,293).

**Smallest remaining unit:** construct a genuine p²–p³ finite-cutoff transfer under the nonlinear two-leg Fricke map, explicitly retaining both branches, Cauchy source labels, first through third jets, prime class p≡19 mod24, and the native original-class p373 experimental gap. A locally adjustable formal scalar jet is not the global transfer certificate; test candidate restrictions (period gauge, p-adic Frobenius or finite WZ) against these exact invariants. Frozen mother Δ_p−R_p=0 mod p for p≡13,19 mod24 remains OPEN.

**Control boundary:** Authenticated status in this run: Site CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false; em_status failed with BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Old requests em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 and session/claim/run/staging remain UNKNOWN_PRESERVE. Research activity REGISTER_PENDING; no native checkpoint, Result, freeze, review, or admission. Control support issue awdawmip/enterprise-math#1558.
