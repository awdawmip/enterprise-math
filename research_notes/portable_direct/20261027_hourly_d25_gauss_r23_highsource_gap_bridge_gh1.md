# D25/LIFT GH-1 — Clausen–R23 high-W source bridge and finite terminal gap

Date 2026-10-27 (Asia/Hong_Kong). Author: independent TASK_RESEARCH hourly logical lane chatgpt-research-hourly-enterprise-math-20260923, *not* on-hour Research or CONTROL_PLANE_MAINTENANCE. Parent D25/LIFT/JT2 OPEN; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.**

**Evidence tier:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is *not* a Source-native CLAIM, run, checkpoint, Result, H0/B0/Frobenius computation or a proof of the W/S full supercongruence.

## Consumed and separately credited prior facts

- The hourly lane's R23, research_notes/portable_direct/20261027_hourly_d25_half_tail_r23.md, established the **genuine reflected factorial W-high source** \(U_p\), the distinct S-high ports and the original fixed-input reduction \(W_p-S_p\equiv L_p+p^2U_p\pmod{p^3}\). R23 did **not** prove the final compensation.
- The separate on-hour Research lane's research_notes/portable_direct/20261027_onhour_d25_original216_clausen_p3_boundary_five_observer_certificate.md established exact Clausen convolution and a cutoff-sensitive *five-observer* certificate (conditional on the already accepted CM0 root and first digit). This note does not take credit for Clausen or those observations.
- R47–R55 and the independent SB boundary analyses are retained with their original proof scopes and authors. No arbitrary rational Green observer is identified with an original six-channel native PF/Hasse carrier without a proved typed map.

## Exact carriers and three valuation bands

Let \(p=6m+1\ge7\) be prime, and for \(0\le n<p\) preserve the original W and S labels:

\[
 w_n=(6n+1)q_n,\quad q_n=\frac{(2n)!(3n)!}{(n!)^5 216^n},
 \qquad s_n=\frac{(8n+1)(4n)!}{(n!)^4 2304^n}.
\]

Use the **auxiliary Gauss carrier**, not a native six-dimensional Enterprise coordinate,

\[
t_k=\frac{(1/6)_k(1/3)_k}{(k!)^2 2^k},
\quad \frac{t_{k+1}}{t_k}=\frac{(6k+1)(3k+1)}{36(k+1)^2},
\qquad
q_n=\sum_{i+j=n}t_it_j.
\tag{1}
\]

The last identity is the consumed **exact** Clausen coefficient identity. Since \(p\mid(6m+1)\) and \(p\mid(3(2m)+1)\), with denominators units at each \(k<p\), the **exact** valuations of \(t_k\) are 0, 1, 2 on respectively \([0,m]\), \([m+1,2m]\), \([2m+1,p-1]\). Define labelled finite-field residues

\[
 \alpha_j=t_j\bmod p\;(0\le j\le m),\quad
 \beta_i=t_i/p\bmod p\;(m<i\le2m),\quad
 \gamma_k=t_k/p^2\bmod p\;(2m<k<p).
\tag{2}
\]

All are nonzero in \(\mathbf F_p\); they are independently attributable ordered-pair sources.

## GH-1A: per-degree high W bridge and upper gap

For every \(3m<n<p\), define

\[
 M_n=\sum_{\substack{i+j=n\\m<i,j\le2m}}\beta_i\beta_j,\qquad
 B_n=\sum_{\substack{j+k=n\\0\le j\le m,\,2m<k<p}}
             \alpha_j\gamma_k .
\tag{3}
\]

**All-prime source-preserving theorem:**

\[
\boxed{\frac{w_n}{p^2}\equiv(6n+1)(M_n+2B_n)\pmod p.}
\tag{GH.1}
\]

For \(4m<n<p\), a stronger *unweighted* coefficient gap holds,

\[
\boxed{M_n=B_n=0\pmod p,\qquad
[z^n]\Big(\sum_{j=0}^{m}\alpha_jz^j\Big)
      \Big(\sum_{k=2m+1}^{p-1}\gamma_kz^k\Big)=0.}
\tag{GH.2}
\]

