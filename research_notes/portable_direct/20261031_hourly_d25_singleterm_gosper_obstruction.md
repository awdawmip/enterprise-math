# D25/LIFT: obstruction to one-summand rational Gosper telescoping

Date: 2026-10-31 (Asia/Hong_Kong). Author-side portable mathematical unit D25-HOURLY-20261031-0220-RATIONAL-GOSPER-OBSTRUCTION; logical Research conversation chatgpt-research-hourly-enterprise-math-20260923 (not the maintenance conversation).
Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Current LIFT task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3; P000 ACTIVE_LOCKED.

## Mathematical statement and scope

For the original weighted 216 hypergeometric term let

\[
a_k=\frac{(1/2)_k(1/3)_k(2/3)_k}{2^k(k!)^3}
=\frac{\binom{2k}{k}^{2}\binom{3k}{k}}{216^k}.
\]

THEOREM: There is NO rational R(k) in C(k) satisfying the formal rational recurrence

\[
(6k+1)a_k=R(k+1)a_{k+1}-R(k)a_k.
\]

It rules out the elementary single-term rational Gosper antidifference for this specific weighted summand in characteristic zero. It DOES NOT rule out multi-term or two-dimensional WZ methods, parameter shifts, p-dependent finite identities, auxiliary non-hypergeometric terms, or a CM/Gauss-Manin special-value relation. It is NOT a counterexample to LIFT.

## Complete elementary proof

The exact ratio is

\[
\frac{a_{k+1}}{a_k}=\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3}.
\]

Write D(k)=(2k-1)(3k-2)(3k-1), so D(k+1) is exactly the numerator above. If a rational antidifference existed, put F(k)=D(k)R(k)/k^3, a rational function. Multiplication and cancellation in C(k) gives

\[
D(k)F(k+1)-36k^3F(k)=36(6k+1)D(k). \tag{1}
\]

Assume F has at least one finite pole. Choose a pole z_max with maximal real part. F(k+1) is regular at k=z_max, because that would require a pole of F at z_max+1, contradicting maximality. Since the right side of (1) is a polynomial, k^3 F(k) must also be regular there; hence z_max=0 (a pole at 0 of order at most 3). Every pole then has real part <=0. Now choose a pole z_min of minimal real part. At k=z_min-1, F(k) is regular, while F(k+1) has a pole. Equation (1) requires D(z_min-1)=0, so z_min belongs to {3/2,4/3,5/3}. All have positive real part, contradiction. Therefore F has no finite poles, hence F is a polynomial.

D(k)=18k^3+O(k^2). If F is a nonzero polynomial of degree d with leading coefficient c, the left of (1) has leading term (18-36)c k^(d+3)=-18c k^(d+3); the right side has leading term 36*6*18 k^4 =3888 k^4. Therefore d=1 and its slope c=-216.

But D(0)=-2, and inserting k=0 into (1) gives F(1)=36. D(1)=2, and inserting k=1 gives F(2)=900. Thus F(2)-F(1)=864, contradicting the required slope -216 for a linear polynomial. There is no rational solution. QED.

## Executed verification

An independently executed SymPy symbolic checker verified the ratio, D(k+1), D(0), D(1), polynomial leading coefficient and the contradictory evaluations. Independently, the standard hypergeometric Gosper decision procedure returned None; that result is auxiliary evidence, not substituted for the proof. Actual output:

    SLOPE_REQUIRED -216; F(1)=36; F(2)=900; FINITE_DIFFERENCE=864
    PASS_GOSPER_SINGLE_TERM_RATIONAL_OBSTRUCTION_CHECK

Exact verifier: research_notes/portable_direct/d25_gosper_singleterm_obstruction_20261031.py. A finite CAS check does not constitute review, formal verification, or canonical admission.

## BRC meaning and next exact problem

Carrier: rational hypergeometric sequences in C(k). Observer: whether the original single summand has a rational Gosper certificate. Future operation: shift k to k+1 followed by antidifference. The obstruction identifies the precise unsound shortcut "assume direct one-term telescoping" rather than discarding the original residual.

The original fixed-X LIFT target is still OPEN, in both p modulo 24 classes {13,19}:

\[
\sum_{k=0}^{p-1}(6k+1)a_k\stackrel{?}{\equiv}p\pmod{p^3}.
\]

Next: seek a genuine two-dimensional/parameterized WZ, CM, or Gauss-Manin evaluation of the FULL joint signed carry + jet - high-degree projection from GH-178/179, optionally using the new exact harmonic/factorial block formulas. Do not assume any of these three ports vanishes separately. Native D25 H0/B0 divided-power, [X]U mod p^2, semilinear Frobenius, eta and native p=373 experiment remain separate obligations.

## Control honesty

Gateway 0.6.11 observed research_authority_granted=false; executor_binding_configured=false; active job quota 5/5; Source CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED. recovery_status was advertised but not callable in this subject's connected client. No new native CLAIM/OPEN/Source checkpoint/Result/review; no old protected session/staging or maintenance role touched. Existing control support enterprise-math #1558; native experiment support #1559. These author-side mathematical notes do not grant Source ownership.
