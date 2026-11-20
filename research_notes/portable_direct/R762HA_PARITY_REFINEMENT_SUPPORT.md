# R762HA — Exact BRC zero-refinement support for K4-STAR moving Port

Date: 2026-11-20, Asia/Shanghai. Research task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`, frozen taskbook \`enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8\`; P000 is kept at the task's frozen scientific pin, with current behavior rules read separately. Predecessor: R762GZ, Draft PR #2856, commit \`3dd8a4b7186bada7a9ef0dca0aaec18f4d74b07a\`. Evidence class: **AUTHOR-PROVED_CANDIDATE_MODEL**; exact author-side checker **PASS** (0 through 48 events); independent review **NOT_REVIEWED**.

## Precise question, model, and observer

Maintain the declared R762GZ K4-STAR auxiliary incidence labels 0,1,2,3 and six signed native X6 axes indexed by their unordered pairs. They are not four new spatial dimensions. Start with named Port 01 and chirality +1. At each event select one of the two currently incident K4 endpoints, causing signed raw-X6 displacement \(\sigma H_v\), \(\sigma\in\{\pm1\}\), and the declared Port update. Event ordinal is separately typed. Each unsigned endpoint word has \(2^m\) *potential* independent sign refinements at length \(m\). Positive BRC multiplicity counts ordered endpoint words; signs are not negative BRC weights.

Define \(F_m\) to be the number of **unsigned ordered endpoint-choice words** of length \(m\) that (i) return to the original named Port 01 and (ii) admit *at least one* assignment of their event signs so that the **full six signed X6 Cell coordinates** return to the initial raw Cell. This is a Boolean-existence support observer over endpoint histories, not the signed-refinement multiplicity \(Z_m\) of R762GZ. All future operations in the asserted compression scope are only the fixed terminal test at the specified length; no previous-history-dependent Link gate is assumed.

## Theorem HA1: exact parity-support formula at every length

\[
\boxed{F_0=1,\qquad
F_m=\begin{cases}
2^{m-4}+2^{m/2-1},&m=6n,\ n\ge1,\\
0,&m>0,\ 6\nmid m.
\end{cases}}
\]

For \(m=6n>0\), the number of unsigned ordered endpoint words returning to Port 01, without the Cell condition, is \(2^{6n-1}\). Thus the **exact share** of Port-returning endpoint words that can be sign-refined into a complete six-axis Cell return is

\[
\boxed{\frac{F_{6n}}{2^{6n-1}}=\frac18+2^{-3n}.}
\]

Consequently the share tends to \(1/8\) with exact exponentially decaying correction; the Port-only observer cannot discard the other endpoint histories when the later target changes.

### Proof, part A — why the support criterion is parity of four inventories

For a fixed endpoint word let \(r_v\) be the count of uses of vertex \(v\). The signed net inventory is \(z_v=\sum_{j:v_j=v}\sigma_j\). Its raw six-axis displacement is \(y_{uv}=z_u+z_v\). The K4 incidence map is injective over \(\mathbb Z^4\): \(y_{01}=y_{02}=y_{12}=0\) forces \(z_0=z_1=z_2=0\), and \(y_{03}=0\) forces \(z_3=0\). Therefore the complete six-axis return is equivalent to \(z_v=0\) for every vertex. Some independent sign assignment achieves this exactly when **every** \(r_v\) is even. If a vertex occurs \(2j\) times, choosing any \(j\) plus signs suffices. The all-even condition requires \(m\) even. Named Port return requires \(m\equiv0\pmod3\), hence \(6\mid m\).

### Proof, part B — finite-character exact extraction from positive BRC words

Let \(a,b,c,d\) be the commuting occurrence markers for vertices 0,1,2,3. By R762GZ, the three-event positive transfer from the ordered matching layers is \(T=ABC\), where

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\quad
B=\begin{pmatrix}a&c\\d&b\end{pmatrix},\quad
C=\begin{pmatrix}a&d\\b&c\end{pmatrix}.
\]

For each \(k\ge0\), \(U_k=(T^k)_{00}\) is the nonnegative-integer histogram of unsigned ordered words of length \(3k\) that return to Port 01. The indicator that all four exponents of a monomial are even is

\[
\frac1{16}\sum_{\varepsilon\in\{\pm1\}^4}\varepsilon_0^{r_0}\varepsilon_1^{r_1}\varepsilon_2^{r_2}\varepsilon_3^{r_3}.
\]

By exact integer linearity,

\[
F_{3k}=\frac1{16}\sum_{\varepsilon\in\{\pm1\}^4}(T(\varepsilon)^k)_{00}.
\]

This is a formal parity-character extraction **of positive integer source counts**; the temporary evaluation \(\varepsilon_v=-1\) is not a negative-branch or physical sign amplitude.

There are exactly three disjoint cases among the 16 sign evaluations:

1. Two assignments with all signs equal: \(T(\varepsilon)=\pm4J\), where \(J\) is the \(2\times2\) all-ones matrix. For \(k\ge1\), their sum of \((0,0)\) entries is \((1+(-1)^k)8^k/2\).
2. Six assignments with two plus and two minus signs: \(T(\varepsilon)=0\).
3. Eight assignments with one sign different: direct multiplication gives \(T(\varepsilon)^2=8I\). For even \(k\), all eight contribute \(8^{k/2}\); for odd \(k\), their \((0,0)\)-entries cancel pairwise under \(\varepsilon\mapsto-\varepsilon\).

For \(k=2n\ge2\),
\[
F_{6n}=\frac{8^{2n}+8\cdot8^n}{16}
=2^{6n-4}+2^{3n-1}.
\]
For \(k\) odd, the extraction is zero. The zero-length word contributes \(F_0=1\). Finally, putting \(a=b=c=d=1\) in R762GZ yields \(2^{3k-1}\) Port-returning unsigned words for \(k\ge1\), giving the share formula. QED.

## Exact independently replicated observations

| Events m | F_m (zero-refinement-capable unsigned Port-return words) | All unsigned Port-return words | Share |
|---:|---:|---:|---|
| 6 | 8 | 32 | 1/4 |
| 12 | 288 | 2048 | 9/64 |
| 18 | 16,640 | 131,072 | 65/512 |
| 24 | 1,050,624 | 8,388,608 | 513/4096 |
| 30 | 67,125,248 | 536,870,912 | 4097/32768 |
| 36 | 4,295,098,368 | 34,359,738,368 | 32769/262144 |
| 48 | 17,592,194,433,024 | 140,737,488,355,328 | 2097153/16777216 |

The stdlib Python checker \`R762HA_CHECK.py\` independently computes the all-even endpoint inventory through **two different exact paths** for every \(k=0,1,\ldots,16\): (i) the 16-character integer Fourier sum of two-state three-block matrices and (ii) forward *positive-weight* BRC dynamic programming on (named Port position, four-bit vertex parity), one event at a time. It also verifies all 16 character evaluations partition as 2+6+8 with the claimed matrices. No floating point is used. Recorded output: \`R762HA_EVIDENCE.json\`, \`verification=PASS\`.

The R762GZ *signed-refinement counts* \(Z_6=88,\ Z_{12}=61{,}160,\ldots\) are a different observer: each endpoint word with even inventory \((r_v)\) contributes \(\prod_v\binom{r_v}{r_v/2}\) refined signed histories, rather than one. Replacing \(Z_m\) by \(F_m\) would lose multiplicity. The present new formula measures **support and exact pruning fraction**, providing a smaller parity automaton for an existential terminal test.

## P000 / native permission boundary and next question

P000 fixes the signed native six-dimensional Cell basis, PERP_E, 120-degree native orthogonality and triadic primitive stability. The K4-STAR incidence transfer and four independent event branches are still a **candidate** composite-event law. In particular, native \`TRIADIC_CLOSURE_E\` Cell/Port/Link/time gate legality and the effect of chirality, hidden Link state, past history and actual physical heartbeat duration are not established by the positive BRC calculations.

**Next discrimination:** extract one actual typed \`TRIADIC_CLOSURE_E\` admissible event predicate from frozen taskbook/P000 and compare the candidate signed branch's full (Cell, Link, Port, event time, provenance) before/after states. If legality depends on the signed history or hidden Link, retain that gate state in the BRC carrier, then repeat the parity-support extraction for the exact legal language. Separately keep the factor-nine full-vector period/lift problem open.

Task contributor provenance: \`EM-X6-3050F6\` is the prior registered research identity and \`RA-6068F717D991DF54FBBDDEED\` its associated Activity. This note does not itself assert current CLAIM, Activity association, independent review, or formal Result.