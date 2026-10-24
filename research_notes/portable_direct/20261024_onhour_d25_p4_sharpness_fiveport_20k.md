# D25 / SECOND-DIGIT-LIFT — same-prime p^4 FIVE-port transport and finite exact sharpness to 20,000

2026-10-24 | author-side TASK_RESEARCH continuation: chatgpt-research-onhour-enterprise-math-20260923.
**UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.**
This is exact number-theoretic author research and locally executed finite arithmetic, **not** a native benchmark, current Source CLAIM/run/checkpoint/Result, independent review, proof of the infinite-prime p^3 target, or native CM/divided-power experiment.

Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Previously identified publication: TP2-B6F4FC938FF94941C1B7.
**Frozen scientific Source pin:** c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).
Current Research lane is distinct from CONTROL_PLANE_MAINTENANCE conversation chatgpt-hourly-enterprise-math-20260921. No other conversation's session, identity, claim or author result is reused as this lane's own.

## 1. Unmodified original target and inputs

For a prime \(p=6m+1\) in the prescribed classes \(p\bmod24\in\{13,19\}\), retain the actual original, finite hypergeometric endpoint
\[
 A_r=\frac{(6r)!}{3^{6r}((2r)!)^3},\quad R_{r,0}=1,\quad
 \frac{R_{r,n+1}}{R_{r,n}}=
 \frac{(4r+2n+1)(3n+1)(3n+2)}
 {36(n+1)(2r+n+1)(4r+n+1)},
\]
\[
 T_{r,n}=A_r(6n+12r+1)R_{r,n},\qquad
 S_r=\sum_{n=0}^{4r}T_{r,n}.
\]
The unchanged hard goal is \(S_m\equiv p(4/3)^{p-1}\pmod{p^3}\) **for every prescribed prime**, along with a distinct same-class CM/divided-power comparison and Source-fixed native benchmark. None of those outstanding universal/native obligations is discharged by this note.

The inherited, precisely scoped author results used without claiming new credit are the exact full-rank WZ identity and its original FIVE tail sources (c7fb90fd7ec451a954b553b963dd85d4ec99fc96), and the fixed-prime p^3 five-port source-faithful reduction (7724e73f2d15c92ce98520e6a55b8231d737fa03). The 575-prime p^3 scan at c6ba00a05c04ef0bbf1fae4a2ec4a4df4aa06ca0 supplies a previously verified bounded domain; its finite result is not assumed as an infinite theorem.

## 2. Theorem A — p-free factorial cubic harmonic jet (exact mod p^4)

For a prime \(p\ge5\) and \(0\le t<2p\), let
\[
 U_p(t)=\prod_{\substack{1\le a\le t\\p\nmid a}}a,\quad
 H_s^{(j)}=\sum_{a=1}^{s}a^{-j},\quad H_s=H_s^{(1)}.
\]
All harmonic denominators here are p-units. When \(t<p\), \(U_p(t)=t!\). For \(t=p+s\), \(0\le s<p\), the following is **a proved universal identity in \(\mathbb Z_{(p)}/p^4\)**:
\[
\boxed{
U_p(p+s)\equiv(p-1)!\,s!\left[
1+pH_s+\frac{p^2}{2}(H_s^2-H_s^{(2)})
+\frac{p^3}{6}\bigl(H_s^3-3H_sH_s^{(2)}+2H_s^{(3)}\bigr)
\right]\pmod{p^4}. }\tag{A}
\]
Proof: divide \(\prod_{a=1}^{s}(p+a)\) by \(s!\) to obtain \(\prod_{a=1}^{s}(1+p/a)\); its elementary symmetric polynomials of degrees 1, 2, 3 are exactly the three displayed harmonic expressions. Terms of degree at least 4 vanish modulo \(p^4\). The factor \((p-1)!\) remains an actual p-adic unit; **no substitution of \(-1\) for it modulo \(p^2\) or higher is made**.

From the exact original ratio, for any \(r,n\) within the factorial range below \(2p\),
\[
A_rR_{r,n}=
\frac{(6r)!(4r+2n)!(3n)!}
{3^{6r}(2r)!216^n(n!)^2((2r+n)!)^2(4r+n)!}.
\tag{F}
\]
Its p-adic valuation is the integer
\[
e_p(r,n)=
\left\lfloor\frac{6r}p\right\rfloor+
\left\lfloor\frac{4r+2n}p\right\rfloor+
\left\lfloor\frac{3n}p\right\rfloor-
\left\lfloor\frac{2r}p\right\rfloor-
2\left\lfloor\frac np\right\rfloor-
2\left\lfloor\frac{2r+n}p\right\rfloor-
\left\lfloor\frac{4r+n}p\right\rfloor.
\tag{V}
\]
Thus (F) has the **exact decomposition** \(A_rR_{r,n}=p^{e_p(r,n)}V_p(r,n)\), where
\[
V_p(r,n)=
\frac{U_p(6r)U_p(4r+2n)U_p(3n)}
{3^{6r}U_p(2r)216^nU_p(n)^2U_p(2r+n)^2U_p(4r+n)}
\in\mathbb Z_{(p)}^\times.
\tag{U}
\]
Here the complete factorization, including the p-power, is exact as a rational equality; (A) supplies the bounded precision jets.

