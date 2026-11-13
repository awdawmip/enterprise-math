# PREFIX-597-R2 — Exact native X6-BRC propagation costs: 96/49/48 states

2026-11-08. Author-side derivation and exact integer verification; independent Driver review pending.
Scientific input remains **awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d**.
Follows PREFIX-595/596 without changing P000, the original 48 phases, 96 ordered bit ports, 576 source-labeled arcs, six native-axis labels, or the three gated arcs.
Researcher-ID: **EM-DIRECT-E14EF0**, Activity-ID: **RA-80E7BEAB2F803F01DD18B4B1**. Formal Task CLAIM not asserted.

## New exact native-96 phase-sum identity

Let `N(i)` denote the three phase successors of phase `i`, `g=4` the marked gate-target phase, `a(i)` its original axis label, and `r_(j,v)` the source value of phase `j`, bit `v∈{0,1}`.
Write `s_j=r_(j,0)+r_(j,1)` and `m_i=Σ_(j∈N(i))s_j`.
The original weighted 96-port transfer operator is **exactly**

```
(A(x,z)r)_(i,0) = x_(a(i)) m_i,
(A(x,z)r)_(i,1) = x_(a(i)) m_i
                    + [g∈N(i)] x_1 (z-1) r_(g,1).
```

**Proof:** For each original source phase `i`, successor `j`, and source/destination bit pair `(u,v)`, all four arcs carry the original axis weight except the unique arc with `j=g,u=v=1` whose weight is `x_1z`. Summing the two destination bit columns gives `m_i` for `u=0`; for `u=1`, replace exactly the marked summand `x_1r_(g,1)` by `x_1zr_(g,1)`. The marked arc's original axis is 1. This proves the formula coefficientwise for arbitrary real `x_a,z`, particularly `x_a≥0,z≥0`. The correction is a difference but the complete original output remains nonnegative for nonnegative input; gate provenance stays typed as its seventh coefficient.

This gives an adequate **optimized original comparator**: 48 bit-pair sums, 144 phase-neighbor occurrences, 96 output scalars, and only three marked-phase corrections per step. Comparing only against 576 unmerged labeled edge accumulations is not a fair claim of a fourfold algorithmic gain.

## Exact 48-state endpoint decoding

After one original step, the two output bits at `g` are equal. Use the PREFIX-596 encoding `v_i=r_(i,0)+r_(i,1)` for `i≠g`, `v_g=r_(g,0)=r_(g,1)`. Given a tail state from the preceding step, define `u_i=Σ_(j∈N(i),j≠g) v_j` and `h_i=[g∈N(i)]`. All complete terminal port values are recovered from

```
r'_((i,0)) = x_(a(i)) (u_i + 2 h_i v_g)
r'_((i,1)) = x_(a(i)) (u_i + (1+z) h_i v_g).
```

For `i=g`, `h_i=0`; the two bit values coincide. This formula is simply `O(x,z)=A(x,z)E_tail` expanded in native bit arcs; it preserves complete **terminal** ports, not each hidden historical branch label. Any nonstationary sequence of length `n≥2` is evaluated as

```
v_1=C_tail A_1 r_0,
v_t=Q_t v_(t-1), t=2,...,n-1,
r_n=O_n v_(n-1).
```

The original, 49-state, and 48-state routes are algebraically equivalent on the declared full-terminal-port observer; the 48-state route saves memory dimensions but its first and last operations retain interface costs.

## New exact sparsity distinction

From seven separately labeled generator matrices, the 49-state positive operator has respectively **[27,24,27,24,24,24,3] nonzero typed entries**, total **153**, occupying **150 distinct (row,column) positions**. The 48-state tail operator has **[24,24,24,24,24,24,3] typed entries**, total **147**, occupying **144 distinct positions**. The three gated entries overlap spatially with regular-axis entries and are counted separately by label. Both numbers are exact structural counts, not runtime operation counts for sparse live inputs.

**Incremental reduction 49→48:** 6 of 153 typed matrix entries (3.92%), not 50% of the scalar work. Thus the proved minimality of 48 states from PREFIX-596 does not by itself imply a proportional speedup.

## Executed exact evidence

The self-contained `PREFIX597_R2_compact_exact_checker.py` reconstructs the native frozen 48-phase / 576 labeled-action BRC, and verifies **1,800 complete 96-port exact integer equalities** among literal original edges, positive49 factorization, 48-tail explicit recurrence, and 48-tail sparse seven-label multiplication; including 96 singleton-port inputs, four additional inputs, zero-axis and nonstationary gate values `z=0,1,2,3,4,5`, and depths `0,1,2,3,6,12`. Actual local output:
```
ALL_ASSERTIONS_PASS 1800 source_edges 576 49_coeff_nnz 153 48_coeff_nnz 147
```

The separate extended `PREFIX597_R2_end_to_end_benchmark.py` (included with full exact JSON output in the conversation research package) additionally tests the optimized original96 recurrence and reports five-run within-process Python integer medians for identical complete-terminal-output workloads:

| Depth | Maximum exact output bits | Literal576 (ms) | Optimized96 (ms) | Positive49 (ms) | Positive48 sparse (ms) |
|---:|---:|---:|---:|---:|---:|
| 2 | 10 | 0.2078 | 0.0364 | 0.0304 | 0.0376 |
| 8 | 34 | 0.2496 | 0.2451 | 0.1025 | 0.1056 |
| 32 | 128 | 1.2737 | 0.7209 | 0.4576 | 0.4419 |
| 64 | 254 | 3.5324 | 1.7238 | 1.1032 | 1.0787 |

Measurements are environment-specific, subject to scheduling and language/loop-layout differences. All algorithms were checked for equal 96-component integer outputs. No universal or bit-complexity speedup is claimed from these medians.

## Precise next research unit

Implement the 96 optimized, 49 positive, and 48 positive recurrences with the **same sparse integer kernel** and terminal query adapter. Measure (i) full 96 output, (ii) selected end-ports, (iii) repeated batch endpoint queries, including encoding/recovery, integer bit length, and original seventh gate-label source observer. Compare `n=2,8,32,128` and zero/positive gate cases; identify workload families with genuine gains and prove any asserted complexity bound on the declared computational model.

Status: **AUTHOR_SIDE_PROVED_BY_TYPED_EDGE_CLASSIFICATION + EXACT_COMPUTATION_CHECKED / UNREVIEWED**.
