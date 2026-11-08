# PREFIX-612-R2 — Exact unknown common probe-scale gauge and one-sensor calibration

Date: 2026-11-09 Asia/Shanghai.
Status: AUTHOR-SIDE EXACT PROOF + EXECUTED ORIGINAL-48-PHASE RATIONAL CHECKS; independent Driver review pending.
Scientific input remains frozen at awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Direct dependencies: PREFIX-602/604 (native-derived 16D tail and 12+4 split), PREFIX-611 (unknown two-step gates, known uniform controlled difference; PR #1840, commit 3eb8d102717bb5675aa729790630bd3545e3cc41).

## Problem, types and observer

Use the original X6 STAR 48 phases, 96 ports and 576 tagged actions, with axis weights (1,1,1,1,0,0) and the source-defined exact nonnegative phase-sum transfer Q(g). The source carrier keeps labeled branch provenance; only phase-sum observer coordinates are asserted here. Let v be an arbitrary unknown nonnegative original 48-phase source, and let the second run start at v + lambda*u, where u=ones(48) is known but its common scalar magnitude lambda>0 is *unknown*. The two runs share exactly the same unknown nonnegative gate word

    b, a, q_1, ..., q_n.

At each transition read the difference of original phase-sum coordinate 3 (zero-based); denote the first two readings by Y_-1,Y_0 and later readings by Y_t. A single *additional* phase-4 contrast at the first transition is denoted by Z. All inputs and gate words may be real and nonnegative; exact rational arithmetic is used by the checker.

## Theorem 612.1: one-dimensional scale–gate gauge for an uncalibrated phase-3 trace

For all lambda>0, b,a,q_t>=0, the original 48-phase operator and the 12+4 split give

    Y_-1 = lambda*(b+7);
    Y_0 = 3*lambda*(a+7);
    c_0 = lambda * ( 3(a+3)/2, (b+7)/2, 3/2, 3/4 )^T;
    c_t = B(q_t)c_(t-1),  B(q)=[[0,0,0,4(q+3)],[1,0,0,0],[0,1,0,0],[0,0,1,0]];
    Y_t = 12*lambda*2^t + 8*(q_t+3)*c_(t-1,3), t>=1.

All c_(t-1,3) are positive. The observed n+2 phase-3 contrast scalars determine the complete (n+3)-parameter tuple (lambda,b,a,q_1,...,q_n) only up to a genuine one-dimensional local gauge around EVERY strictly positive tuple and every finite n. In particular they never uniquely determine that tuple on the unrestricted strictly positive domain.

**Constructive proof.** Fix an observed trace Y from one strictly positive parameter tuple. For any candidate positive scale L sufficiently close to the true lambda, define

    b(L) = Y_-1/L - 7;
    a(L) = Y_0/(3*L) - 7;
    c_0(L) = L*(3(a(L)+3)/2,(b(L)+7)/2,3/2,3/4)^T.
    q_t(L) = (Y_t-12*L*2^t)/(8*c_(t-1,3)(L)) - 3;
    c_t(L) = B(q_t(L))*c_(t-1)(L).

At L=lambda the definitions reproduce the original tuple. Every expression is rational and continuous in L wherever its denominators are nonzero. All original denominators and parameters are strictly positive, so for any fixed finite n there is an open interval of L on which each resulting gate remains positive. The recurrence reproduces EVERY recorded Y exactly. This provides a continuum of distinct parameter tuples with precisely identical single-sensor traces, and is a direct, all-finite-horizon nonidentifiability proof. At lambda fixed the mapping from gates to phase-3 readings is triangular with diagonal lambda,3lambda,8c_(0,3),...,8c_(n-1,3), all positive. Hence its Jacobian has full row rank n+2 and the gauge is locally exactly one dimensional by the implicit-function theorem.

**Exact positive rational witness (n=2).** Two worlds

    W:  lambda=1,       (b,a,q1,q2)=(1,2,1,2);
    W': lambda=101/100, (b,a,q1,q2)=(93/101,193/101,93/101,193/101)

give exactly the same four original phase-3 contrasts

    (Y_-1,Y_0,Y_1,Y_2)=(8,27,48,108).

These can use the same strictly positive unknown base v=u. They differ in lambda and in every gate. The equalities follow from the native Q and the displayed formulas; the executable checker additionally evaluates the full 48-phase transitions.

## Theorem 612.2: one extra ORIGINAL phase-4 contrast removes the gauge

The gated row of the frozen source Q(g) at zero-based original phase index 4 is independent of g: it sends the uniform input u to exactly 3. Therefore at the first transition,

    Z = [Q(b)(v+lambda*u)-Q(b)v][4] = 3*lambda.

Consequently the single added contrast Z uniquely calibrates lambda=Z/3, and then

    b=Y_-1/lambda-7, a=Y_0/(3*lambda)-7,

followed by the exact PREFIX-611 recurrence in Theorem 612.1 reconstructs every q_t. Every denominator is positive for lambda>0 and gates>=0; the reconstruction also covers zero and unit gates. This is a global constructive uniqueness statement on the specified nonnegative domain, not merely generic identifiability.

For W and W' above, their phase-4 first-transition contrasts are respectively 3 and 303/100, which separates their indistinguishable phase-3 traces. Equivalently, one may calibrate using the phase-3 contrast *before* any transition, equal to lambda; the same-time phase-4 sensor avoids a pre-transition observation.

The n+3 scalars (Z,Y_-1,Y_0,Y_1,...,Y_n) exactly recover n+3 independent real unknowns. The n+2 phase-3 scalars alone provably do not; moreover any continuously differentiable lossless encoding with differentiable recovery of all unknowns needs at least n+3 real statistics by Jacobian rank. For two synchronized experiments the raw readout is 2(n+3) phase scalars: twice each of the n+2 phase-3 post-gate readings, plus twice phase 4 at the first gate.

## Exact verification and reproducibility

Standalone script: PREFIX612_R2_unknown_probe_scale_checker.py.
Machine output: PREFIX612_R2_unknown_probe_scale_results.json.
Required Python package: SymPy. Run from the containing directory with:

    python PREFIX612_R2_unknown_probe_scale_checker.py

The script reconstructs the frozen X6 STAR phase ordering, successor mapping and original 48x48 Q(g), rather than testing only the reduced 4D recurrence. It symbolically checks the two native first-gate sensor identities, the second-gate phase-3 identity, and scale calibration; it then exercises 3 nonnegative original sources, 3 positive rational scales and an 8-gate word (two unknown transient gates plus six subsequent gates, including q=0), recovering 72 gate values. It additionally validates 3,456 original phase-coordinate difference entries and the exact rational witness with a strictly positive source. All executable assertions passed in the author-side environment on 2026-11-09.

For complete mathematical scope, the all-finite-horizon gauge and global calibration result are derived from the proven PREFIX-611 formulas and the row of Q(g), not inferred from the finite tests. The check is not independent Driver review or Foundation promotion.

## Method reuse and next executable unit

BRC interface resolution: COMPOSE_APPLIED to frozen native Q, 16D common-tail, 12+4 split and PREFIX-611 decoder. Information retained: original phase identities 3/4, unknown controlled-input scale, complete future gate word. Information projected out: original 96-port individual tagged histories; the claim is limited to linear phase-sum observation under the stated paired experiment.

Next question: replace the uniform controlled direction lambda*u by an unknown positive direction d, and classify when one or two early phase-sensor calibration observations allow recovery of the gate program. Also examine bounded gate mismatch between the paired runs via a residual model; quantify the exact degeneracies before introducing numerical approximation. For performance claims, count native 96-port preparation, two-run synchronization, rational bit growth, and full readout costs.

Owner/registration: author-side independent research, no formal TASK CLAIM or Native Result asserted. A native session start and current-owner query were queued during this work; use only their eventual authenticated receipts for Researcher-ID/Activity-ID and Owner.
