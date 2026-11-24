# PREFIX-1055 — Signed square-root certificate on the lower spectral branch

Date: 2026-11-24. Parent PREFIX-1054. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_CHECKED / NOT_REVIEWED.

## Scope
Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json, Stage46 signed W=J12−6I12, incoming −e1, bidirectional exclusion of Link {0,e1}, exactly one outgoing negative step. Preserve native Cell–terminal-port–grade, sign, branch identity, multiplicity and provenance. This is an internal analytic certificate for the inherited auxiliary scalar ODE; no new native evolution, phase/pi evaluation or classical comparison run. NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION. Mother B_fix,odd(32) in {19,20} remains open.

Immutable scientific inputs actually read: PREFIX-1052 de0250c78a0952c5b282623dacedce81c47bad90:research_notes/portable_direct/2026-11-24_r6_prefix1052_exact_critical_connection_and_middle_analytic_branch.md (six ODE polynomials and cusp connection), PREFIX-1054 8c65067dfaa0cde6a032472d9cb7a9162ac81478:research_notes/portable_direct/2026-11-24_r6_prefix1054_complete_middle_spectral_positivity.md (strict positivity on [4,36), lower-branch initial intervals and inverse-convolution lemma). PREFIX-1054 checker bda07a82cf7828d43f041f14b00ef3d2a9b1cbf1 also read. The proof depends on those connection and scalar ODE premises.

## Result
For c>0 the inherited upper-edge coefficient,
5g(y)/c > 15390000 for every y in [39/16,4].
Thus g(y)>3078000c on this band and g>0 throughout [39/16,36). The remaining unconnected interval has length 39/16=2.4375 (previously 4). This is a continuous interval certificate, not sign sampling.

## Proof
Set x=4−y, s=sqrt(x) in [0,5/4]. This is an auxiliary scalar reparameterization, not a new native coordinate. With B_j(x)=R4_j(−x), C(x)=C4(−x), the lower density is
u(y)=rho(y)/c=sum_(j=0..3) Q4_j B_j(x)−135 s^3 C(x).
The primitive v=U/c satisfies v'= (y−6)u, initial value v(4). Retain the cusp separately even though it contributes a polynomial in s after truncation. The exact initial box is PREFIX-1054's hundredth box:
Q0=[235698,235702]/100, Q1=[−44062,−44059]/100, Q2=[6845,6848]/100, Q3=[−1244,−1242]/100, v(4)=[−5241077,−5241068]/100. C(0)=1 and B_j has initial coefficient (−1)^j at index j and zero at the other indices 0..3.

Let A_j(x)=(−1)^j a_j(4−x), where a_j are the six exact polynomials of PREFIX-1052 (also included in the standalone checker). For alpha=0 or 3/2, write x^alpha sum b_n x^n and d_n=r^n b_n, r=2. Direct coefficient comparison at power n+alpha−4 gives
W_k(n)=r^k sum_(j=0..5) [x^(k−4+j)]A_j(x) (n+alpha−k)_j,
sum_(k=0..7) W_k(n)d_(n−k)=0.
Negative indices vanish. The analytic recurrence starts at n=4, the fractional one at n=1. The leading coefficient W_0 is nonzero in these ranges by the critical indicial formula of PREFIX-1052. This is the inherited local branch, with convergent Frobenius series for x<4.

Define l_k=−LC(W_k)/LC(W_0). For both exponents the checker verifies the polynomial identity
1−sum l_k z^k=(1−r z/4)^5(1+r z/12)(1+r z/32).
Hence the causal inverse convolution has absolute sum at most K=1/((1−r/4)^5(1−r/12)(1−r/32)). To bound coefficient perturbation for all n>=N=2000, shift n=N+w, sign-normalize W_0 and check all six coefficients strictly positive. Each ratio of the absolute coefficients of (−W_k−l_k W_0) to those of W_0 bounds the corresponding residual polynomial ratio on w>=0. Sum maxima to obtain e. Exact comparisons verify Ke<1 for both exponents. Put L=sum |l_k|+e. On each finite tail, causal inversion gives M_tail<=K(L B+e M_tail), with B the preceding seven coefficients' maximum modulus. Therefore sup_(n>=N)|d_n|<=K L B/(1−Ke), uniformly over every prefix.

Compute the first 2000 scaled coefficients by integer floor with scale M=10^4000, all initial scaled coefficients exact. Propagate absolute rounding errors in units 1/M by E_n=1+ceil(sum_(k>=1)|W_k(n)| E_(n−k)/|W_0(n)|). Every finite coefficient has error <=delta=max(E)/M; the checker asserts delta<10^−30. For the infinite tail use B=max |computed terminal state|/M+delta. Take T=max(KLB/(1−Ke),max_(101<=n<N)|computed d_n|/M+delta). Then every omitted scaled coefficient has absolute value <=T. Round the first 101 scaled coefficients downward to grid 10^−30; their errors are <=eta=delta+10^−30. This keeps finite representation error and infinite truncation error separate.

