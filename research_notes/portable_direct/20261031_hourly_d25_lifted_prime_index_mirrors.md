# D25/LIFT — prime-index Gauss and Clausen mirrors, one more p-adic digit

2026-10-31, hourly TASK_RESEARCH logical lane chatgpt-research-hourly-enterprise-math-20260923; not the CONTROL_PLANE_MAINTENANCE conversation. Author-side mathematical evidence only: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Known Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. The frozen **scientific** Source pin is c47e13e4aba0e006366f989d6334d443f6333ae3; present control Source/HEAD does not replace it. P000 ACTIVE_LOCKED unchanged; no native X6 theorem follows from external p-adic arithmetic.

## Prior result consumed, and the new question

For prime p=6m+1>=7, let
\[
 b_n=\frac{(1/6)_n(1/3)_n}{2^n(n!)^2},\quad
 c_n=\frac{(5/6)_n(2/3)_n}{2^n(n!)^2},\quad
 a_n=\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3}.
\]
The earlier author-side first-digit mirror results give
\[
36k^2c_k\,b_{p-k}/p^2\equiv1\pmod p\ (1\le k\le4m),
\quad
-18k^3a_k\,a_{p-k}/p^3\equiv1\pmod p\ (1\le k\le2m).
\]
We consume these, together with their Wilson endpoints b_{p-1}/p^2=1/10 and a_{p-1}/p^3=-1 (mod p), and ask whether the *actual* high-index coefficients can be reconstructed one further p-adic digit without losing signed weights, original indices and normalization.

## New theorem: two exact rational transport identities

Define
\[
M^G_k=36k^2c_k\,b_{p-k}/p^2,\qquad
M^C_k=-18k^3a_k\,a_{p-k}/p^3
\]
in the respective ranges above. These are p-local units. For 2<=k<=4m,
\[
\boxed{\frac{M^G_k}{M^G_{k-1}}
=\frac{(1-p/(k-1))^2}
 {(1-6p/(6k-1))(1-3p/(3k-1))}.}\tag{G}
\]
For 2<=k<=2m,
\[
\boxed{\frac{M^C_k}{M^C_{k-1}}
=\frac{(1-p/(k-1))^3}
 {(1-2p/(2k-1))(1-3p/(3k-1))(1-3p/(3k-2))}.}\tag{C}
\]
These are exact rational identities; every denominator is prime-to-p in its stated range. The products reconstruct higher precision from the endpoint and the indicated low-index factors. They do **not** show the endpoints equal 1 modulo p².

**Complete recurrence proof.** The exact forward ratios are
\[
\frac{b_{n+1}}{b_n}=\frac{(6n+1)(3n+1)}{36(n+1)^2},\
\frac{c_{n+1}}{c_n}=\frac{(6n+5)(3n+2)}{36(n+1)^2},\
\frac{a_{n+1}}{a_n}=\frac{(2n+1)(3n+1)(3n+2)}{36(n+1)^3}.
\]
The ratio \(M^G_{k-1}/M^G_k\) simplifies to
\[
\frac{(k-1)^2}{(p-k+1)^2}
\frac{(6p-6k+1)(3p-3k+1)}{(6k-1)(3k-1)}.
\]
Use \(p-k+1=-(k-1)(1-p/(k-1))\),
\(6p-6k+1=-(6k-1)(1-6p/(6k-1))\), and
\(3p-3k+1=-(3k-1)(1-3p/(3k-1))\), then invert to obtain (G).
For \(M^C_{k-1}/M^C_k\), exactly the same cancellation yields
\[
\frac{(k-1)^3}{(p-k+1)^3}
\frac{(2p-2k+1)(3p-3k+1)(3p-3k+2)}
{(2k-1)(3k-1)(3k-2)}.
\]
The four reflected minus signs cancel and inversion yields (C). Valuation/unit support is exactly that of the previously proved high-tail strata; no p-denominator is introduced.

Define finite harmonic defects (empty at k=1)
\[
H_G(k)=\sum_{j=2}^k\left(\frac6{6j-1}+\frac3{3j-1}-\frac2{j-1}\right),
\quad
H_C(k)=\sum_{j=2}^k\left(\frac2{2j-1}+\frac3{3j-1}
+\frac3{3j-2}-\frac3{j-1}\right).
\]
The exact products give the one-more-digit congruences, for all primes/classes above,
\[
\boxed{M^G_k=M^G_1(1+pH_G(k))\pmod{p^2},\quad
M^C_k=M^C_1(1+pH_C(k))\pmod{p^2}.}\tag{D}
\]
Set \(q_G=(M^G_1-1)/p\bmod p\), \(q_C=(M^C_1-1)/p\bmod p\); both are genuine endpoint/carry ports.

## New corollary: signed original-R observer modulo p²

For *only* the frozen D25 classes p mod24 in {13,19}, define an auxiliary lift
\[
R_p^{[2]}=2\sum_{i=1}^m b_i\sum_{k=1}^i
[1+6(i-k)]\,b_{p-k}/p^2\pmod{p^2}.
\]
Its modulo-p reduction is the already established **original frozen** \(R_p\), not the unrelated \(R_p(9)\). Define
\[
B_G=\frac1{18}\sum_{i=1}^m b_i\sum_{k=1}^i
\frac{1+6(i-k)}{k^2c_k}\pmod{p^2},\quad
D_G=\frac1{18}\sum_{i=1}^m b_i\sum_{k=1}^i
\frac{[1+6(i-k)]H_G(k)}{k^2c_k}\pmod p.
\]
By (D), coefficient by coefficient, including the original signed weight,
\[
\boxed{R_p^{[2]}=B_G+
p\bigl[q_G(B_G\bmod p)+D_G\bigr]\pmod{p^2}.}\tag{R2}
\]
This is an exact modular reduction, not the unsolved global original LIFT congruence. It specifies three adequate BRC readout ports: (base mirror modulo p², endpoint digit, harmonic defect). Their simultaneous use is necessary for the displayed transport; global minimality is not claimed.