This yields the exact finite-index annihilator

\[
\boxed{\gamma_n=-\sum_{j=1}^m\alpha_j\gamma_{n-j}\pmod p,
       \qquad4m+1\le n\le p-1.}
\tag{GH.3}
\]

**Proof.** Since \(n<p\), Legendre gives \(v_p(q_n)=\lfloor2n/p\rfloor+\lfloor3n/p\rfloor\), equal to 2 on \(3m<n\le4m\) and 3 on \(4m<n<p\). In the *exact coefficient* convolution (1), pairs low–low have degree at most \(2m\), low–middle at most \(3m\), middle–high valuation at least 3, and high–high at least 4. At degrees \(n>3m\) **only** the ordered middle–middle and the two ordered low–high orientations can survive after dividing by \(p^2\). This proves GH.1. Above \(4m\) middle–middle pairs are impossible; the unchanged factorial coefficient has valuation 3 and \(2(6n+1)\) is a \(p\)-unit, proving \(B_n=0\), and hence GH.2. Because \(\alpha_0=1\) and all \(n-j>2m\) in the stated terminal window, solving the coefficient gap for \(\gamma_n\) gives GH.3. The nonzero *individual* low–high residues cancel collectively; they are **not** individually removable. QED.

## GH-1B: original reflected W source equals two Gauss ports

Define separately

\[
G_{MM}=\sum_{n=3m+1}^{4m}(6n+1)M_n,\qquad
G_{LH}=2\sum_{n=3m+1}^{4m}(6n+1)B_n.
\tag{4}
\]

The **original** R23 reflected W-high source, distinct from the R23 S-only tail quantities, is

\[
U_p=\sum_{j=2m}^{3m-1}
 \frac{(6j+5)216^j(j!)^5}
 {(2j+1)!(3j-6m+1)!}\pmod p.
\tag{5}
\]

Summing GH.1 exactly over \(3m<n\le4m\), then applying the **previously established R23 factorial reflection** \(w_{p-1-j}/p^2\equiv A_j\), proves the **new cross-carrier source-port intertwiner**

\[
\boxed{U_p=G_{MM}+G_{LH}\pmod p.}
\tag{GH.4}
\]

This is a finite, unchanged-original-input equality of **two distinct Gauss ports to one declared W-high observer**, not a termwise W/S map or the final low-half WZ compensation. QED.

## GH-1C: cutoff-sensitive identification with the other lane's five-observer tail

Set

\[
A=\sum_{j\le m}\alpha_j,\quad J=\sum_{j\le m}j\alpha_j,\quad
C=\sum_{k>2m}\gamma_k,\quad C_1=\sum_{k>2m}k\gamma_k,
\]

\[
H=\sum_{\substack{k>2m,\,0\le j\le m\\k+j\ge p}}
(6(k+j)+1)\gamma_k\alpha_j,\quad
G_{LH}^{low}=2\sum_{n=2m+1}^{3m}(6n+1)B_n .
\tag{6}
\]

**Cutoff-preserving theorem, all \(p=6m+1\ge7\):**

\[
\boxed{
2\{AC+6(JC+AC_1)-H\}=G_{LH}^{low}+G_{LH}\pmod p.}
\tag{GH.5}
\]

**Proof.** In the rectangular ordered low–high product, expand \(6(j+k)+1\) into \(1+6j+6k\). The full rectangular product has value \(2\{AC+6(JC+AC_1)\}\). Restricting the authentic degree to \(j+k<p\) subtracts **exactly** the signed weighted upper-cutoff set \(2H\); it is not licensed to be dropped. Group remaining pairs by \(n=j+k\). Terms \(n\in[2m+1,3m]\) yield \(G_{LH}^{low}\), terms \(n\in[3m+1,4m]\) yield \(G_{LH}\), and terms \(4m<n<p\) vanish **only after the whole degree coefficient is summed**, by GH.2. QED.

For the frozen CM0 target \(p\equiv13,19\pmod{24}\), the prior **accepted** CM0 input gives \(A=0\) modulo \(p\); hence the exact on-hour five-observer boundary/tail coordinate admits the source-refined split

