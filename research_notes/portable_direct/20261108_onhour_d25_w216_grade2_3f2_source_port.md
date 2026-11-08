# D25 / Original weighted-216: explicit finite grade-two hypergeometric source port

Date: 2026-11-08 Asia/Hong_Kong. TASK_RESEARCH author-side **algebraically PROVED**, separately **exact-tested at 148 primes**, **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Stable logical Research lane `chatgpt-research-onhour-enterprise-math-20260923`; not maintenance `chatgpt-hourly-enterprise-math-20260921`. This is a distinct author-side source-port reduction, not another native H0/B0 experiment.

## Exact original object and graded question

For every prime (p=6m+1\ge7), in (\mathbb Z_{(p)}), retain the **original unchanged** index, weight and coefficient:

\[
w_n=(6n+1)\frac{(2n)!(3n)!}{(n!)^5\,216^n},\quad W_p=\sum_{n=0}^{p-1}w_n.
\]

The original coefficient valuation (e(n)=\lfloor2n/p\rfloor+\lfloor3n/p\rfloor) is exactly 2 on the index interval (N=3m+1=(p+1)/2\le n\le4m). Define the original source-typed grade-two digit

\[
T_W(p)=\frac1{p^2}\sum_{n=N}^{4m}w_n\pmod p.
\]

This quotient is defined in (\mathbb Z_{(p)}), as every summand has valuation at least two; the weight may raise individual valuations.

**Theorem (all primes (p\equiv1\bmod6)).** Define

\[
C_p=\frac{N+1}{(N!)^4\,216^N}\in\mathbb F_p^\times,\quad
K_r=\frac{(1)_r(5/6)_r(7/6)_r}{(3/2)_r^3\,2^r}\in\mathbb F_p
\quad(0\le r\le m-1).
\]

Then the **original** grade-two digit is

\[
\boxed{T_W(p)=C_p\sum_{r=0}^{m-1}(6r+4)K_r\pmod p.}\tag{1}
\]

Equivalently (K_0=1) and

\[
\boxed{K_{r+1}=K_r\,
\frac{(r+1)(6r+5)(6r+7)}{9(2r+3)^3}\pmod p}\tag{2}
\]

for (0\le r<m-1). All denominators in (1) and (2) are (p)-units in the declared ranges. This is a finite source-provenance identity, not a conjectural cross-model transform.

## Proof

Write (n=N+r), where (0\le r\le m-1). Both (2n=p+(1+2r)) and (3n=p+(N+1+3r)), with respective remainders between (0) and (p-1). Wilson's theorem implies, for (0\le a<p),

\[
\frac{(p+a)!}{p}\equiv -(a!)\pmod p.
\]

The two negative factors cancel, hence exactly

\[
\frac{w_{N+r}}{p^2}\equiv (6N+6r+1)
\frac{(1+2r)!(N+1+3r)!}{((N+r)!)^5\,216^{N+r}}\pmod p.\tag{3}
\]

The unweighted factorial fraction in (3) has initial value (C_p). Taking successive ratios and using (N\equiv1/2\pmod p) yields

\[
\frac{(2r+2)(2r+3)(N+2+3r)(N+3+3r)(N+4+3r)}
{216(N+r+1)^5}
\equiv
\frac{(r+1)(r+5/6)(r+7/6)}
{2(r+3/2)^3}\pmod p.
\]

Since (6N+1=3p+4\equiv4\pmod p), summation proves (1). The integer-friendly recurrence (2) is algebraically identical. QED.

## Consequence for the frozen mother and cross-model transfer

The (e\ge3) part of (W_p) vanishes modulo (p^3). Let (W_{<2}=\sum_{e(n)<2}w_n), preserving original (n) and grade. We have the exact theorem

\[
\boxed{W_p\equiv W_{<2}+p^2 C_p\sum_{r=0}^{m-1}(6r+4)K_r\pmod{p^3}.}\tag{4}
\]

In the frozen (p\equiv13,19\bmod24) target, the previously source-accepted first-digit congruence ensures (W_{<2}\equiv p\pmod{p^2}). The original mother (W_p\equiv p\pmod{p^3}) is therefore **equivalent** to the single explicit p-digit cancellation condition

\[
\boxed{\frac{W_{<2}-p}{p^2}
+C_p\sum_{r=0}^{m-1}(6r+4)K_r\equiv0\pmod p.}\tag{5}
\]

Equation (5) is an exact reduction of the original question, not an unconditional solution of it. Its first term retains lower-grade source information; its second is now one finite terminating ( {}_3F_2 ) derivative port in the **original** grade-two source.

The previously source-derived Guo–Zudilin **2304** grade-two tail zero is a separate **all-prime theorem**. At (p=13), our original (T_W=10\ne0) while (T_V=0), so the existing diagonal/grade-preserving transfer falsifier remains valid; any source-preserving W/V correspondence must explicitly redistribute the W port into lower-grade observations. No CM class, third native X6 coordinate, Frobenius normalization or odd Hesse port is inferred from this scalar formula.

## Executed exact certificate and next step

Independent Python verifier `research_notes/portable_direct/d25_w216_grade2_3f2_checker_20261108.py` checks (1) at **all 148 primes** (7\le p\le2000, p\equiv1\pmod6), including all **77** frozen target primes in that interval. Each check uses two independent paths: a direct original integer-binomial evaluation modulo (p^3), and the modular finite (K_r) recurrence. All 148 agree.

Exact probes `(p, N, T_W, S_p, C_p)` where (S_p=\sum(6r+4)K_r):
- (7,4,5,4,3)
- (13,7,10,1,10)
- (19,10,9,5,17)
- (37,19,20,5,4)
- (211,106,202,130,47)
- (373,187,266,217,290)

At (p=373): (217\cdot290\equiv266\bmod373). The original grade-two contribution is (266\cdot373^2\pmod{373^3}), exactly the prior independently obtained original-index tail. This directly reuses the earlier (p=373) observer and does not rerun the 1227-prime full W scan.

**Next precise portable science:** seek an explicit finite lower-grade Fricke/Cartier map whose correction coefficient is the proven (C_p S_p), first testing (p=13,19,373); if a proposed map fails, preserve its exact signed residual. Do not replace original (\Delta_p-R_p\) or the native experiment with (5).

**Highest native debt:** [#1559](https://github.com/awdawmip/enterprise-math/issues/1559), original-class (p=373) H0/B0 divided-power ([X]U\bmod139129), actual module rank, Frobenius direction/eta, signed Green/Hesse (\kappa), original (\Delta-R), raw inputs and independent replication; responsible executor pending.

**Source at 2026-11-08 04:56 UTC:** `em_status` and original `em_control_result` read both returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`. Site local diagnostic `CONFIGURED_NOT_LIVE_VERIFIED`, `research_authority_granted=false`. Original `target_request_id=onhour11-20261106-1400-exact-research-lane-continuation` preserved without resend; no native session, claim, run, freeze or Source checkpoint. Register pending, external contribution not yet formally admitted. Frozen source pins unchanged.
