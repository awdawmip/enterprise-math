# D25/LIFT: complete top-digit semilinear gauge classification near the identity

Date: 2026-10-25, portable TASK_RESEARCH author derivation. Status: AUTHOR-PROVED / AUTHOR-CHECKED; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM. This note is a **second, logically distinct scientific unit** after the rank-two observer-loss witness in the preceding project artifact. No new native Source claim/run/checkpoint or independent mathematics review is asserted.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; parent D25/LIFT/JT2 OPEN. Existing native checkpoint 220ee1ba360f21152912d0b4c1abdf867a1e4496 and frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 are unchanged. The earlier rank-one Hesse candidate and this **local rank-two near-identity** classification are distinct coefficient models; neither supplies the missing native H0/B0.

## Precise infinitesimal question

For an odd p, r>=2, A_r=Z/p^r Z, R_r=A_r[T]/(T^2-2), sigma(a+bT)=a-bT and q=p^{r-1}, consider the free rank-two sigma-semilinear maps
\[
F_D(v)=C_D\,\sigma(v),\qquad C_D=I_2+qD
\]
where D is a 2x2 matrix over R_1=R_r/pR_r and is lifted arbitrarily to R_r; C_D is independent of this lift because p q=0. The relevant near-identity change of basis is \(P_X=I_2+qX\) for X in M_2(R_1). Here q^2=0, so all these C_D and P_X are units over R_r.

Define the sigma-even and sigma-odd parts
\[
D_+=(D+\sigma D)/2,\qquad D_-=(D-\sigma D)/2.
\]
Because p is odd, 2 is invertible. More specifically, R_1=F_p\oplus T F_p, D_+ is in M_2(F_p), and D_- is T times an F_p-matrix.

