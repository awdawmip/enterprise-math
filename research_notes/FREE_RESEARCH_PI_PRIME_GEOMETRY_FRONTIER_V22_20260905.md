# Pi-to-Prime Frontier V22 — quantitative real-variable closure

Date: 2026-09-05 (Asia/Taipei)
Researcher-ID: EM-FREE-PI-PRIME-20260905
Status: RESEARCH_NOTE_PROOF / V21_CONVERGENCE_GATE_CLOSED_AT_REAL_VARIABLE_STRENGTH / AUTONOMOUS_S3_RECURRENCE_NOT_PROVED / NOT_WORKING_TRUTH / NOT_FOUNDATION
Source recovery: 23a7f1f71e27c34c6147c323596b9aae22926ba3

## Exact change

V21 allowed either an autonomous eight-chamber recurrence or a native slow-oscillation route. V22 takes the latter at the explicitly stated elementary arithmetic + real-variable completion layer. It does not assume PNT or import any previously proved PNT remainder.

The complete proof is in:

`research_notes/FREE_RESEARCH_QUANTITATIVE_SLOW_OSCILLATION_CLOSURE_V22_20260905.md`

The already available Chebyshev, first-mass and Selberg identities yield, for v(T)=psi(exp(T))/exp(T)-1:

1. |v|<=B;
2. every signed interval integral of v is bounded by K0;
3. |v(t+h)-v(t)|<=Lh+J/t for 0<=h<=1;
4. |v(T)|<=2/T^2 integral_0^T (T-t)|v(t)|dt+C0/T.

A block of length 8K/m lying under the envelope |v|<=m has integral deficit at least m^2/(32L), provided J/a<=m/8. Hence the triangular mean loses a fixed multiple of m^3 in a macroscopic middle band.

The comparison function b(T)=M/sqrt(log(e+T)) has triangular-average excess at most 4 b(T)^3/M^2. Choosing M large and handling the finite initial range excludes a first contact of |v| with b, including upward arithmetic jumps.

Thus:

`r(x)=O(1/sqrt(log(e+log x)))`.

Retaining the exact V21 stopped endpoint, suffix convention r(0)=0, and pair S3 normalization, endpoint mass estimates then give:

`D4(r;N)=O(1/log(e+log N))`.

The product-bounded historical average at any integer depth h=O(log log N) has the same rate. This closes the specific convergence claim and the growing-history average requested by V21 without relying on hidden constants in its reverse frame.

## Arithmetic consequences

`psi(N)=log det W_N=N+O(N/sqrt(log log N))`.

`pi_P(x)=Li(x)+O(x/(log x sqrt(log log x)))`.

These estimates are weak compared with classical quantitative PNT; no external novelty is claimed. P000 and the distinction between spatial coordinates and arithmetic valuation fibers are unchanged.

## What is NOT promoted

The proof does not establish that the actual prime error is iterated by an abstract 1/9 mixer. No autonomous eight-chamber S3 recurrence, pure primitive-rotation derivation, RH-scale estimate, Lean verification, CI-green, Working Truth, or Foundation promotion is asserted.

The mathematical convergence target is closed at the specified real-variable strength. Independent proof audit and/or formalization remains a validation task, not an additional assumed inequality in the written proof.

## Verification

`scripts/check_v22_slow_oscillation.py` was executed in the current runtime. The standard-library Fraction suite passed 492 assertions for finite algebra, endpoint supports and block constants. Optional NumPy/SciPy checks passed for the barrier quadrature and N=100,300,1000,2000 prime-power data. Numerical data are not used to infer convergence; D4 is not numerically monotone at these small scales.

The full real-variable proof itself has not been checked by a proof assistant or independent referee.
