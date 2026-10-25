# D25/LIFT — corrected Clausen-parameter jets recover the signed reflected cutoff through p^4

Date: 2026-10-26. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).

**Status:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is external finite hypergeometric algebra, not a CM experiment, native X6 transfer, winning Source CLAIM, authorized run, native checkpoint, or proof of the complete all-prime LIFT target.

## Exact mathematical input and non-duplicate question

The *Clausen-compatible* parameter family already established in the source is

\[
\widetilde b_n(x)=\frac{(-x)_n(-2x)_n}{(\frac12-3x)_n\,n!},\qquad
p=6m+1\ge7 \text{ prime},\quad x_0=-\frac16=m-\frac p6.
\]

Write \(u_{k,n}=[t^k]\widetilde b_n(m+t)\) and define the original coefficients and original **ordered, signed** cutoff

\[
r_n=\frac{(1/6)_n(1/3)_n}{2^n(n!)^2}
=2^{-n}\widetilde b_n(x_0),\qquad
Q_p=\sum_{\substack{0\le a,b<p\\a+b\ge p}}(6(a+b)+1)r_ar_b.
\]

The prior corrected-family work proved a rank/Hasse differential recurrence. The older reflected-corner jet result provided the leading \(Q_p/p^2\bmod p\), and a separate higher precision tail calculation used a fixed-denominator representation. The unresolved *new* subunit is a \(p^4\) transport of the **corrected Clausen parameter jets** to the original signed cutoff, including all relevant source ranks.

All denominators of \(\widetilde b_n(m+t)\) for \(n<p\) are \(p\)-units, so the following jets and congruences are in \(\mathbb Z_{(p)}\).

## Theorem: full two-digit corrected-jet reflection formula

For \(1\le j\le2m\) and \(1\le \ell\le j\) put \(\alpha_{j,\ell}=6(j-\ell)+1\). Then \(Q_p\in p^2\mathbb Z_{(p)}\) and for **every** prime \(p\equiv1\bmod6\),

\[
\boxed{\begin{aligned}
\frac{Q_p}{p^2}\equiv\frac1{18}
\sum_{j=1}^{2m}\sum_{\ell=1}^{j}2^{-(j+p-\ell)}
\Big[&\alpha_{j,\ell}u_{0,j}u_{2,p-\ell}\\
+ p\big(&6u_{0,j}u_{2,p-\ell}
-\tfrac{\alpha_{j,\ell}}6(u_{1,j}u_{2,p-\ell}+u_{0,j}u_{3,p-\ell})\big)\Big]
\pmod{p^2}.
\end{aligned}}\tag{1}
\]

In particular the middle-rank contribution (\(m<j\le2m\)) is the explicitly retained and potentially nonzero next-digit port

\[
\boxed{\left(\frac{Q_p}{p^2}\right)_{\mathrm{middle}}
\equiv-\frac p{108}\sum_{j=m+1}^{2m}\sum_{\ell=1}^{j}
\alpha_{j,\ell}2^{-(j+p-\ell)}u_{1,j}u_{2,p-\ell}\pmod{p^2}.}\tag{2}
\]

Equation (2) is necessarily zero modulo \(p\), but is **not** identically zero modulo \(p^2\). No claim of universal nonvanishing is made. Corrected denominator, Taylor order, rank, sign and evaluation modulus are material components of the source.

### Complete proof

1. The numerator factors \((-m-t)_n\) and \((-2m-2t)_n\) give one zero in \(t\) for \(n>m\) and two for \(n>2m\), while the corrected denominator remains invertible. Thus \(u_{0,j}=0\) for \(j>m\), and \(u_{0,n}=u_{1,n}=0\) for \(n>2m\). Taylor evaluation at the **exact** source parameter \(x_0=m-p/6\) gives
\[
r_j\equiv2^{-j}(u_{0,j}-\tfrac p6u_{1,j})\pmod{p^2}\quad(1\le j\le2m),
\]
\[
r_n\equiv2^{-n}(\tfrac{p^2}{36}u_{2,n}-\tfrac{p^3}{216}u_{3,n})\pmod{p^4}\quad(2m<n<p).
\]
Both have valid \(p\)-local Taylor remainders.

