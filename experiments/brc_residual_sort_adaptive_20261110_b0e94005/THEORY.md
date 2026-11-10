# Bounded quantile repair and exact bin omission

This note concerns complete ascending order of a `uint64_t` multiset, including
the multiplicity of every input occurrence. It does not promise stability for
attached records or introduce a new BRC address convention. Phase two changes
model selection while retaining the exact count-and-spill representation.

The inherited argument and compact-interval construction are documented in the
[phase-one THEORY.md at immutable scientific commit
085ff2fb544cd2bfc85beb75cfd72ed15f6a0569](https://github.com/awdawmip/enterprise-math/blob/085ff2fb544cd2bfc85beb75cfd72ed15f6a0569/experiments/brc_residual_sort_robust_20261110_b0e94005/THEORY.md).
The present policy is implemented in [adaptive_kernels.hpp](adaptive_kernels.hpp);
the deterministic constructions and diagnostic checks are in
[adaptive_bench.cpp](adaptive_bench.cpp). These source references distinguish
implementation statements from the deductions below.

## 1. Fixed policy and actual acceptance

For a modeled node of size \(m\), the original sample has
\(S=\min(m,1024)\) observations. The counter budget remains

\[
C(m)=\min\!\left(2^{22},\max\!\left(4096,\lfloor m/2\rfloor\right)\right).
\]

Nodes of size at most 256 use the inherited small-array terminal; depth 16
uses the inherited radix terminal. The original compact-interval opportunity
and the original sparse-bin model are considered before any repair.

| Candidate | Quantile cuts when the original model is over budget | Bin omission |
|---|---|---|
| `adaptive_trim_1024` | \(\lfloor S/64\rfloor,\lfloor S/16\rfloor,\lfloor S/4\rfloor\) | None |
| `adaptive_prune_1024` | \(\lfloor S/64\rfloor\) | After that trimmed layout remains over budget |
| `adaptive_combined_1024` | All three cuts | After each trimmed layout remains over budget |

Every cut selects zero-based ranks \(t\) and \(S-t-1\) from the complete
original sample. Selection permutes that vector but does not shorten it.
The new layout uses all observations inclusively between the two selected
values, including all boundary ties. Each attempt independently rebuilds its
grid, local sample ranges and padding.

At each attempted cut, the policy prefers the inherited compact interval when
the selected numerical span fits the budget; otherwise it accepts an ordinary
grid that fits. If both fail and omission is enabled, it considers the bounded
omission proposal described below. There is no omission attempt on the
original grid before the first cut.

The first viable model receives one exact membership scan. A completed scan
may recurse only if its actual spill count is at most \(\lfloor m/2\rfloor\).
A failed spill test goes directly to the inherited radix terminal on the intact
current input. It does not trigger another quantile or omission attempt.

## 2. Omission preserves the multiset invariant

Let the positive-width counting intervals after a particular quantile rebuild
be \(J_j\), with widths \(w_j>0\) and learning observation counts \(s_j\ge1\).
The intervals are disjoint and ordered by their coarse-bin indices. Their
total width is \(L=\sum_j w_j\); their learning counts sum to the number \(R\)
retained by that quantile filter, with \(R\le S\).

The implementation sorts active bin indices by decreasing width, then by
increasing bin index for equal widths. It proposes removing the shortest prefix
whose removal leaves at most \(C(m)\) counter positions. It commits the proposal
only when the retained learning count \(M\) also satisfies

\[
2M\ge S,\qquad\text{equivalently }M\ge\lceil S/2\rceil.
\]

The denominator is the original sample size \(S\), not the already filtered
count \(R\). A rejected proposal changes no bucket width, grid or cell demand.
A committed proposal sets the omitted widths to zero; offsets are assigned
after selection, immediately before allocating the counter table.

Deleting some intervals leaves the surviving intervals disjoint and ordered.
The inherited width test rejects a zero-width bin, so every occurrence in an
omitted region becomes an exact spill. For a completed scan of input multiset
\(A\), with surviving counting region \(I\), the original identity remains

\[
\mu_A=\sum_{x\in I}c_x\delta_x+\sum_{y\in E}\delta_y.
\]

For an aborted scan, this identity applies to the scanned prefix. Every scanned
occurrence contributes to exactly one side. The current input array remains
unchanged until a complete scan and any required child sort have succeeded.
Discarding temporary counters after rejection is consequently safe.

Expanding the counters in numerical order, recursively sorting \(E\), and
merging the two sorted sequences proves the accepted case. The inherited exact
terminal sorts prove the terminal cases. Induction proves correctness of the
whole algorithm, including repeated values and the endpoints 0 and
\(2^{64}-1\). All selected table widths remain budget checked, and the inherited
128-bit span and padding calculations are unchanged.

An all-empty omission proposal has \(M=0\) and cannot pass the gate at a modeled
node. Thus a committed omission cannot accidentally turn an oversized layout
into an accepted empty counting model.

## 3. Learning mass is not actual coverage

The gate counts observations retained for bucket learning. It does not measure
the fraction of the full input covered by the proposed model. Padding can also
cover some sample observations excluded by the quantile filter, so \(M\) need
not equal even the exact covered population of the original sample.

Only a completed full membership scan supplies a contraction certificate.
If it uncovers \(e>0\) occurrences and \(e\le\lfloor m/2\rfloor\), there is one
recursive edge whose child size is exactly \(e\). If the scan encounters its
\(\lfloor m/2\rfloor+1\)-st spill, it aborts with child size zero. The diagnostic
spill count then describes the processed prefix, not all uncovered values in
the node.

Accordingly, `prune_accepted` and `compact_accepted` mean that a model was
selected. They do not mean that its actual scan succeeded. Summing spill
occurrences across recursive levels can count the same surviving original
occurrence more than once; it is neither a branch count nor a count of distinct
original outliers.

## 4. What widest-first omission does and does not optimize

**Minimum-cardinality lemma, with only the width constraint.** Suppose \(L>C\).
Write the positive widths in decreasing order as
\(w_{(1)}\ge\cdots\ge w_{(B)}\), and let

\[
k=\min\left\{r:\sum_{i=1}^{r}w_{(i)}\ge L-C\right\}.
\]

Removing those \(k\) bins satisfies the counter budget. Any set of at most
\(k-1\) bins has total width at most
\(\sum_{i=1}^{k-1}w_{(i)}<L-C\), so it cannot satisfy the budget. The proposal
therefore omits the fewest bins possible under the width constraint alone.
The index tie break makes the chosen set deterministic without changing this
cardinality argument.

This lemma ignores the learning-mass gate. It does not minimize lost learning
mass, and it does not guarantee finding a layout that passes that additional
gate whenever one exists.

For a concrete **abstract local-layout counterexample**, take

| Bin | Width \(w_j\) | Learning observations \(s_j\) |
|---|---:|---:|
| 1 | 60000 | 900 |
| 2 | 40000 | 60 |
| 3 | 20000 | 64 |

Let \(S=1024\) and \(C=60000\). Total width is 120000. Widest-first omission
removes bin 1, fits the budget exactly, and retains only \(60+64=124\)
observations. The gate rejects that proposal because \(124<512\).
Removing bins 2 and 3 instead also fits the budget exactly, but retains 900
observations and passes the gate. The current policy does not search for that
alternative.

These numbers describe an abstract selection problem; they are not asserted
to be a layout generated by the frozen benchmark. They show the limitation of
the greedy objective, not a measured timing result. Neither the number of bins
nor their learning mass determines actual spill population, radix cost or
backward-merge writes, so no optimum for those costs follows either.

## 5. A deterministic repair of the four-poison construction

The following exact counts refer specifically to the implemented
`central_poison` construction, not arbitrary twenty-cluster samples.
For bank 0, put \(a=2^{48}\) and use ordinary values

\[
v(i)=a+2^{20}\left\lfloor\frac{i\bmod160}{8}\right\rfloor+(i\bmod8).
\]

Fill the array with \(v(i)\), then overwrite its 1024 actual deterministic
sample positions with \(v(k)\), \(k=0,\ldots,1023\), as in the frozen
`trim_witness(n,0,0)`. At sample indices numbered \(800+j\), insert
\(a+j2^{20}+16384\) for \(j=8,9,10,11\). Other banks translate \(a\) by the
specified aligned bank offset without changing this geometry.

At cut 16, the selected bounds are \(a+2\) and \(a+19\cdot2^{20}+5\).
Inclusive ties retain 998 learning observations. Each of the four affected
bins retains 49 observations and has raw width 16385. Its padding is

\[
\left\lfloor\frac{4\cdot16385}{49+1}\right\rfloor=1310.
\]

The coarse interval clips padding at its left boundary, giving padded width
17695. The other sixteen bins contribute 254 counter positions in total.
Thus the first rebuilt layout has \(4\cdot17695+254=71034\) positions.

| Node size | Budget | Omitted bins | Remaining counters | Retained learning observations |
|---|---:|---:|---:|---:|
| 100000 | 50000 | 2 | 35644 | 900 of 1024 |
| 8192 | 4096 | 4 | 254 | 802 of 1024 |

These table entries are source-derived counts. The equal-width index rule
removes bins for clusters 8 and 9 first. At size 100000, two removals already
fit; removing four would contradict the policy's stopping rule. At size 8192,
each affected bin alone exceeds the budget, so all four must be omitted.
Both proposals pass the original-sample mass gate.

This construction also has a direct actual-population bound. Before the
sample-position overwrites, clusters 8 and 9 contain 10000 occurrences at
size 100000; clusters 8 through 11 contain 1632 occurrences at size 8192.
All subsequent modifications occur at at most 1024 sample positions.
Every value in a surviving bin is covered by its learned padded interval.
Actual spills are therefore at most 11024 and 2656 respectively, both strictly
below the corresponding half-input limit. Both roots have nonempty spills and
accept recursion. The harness additionally reconstructs the chosen intervals
and checks the exact actual prefix membership; the loose bounds above do not
substitute sample mass for actual population.

The contrasting hidden-majority construction preserves all sample positions
but puts every nonsampled value into the first omitted bin. It presents the
same learning evidence and passes the same proposal gate, yet the actual scan
must abort at \(\lfloor m/2\rfloor+1\). This isolates model selection from actual
contraction, without changing sorting correctness.

## 6. Ladder boundaries and remaining routing limits

For \(S=1024\), the cuts are 16, 64 and 256 per tail. With \(t+1\) identical
maximum observations strictly above all other observations, rank \(S-t-1\)
already equals that maximum, so an inclusive cut at \(t\) retains all those
ties. Larger cuts can change that outcome, but they can also remove entire
ordinary clusters. Neither actual coverage nor runtime is guaranteed to improve
monotonically with the cut.

The implemented broad-collapse witness uses
`trim_witness(100000,17,1000)`. At cut 16, omission of the enormous ordinary
bin would retain only the 17 extreme learning observations, so the mass gate
rejects before scanning. The ladder can select a grid at cut 64. That cut can
also discard an endpoint cluster, so its actual spill count must not be stated
as exactly the 1000 far-tail occurrences.

The ladder stops at three prescribed scales. Omission stops at its first
width-feasible prefix and does not search other subsets. A selected model that
fails the actual spill test is not replaced with a later candidate. These are
specific limitations of the frozen policy, not impossibility results for
other robust estimators or routing strategies.

## 7. Work bound and its computational scope

Let \(m_i\) be the actual node sizes. Every recursive edge satisfies
\(m_{i+1}\le\lfloor m_i/2\rfloor\), hence

\[
\sum_i m_i<2n
\]

for nonempty input. The number of nodes is at most 17. This population sum is
not a total instruction count.

At a modeled node, all sample acquisition, sample-bound scans, rank selections,
filtered observations, grid construction and padding must be charged. There is
one original grid and at most three rebuilt grids, each with at most 1025 slots.
There are at most three sorts of at most 1025 active bin indices and at most
four compact-span checks. A failed proposal incurs its selection work even
though it allocates no counter table.

The selection routines are not claimed to have a standard worst-case linear
`nth_element` guarantee. Their sample size is fixed at at most 1024 here.
If sample size or the number of candidate models were allowed to grow, their
actual selection cost would have to be retained in a new bound. The
widest-bin ordering costs \(O(B\log B)\) per proposal with \(B\le1025\).

After selection, counter initialization, one full or prefix membership scan,
count emission and backward merging each incur their own cost. There is no
full-input extrema probe in these three adaptive policies; a radix fallback's
own extrema scan and at most seven 10-bit passes remain charged. The inherited
compact padding and all retry and scratch allocations are part of the measured
call.

Only the selected counter table is allocated, with \(L_i\le C(m_i)\), and

\[
\sum_iL_i\le\sum_i(m_i/2+4096)<n+4096D,
\qquad D\le17.
\]

The temporary omission-order vector is destroyed before counter allocation or
descent. Ancestor counter, sample, bucket and spill buffers remain charged;
in particular, a small actual spill count does not eliminate the reservation
of \(\lfloor m_i/2\rfloor+1\) spill slots at that node.

Assuming successful allocation, these bounds give \(O(n)\) operations and
\(O(n)\) auxiliary storage in the fixed-64-bit word-cost model. They do not
improve the asymptotic bound already available to fixed-width radix sorting.
For natural numbers of growing bit length, word operations, input access and
the number of radix passes need an explicit bit or variable-word model. This
experiment establishes no new general-natural-number complexity bound.

## 8. Diagnostic interpretation and status

- `robust.trim_attempts` counts nodes that attempted a trim;
  `ladder_attempts` counts all attempted cut levels.
- Core trim bounds, included observations and `trimmed_cells` describe the
  last attempted level. Learning visits, filter visits and selection-call
  counts accumulate every attempted level.
- Per-attempt omitted counts describe proposals, including rejected proposals.
  Node-level omitted counts describe only a committed proposal.
- Retained learning mass, selected counter width, actual processed-prefix
  population and actual child size are separate measurements.
- Logical visit counters are not counts of machine instructions, cache misses
  or selection comparisons. The temporary-order byte metric is not peak RSS.

The statements above are author-side arguments about the implementation and
specified deterministic constructions. Finite diagnostics support the audited
routes; they do not constitute a formal shared-task mathematical acceptance.
The claims concern exactness, bounded work and limited routing objectives.
There is no claim of novelty of counting, radix sorting, sample quantiles,
exception repair or greedy bin omission.
