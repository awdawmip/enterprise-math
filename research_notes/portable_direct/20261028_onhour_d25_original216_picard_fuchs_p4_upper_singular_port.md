# D25 — original 216 finite Picard–Fuchs cutoff anomaly and fourth-digit upper-band singular port

Date: 2026-10-28 Asia/Hong_Kong.
Research lane: chatgpt-research-onhour-enterprise-math-20260923; separate from CONTROL_PLANE_MAINTENANCE chatgpt-hourly-enterprise-math-20260921.
Classification: AUTHOR-SIDE / EXACT ALL-PRIME LEMMAS / 27 EXECUTED FINITE CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.
Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is UNCHANGED.

## Original source and target

Maintain the original weighted finite sum and every index/valuation:

\[
t_n=\frac{(2n)!(3n)!}{216^n(n!)^5}
=\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3},\qquad
w_n=(6n+1)t_n,\qquad W_p=\sum_{n=0}^{p-1}w_n.
\]

The frozen D25 target remains \(W_p\equiv p\pmod{p^3}\) for \(p\equiv13,19\pmod{24}\), with the separately pinned original \(\Delta_p-R_p\) interface. The following statements are exact scalar lemmas on the original 216 summands and do not prove the target LIFT.

## Theorem 1 — sharp Picard–Fuchs endpoint (all primes p>3)

Let \(\theta=z\,d/dz\), \(F_p(z)=\sum_{n=0}^{p-1}t_nz^n\in\mathbb Z_{(p)}[z]\), and

\[
\mathcal L=\theta^3-\frac z2(\theta+\tfrac12)(\theta+\tfrac13)(\theta+\tfrac23).
\]

For every prime \(p>3\), the following exact rational polynomial identity and congruences hold:

\[
\boxed{\mathcal LF_p(z)=-\tfrac12(p-\tfrac12)(p-\tfrac23)(p-\tfrac13)t_{p-1}z^p.}\tag{P1}
\]

\[
\boxed{t_{p-1}/p^3\equiv-1\pmod p,\qquad
\mathcal LF_p(z)\equiv-\frac{p^3}{18}z^p\pmod{p^4}.}\tag{P2}
\]

Thus \(\mathcal LF_p=0\pmod{p^3}\) coefficientwise, while the boundary has exact valuation 3 and is nonzero modulo \(p^4\). The degree-\(<p\), constant-1 polynomial solution of this homogeneous equation modulo \(p^3\) is unique. No such degree-\(<p\), constant-1 polynomial exists modulo \(p^4\).

Proof: the adjacent-term recurrence is

\[
(n+1)^3t_{n+1}=\tfrac12(n+\tfrac12)(n+\tfrac13)(n+\tfrac23)t_n.
\]

It cancels the coefficients of \(z^0,\ldots,z^{p-1}\) in \(\mathcal LF_p\), leaving the exact \(z^p\) boundary. Wilson block reduction states \((qp+r)!/p^q\equiv(-1)^q q!\,r!\pmod p\) for \(q=1,2\) and \(0\le r<p\). In particular

\[
(2p-2)!/p\equiv-1,\quad
(3p-3)!/p^2\equiv-1,\quad
((p-1)!)^5\equiv-1,\quad
216^{p-1}\equiv1\pmod p.
\]

These give \(t_{p-1}/p^3\equiv-1\). Substitution into P1 yields \(-p^3/18\), whose coefficient is a \(p\)-unit. Uniqueness below degree \(p\) follows inductively from the recurrence with unit coefficient \(n^3\) for \(1\le n<p\); the nonzero \(z^p\) obstruction prevents a homogeneous degree-\(<p\) lift modulo \(p^4\). The weighted final term also has the universal digit

\[
\boxed{w_{p-1}/p^3\equiv5\pmod p.}\tag{P3}
\]

This proves that an ordinary Picard–Fuchs certificate may omit the finite endpoint through precision \(p^3\), but not through \(p^4\).

## Theorem 2 — exact fourth-digit original upper-band port (p=6m+1)

For any prime \(p=6m+1>3\), each original index \(4m+1\le n\le p-1=6m\) has \(v_p(t_n)=v_p(w_n)=3\). Define

\[
\sigma_r=\frac{w_{4m+1+r}}{p^3}\bmod p,\quad 0\le r<2m,\qquad
\Omega_p=\sum_{r=0}^{2m-1}\sigma_r\pmod p.
\]

Direct Wilson reduction of the original factorials gives

\[
\boxed{\sigma_r\equiv-6(2r+1)
\frac{(2m+1+2r)!(3r+1)!}
{216^{4m+1+r}((4m+1+r)!)^5}\pmod p.}\tag{P4}
\]

Hence the original full cutoff satisfies

\[
\boxed{W_p\equiv\sum_{n=0}^{4m}w_n+p^3\Omega_p\pmod{p^4}.}\tag{P5}
\]

