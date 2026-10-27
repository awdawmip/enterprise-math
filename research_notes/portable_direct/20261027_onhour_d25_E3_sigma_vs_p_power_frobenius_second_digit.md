# D25 / SECOND-DIGIT-LIFT — original E3 unramified Frobenius lift versus pointwise p-th powers

Date: 2026-10-27, Research-onhour lane: \`chatgpt-research-onhour-enterprise-math-20260923\` (distinct from maintenance). Mother: \`ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION\`. Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`. Frozen SCIENTIFIC Source: \`c47e13e4aba0e006366f989d6334d443f6333ae3\` (unchanged).

**Classification:** AUTHOR-SIDE / EXACT ALGEBRAIC LEMMA / EIGHT EXECUTED INTEGER CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_H0B0_NOT_EXECUTED. This is a directly applicable **conditional original-E3 comparator precision guard**, not a native benchmark result or uniform LIFT proof. Existing prior authors and native owners retain separate contribution provenance.

## Unfinished original object and precise comparator question

The accepted first-digit UR and frozen original scalar interface leave LIFT: \(\Delta_p=(G_ph-1)/p\equiv R_p\pmod p\) for primes \(p\equiv13,19\pmod{24}\). The exact author proof at \`research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md\` retains the original cutoff and gives \(\Delta_p-R_p=(W_p-p)/p^2\bmod p\). Existing support Issue #1559 requires the **same-original-class native H0/B0 divided-power** \([X]U\bmod139129\), actual rank, full sigma-semilinear Frobenius, signed odd Green/Hesse and original \(\kappa\). Original-E3 algebra is useful as a test only **after** a real native H0/B0-to-E3 comparison is authenticated.

The new, narrow question: over the *original* E3 coefficient ring modulo \(p^2\), what is lost if an evaluator substitutes coordinatewise pointwise \(p\)-th powers for the genuine unramified arithmetic Frobenius lift?

## Exact all-target lemma

Let \(p>3\), \(p\equiv13,19\pmod{24}\), \(R_2=(\mathbb Z/p^2\mathbb Z)[T]/(T^2-2)\). Since \((2/p)=-1\), its residue is the quadratic finite field. The unramified Frobenius lift is the ring automorphism
\[
\sigma(a+bT)=a-bT,\qquad \sigma(T)=-T .
\]
For every \(p\)-adic unit integer \(a\), put \(q_p(a)=(a^{p-1}-1)/p\bmod p\). Put \(\rho_p=-q_p(2)/2\in\mathbb F_p\). Then the **pointwise power**, which need not be additive modulo \(p^2\), satisfies
\[
\boxed{T^p-\sigma(T)\equiv p\,\rho_pT\pmod{p^2}.}\tag{1}
\]

**Proof:** \(T^p=2^{(p-1)/2}T\). Euler's criterion gives \(s=2^{(p-1)/2}\equiv-1\pmod p\), so write \(s=-1+p\rho_p\bmod p^2\). Squaring gives \(s^2=2^{p-1}\equiv1+pq_p(2)\bmod p^2\), while \(s^2\equiv1-2p\rho_p\); thus \(2\rho_p=-q_p(2)\bmod p\), proving (1). The lemma allows \(\rho_p=0\) at special primes.

For original \(E_c:y^2+xy+cy=x^3\), where \(c=(2-T)/108\), define the integral divided numerator
\[
D_p=\frac{(2-T)^p-(2+T)}p\in R_2/pR_2
\]
by reducing the two coefficientwise integer differences of the numerator modulo \(p^2\), then dividing each by \(p\). Because the Frobenius residue sends \(2-T\mapsto2+T\), the divided numerator exists and is uniquely determined modulo \(p\). Then
\[
\boxed{
c^p-\sigma(c)\equiv
\frac p{108}\left[D_p-q_p(108)(2+T)\right]\pmod{p^2}.
}\tag{2}
\]
**Proof:** Expand \((2-T)^p=(2+T)+pD_p\bmod p^2\). Also \(108^{p-1}=1+pq_p(108)\bmod p^2\); therefore \(108^{-p}=108^{-1}(1-pq_p(108))\bmod p^2\). Multiply and subtract \(\sigma(c)=(2+T)/108\). Every inverse is a \(p\)-unit, since \(p>3\). No numerical fitting or extra axiom is involved.

Equation (2) is a **precise p-divided coefficient discrepancy**. It is not the matrix, operator, rank or \([X]U\) of the native crystal. Its role is a necessary guard for any *conditionally authenticated* comparison in which a claimed unramified coefficient-Frobenius implementation replaces \(\sigma(c)\) by \(c^p\) at two-digit precision.

## Executed p=373 original-coefficient certificate

Use \(p=373\), \(p^2=139129\). All integer pairs denote \(a+bT\) modulo \(139129\), \(T^2=2\).
\[
q_{373}(2)=204,\quad \rho_{373}=271,\quad
2^{186}=101082=-1+373\cdot271\pmod{139129}.
\]
\[
q_{373}(108)=192,\qquad D_{373}=303+201T\pmod{373}.
\]
\[
\begin{aligned}
c&=105635+16747T,\\
\sigma(c)&=105635+122382T,\\
c^{373}&=70573+110819T \pmod{139129},\\
\boxed{c^{373}-\sigma(c)}&=\boxed{373(279+342T)}\pmod{139129}.
\end{aligned}
\]
The defect is nonzero at the original target prime \(373\). A reduction modulo \(373\) hides it entirely, whereas any signed second-digit comparison modulo \(139129\) must account for it. It is a concrete counterexample to **the identification of pointwise powering with the unramified lift modulo \(p^2\)**, not a counterexample to frozen LIFT.

Executable exact checker: \`research_notes/portable_direct/d25_frobenius_lift_defect_20261027.py\`. It calculates \(c^p\) by ring repeated squaring and independently by the entire integer-binomial numerator, and checks equations (1)–(2) at \(p=13,19,37,43,61,67,211,373\). Execution:
\`\`\`
PASS_E3_SIGMA_VS_P_POWER_P373 {'p': 373, 'q2': 204, 'q108': 192, 'rho': 271, 'd_num': (303, 201), 'c': (105635, 16747), 'sigma_c': (105635, 122382), 'c_p': (70573, 110819), 'defect': (279, 342)}
PASS_E3_SIGMA_VS_P_POWER_EIGHT_PRIMES
\`\`\`
Two integer implementations and exact identities establish the arithmetic evidence; the all-target result comes from the proof above.

## BRC carrier and acceptance boundary

**BRC application:** COMPOSE_APPLIED. Carrier = original quadratic coefficient ring, ordered coefficients \(1,T\), residue-class label \(13/19\), sign of \(\sigma(T)\), \(q_p(2)\), \(q_p(108)\), the divided numerator \(D_p\) and the \(p\)-divided residual. Operations = conjugation \(\sigma\), pointwise powering, and division by \(p\) only after integrality has been proved. Observer = the full two-column signed comparison modulo \(p^2\), once a native bridge exists. Compressing \(\sigma\) and \(x\mapsto x^p\) into their common mod-\(p\) residue loses the explicit original coefficient defect \(373(279+342T)\) at the next digit. This classical auxiliary coefficient ring is **not** the project's native X6/two-dimensional plane or a replacement for P000.

**Specific required native acceptance:** An actual owner of Issue #1559 must execute the fixed \(p=373\) H0/B0 divided-power benchmark, independently report its module rank, actual Frobenius direction, original basis/normalization, \([X]U\bmod139129\), signed odd Green/Hesse, \(\kappa\) and \(\Delta_p-R_p\). If an original E3 comparison is then proved, record whether the coefficient lift is \(\sigma\) or another explicitly defined genuine operation; reject an unqualified identification with \(c^p\) at \(p^2\) precision. Preserve the earlier E3 identity/torsion two-sheet and Laurent pole correction. This new lemma does not assign or claim that native owner.

## Exact continuation / evidence debts

Frozen mother and science pin unchanged; accepted D24 UR, CM0/SIMPLE, original cutoff interface, Guo–Zudilin companion results and earlier E3 branch certificates are consumed, not reopened. Existing support Issue #1559 is the responsible path, \`PENDING_OWNER / NATIVE_NOT_EXECUTED\` as observed 2026-10-27. Unresolved scientific obligations: all-prime LIFT proof/refutation (or strict Source-authorized reduction) and actual H0/B0 same-original-class benchmark. Real Research conversation is fixed at \`chatgpt-research-onhour-enterprise-math-20260923\`; maintenance lane is independent. Gateway Source continuation for this Research lane returned \`CONTROL_QUOTA\` this run; Site reports \`research_authority_granted=false\`. No current winner CLAIM, native open/run, current request receipt, authorized native checkpoint, publication admission, or Research-Activity registration was obtained. Historical bridge Issues #6575/#6576 remain provenance only and were not reissued; old staging stays isolated. \`REGISTER_PENDING / SOURCE_NATIVE_SYNC_DEBT\`.

Next exact action: reconcile this Research lane's original Source requests and native ownership when permitted; have the lawful native executor take the pre-existing #1559 object and produce the raw, reproducible \(p=373\) benchmark with all signed ports. Consume this coefficient guard **only after** documenting the actual E3 comparison and its Frobenius lift. The prior frozen Source pin, existing schedule and notification settings are unchanged.