\[
\boxed{12JC-2H=G_{LH}^{low}+G_{LH}\pmod p.}
\tag{GH.6}
\]

Here \(J,C,H\) correspond to the already existing on-hour \(j,c,h\) *after their stated \(p^2\) divisions*, not to arbitrary nonnative operators. GH.4 and GH.6 are **necessary carrier compatibility** identities, **not** a proof that the on-hour five-observer obstruction vanishes for all primes.

## Actual executed exact checks and residuals

The companion Python 3 standard-library checker 20261027_hourly_d25_gauss_r23_highsource_gap_bridge_gh1_check.py was executed on **all 80** primes \(7\le p<1000,\ p\equiv1\pmod6\). It compared 6,098 \(p^2\)-divided original factorial ranks against GH.1 using a separate factorial-unit implementation; checked 12,196 terminal coefficient-gap and recurrence instances; independently recomputed (5); checked GH.4 and cutoff-sensitive GH.5 for every prime; and checked CM0-specialized GH.6 only for primes in its frozen residue classes. **PASS**. These are author exact tests, not independent review, Lean or native H0/B0.

Selected certificates (all residues modulo \(p\)):

| \(p\) | \(G_{MM}\) | \(G_{LH}\) | R23 \(U_p\) | \(G_{LH}^{low}\) | full cutoff LH |
|---:|---:|---:|---:|---:|---:|
| 13 | 12 | 11 | 10 | 11 | 9 |
| 19 | 3 | 6 | 9 | 7 | 13 |
| 139 | 97 | 55 | 13 | 120 | 36 |
| 181 | 111 | 41 | 152 | 1 | 42 |
| 199 | 190 | 181 | 172 | 67 | 49 |
| 277 | 188 | 99 | 10 | 187 | 9 |
| 373 | 213 | 53 | 266 | 321 | 1 |

At \(p=373\), \(J=294,C=252,H=98\) give \(12JC-2H=1\), matching the separate on-hour certificate; \(G_{MM}+G_{LH}=213+53=266=U_{373}\). Both ports are nonzero, so either one-port deletion is falsified. At \(p=199\), which is *outside* CM0's frozen residue classes, the measured \(A=14\ne0\): GH.5 remains true but GH.6 **must not** be imposed.

**BRC COMPOSE_APPLIED:** carrier is the ordered labelled Gauss-factor pair with exact finite valuation bands and signed \(\mathbf F_p\) residues; observer is p-adic-divided W-high sum, genuine truncation and weighted moment; future allowed operations are degreewise finite convolution, R23 reflection and five-observer readout. The aggregate degree-gap is not termwise source deletion. No invented P000 axiom, native X6 embedding, unauthorized independent reviewer or fixed source-pin change occurs.

## Frontier and exact next action

**GH-1 proof/author verification complete as portable evidence, unreviewed and not admitted.** Preserve earlier R23, on-hour Clausen, R47–R55 and SB results under their existing credit; do not redo them.

Next nonduplicative mathematical unit: construct or falsify an **S-sourced and actual PF/Hasse-compatible** finite intertwiner that connects the existing separately labelled Guo–Zudilin S high/low cancellation to GH.4–GH.6 and to the original R36 integral PF Green *without identifying the different source carriers by fiat*. Retain both finite endpoints, positive-direction infinity, all six original fixed \(z=2\) Hasse J/E labels, authentic \(\eta/\kappa\), and \(p=139,181,199,277,373\) exceptional witnesses. The still-open identity \(L_p/p^2+U_p=0\pmod p\), original H0/B0 divided-power module, \([X]U\bmod p^2\), native \(p=373\) experiment and independent Driver review are **not** discharged.

Ordinary-control current connector is read-only for this subject (no winning Claim/open/run verified). Existing exact recovery #6622 and continuation #6623 in awdawmip/kimi-query-bridge are own-session read evidence, not authorization. The longstanding predecessor conflict remains awdawmip/enterprise-math#1558; preserve old session, sixteen prior contributions, original request IDs and two neutral staging manifests. Current new Research-Activity semantic event: **REGISTER_PENDING** until an actual approved role-bound write and Source readback.
