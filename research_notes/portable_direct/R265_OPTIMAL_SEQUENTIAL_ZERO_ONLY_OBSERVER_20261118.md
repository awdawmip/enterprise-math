# R265 — exact optimal sequential zero-only observer over a full 2184-event period

Date: 2026-11-18 (Asia/Shanghai). Research status: **AUTHOR_PROVED / EXACT_FINITE_VERIFICATION / NOT_REVIEWED**.

## Frozen scientific input and problem

This is an independent portable-research continuation of R262–R264 using the existing auxiliary **63-mask positive-rational scalar model**, with frozen science pin \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Fix \(s=67/169\), \(J=1184397599\), \(T=989553240\), \(K=3805974000\), \(p=13\), and integer-normalized labelled sequences

\[
q_{m,k}=\frac{JT^k}{K}h_{m,k}\quad(0\le m<63,\;k\ge3).
\]

A **sequential Boolean zero-only observer** receives an unknown event position \(k\), can query \([q_{m,k}\not\equiv0\pmod {13}]\) for an original named mask \(m\), may stop as soon as any query is nonzero (certifying that not all 63 masks vanish), and must correctly output the all-63 simultaneous-zero predicate on every \(k\ge3\). It may stop and return all-zero only after its queried zero labels logically force that conclusion. It cannot inspect \(k\bmod2184\) directly or obtain unqueried scalar values. Cost is **number of original-label Boolean probes**; probability model is uniform over \(2184\) consecutive events. No preprocessing cost claim is made for choosing the order.

## Theorem

The 63 exact labelled sequences are periodic modulo 13 with period dividing 2184. Exactly **39 masks are identically zero** and the other **24 masks fall into six distinct nonzero-event support profiles**, with these original-label equivalence classes:

| Profile representative | Identical-support original labels | Nonzero event count |
|---|---|---:|
| 9 | 9,14,27,29,41,46,59,61 | 2028 |
| 10 | 10,25,30,42,57,62 | 1820 |
| 12 | 12,15,44,47 | 1872 |
| 13 | 13,45 | 1638 |
| 24 | 24,56 | 1456 |
| 26 | 26,58 | 2016 |

The union of all nonzero-event supports contains **2182** of 2184 events; the remaining two are the known simultaneous-zero events. The smallest valid fixed, nonadaptive set of original labels has cardinality 4 (matching R262), with **384 valid four-label sets**.

Among *all deterministic adaptive sequential zero-only algorithms* in the specified probe model, an optimal strategy is to query, in order,

\[
\boxed{9\longrightarrow26\longrightarrow10\longrightarrow13,}
\]

stopping at the first nonzero read, or returning all-zero after all four are zero. Its total reads on one uniform period are

\[
\boxed{2184+156+12+4=2356},
\qquad
\boxed{\mathbb{E}[\mathrm{reads}]=\frac{2356}{2184}=\frac{589}{546}.}
\]

This is the exact global optimum in the stated observer model. In comparison, early stopping with the previous valid order \(9,10,13,26\) consumes \(2184+156+52+26=2418\) reads. The new ordering saves **62** Boolean probes per complete 2184-event cycle. Always reading all four would require \(4\cdot2184=8736\) probes; optimal early-stop ordering saves **6380**.

## Finite certificate and all-event proof

Construct every labelled sequence by the frozen rational formulas and its integer-scaled monic characteristic recurrence. For a label whose recurrence order is \(d_m\), compute its initial values and the following 2184 shifts modulo 13. The checker verifies

\[
q_{m,3+j+2184}=q_{m,3+j}\pmod {13}
\quad(0\le j<d_m)
\]

for **all 63 labels**, a total of \(\sum_m d_m=249\) equalities. Since each recurrence is monic, these finite equality tests imply each infinite sequence is 2184-periodic by induction. Exact finite support sets over one period therefore represent all \(k\ge3\).

The checker groups all 63 supports, counts 39 empty supports and exactly six distinct active supports, and computes the stated support cardinalities. It independently exhausts all \(\binom{24}{3}=2024\) active triples: none covers the full union. Exhausting all four-element active subsets finds exactly 384 valid fixed sets.

For the sequential optimum, a continuing computation has observed **only zero** responses. Consequently every deterministic algorithm's continuation is its single all-zero response path: querying a previously queried mask, an identically-zero mask, or a second member of the same support class cannot improve any decision. Thus it suffices to choose a sequence of the six distinct support profiles, stopping when the union of queried nonzero-support sets equals the full union \(U\). Let \(A(S)\) be the nonzero-event union of the chosen profile subset \(S\), and let \(N(S)=2184-|A(S)|\) be the number of event positions that require another query. The exact remaining read cost satisfies the finite recurrence

\[
F(S)=
\begin{cases}
0,& A(S)=U,\\
N(S)+\displaystyle\min_{i\notin S}F(S\cup\{i\}),&A(S)\ne U.
\end{cases}
\]

There are at most \(2^6=64\) states. Exact integer bitset evaluation yields \(F(\varnothing)=2356\), with lexicographically selected optimal order \((9,26,10,13)\). Independently enumerating **all \(6!=720\)** profile permutations gives the identical global minimum, as does testing all valid four-label sets and their 24 orders. This is a complete finite optimization proof under the defined oracle model, with the recurrence shift proof extending applicability from one period to every \(k\ge3\).

The accompanying standard-library-only \`R265_optimal_sequential_observer.py\` rederives all 63 exact initial rational sequences, produces the modular supports, checks period shifts, repeats the 2024-triple exclusion, 384 four-set count, 64-state DP and 720 independent permutations, then emits \`R265_verification.json\`. The program was executed and returned **R265 PASS**. All computations use integer and \`Fraction\` arithmetic, with no floating-point tolerances.

## Mathematical and information-preservation scope

This theorem preserves the **Boolean** all-zero predicate and the *original labels used as inputs*, but deliberately does not reconstruct all values or preserve phase/signed-port information. Its expected cost is conditional on an unknown event index and uniform 2184-event workload. Access to the phase index, a different event distribution, multiplexed probes, or other adaptive query semantics defines a different optimization question. No native BRC/X6 model transfer is claimed.

## Next scientific directions

Generalize the exact sequential-observer design to arbitrary nonuniform event distributions and expensive/heterogeneous source probes, and seek a structural characterization of low-cardinality Boolean supports without full 2184-state enumeration. A typed source/provenance preserving BRC interface remains an independent potential application.