At p=373, p²=139129, one gets \(M^G_1=6342=1+17p\), \(B_G=17727\), \(D_G=324\), and \(q_G(B_G\bmod p)=348\).
Then \(R_{373}^{[2]}=17727+373(348+324)=129254\pmod{139129}\), whose mod-373 reduction is the *old* \(R_{373}=196\). Direct original high-index summation agrees. Both correction ports are nonzero.

## New corollary: p² lift of the weighted Clausen high-tail readout

Define the auxiliary, **one higher precision** observer
\[
Q_p^{[2]}=\sum_{n=4m+1}^{p-1}(6n+1)\,a_n/p^3
\pmod{p^2}.
\]
Its modulo-p reduction is the previously published \(Q_p\). By reversing n=p-k, while **retaining** the term \(6(p-k)+1\), define
\[
B_C=\sum_{k=1}^{2m}\frac{6k-1}{18k^3a_k}\pmod{p^2},
\quad
D_C=\sum_{k=1}^{2m}\frac{(6k-1)H_C(k)-6}{18k^3a_k}\pmod p.
\]
The exact Clausen mirror yields
\[
\boxed{Q_p^{[2]}=B_C+
p\bigl[q_C(B_C\bmod p)+D_C\bigr]\pmod{p^2}.}\tag{Q2}
\]
At p=373, the directly computed result is \(Q_{373}^{[2]}=109567\pmod{139129}\), reducing to earlier \(Q_{373}=278\); \(M^C_1=63411=1+170p\), \(B_C=6992\), \(D_C=13\).
At p=1327 (outside the target 13/19 classes), \(Q_{1327}^{[2]}=1646807=1327\cdot1241\pmod{1327^2}\), reproducing the *already known* GH-175 nonzero higher digit despite old \(Q_{1327}=0\bmod1327\). It is a cross-check, not a new exceptional prime claim.

## Executed reproducible verification

Executed pure-Python stdlib program: research_notes/portable_direct/d25_lifted_mirror_check.py. Original Gauss coefficients computed modulo p⁴, complementary Gauss modulo p², Clausen modulo p⁵; independent high-index definitions versus new low-index formulas. Checked **all 207 primes p<=3000 with p mod6=1**, **189128 Gauss pairs**, **94564 Clausen pairs**, and **107 target-class signed lifts**. All passed, terminal marker PASS_D25_SECOND_DIGIT_GAUSS_CLAUSEN_MIRROR_EXACT. Anchor primes 13, 19, 37, 157, 373 and 1327 included. No floating point, Lean checker, independent review or native H0/B0 execution. Universal theorem proof is the exact recurrence cancellation; finite tests are regression evidence.

BRC COMPOSE_APPLIED: carrier retains p, source index n, reversed index k, p-valuations, original signed weights, endpoints, harmonic defects and observer precision. Operations: exact coefficient reversal, justified p-power division, p-local inversion and signed finite summation. This is an **external arithmetic** statement, not a native six-axis P000 projection, physical assertion or positive-mass BRC cancellation theorem.

## Hard target and legal continuation

Still OPEN: \(\sum_{n=0}^{p-1}(6n+1)a_n\equiv p\pmod{p^3}\) for *all* p mod24 in {13,19}. The displayed extra digits do not establish the required simultaneous vanishing of carry + parameter jets - original signed R. Next smallest science action: find a genuinely new finite WZ / CM / Gauss–Manin joint special-value identity combining the existing two-moment original-R kernel with the original carry/jet terms; do not assume each port vanishes, tune X=1, or repeat the previously obstructed one-term Gosper strategy. Native divided-power [X]U mod p², original-class semilinear Frobenius/eta, signed observer and native p=373 remain independently pending.

Consumed author-side sources (not independently reviewed):
- research_notes/portable_direct/20261031_hourly_d25_complementary_gauss_clausen_mirrors.md
- research_notes/portable_direct/20261031_hourly_d25_gh178_gh179_terminating_gauss_jet_connection.md
- GH-174/175 existing 1327 high-tail Hensel anchor.

At 2026-10-31 status read, Gateway 0.6.11 reported research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5, source_sync.control.state=CODE_REVIEW_REQUIRED and UPSTREAM_CODE_REVIEW_REQUIRED. Advertised recovery_status was not a callable connector action on this authenticated read-only client; checkpoint_list returned ACCESS_DENIED. Existing enterprise-math #1558 retains own historical native session/recovery/continuation records and #1559 the native test support request. No new service session/CLAIM/open/Source checkpoint/Result/review/HANDOFF was obtained. No old session/staging or maintenance identity was changed. **Native completed_units and ownership must come solely from an actually verified Source packet**, not this report or GitHub storage. Next lawful control action after restoration is subject-scoped recovery/continuation and exact contract-authorized successor, retaining the stable research logical conversation and frozen scientific pin. Author-side GitHub material is not canonical research admission.