**Theorem (complete gauge quotient for the last p-adic digit under near-identity basis changes).** For D,D' in M_2(R_1), the following are equivalent:
1. There exists X in M_2(R_1) such that \(C_{D'}=P_X^{-1}C_D\sigma(P_X)\) modulo \(p^r\).
2. \(D'_+=D_+\) in M_2(F_p).
3. \(F_{D'}^2=F_D^2\) as exact R_r-linear matrices, i.e. they have the same *full matrix* square, not merely characteristic polynomial.

Moreover,
\[
P_X^{-1} C_D \sigma(P_X)=I_2+q(D+\sigma X-X),\qquad
F_D^2=C_D\sigma(C_D)=I_2+2qD_+.
\]
These formulas hold exactly modulo \(p^r\) for **every r>=2**. Consequently, \(D_+\), or equivalently the full normalized square digit \((F_D^2-I_2)/(2q)\bmod p\), is a complete invariant in this precisely restricted near-identity gauge problem.

**Proof.** From q²=0,
\(P_X^{-1}=I_2-qX\) and the displayed first formula follows by multiplying three factors and retaining exactly the q terms. Taking the sigma-even part kills sigma(X)-X, proving 1 => 2. Conversely, if D'_+=D_+, let \(\Delta=D'-D\), so sigma(Delta)=-Delta. Taking \(X=-\Delta/2\) gives sigma(X)-X=Delta; this gives 2 => 1 constructively, without lifting a solution iteratively or dividing by p. Direct multiplication gives the full square formula. The map from D_+ to \(I_2+2qD_+\) is injective: 2 is invertible modulo p and multiplication by q identifies each nonzero residue of F_p with a nonzero top p-adic digit in A_r. Thus 2 <=> 3. QED.

**Corollary (pure gauge vs genuine last-digit residual).**
- If D=T E_12 is sigma-odd, \(F_D^2=I_2\) and an explicit near-identity gauge to the trivial sigma-semilinear map is \(X=(T/2)E_{12}\): \(P_X^{-1}C_D\sigma(P_X)=I_2\).
- If D=E_12 is sigma-even, the square is \(I_2+2p^{r-1}E_{12}\ne I_2\); it is not gauged to the identity, even by an unrestricted change of basis, since square matrices of equivalent semilinear maps must be conjugate.
- If D_+ is any nonzero traceless matrix, both \(\operatorname{tr} F_D^2=2\) and \(\det F_D^2=1\) hold exactly, and the characteristic polynomial is \((X-1)^2\), although \(F_D^2\ne I_2\). This explains the entire traceless last-digit characteristic-polynomial information loss in the previous note (not just one E_12 example). In general,
\[
\operatorname{tr}(F_D^2)=2+2q\operatorname{tr}D_+,\quad
\det(F_D^2)=1+2q\operatorname{tr}D_+,\quad
\chi_{F_D^2}(X)=(X-1)^2-2q\operatorname{tr}D_+(X-1).
\]
The determinant identity uses q²=0, not a false general rule that matrix determinant is determined by trace over arbitrary rings.

At p=373,r=2: the even E_12 class has exactly 746 in the upper off-diagonal square position modulo 139129; the odd T E_12 class is pure gauge and its square is precisely I. At r=3 the even coefficient is 278258 modulo 51895117. These are structural coefficient-ring computations, **not** a native CM divided-power measurement.

## BRC observer and residual-fidelity scope

Applied existing BRC global typing to the precise future operation: the carrier stores sigma-even and sigma-odd top-digit branches separately until the declared observer is fixed. For *near-identity semilinear gauge equivalence and the full-square observer only*, the quotient \(D\mapsto D_+\) is **safe and complete**, by the theorem: the sigma-odd coordinate is removable with the explicit X above. For an observer that insists on the original fixed H0/B0 basis, original signed Hesse A/B ports, or a source-dependent kappa readout, that quotient is **not automatically safe**: the basis transformation or a proof that the observer is invariant under it must be retained. By contrast, the coarser trace/determinant projection remains unsafe even for the full-square observer, as shown by the nonzero traceless D_+ fiber.

This is an exact operator/observer lease on a finite-ring semilinear matrix carrier. It neither asserts a two-dimensional native Enterprise spatial plane (this is an external auxiliary rank-two module), nor promotes a signed Frobenius action into positive-mass BRC recurrence, nor changes P000.

## Focused exact author validation

Used standard-library Python exact pair arithmetic \((a,b)\leftrightarrow a+bT\) with \(T^2=2\), sigma(a,b)=(a,-b), and exact 2x2 matrix multiplication mod \(p^r\). For p=13,19,373 and r=2,3, tested D equal to E_12, T E_12, and one generic 2x2 mixed-even/odd matrix, with X equal to T E_12 and one generic mixed matrix. Verified:
- the full gauge transport identity \(P_X^{-1} C_D\sigma(P_X)=I+q(D+\sigma X-X)\);
- the full square identity \(C_D\sigma(C_D)=I+q(D+\sigma D)\);
- explicit elimination of the pure-odd \(D=T E_{12}\) using \(X=(T/2)E_{12}\);
- nonzero even square defect for \(D=E_{12}\) at all six declared (p,r) pairs.
All these author checks passed. The displayed proof, not the six-case test, establishes the universal statements.

## Preserved frontier and next action

The preceding GitHub portable unit established *nonfaithfulness* of determinant/trace for general rank-two finite-ring coefficients. This second unit provides a *complete constructive remedy* at the last p-adic digit near identity under explicitly restricted gauge. These are two separate author contributions, both UNREVIEWED/NOT_ADMITTED and **not** newly admitted Source task progress.

The genuinely missing original-class native data are still fixed H0/B0, [X]U mod p², rank, sigma action, normalization eta and the map to \(\omega+6\nabla_\lambda\omega\), kappa and \(\Delta_p-R_p\). Before using the last-digit theorem on actual native data, verify that the Frobenius coefficient matrix is invertible, rank two, and *already normalized to I modulo p^{r-1} in a declared basis*; otherwise these hypotheses do not hold and a different local expansion is required. The first exact test if the hypotheses hold is the sigma-even normalized D_+ (or full square top digit), **not** merely its trace and determinant. If native rank is one, consume the previously established rank-one norm law instead.

The native gateway in this author run returned CONTROL_QUOTA for both exact task and continuation reads. The existing checkpoint and earlier HANDOFF are historical immutable Source facts; they are not authorization for this run. No invented owner identity, CLAIM, open, Source checkpoint, experiment, Result, review or freeze. Support path: existing Enterprise Math Issue #1558, pending lawful Source read/claim/open and next checkpoint after the quota resolves. Frozen scientific pin remains unchanged.
