# D25/LIFT — exact rankwise Clausen jet recurrence and boundary-only repair obstruction

Date: 2026-10-25. TASK_RESEARCH portable continuation for Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT` / publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged.

**Status:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. No claimed current native Source run/CLAIM/checkpoint, no original-class CM experiment, and no proof of the global supercongruence. The equations below describe an external finite hypergeometric representation; no native Heartbeat X6 embedding is inferred.

## Next problem consumed

The preceding new proof shows that the Clausen-compatible denominator \(c(x)=1/2-3x\) collapses the mod-\(p\) cutoff Hasse support to exactly orders \(2,p+1\), with explicit intermediate leakage mod \(p^2\). But changing **only the cutoff forcing** while leaving the old fixed-denominator differential operator would violate the interior series. The next smallest unit is to transport the entire differential operator and quantify the obstruction to such a boundary-only repair.

Let \(p=6m+1\ge7\) be prime, \(N=p-1\), \(x=m+t\), and

\[
u_r(x)=\frac{(-x)_r(-2x)_r}{(\frac12-3x)_r\,r!},
\qquad
u_{k,r}=[t^k]u_r(m+t),\qquad
0\le r\le N.
\]

Set \(u_{k,r}=0\) if \(k<0\), \(r<0\), or \(r>N\). Work over the p-local formal Taylor coefficient ring; all the displayed denominators are units for \(r<p\).

### Theorem C — exact signed rank/Hasse source recurrence

For every \(0\le r\le N\), every \(k\ge0\),

\[
\boxed{
r(r-p/2)u_{k,r}
-(r-1-m)(r-1-2m)u_{k,r-1}
-3r\,u_{k-1,r}
+\bigl(3(r-1)-4m\bigr)u_{k-1,r-1}
-2u_{k-2,r-1}=0.
}\tag{1}
\]

The terminal omitted rank \(r=p\), rather than being set to zero as a source statement, is the exact cutoff boundary equation

\[
\boxed{
\widetilde J_{k,p}
=-(N-m)(N-2m)u_{k,N}
+(3N-4m)u_{k-1,N}-2u_{k-2,N}.
}\tag{2}
\]

In particular \(u_{0,N}=u_{1,N}=0\), so \(\widetilde J_{2,p}=-(N-m)(N-2m)u_{2,N}\). Using the already-proved \(\widetilde J_{2,p}\equiv-2\bmod p\) gives

\[
\boxed{u_{2,N}\equiv18/5\pmod p,}\tag{3}
\]

a coefficientwise source explanation for the universal second-order boundary forcing. At \(z=1/2\), the ordinary second parameter derivative of the cutoff equation carries \(-4(1/2)^p\equiv-2\bmod p\). The rank and Hasse sources are preserved until the evaluation is actually performed.

**Proof.** Write the Clausen-compatible operator as a *polynomial in the parameter increment*:

\[
\widetilde{\mathcal L}_{m+t}
=\theta\!\left(\theta-\frac p2\right)
-z(\theta-m)(\theta-2m)
+t\underbrace{\left[3(z-1)\theta-4mz\right]}_{\mathcal L_1}
-2t^2z.
\]

Its exact cutoff action is

\[
\widetilde{\mathcal L}_{m+t}\sum_{r=0}^N u_r(m+t)z^r
=\sum_{k\ge0}\widetilde J_{k,p}t^kz^p .
\]

For \(r<p\), the \(z^r t^k\) coefficient is zero and equals the left-hand side of (1). For \(r=p\), only the \(z\)-shifted terms from rank \(N\) survive and yield (2). Both identities are exact, not merely congruences. The numerator at rank \(N\) has two simple parameter zeros at \(x=m\), proving \(u_{0,N}=u_{1,N}=0\); since \((N-m)(N-2m)\equiv5/9\pmod p\), equation (3) follows. \(\square\)

### Theorem D — a rank-one no-go certificate for boundary-only correction

Let \(\mathcal L^{\rm fixed}_m=\theta^2-z(\theta-m)(\theta-2m)\), the operator belonging to the *fixed* denominator family. Applying it to the Clausen-compatible terminating series, the interior coefficient at \(z^1\) is exactly

\[
\boxed{
[z]\,\mathcal L^{\rm fixed}_m\widetilde\Phi_p(m,z)
=\frac{pm^2}{1-p/2}
\equiv pm^2\not\equiv0\pmod{p^2}.
}\tag{4}
\]

**Proof.** Since \(u_0(m)=1\), \(u_1(m)=2m^2/(1-p/2)\), the \(z^1\) coefficient is \(u_1(m)-2m^2\). Simplify to (4). The numerator has valuation exactly one, while \(1-p/2\) and \(m\) are \(p\)-units. A proposed correction supported only at the omitted cutoff monomial \(z^p\) has zero coefficient at \(z^1\), so it cannot repair (4). \(\square\)

This no-go is limited to the stated *boundary-only* substitution; it does not forbid a correction that also transports the interior operator/coefficients, nor does it decide the global Clausen reflected-tail identity.

## Exact checker and new continuation frontier

The adjacent `20261025_hourly_d25_clausen_operator_rank_boundary_check.py` constructs all Taylor coefficients through order six using the *full* rational Clausen denominator as an invertible finite-series factor over \(\mathbb Z/p^2\). Author run: **2,346** rank/Hasse/boundary-low-order/no-go checks across eight primes \(p=7,13,19,31,37,43,73,103\), all PASS. Finite checks support, rather than replace, the exact identities above.

Previously consumed theorem A/B (two-port support and all-middle leakage): `research_notes/portable_direct/20261025_hourly_d25_clausen_corrected_hasse_bridge_r11.md` at commit `5112b02283d53205fc96651c61b204ee41bf28da`. Avoid re-crediting its earlier conclusions.

**BRC/source obligations:** the true signed residual depends on the operator itself, parameter family, denominator, rank and Hasse order; no source-safe quotient may keep just a cutoff port while forgetting the rank-one interior term. The next executable mathematical action is to combine the exact rankwise recurrence (1) with the *ordered signed Clausen reflection tail* at \(z=1/2\), seeking a genuine all-target-prime telescoping certificate rather than assuming one. Exact original CM \(H_0/B_0\), \([X]U\bmod p^2\), Frobenius direction/normalization and \(\kappa\) source bridge remain unverified. D25/LIFT/JT2 parent OPEN.

Original control support Issue #1558 retains the predecessor CLAIM mismatch; one fresh continuation read in this run returned `INVALID_ARGUMENT / CONTROL_QUOTA`. There is no new authorized native Source checkpoint or scientific admission.