## 3. Theorem B — full same-prime p^4 five-port transport

Let \(p=6m+1\) be **any prime** with \(m\ge2\), \(\ell=\lceil m/2\rceil\) and \(\ell\le k\le m-1\). Use the original WZ five sources:
\[
E_0(k)=T_{k,4k+1}g(k,4k+1),\quad
E_j(k)=T_{k+1,4k+j}\;(j=1,2,3,4),
\]
with the inherited exact identity \(S_{k+1}-S_k=\sum_{j=0}^4E_j(k)\) and exact WZ boundary factorization
\[
(6(4k+1)+12k+1)g(k,4k+1)
=\frac{2(3k+1)(360k^2+274k+49)}{3(2k+1)(8k+3)}.
\tag{G}
\]
Define \(N=4k+1\), \(q=8k+3\), \(\epsilon={\bf1}_{q=p}\), \(q^\star=q/p^\epsilon\), \(Q=360k^2+274k+49\). For each port, every factorial argument in (F) is less than \(2p\), the two numerator factorials contribute one p each, and the only possible denominator-factorial p is in \((4r+n)!\). In particular
\[
e_p(r,n)=2-{\bf1}_{4r+n\ge p}
\quad\text{at each of the five original ports.}
\tag{E}
\]
The exceptional case \(8k+3=p\) occurs only when the old port's factorial exponent equals 2, making its total normalized exponent nonnegative.

Define explicit, individually p-integral normalized ports modulo \(p^3\):
\[
\boxed{
d^{(3)}_{p,k,0}=
p^{e_p(k,N)-1-\epsilon}V_p(k,N)
\frac{2(3k+1)Q}{3(2k+1)q^\star}
\pmod{p^3}, }\tag{P0}
\]
\[
\boxed{
d^{(3)}_{p,k,j}=
p^{e_p(k+1,4k+j)-1}V_p(k+1,4k+j)
(36k+6j+13)
\pmod{p^3},\quad1\le j\le4. }\tag{Pj}
\]
All denominators are p-units **after the explicit resonance cancellation**. The normalization uses at most quadratic harmonic jet terms from (A) modulo \(p^3\); the full seed \(S_\ell\bmod p^4\) may require the cubic terms.

Then the all-primes algebraic transport identity is
\[
\boxed{
S_m\equiv S_\ell+
p\sum_{k=\ell}^{m-1}\sum_{j=0}^{4}d^{(3)}_{p,k,j}
\pmod{p^4}.
}\tag{T4}
\]
Proof: Substitute the exact p-valuation-separated factorial ratios (F),(E) and the original boundary factorization (G) into the exact WZ FIVE identity; divide only individually proved p-integral ports by p. Sum over the same fixed prime \(p\) and ranks \(k=\ell,\dots,m-1\); reduce each \(E_j/p\) modulo \(p^3\). No cross-prime induction, inexact cancellation, p-inverse, changed terminal, or replacement of the original \(1/3\) jump is involved. This is an **exact algebraic derivation conditional only on the explicitly inherited WZ identity**, not independent Source admission of that upstream identity.

The NEW precision is one entire p-adic digit beyond the inherited p^3 transport. It lets the first omitted-prime-power coefficient be tracked by the five source-labeled WZ ports:
\[
\delta_p=\frac{S_m-p(4/3)^{p-1}}{p^3}\pmod p
\quad\text{whenever the numerator is p^3-divisible.}\tag{D}
\]
The bounded computation below verifies that divisibility for its exact finite set. For an arbitrary unverified prime, (D) is **not** used to assume the p^3 hard target.

## 4. Exact bounded result — 575 primes, every one sharply p^3

Both prescribed classes were exhaustively enumerated by a deterministic prime sieve up to \(20{,}000\):
288 primes \(p\equiv13\pmod{24}\); 287 primes \(p\equiv19\pmod{24}\). All 575 satisfy
\[
S_m\equiv p(4/3)^{p-1}\pmod{p^3}
\quad\text{and}\quad
\boxed{v_p(S_m-p(4/3)^{p-1})=3.}
\]
**No prime in this finite domain lifted to the stronger mod-\(p^4\) congruence.** This last sentence is *not* a theorem about all primes; absence of p^4 exceptions beyond 20,000 is unverified and not inferred. Representative exact \(\delta_p\bmod p\):
\[
\begin{array}{c|rrrrrr}
p&13&19&37&211&307&19963\\
\hline
\delta_p&12&8&19&89&1&7079
\end{array}
\]
The calculation includes every original \(n=0,\ldots,4m\), with the LOW \(0\le n\le m\) and HIGH \(m+1\le n\le4m\) provenance retained separately. For the full-rank original target, \(v_p(T_{m,n})=0\) in LOW and exactly 1 in HIGH; this previously proved valuation pattern was rechecked termwise in the independently stripped recurrence stream.

