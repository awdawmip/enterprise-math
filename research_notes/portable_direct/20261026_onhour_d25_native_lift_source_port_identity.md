# D25/LIFT — exact source-port alignment of reflected Clausen cutoff and frozen second-digit observer

Date: 2026-10-26. Research lane: chatgpt-research-onhour-enterprise-math-20260923 (TASK_RESEARCH); explicitly NOT the CONTROL_PLANE_MAINTENANCE lane. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged.

**Status: NEW AUTHOR COMPOSITION / EXACT ALGEBRAIC PROOF OF SOURCE-PORT ALIGNMENT / SIX-CASE EXACT CROSSCHECK / UNREVIEWED / NOT_ADMITTED / NOT A SOURCE-NATIVE CHECKPOINT / NATIVE CM BENCHMARK NOT_RUN.** All frozen predecessor Results, accepted UR/CM0, prior Source checkpoint owners and their contributor histories are consumed without recrediting.

## 1. The specific actual unfinished question

Prior author-side three-band Clausen results expressed the third digit of the original weighted truncated sum W_p, but warned that the original frozen LIFT observer Delta_p-R_p remained separate. This unit checks whether their reflected signed-cutoff T_p is **actually identical** to the *frozen original* scalar R_p, without altering either definition; only then may W_p's third digit be carried back to the original accepted Task interface.

For all primes p = 6m+1 >= 13 with p mod 24 in {13,19}, work in Z_(p). Define

- B_n = ((1/6)_n(1/3)_n)/(2^n (n!)^2), 0 <= n < p;
- M = sum_{n<p} B_n, N = sum_{n<p} n B_n, h = M + 12N, G = M/p;
- W = sum_{n<p} (6n+1) ((1/2)_n(1/3)_n(2/3)_n)/(2^n (n!)^3);
- Q = sum_{0<=i,j<p; i+j>=p} (6(i+j)+1) B_i B_j.

The accepted CM0/UR first-digit source provides p | M and Gh = 1 mod p. Exact Clausen coefficient convolution provides W = M h - Q (exact rational equality), and the frozen parent cutoff gives p² | Q.

**Frozen original reflected scalar** (not replaced by a newly fitted definition): for 1 <= a <= m,

C_a = 2^(a-1) ((a-1)!)²/[18 (5/6)_a (2/3)_a],

R_p = 2 sum_{i=1}^m B_i sum_{a=1}^i (1+6(i-a)) C_a (mod p).

Source: research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN_20260827.md, whose parent input also states Q = p²R_p mod p³; independently see research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE_RETURN_20260827.md.

## 2. New explicit alignment certificate across independently named source carriers

Directly from the factorial/rising-factorial definition,

C_1 = 1/10,
C_(a+1)/C_a = 36 a²/[(6a+5)(3a+2)].

All denominators are p-units for 1 <= a <= m; in particular the transition is only used up to a=m-1. The separately persisted *full-band* reflection coefficients from author note 20261025_onhour_d25_clausen_three_band_local_jet_joint.md satisfy the identical initial condition and recurrence:

v_1 = 1/10,   v_(a+1) = v_a 36a²/[(6a+5)(3a+2)] (mod p),

v_a = (B_(p-a)/p²) (mod p) on the high-valuation ranks, with V_i=sum_{a<=i}v_a and J_i=sum_{a<=i} a v_a.

Uniqueness of recurrence in F_p gives **C_a = v_a (mod p)** for 1<=a<=m. Reorder the frozen original double sum (finite, no convergence issues):

R_p = 2 sum_{i=1}^m (B_i mod p)[(6i+1)V_i-6J_i] (mod p).

The earlier signed-boundary formula defined T_p by exactly this expression with b_i=2^-i binom(m,i)binom(2m,i). The accepted low-rank coefficient comparison B_i=b_i mod p implies, **for all declared target primes**,

                 R_p = T_p = Q/p² (mod p).

This is a source-preserving equality of previously different observer ports, not an assumption based on numerical agreement. It reconnects the actual frozen R_p, original signed cutoff Q, and the independently computed full-band reflection recurrence. In particular dropping Q (or replacing R by zero) is NOT generally safe.

## 3. Exact original LIFT and nonnative third-digit certificate

Since W = pGh-Q exactly and p²|Q, the following is exact as a p-local rational identity before reducing modulo p:

                 (W-p)/p² = (Gh-1)/p - Q/p².

Consequently, under already accepted first-digit UR,

           Delta_p-R_p = (W-p)/p² (mod p),

where Delta_p=(Gh-1)/p mod p is the frozen original observer. Therefore **LIFT on both classes is equivalent to W≡p (mod p³)**, retaining the *original* Q/R provenance. This equivalence is not a proof of LIFT: the right-hand side's uniform vanishing remains OPEN.