For X=25/16, q=X/r=25/32, uniform bounds on the analytic factor's approximation and its x derivative are
e0=eta/(1−q)+T q^101/(1−q),
e1=(eta/(1−q)^2+T q^100(101/(1−q)+q/(1−q)^2))/r.
These follow from exact geometric sums and their differentiated sums. For the cusp multiply e0 by (5/4)^3 and bound the y derivative error by (5/4)^3 e1+(3/2)(5/4)e0_original. The actual checker uses the larger scaled e0 in that second term, still a valid bound. No division singularity occurs at s=0: the cusp starts with s^3, the analytic factors contain even powers only.

For each basis polynomial p(s), its y derivative is exactly −p'(s)/(2s), a polynomial including at zero. Its primitive increment in s is the integral from 0 to s of (4s+2s^3)p(s). In the normalized contrast
5g/c=4 H' u+4 H u'−2P u+12(11+y)v,
H=y²(36−y)², P=y(y−36)(17y−91),
these become rational polynomials in s. The separate primitive constant contributes 12(11+y)v(4). The primitive approximation error is <=6 X e0_basis. Use |H|<=36^4, |H'|<=4*36^3, |P|<=36²(17*36+91), |11+y|<=47 on the band to bound each contrast-basis error by
4(4*36^3 e0_basis+36^4 e1_basis)+2*36²(17*36+91)e0_basis+12*47*6X e0_basis.
These deliberately coarse universal polynomial bounds are sufficient.

Finally combine all six contrast polynomials at the midpoint of the coefficient box, including the fixed −135 cusp. For each of the 256 closed intervals [5i/1024,5(i+1)/1024], i=0..255, apply directed interval Horner arithmetic on grid 10^−30, taking min/max of all four endpoint products and rounding outwards at every stage. The inputs are represented exactly on that grid. Enclose the midpoint polynomial below and each uncertain basis polynomial in absolute magnitude; subtract sum radius_j*sup|basis_j| and sum (|mid_j|+radius_j)*analytic_error_j. This is a rigorous lower enclosure on each interval; their union is the entire s domain. The checker asserts their minimum >15390000 using exact integer/Fraction arithmetic. This proves the claimed strict lower band and joins the prior [4,36) certificate.

## Execution
Standalone checker: 33486aa74da9a705d72c510d1b252850a2edd2fc:research_notes/portable_direct/PREFIX1055_R6_LOWER_SQUARE_ROOT_CHECK.py, Git blob 3ff083715e5d121956637d4749c49ff97966f7bb, SHA256 fe7cf140df624af1a4659292d801a5589017166c21bc297043f9b00e3228ebc1. Actual local Python/SymPy/Fraction run verified the same Git blob as the exact remote readback. Run python PREFIX1055_R6_LOWER_SQUARE_ROOT_CHECK.py. Output (float diagnostics only):
alpha 0 Ke 0.6481831042120071 T 8.364171756874934e-35
alpha 0 Ke 0.6481831042120071 T 4.648073303698236e-33
alpha 0 Ke 0.6481831042120071 T 5.103019199033253e-31
alpha 0 Ke 0.6481831042120071 T 3.9114347384519295e-30
alpha 3/2 Ke 0.6476978056795615 T 1.0590534057415653e-32
lower 5g/c 15391021.353123883 tail err 2.6533594724220263e-19
PREFIX1055_LOWER_BAND_CERTIFICATE_PASSED
All exact assertions passed. No independent review or native signed BRC execution is claimed. Float underflow in displayed delta is not a zero-error claim; the exact rational delta was used throughout.

## Continuation
Remaining lower branch (0,39/16). At y=39/16 the square root coordinate is exactly 5/4, so the full five density jets and primitive can be transported rationally without losing the cusp. Improve the connection box if cancellation near 0 requires it, or derive the lower-edge expansion with explicit remainder and bridge the middle gap using ordinary centers. The proof certificate is local to the scalar observer; retain all native joint components and resolve the observer correspondence separately. No formal task claim or completion.

Control: original registration r6-20261123-2358-session-start-own-v1 SUCCEEDED, historical researcher EM-DIRECT-780BBE, RA-0ABD84561C86E53067DB0322. Current logical session authority not established. Owner query r6-20261124-1350-leased-observe-v1 last read RUNNING/SOURCE_MATERIALIZATION, error=null; no new CLAIM. Activity association pending. Preserve independent note without mutating shared control state.
