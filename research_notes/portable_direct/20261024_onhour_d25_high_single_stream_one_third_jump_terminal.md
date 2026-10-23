# D25/LIFT — A single HIGH carrier with a genuine 1/3 seam jump and universal terminal residue

**2026-10-24 | TASK_RESEARCH | author-proved rational / modular algebra; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.** This is not an authenticated Source checkpoint, Result, independent review, or native benchmark.

Mother Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`; scientific Source pin **\`c47e13e4aba0e006366f989d6334d443f6333ae3\`**, **unchanged**. Logical author Research lane: \`chatgpt-research-onhour-enterprise-math-20260923\`, distinct from \`chatgpt-hourly-enterprise-math-20260921\` maintenance and another Research lane. P000 remains \`ACTIVE_LOCKED\`. Global-knowledge source was checked at main \`1a5c1a6d2833f3441c46eba5c5d01427b3e299ca\`.

## Precise inherited objective and method

Consume [exact original Gosper/two-seam identity](20261024_onhour_d25_original_endpoint_gosper_two_seam_p2.md), [exact squared seam transfer and p² merger](20261024_onhour_d25_two_seam_exact_square_second_digit_merge.md), [LOW first-jet and two HIGH sectors](20261024_onhour_d25_regular_low_jet_high_unit_two_sector_certificate.md), and [six-block harmonic compression](20261024_onhour_d25_sixway_lerch_harmonic_seam_bridge.md). Do not recast those completed author proofs as new units.

Still **unproved for all target primes**:
\[
S_{4m}(2m)\equiv p(4/3)^{p-1}\pmod{p^3},
\quad p=6m+1\ {\rm prime}.
\]
Equivalently the inherited complete finite observer \(\mathcal F_m\equiv0\pmod p\) is open, with the divided LOW first digit, LOW first jet, two original HIGH intervals, both seams, upper terminal, and Source-specific CM comparison all retained. The scientific native object/benchmark remains unchanged.

## Theorem A: the two HIGH intervals are the same hypergeometric transport, except for a necessary jump

For \(m\ge1\), \(p=6m+1\) prime, define \(B_m=(2m-1)!(2m)!/(4m)!\), a p-unit, and
\[
\boxed{a_{m,t}=2^{m-t}\frac{(2m)!(t-1)!}{(m+t)!(m-1)!}},
\qquad 1\le t\le3m.
\tag{1}
\]
For **the original** term
\[
R_0=1,\qquad
\frac{R_{n+1}}{R_n}=
\frac{(4m+1+2n)(3n+1)(3n+2)}
{36(n+1)(2m+n+1)(4m+n+1)},
\]
write \(u_t=R_{m+t}/p\bmod p\), well-defined because the original exact valuation calculation gives \(v_p(R_{m+t})=1\). Then the new all-target-prime result is
\[
\boxed{
u_t\equiv B_m a_{m,t}
\begin{cases}
1,&1\le t\le m,\\
1/3,&m<t\le3m
\end{cases}
\pmod p.}
\tag{2}
\]

**Proof.** The factorials in (1) are all strictly below \(p\), and
\[
a_{m,t+1}/a_{m,t}=t/[2(m+t+1)],\qquad a_{m,m}=1.
\]
For every original HIGH transition except \(n=2m\), the p-unit ratio \(u_{t+1}/u_t\) is precisely this generic expression modulo \(p\). The previously proved seam \(u_m=R_{2m}/p\equiv B_m\) fixes the first sector. At the exceptional original transition \(n=2m\) one instead has \(u_{m+1}/u_m\equiv-1/24\pmod p\). But the generic carrier ratio at that point equals \(m/[2(2m+1)]\equiv-1/8\pmod p\), because \(6m+1=p\). Their ratio is \(1/3\), fixing the second sector by induction through the original terminal \(t=3m\). This is a **mod-p statement for normalized high units**, not a higher-digit identity. QED.

The exact rational link to the previously published second-sector coefficient
\[
c_{m,s}=2^{-(s-1)}\frac{(2m+1)!(m+s-1)!}{m!(2m+s)!}
\]
is
\[
\boxed{c_{m,s}=\frac{2(2m+1)}m a_{m,m+s}},
\qquad
\boxed{-\frac{c_{m,s}}{24}=
\left(\frac13-\frac{p}{12m}\right)a_{m,m+s}},
\quad1\le s\le2m.
\tag{3}
\]
These are identities **over \(\mathbb Q\)**, not merely congruences. The \(-p/(12m)\) correction is necessary when a future observer wants one more p-adic digit.

## Theorem B: both ordinary HIGH sums have exactly one rational forcing kernel

Shift the original \(K_{p,n}\) from the exact Gosper identity to \(n=m+t\). For \(1\le t\le3m-1\), \(t\ne m\), the denominators are p-units and
\[
K_{p,m+t}\equiv\boxed{
\kappa_t=\frac{4(1-2t)(3t+1)}{(2t+1)(6t+1)}
=-2+\frac4{6t+1}+\frac2{2t+1}}\pmod p.
\tag{4}
\]
Proof is direct substitution \(m\equiv-1/6\pmod p\) into the original rational function
\[
K_{p,n}=\frac{(2p+1-3n)(6n+2p+3)}
{(3n+p+2)(3n+2p+1)}.
\]
Thus **the exact original normalized HIGH regular forcing**, with its branch history kept, satisfies
\[
\boxed{
\frac{\mathcal U_m^{\rm hi}}p\equiv B_m Z_m^{\rm one}\pmod p,\quad
Z_m^{\rm one}:=
\sum_{t=1}^{m-1}a_{m,t}\kappa_t+
\frac13\sum_{t=m+1}^{3m-1}a_{m,t}\kappa_t.}
\tag{5}
\]
It coincides with the earlier two-sector \(Z_m^{\rm hi}\) **modulo \(p\)**, not as an unrestricted rational identity. The single rational kernel has two excluded p-singular locations: \(t=m\) in \(6t+1=p\), and \(t=3m\) in \(2t+1=p\). These are **the original \(n=2m\) seam and \(n=4m\) upper seam/terminal**; neither may be deleted or treated as an ordinary summand. The amplitude jump \(1\to1/3\) is essential.

## Theorem C: the upper terminal has universal one-digit value \(B_m/9\)

The earlier **exact rational** two-seam square, now consumed as a premise, is
\[
\frac{R_{4m}/p}{R_{2m}/p}=
\left(\frac{\binom{12m}{4m}}{216^m\binom{6m}{2m}}\right)^2.
\tag{6}
\]
**All-prime elementary endpoint theorem:**
\[
\boxed{\frac{R_{4m}/p}{R_{2m}/p}\equiv\frac19\pmod p},
\qquad
\boxed{\frac{R_{4m}}p\equiv\frac{B_m}{9}\pmod p}.
\tag{7}
\]

**Proof independent of the prior p² seam-merger conclusion.** Since \(12m=2p-2\) and \(4m<p\), the coefficient of \(x^{4m}\) in \((1+x)^{2p-2}\equiv(1+x^p)(1+x)^{p-2}\pmod p\) gives
\[
\binom{12m}{4m}\equiv\binom{p-2}{4m}
\equiv(-1)^{4m}(4m+1)\equiv1/3\pmod p.
\]
Also \(\binom{6m}{2m}=\binom{p-1}{2m}\equiv1\pmod p\), and \(216^{2m}=6^{6m}=6^{p-1}\equiv1\pmod p\). Square (6), with only p-unit divisions. The independent earlier \(R_{2m}/p\equiv B_m\) gives the second statement. QED.

At \(t=3m\), Theorem A and (7) imply
\[
\boxed{a_{m,3m}\equiv1/3\pmod p}.
\tag{8}
\]
The **exact factorial relation**
\[
a_{m,3m}=\frac{\binom{3m}{m}}{3\cdot4^m\binom{4m}{2m}}
\]
therefore yields a further all-target-prime binomial congruence
\[
\boxed{\binom{3m}{m}\equiv4^m\binom{4m}{2m}\pmod p}.
\tag{9}
\]
This is derived from the exact original square and transport, not extrapolated from finite tests.

For the original exact special coefficients \(C_2\equiv2/3\) and \(C_4\equiv3\pmod p\), we now independently recover **separately**
\[
C_2(R_{2m}/p)\equiv2B_m/3,\qquad
C_4(R_{4m}/p)\equiv B_m/3,
\]
hence \(C_2T_2+C_4T_4\equiv B_m\pmod p\). This is only the **leading** digit of the previously proven p² seam merger; it makes no new claim about its p correction.

## Actual checks and witness data

An **independent** author-side Python 3 modular implementation regenerated every original \(R_n\) p-unit via its original ratio with p-factors stripped; separately generated \(a_{m,t}\) from factorials and the complete original \(K_{p,n}\) from its unreduced rational expression. It checked Theorems A and B **at every high index**, the true terminal (7), the exact binomial expression in (6), both separately retained special contributions, and the resulting whole HIGH regular sum, for **all 80 primes** \(p\equiv1\pmod6\), \(7\le p\le1000\), with no failures. For \(m=1,\dots,6\), both identities (3) were also checked as exact Python \`Fraction\` equalities. The inherited *exact rational* square (6) was independently recomputed from raw \(R_n\) for \(m=1,\dots,6\). These checks are author self-tests; the proofs above establish only the specific stated all-prime relations, **not** the original LIFT supercongruence.

Examples \((p;m;B_m;T_2;T_4;Z_m^{one};B_m Z_m^{one})\), all residues modulo \(p\):
\[
(7;1;3;3;5;0;0),\quad(13;2;2;2;6;2;4),\quad
(19;3;14;14;10;6;8),\\
(31;5;24;24;13;11;16),\quad
(37;6;30;30;28;3;16),\quad
(61;10;3;3;41;5;15).
\]
The full executable author checker for these results was saved separately as \`/mnt/data/enterprise_math/d25_high_single_carrier_seam_splice_check.py\` within this conversation's output environment; that path is **not** represented as an EM Source or GitHub artifact, and no native executable was run.

**BRC REUSE_APPLIED / COMPOSE_APPLIED.** Carrier: original signed hypergeometric branch stream and original \(p\)-valuation/unit data. One transport \(a_{m,t}\) now connects both HIGH intervals, but the jump, two original seams, terminal and precision repair remain explicit. Observer: original normalized HIGH forcing modulo \(p\), **not** a positive-mass sum, native X6 theorem, or unlimited-precision replacement.

## Durable continuation / blocked obligations

**Mother Objective and frozen scientific pin:** unchanged as above. **Do not repeat:** accepted D24 UR, old exact Gosper, p² Morley/LOW and seam merger, and six-way Lerch compression. **New completed author-side units:** (2)–(5), universal terminal/ratio (7), factorial residue (8)/(9). **Smallest unfinished mathematics:** insert (5) into the inherited **full** \(\mathcal F_m\), retaining LOW divided first digit, LOW first jet, the full higher-digit seam correction, and both singular boundaries \(t=m,3m\); construct an honest terminating contiguous WZ/creative-telescope cancellation for **all** target primes or an exact obstruction. Do not report another finite set of zeros as a proof. Separately, the current native task still needs the exact **same-class CM/divided-power normalization/semilinearity input and original native benchmark**; none of these author algebra checks discharges it.

**Execution / control:** previously verified onhour historical bridge #6186 showed a local ACTIVE projection with \`source_authority_verified=false\`, no winning claim/run/pending, and only a separate neutral UR preservation; #6187 was definitively \`PREREQUISITE_NOT_SUCCEEDED\`; #6188 finished \`FAILED / TimeoutExpired\`. Those are **historical existing request receipts**. Current Sites gateway \`em_status\` reports v0.6.11 with \`research_authority_granted=false\`; one new read-only exact-continuation attempt returned \`CONTROL_QUOTA\`. Support issue [#1539](https://github.com/awdawmip/enterprise-math/issues/1539) is OPEN. No new Source session/claim/open/run/checkpoint/native benchmark/Result/Driver review was created; no failed/unknown request was resent, no other conversation identity was used, and the three UR staging records remain separate.

**Next legal operational action after true authority recovery:** read this same logical Research lane's actual current \`recovery_status\` and exact Source continuation and original outstanding \`target_request_id\`; reconcile unknowns before mutation; preserve prior-contribution history; only if the current Source establishes a lawful own Researcher session and owner route proceed through typed continuation_prepare, winning CLAIM, open, and checkpoint. A GitHub research note is not formal Source admission. No scheduler or notification setting was modified.