**One fully labeled five-port example:** \(p=211,m=35,\ell=18\), all residues modulo \(211^4=1{,}982{,}119{,}441\):
\[
S_{18}=406{,}877{,}630,\qquad
\sum_{k=18}^{34}(E_0,\ldots,E_4)/211
=(1037902,4143323,1187428,3526623,3355735)
\pmod{211^3}.
\]
The five totals sum to \(3{,}857{,}080\pmod{211^3}\), whence (T4) gives
\[
S_{35}=406877630+211(3857080)
=1220721510\pmod{211^4}.
\]
The unchanged right side is \(211(4/3)^{210}=384661651\pmod{211^4}\); their difference is \(89\cdot211^3\). This independently reproduces the older single-prime sharpness witness rather than re-crediting it.

## 5. Actual execution, independent paths, and reproducibility

Published source files in this directory:
- 20261024_onhour_d25_p4_precision_boundary_scan.py — factorial p-free exact original endpoint, independent stripped *original recurrence* at p^4, complete prescribed-class prime sieve, LOW/HIGH labels and CSV option.
- 20261024_onhour_d25_p4_fiveport_same_prime_transport_check.py — independently computes original seed, all FIVE source-labeled normalized ports, exact same-prime p^4 reconstruction, and direct endpoint comparison.

**Executed:** the first checker on all 575 prescribed primes through 20,000; factorial path and independently stripped original recurrence agree on **575/575 p^4 original endpoints**; all 575 p^3 hard targets hold and all 575 \(\delta_p\) are nonzero. The second checker independently reconstructs all five WZ ports and the complete endpoint for **575/575 primes** at p^4; for each prime it also recalculates the full original rank endpoint. The first checker was additionally projected back to and matched **all 575 rows** of the predecessor p^3 CSV. The cubic harmonic jet (A) was separately compared to direct p-free products for **eight** representative primes including \(p=19963\). All listed checks passed.

Run from this directory:
    python 20261024_onhour_d25_p4_precision_boundary_scan.py --limit 20000 --out d25_p4_20000.csv
    python 20261024_onhour_d25_p4_fiveport_same_prime_transport_check.py --limit 20000

The complete locally generated CSV contains 575 rows; its SHA-256 is
cfc287a39a849be924ac48234bc703cc0a23d5d4d1a968ef0c02ea870f64c2ef.
The CSV is a regenerable arithmetic artifact, not Source checkpoint evidence or an admitted benchmark. These are author-side exact integer modular computations, not independent reviewer evidence. All arithmetic avoids inversion of multiples of p. No native experiment was executed.

**BRC COMPOSE_APPLIED**: use a signed, labeled port/valuation/unit jet carrier \((p,k,j,v_p,\text{p-free unit mod }p^3,\text{source identity})\). The declared future operations are five-port composition, fixed-p rank transport and final reduction modulo \(p^4\). The old mod-\(p^3\) scalar observer is *not* sufficient to recover the next digit \(\delta_p\); the additional jet and port provenance repair that loss. No positive BRC mass is treated as signed cancellation, and this number-theoretic auxiliary representation is not promoted into P000 native X6 dynamics or a Heartbeat benchmark.

## 6. Exact handoff / outstanding obligations

Mother target still **OPEN**. Highest author-durable frontier is (A), (T4), the complete 575-prime original p^4 sharpness table and the two executed checkers. Reuse without redoing the exact full-rank WZ, existing LOW Jacobi third-digit seed, previous FIVE p^3 transport, and predecessor p^3 scan. The next minimal **proof-bearing** unit is an **infinite-prime** identity linking the full same-class LOW seed jet and five-port sum to the source-fixed CM/divided-power normalized target modulo \(p^2\); (T4) provides an extra precision observer for falsifying unsuitable normalizations, but is not itself that bridge.

Native benchmark: **NOT RUN**, original objects, host, conditions, expected receipt and verification remain independent; the executed modular Python checkers do not count as native benchmark. Legitimate Source Researcher execution is likewise still unavailable to the presently verified Sites identity: static read-only scopes; research_authority_granted=false; executor_binding_configured=false. Existing support path is enterprise-math#1539 for the failed session-start/recovery and exact D25 continuation. Native benchmark actual executor: **NATIVE_EXECUTOR_UNASSIGNED** until verified otherwise; accepting path requires a real owned Source session/CLAIM/open plus native benchmark run and inspected native receipt under the frozen input, followed by independent Driver review. No new unowned control request, maintenance-lane session, or fake CLAIM was created.

**Author delivery only:** UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT, even after GitHub storage. Preserve old UR staging as a distinct source; do not merge it into D25. Frozen Source pin, original task, model premises, timer frequency/phase, enabled state and notification behavior are untouched.