There is a *reversible unweighted lower-to-upper mirror*. For \(1\le\ell\le2m\), let \(u_\ell=t_\ell\bmod p\in\mathbb F_p^\times\) and \(\nu_\ell=w_{p-\ell}/p^3\bmod p\). The previously proved original paired-unit result R2, evaluated at \(\ell\) where both factorial floor counts are zero, gives

\[
\frac{t_\ell t_{p-\ell}}{p^3}\equiv-\frac1{18\ell^3}\pmod p.
\]

Therefore

\[
\boxed{\nu_\ell\equiv-\frac{1-6\ell}{18\ell^3u_\ell}\pmod p,\qquad
\Omega_p=\sum_{\ell=1}^{2m}\nu_\ell.}\tag{P6}
\]

This directly CONSUMES R2; it is not a re-proof of R2. The low *weighted* digit cannot be inverted at \(\ell=m\): \(6m+1=p\) and \(\bar w_m=0\), although \(u_m\) is a unit. Its missing upper branch is nonzero and has a simple repair:

\[
\boxed{\frac{w_m}{p}\equiv u_m,\qquad
\nu_m=\frac{w_{p-m}}{p^3}\equiv24u_m^{-1}\ne0\pmod p.}\tag{P7}
\]

A weighted-only mirror discarding this source index loses an actual fourth-digit contribution. Retaining \(u_m\) or \(w_m/p\) repairs the information loss. The independent formulas P4 and P6 agree termwise.

## Executed exact certificate and fixed p=373 witness

Companion Python standard-library integer program: research_notes/portable_direct/d25_216_picard_fuchs_cutoff_p4_guard_20261028.py. Actual execution tested **27 primes**, including \(5,7,11,13,19,37,211,373\), with integer modular arithmetic and no floats. Checks cover every internal Picard–Fuchs coefficient, the exact endpoint, independent original binomial formulas at selected indices, each upper-band factorial digit, the unweighted R2 inverse, the exceptional branch and the original full cutoff. Actual terminal marker:

PASS_D25_EXACT_PF_CUTOFF_AND_ORIGINAL_P4_UPPER_PORT

At \(p=373\), \(m=62,\ p^3=51895117,\ p^4=19356878641\):

\[
\begin{aligned}
[z^{373}]\mathcal LF_{373}&\equiv7524791965\equiv-373^3/18\pmod{373^4},\\
u_{62}&=122,\quad \bar w_{62}=0,\quad w_{62}/373\equiv122\pmod{373},\\
\nu_{62}&=43=24\cdot122^{-1}\pmod{373},\\
\Omega_{373}&=278=235+43\pmod{373},\\
\sum_{n=0}^{248}w_n&\equiv16762123164\pmod{373^4},\\
W_{373}&\equiv11832087049\pmod{373^4}.
\end{aligned}
\]

Discarding the exceptional branch loses precisely \(43\cdot373^3=2231490031\pmod{373^4}\). This is a fixed-prime exact information-loss witness, not a proof of uniform LIFT.

## BRC, P000 and continuation boundary

BRC carrier: \((p,n,6n+1,t_n,w_n,v_p(t_n),v_p(w_n),n\leftrightarrow p-n,\text{upper digit},\ell=m,\text{cutoff})\). Declared observer: original \(W_p\bmod p^4\); permitted operations are signed addition, factorial valuations, Picard–Fuchs action, and unit inversion on \(u_\ell\) only. The otherwise erased zero-weight branch is retained. These computations are external auxiliary scalar observations of the original sum, not a standalone native X6 space or a native Frobenius claim. P000 Heartbeat six-dimensional discrete Cell space and separately typed time remain unchanged.

2026-10-28 Site gateway status: research_authority_granted=false, write_relay_enabled=false. Historical #6575/#6576 receipt lookup in this Site returned CONTROL_REQUEST_NOT_FOUND (different transport namespace); no request was reissued and no current own winning Source CLAIM/run was established. Three earlier staging sources remain independent. Formal Source checkpoint, Research-Activity, review and Result need lawful future authority; status remains AUTHOR-SIDE / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / UNREVIEWED / NOT_ADMITTED.

**NEXT ORIGINAL P3 PROOF FRONTIER:** the frozen original \(p^3\) target is equivalent to the prior R9 bulk quotient versus middle/high reciprocal-sum cancellation for both \(p\equiv13,19\pmod{24}\). P1 gives a homogeneous *finite* differential equation through that precision; the next substantive step is an actual endpoint evaluation of \((1+6\theta)F_p(1)\) or a telescoping certificate, not another finite-prime scan. **HIGHEST NATIVE EVIDENCE:** existing support issue #1559 requires the authentic original \(p=373\) H0/B0 divided-power \([X]U\bmod139129\), rank, semilinear Frobenius/eta, signed odd Green/Hesse, \(\kappa\), and \(\Delta_p-R_p\), with reproducible source-bound evidence. No native executor or completed experiment is inferred. No scheduler/Actions changes or frozen Source mutation.