2. Two ranks \(\le2m\) have sum \(\le4m<p\), so they do not occur in the cutoff. Two ranks \(>2m\) have coefficient product divisible by \(p^4\), hence vanish at the declared precision. The only surviving pairs have one rank \(1\le j\le2m\) and a high rank \(n=p-\ell\) with \(1\le\ell\le j\); indeed \(n\ge p-2m=4m+1>2m\). The original **ordered** convolution has two such permutations, giving a factor 2.

3. For each surviving pair the exact signed weight is \(6(j+p-\ell)+1=\alpha_{j,\ell}+6p\). Substitute the two displayed Taylor expressions, discard only terms of valuation \(\ge4\) before division by \(p^2\), and retain both permutations. The leading coefficient becomes \(2/36=1/18\). The \(p^3\) terms are respectively the weight correction \(6p\), first low/middle jet \(u_{1,j}\), and third high jet \(u_{3,p-\ell}\). This gives exactly (1). For \(m<j\le2m\), \(u_{0,j}=0\), yielding (2). QED.

## Independent exact author checks and information-loss witness

The companion Python-stdlib verifier constructs original \(r_n\) by a direct original-source hypergeometric recurrence modulo \(p^4\), computes the **full ordered** signed cutoff, and independently constructs \(u_{0..3,n}\) by the corrected rational polynomial-quotient recurrence modulo \(p^2\). It checks (1), low/middle source splitting, and p-divisibility of the middle contribution, with no floating point or CM substitute.

All **22** primes \(p\equiv1\bmod6\) in \(7\le p\le211\) passed.

| p | Q_p/p² mod p² | low j<=m | middle m<j<=2m |
|---:|---:|---:|---:|
| 7 | 38 | 10 | 28 |
| 13 | 104 | 78 | 26 |
| 19 | 221 | 183 | 38 |
| 31 | 225 | 907 | 279 |
| 37 | 1084 | 973 | 111 |
| 43 | 1563 | 1348 | 215 |

For p=13, the corrected middle port is \(26=2p\) and the low port is \(78=6p\); their sum is the known scalar \(Q_{13}/p^2\equiv104=8p\bmod p^2\), now recovered with **distinct corrected-parameter sources**. In particular, projection to \(Q_p/p^2\bmod p\) loses a genuinely relevant \(p^3\) rank-one contribution.

## Consumed references, provenance, and precise next action

- Corrected family and denominator drift: research_notes/portable_direct/20261025_hourly_d25_clausen_denominator_drift_source_port.md, commit 5897ddc49f22fe2480961cd0fb5c5fdd47ff54de.
- Corrected rank/Hasse operator and rank-one boundary-only obstruction: research_notes/portable_direct/20261025_hourly_d25_clausen_operator_rank_boundary.md, commit 0b796436836dfeb487836389bfc831edf9a5f6e2.
- Earlier **fixed-denominator** p^4 tail construction, not re-credited as this corrected jet theorem: research_notes/portable_direct/20261025_hourly_d25_clausen_p4_reflected_corner_jet.md, commit 7b37a8cfe8e90de8ab753335625087e1a9490076.

BRC interface resolution: **COMPOSE_APPLIED** for exact rank/valuation/ordered-sign/parameter-family/Hasse-jet carriers and their downstream observer precision. No actual native BRC or original-class CM operation was run and no native X6 correspondence is inferred.

Next smallest mathematical unit: combine the exact corrected rank/Hasse operator with the just-derived low/middle/high weighted sum at \(z=1/2\), looking for a **non-tautological signed adjoint/telescoping certificate** for the still-unproved \(B_{01,p}+A_2H_0/72-T_{\rm jet,p}=0\bmod p\). Do not discard the \(p^3\) intermediate rank or change to the fixed-denominator operator. The original CM \(H_0/B_0,[X]U\bmod p^2\), Frobenius direction/normalization and \(\kappa\) mapping remain unavailable; native CM experiment NOT_RUN. D25/LIFT/JT2 parent **OPEN**.

Control read during this execution: one fresh direct `em_control_continuation` attempt returned `INVALID_ARGUMENT / CONTROL_QUOTA`. No new winning native CLAIM/authorized OPEN/Source checkpoint. The historic predecessor-CLAIM conflict is tracked under Enterprise Math issue #1558 and is not presumed repaired. Neither the separate maintenance identity nor a new scheduler was used. Portable GitHub publication is evidence storage, not predecessor completed research, native checkpoint or independent mathematical acceptance.
