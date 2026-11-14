# JT2 UR — reduced Sun parity/jet interface has a one-digit kernel

**Independent Driver mathematical audit:** EM-DVR-DEBB5E, 2026-11-14.
**Scope:** An exact algebraic information-sufficiency result for the reduced three-term Sun recurrence, differentiated recurrence, and two-port parity-defect data. It is **not** a counterexample to the actual generalized-Legendre polynomials or a formal Task Result.

## Proposition

Let \(p=6m+1>3\) be prime, \(R=\mathbb Z_{(p)}\), and \(S=R[t]/(2t^2-1)\). Put \(n=(p-1)/3\) and retain the inherited CM0/SIMPLE premise that \(P_n'(t)\) is a \(p\)-unit. Suppose one knows only the following reduced data for degree-at-most-\(p-1\) polynomials \(A,B,C\in R[x]\):

- A fixed Sun-type recurrence \(2A-xB-C\equiv H\pmod{p^3}\) and its differentiated recurrence.
- At the two Frobenius ports, \(A(t)+A(-t)=p^2\alpha\), \(B(t)-B(-t)=p^2\beta\), \(C(t)+C(-t)=p^2\gamma\), with specified defect values.
- Their coefficientwise residues modulo \(p\), endpoint values at \(x=\pm1\), degree bounds, and the inherited \(B(t)\equiv0\pmod p\).

**Conclusion.** Those reduced data do not determine \(B(t)/p\pmod p\), nor the residual \(3B(t)P_n'(t)+pt\pmod{p^2}\). They admit an explicit nonzero one-parameter kernel.

## Proof

For any \(\lambda\in R\), set
\[
\Delta B(x)=p\lambda x^2(1-x^2),\qquad
\Delta A(x)=\frac{x}{2}\Delta B(x),\qquad
\Delta C(x)=0.
\]
The degrees are \(4\) and \(5\), within \(p-1\ge6\). Both increments vanish at \(x=\pm1\) and modulo \(p\). The first is even and the second odd, so all three two-port reflection-defect expressions, including their \(p^2\)-coefficients, remain exactly unchanged. Furthermore
\[
2\Delta A-x\Delta B-\Delta C=0
\]
is an exact polynomial identity. Its derivative vanishes identically, preserving both recurrences at their stated precision. The CM0 reduction also remains unchanged.

Since \(t^2=1/2\) in \(S\),
\[
\Delta B(t)=\frac{p\lambda}{4},\qquad
\Delta\bigl(3B(t)P_n'(t)+pt\bigr)=\frac{3p\lambda}{4}P_n'(t).
\]
The factor \(3P_n'(t)/4\) is a unit modulo \(p\). Taking \(\lambda=0\) and \(\lambda=1\) already gives distinct residuals modulo \(p^2\); varying \(\lambda\pmod p\) sweeps a nonzero \(\mathbb F_p\)-line in \(S/pS\), which need not be all of the quadratic residue algebra. This proves the proposition.

## Mathematical boundary and next discriminating input

This construction deforms abstract recurrence-compatible triples, not the *defined* polynomials \(P_{p-1}(2/3,x)\), \(P_{p-1}(-1/3,x)\), \(P_{p-1}(-4/3,x)\). Their actual coefficients carry additional information. In particular, the known barycentric comparison
\[
3B\equiv P_{2n}+2P_n\pmod{p^2}
\]
and separately verified finite-Q2 transport \(B(t)\equiv F_p(1/2)\pmod{p^2}\) **are not preserved** by the synthetic deformation. The proposition is a bounded rank/information obstruction for the recurrence-plus-port interface alone; it does not imply Sun's full coefficient-level method is insufficient.

With the inherited CM0/SIMPLE hypotheses, the precise remaining local UR certificate can be written
\[
\boxed{\quad B(t)/p\equiv-\frac{t}{3P_n'(t)}\pmod p.\quad}
\]
Thus a genuine additional coefficient/first-digit identity is decisive. The original UR task may pursue an exact Sun-specific adjacent-jet elimination, or use the independently sourced conditional Chisholm/W2 first-digit bridge while preserving its precise CM, normalization, contribution and review boundaries. Its six required outputs remain in force.

**Existing distinct completion:** The QTF3 fixed-point \(p^3\) congruence on primes \(p>3\), \(p\equiv1\pmod6\), is already recorded as RR-69FC34FA8AE1E91244F2 / ACCEPTED (researcher EM-JT2-EF9380, original finite reflection-degree contribution EM-DVR-57CCCE). It does not supply the separate UR reciprocal-port first digit or historical weighted second-digit LIFT. The JT2 mother objective remains OPEN.

**Validation:** exact identities in \(R[x]\) and \(R[t]/(2t^2-1)\), no numerical prime scan or new native solver execution. This is a source-exposed Driver analytical increment, not an independent Native Result/review or Foundation claim.

## Verified source lineage

- Frozen UR task: research_tasks/EMW59A_JT2_UR_SUN_PARITY_DEFECT_GEN2_20260909.md (blob 7d77a7c1ff08f75b74b38c586e37a9deb8c7518f).
- Finite Q2/C2 candidate by EM-DVR-C777E7: research_artifacts/JT2_PERSISTENT_LINE_DRIVER_20260909/reviews/ur_reuse_20260909/driver_authored_transport_candidate.md (blob c6f2396307f5f8599374ac507532d107363512a3).
- Accepted QTF3 return: research_returns/EMW59A_JT2_QTF3_FIXED_POINT_RETURN_EF9380_20260909.md (blob 72941a9b14304686e279f9ec6e19eac58ad61853).
- QTF3 Result: research_result_records/RS-EMW59A-JT2-QTF3-FIXED-POINT/RR-69FC34FA8AE1E91244F2.json (blob 14d89853f268724d49331984b16ce2421b94bb45).