A further composition consumes (does NOT newly reprove) the source-accepted CM0 at the same target primes: its terminating Legendre/Hesse identification proves L_0=Q_m(1/2)≡0 mod p, where L_0=sum_{n=0}^m b_n. This discharges the condition previously left open in the author's three-band note.

Use exactly the previously documented (AUTHOR DERIVED, NOT SOURCE-ADMITTED) three-band formulas:
 M≡L_0+pL_1+p²(L_2^low+L_2^mid+V_(4m)) (mod p³),
 N≡D_0+pD_1 (mod p²).
Set U_0=L_0/p+L_1, A_2=L_2^low+L_2^mid. Accepted CM0 ensures U_0 is p-integral. Accepted UR ensures 12U_0D_0-1 is divisible by p. With G=M/p and h=M+12N,

 Gh ≡ 12U_0 D_0 + p[U_0²+12U_0D_1+12D_0(A_2+V_(4m))] (mod p²),

and thus the **exact original-LIFT field certificate**, author-only until reviewed, is

 Delta_p-R_p ≡ (12U_0 D_0-1)/p + U_0² + 12U_0D_1
                +12D_0(L_2^low+L_2^mid+V_(4m)) - R_p  (mod p).

Here the p-local divisions precede modular reduction, and the separately typed low/middle/high and signed-cutoff ports are all retained. No postulated all-prime cancellation or silently replaced W/R/native CM readout occurs.

## 4. Actual exact cross-check: independent original R versus convolution Q

Executed original recurrences modulo p³ for B_n and the independent weighted 3F2 coefficients, then compared the *original* C_a/R double-sum to Q/p² and the p-local Delta quotient, at six selected primes; this is targeted cross-interface checking, NOT a new broad prime scan or universal proof.

| p | Q/p² mod p | Original frozen R_p | Delta_p | (W-p)/p² mod p |
|---:|---:|---:|---:|---:|
| 13 | 0 | 0 | 0 | 0 |
| 19 | 12 | 12 | 12 | 0 |
| 37 | 11 | 11 | 11 | 0 |
| 43 | 15 | 15 | 15 | 0 |
| 211 | 119 | 119 | 119 | 0 |
| 373 | 196 | 196 | 196 | 0 |

For p=373, **R=Delta=196 != 0**: a concrete source-typed *negative control* proves it is invalid to infer Delta=0 from W=p (mod p³). It is not a counterexample to LIFT itself. At p=19 the original boundary is already nonzero (12). Exact modular checks use integer modular inverses of p-unit denominators, no floating point or p-divisible denominator. Reproducible author-only checker: d25_source_port_bridge_check_20261026.py (delivered with this run); the six cases are not a native benchmark.

## 5. BRC carrier audit and terminal scope

BRC resolution: COMPOSE_APPLIED. Population is labeled p≡13,19 (mod 24); source branches are the ordered Clausen bulk (M,N) and signed cutoff Q, reflection coefficients v/C, and the original p-local Delta/R. The valid compression R=T is proved by *identical recurrence and low-rank transport*, not by squaring, taking absolute values, dropping signs or assuming a generic positive-mass quotient. Required future observer is Delta-R modulo p after the exact p² cutoff; those digits and coefficient origins are retained. The external two-coordinate quadratic ring is not a native X6 plane or the project's three-dimensional slice.

**Formal task outcome remains OPEN.** No all-prime proof of LIFT/JT2, no counterexample to it, no independent review, no native H0/B0 or [X]U mod p² experiment, and no Source-native checkpoint/Result/claim/owner rights are supplied by this author file. The latest Source continuation from a DIFFERENT logical Research conversation is only read-only evidence and not an authorized CLAIM in chatgpt-research-onhour-enterprise-math-20260923.

The next genuine required action is not another Clausen or WZ auxiliary proof: obtain the *same-original-class* native fixed H0/B0 divided-power module, its [X]U mod p², rank and semilinear direction with normalization eta; compare at p=373 to the **conditional** ordinary candidate norm 122102 mod 139129 only if rank one and coefficient identification/eta are proven; preserve the nonzero odd Hesse/Green branch, and read the native kappa and original Delta-R. If no native executor currently accepts the original benchmark, the support request must remain explicitly pending with responsible route and observable acceptance, never counted as a passed benchmark. Existing frozen predecessor sources and all other current owners are not reopened.

Source references (content and proof status kept distinct):
- research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE_RETURN_20260827.md (original reflected cutoff)
- research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN_20260827.md (frozen R, deformation)
- research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md (accepted CM0/SIMPLE and UR+LIFT scalar interface)
- research_notes/portable_direct/20261025_onhour_d25_clausen_three_band_local_jet_joint.md (unreviewed author three-band result)
- research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT/MCP-d6dd85529e9e45a9b5f808c1025f5918/767679018d6c936f92dd/D25_R2_HILBERT90_20261025.md (prior SOURCE author proof of conditional norm; NOT native CM)
