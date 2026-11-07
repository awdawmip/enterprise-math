# D25: low-degree square folding and weighted CM jet transport (2026-11-07)

Status: AUTHOR-SIDE PROVED ALGEBRA / 52 EXACT TARGET PRIMES CHECKED / UNREVIEWED / NOT_ADMITTED.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Same-lane author-side continuation; native Researcher/claim/run not verified. Prior inputs: frozen 216/2304 definitions, Clausen, previous Frobenius carry factorization, and earlier CM/Hasse theorem. Distinct from independent onhour X0(6) Fricke branch/period calculation at 6ffcf3e8e7a2876fdd4e35ddd7b1ca4d35754e07.

Let theta=z d/dz, A_<p(z)=sum_{n=0}^{p-1} ((1/2)_n(1/3)_n(2/3)_n/(n!)^3) z^n, B_<p(z)=sum_{n=0}^{p-1} ((1/4)_n(1/2)_n(3/4)_n/(n!)^3) z^n. The corresponding weighted source observers are P_A=(1+6theta)A_<p and P_B=(1+8theta)B_<p. All equalities below are polynomials over F_p, with original source labels and the high-degree Frobenius carry retained as distinct provenance (no p-adic source-collapse is asserted).

## Theorem 1: exact degree-<p square folding

For p=6m+1 prime define F_m(z)=sum_{j=0}^m binom(m,j)binom(2m,j) z^j. For p=8k+5 prime define H_k(z)=sum_{j=0}^k binom(3k+1,j)binom(k,j) z^j. Then
  A_<p(z) = F_m(z)^2,  p=6m+1;
  B_<p(z) = (1-z) H_k(z)^2,  p=8k+5.
Consequently
  P_A(z)=F_m(z)^2+12z F_m(z)F_m'(z);
  P_B(z)=(1-9z)H_k(z)^2+16z(1-z)H_k(z)H_k'(z).

Proof: rational Clausen identities identify each first p 3F2 coefficients as the degree-<p projection of its 2F1 Cauchy square. For A, the mod-p Gauss series stops at degree m with coefficients binom(m,j)binom(2m,j), and its square has degree 2m<p. For B, the previous exact characteristic-p factorization G=(1-z)^((p+1)/2)H_k yields G^2=(1-z^p)(1-z)H_k^2. The projected low-degree component is (1-z)H_k^2, degree 2k+1=(p-1)/4<p, while the signed discarded source is -z^p(1-z)H_k^2. Differentiate the exact projected polynomial identities to obtain the stated weighted formulas. QED.

## Theorem 2: universal 2304 weighted simple zero and second jet

For every p=13 mod24, the previously established CM/Hasse result supplies H_k(1/9)=0 and H_k'(1/9)!=0. At z_B=1/9,
  P_B(z_B)=0;
  P_B'(z_B)=(128/81) H_k'(z_B)^2 != 0;
  P_B''(z_B)=(-88/9) H_k'(z_B)^2;
  P_B''(z_B)/P_B'(z_B)=-99/16.
Proof: H_k(z) solves z(1-z)H''+(1+4kz)H'-k(3k+1)H=0. With 8k+5=p and H_k(1/9)=0, evaluation yields 16H_k''(1/9)+117H_k'(1/9)=0. Differentiate the weighted expression from Theorem 1 once and twice at this simple root: P_B'=16z_B(1-z_B)H'^2=128/81 H'^2; P_B''=32(1-2z_B)H'^2+48z_B(1-z_B)H'H''=-88/9 H'^2. Quotient follows. The unweighted projected square has a double zero at the CM point; the actual weighted observer has a simple zero, showing a first-jet BRC detector. QED.

## Theorem 3: conditional 216 jets and an exact affine-gauge condition

For any p=6m+1 satisfying F_m(1/2)=0 (the pre-existing CM0 first-digit condition for the target p=13,19 mod24), F_m is squarefree. It obeys z(1-z)F''+[1+(3m-1)z]F'-2m^2F=0; at z=0 it is 1, at z=1 it is binom(3m,m)!=0, and a multiple root elsewhere would force every derivative to vanish by successive ODE differentiation (degree m<p). Thus F'(1/2)!=0. Its ODE at z_A=1/2 yields F''(z_A)=-F'(z_A). Hence
  P_A(z_A)=0;
  P_A'(z_A)=6F_m'(z_A)^2 != 0;
  P_A''(z_A)=8F_m'(z_A)^2;
  P_A''(z_A)/P_A'(z_A)=4/3.
This is conditional on the earlier first-digit CM0 root, which is not reproved here. Proof of derivatives: P_A=F^2+12zFF'; twice differentiate and substitute F=0, F''=-F'. QED.

For p=13 mod24, the simple **affine alignment** w=cz, c=2/9, maps z_A=1/2 to z_B=1/9. Its B normalized second derivative is c P_B''/P_B'=-11/8, whereas A has 4/3. Their difference is 65/24 mod p, nonzero for every p=13 mod24 except p=13. Therefore a *constant* nonzero scalar gauge cannot identify the two weighted polynomials through second local Taylor order under this particular affine map for p>13. A variable nonvanishing gamma(z) making P_A(z)=gamma(z)P_B(cz)+O((z-z_A)^3) necessarily satisfies
  gamma(z_A)=P_A'(z_A)/(c P_B'(z_B));
  gamma'(z_A)/gamma(z_A)=65/48.
These are scoped local finite-field conditions; they do not exclude the actual nonlinear branch-sensitive Fricke maps, non-scalar intertwiners, WZ identities or the target mod-p^3 supercongruence.

## Executed exact arithmetic, scope and next unit

The attached script independently computes ALL first p coefficients of both original 3F2 expressions modulo p from exact integer recurrences, compares entire coefficients with the square/fold polynomial, and directly differentiates the ORIGINAL weighted coefficient lists (not just the derived formulas). It ran successfully on all 52 primes p<1200 in the target classes: 26 p=13 mod24, 26 p=19 mod24. On the 26 p=13-class primes it also checks H root, H ODE, two B jet formulas, -99/16 ratio and exceptional affine mismatch. For A it verifies polynomial square, the observed CM0 root, simplicity and both jet formulas in all 52 cases. Selected direct witnesses (p; F',H'; P_A',P_A''; P_B',P_B''), modulo p:
  13;1,4;6,8;11,1
  37;11,11;23,6;19,5
  61;25,27;29,59;54,9
  109;92,14;99,23;85,94
  181;28,124;179,118;26,88
  373;215,369;211,157;320,258.
No floats, no native p373 experiment, no universal proof inferred from the finite scan.

Next: consume the independent exact Fricke X0(6) z(t),w(t), common t=+/-6sqrt(2) and Jacobian. Construct the genuine nonlinear, branch-aware mod-p weighted first-/second-jet transport preserving p-adic carry source labels. Compute exact necessary local gauge and derivative or a scoped counterexample, then investigate the still-open p^2/p^3 cutoff compensation. Frozen mother objective Delta_p-R_p=0 mod p for p=13,19 mod24 remains OPEN.

Control provenance as checked on 2026-11-07: Site CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false; native em_status fault BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false. Original requests em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 remain UNKNOWN_PRESERVE; session/claim/run/staging unverified; activity REGISTER_PENDING; no native checkpoint, Result, review or admission. Existing support awdawmip/enterprise-math#1558.
