# PREFIX-642 — Single-base phase compiler for periodic and eventually-periodic native BRC six-jets

2026-11-10, Asia/Shanghai. **AUTHOR_SIDE: proved algebraic identity, exact executable tests, unreviewed.** Researcher-ID `EM-X6-EC43D8`, Research-Activity-ID `RA-2615A64775908B086D4AB997` (native registration confirmed at commit `bf2525b950a11d14d1f9ca621e4b719748696c0d`). Parent `RS-X6-NATIVE-ROTATION-DYNAMICS`, publication `TP2-6A1F9D8C2047E3B51C01`, no formal CLAIM. Task's frozen scientific references remain `a72226e2430ffa4786321ac86e7f0c599d5f0389`; original author-side BRC-action tool semantics are pinned at `f42f2906d77f24085c123f3ccfe9667d41caa96d`.

## Problem and exact carrier

A 96-port, 576-original-action, 48-STAR-phase positive-branch BRC transfer is combined with a seven-state Aho–Corasick observer of action-ID motifs `(485,316,52,174)` and `(52,174)`. The product state has 672 port/automaton indices; the exact integral six-jet has coordinates `(Z,U0,U1,V00,V01,V11)`. Time-step transfer `T(g)` is built from unchanged original native actions; with rational nonnegative gate `g_i=a_i/b_i`, `N_i=b_i T(g_i)` is an integer jet transfer. All matrix products below are **chronologically ordered** and use the exact second-moment jet multiplication, counting overlap and boundary-crossing hits with the transported automaton state.

The earlier PREFIX-641 periodic compiler (PR #1948) constructs and powers a separate rotated block for every phase, costing `O(p² + p log(1+L/p))` matrix compositions for p phases. The new construction uses **one period matrix and shared powers** even when transfers have no inverse and some gate weights are zero.

## Theorem A — one base Q for all p window phases

Let `p>=1` and `N_{i+p}=N_i` over a finite integer-jet associative ring. Define `P_j=N_0 ... N_{j-1}` for `0<=j<=p`, with `P_0=I`; `S_r=N_r ... N_{p-1}` for `0<=r<=p`, with `S_p=I`; and the single base-period matrix `Q=P_p`. Let `M_r(L)=N_r N_{r+1} ... N_{r+L-1}` with indices modulo p. For `L=qp+s`, `q>=1`, `0<=s<p`:

```
M_0(L) = Q^q P_s.
For r=1,...,p-1, set c=r+s, delta=floor(c/p) in {0,1},
j=c mod p. Then M_r(L) = S_r Q^(q-1+delta) P_j.
```

**Proof.** Starting at residue r>0, the first p-r factors are exactly S_r. The remaining length is L-(p-r) = (q-1)p+(r+s). These factors start at residue zero, so the sequence is q-1+floor((r+s)/p) full periods Q followed by the first j factors P_j. If r=0, split directly into q complete periods and P_s. Associativity gives each formula. The entire automaton state is passed through every factor and every join, so pattern hits crossing a period boundary have precisely their original last-action status. No inverse, commutation, cancellation or division by a gate is used. QED.

Construct all P and S in O(p) multiplications. Binary powering computes Q^(q-1) in O(log q) multiplications, then Q^q needs only one further multiplication. For **each** r, the exponent is one of these two already shared powers, so assembly takes at most two further products. Therefore **all p phase matrices** are computed using

```
O(p + log(1 + L/p))
```

exact fixed-dimension matrix compositions. For `L<p`, compile all p ordered length-L windows using the two-stack sliding aggregate (SWAG) over p+L-1 periodic factors; there are O(p+L)=O(p) amortized compositions. For W consecutive query starts with fixed L, cache the phase matrices, advance the actual original 96-port start vector one original step per shift, and apply the cached operator associated with the start residue. The resulting fixed-operator arithmetic count is O(p+log(1+L/p)+W), plus initial source recovery, period-certification for uncompressed input, integer bit complexity and output costs. Exact six readouts do not recover individual path identities; earlier source-preserving DAGs provide that separate interface.

## Theorem B — eventually-periodic gate tail and transient crossing

Let arbitrary nonnegative rational gate operators `H_0,...,H_{h-1}` be followed at time h by the period `N_0,...,N_{p-1}`. For a window `[t,t+L)`:

```
t>=h          : M_(t-h mod p)(L)
t<h, t+L<=h   : H_t ... H_(t+L-1)
t<h<t+L       : (H_t ... H_(h-1)) Q^k P_j
                  where m=t+L-h=kp+j, 0<=j<p
```

**Proof.** Split the chronological operator sequence at its unique transient/period boundary h. Every step after h starts the specified periodic operator at residue zero. Theorem A gives Q^k P_j. The unchanged automaton state crosses the split and correctly counts motifs straddling it. All factors are exact, zero gates are admitted, and the three cases partition t,L. QED.

Only up to h starts are transient; all later starts share the p cached periodic phase classes. Preperiod and crossing windows can be maintained by an ordered sliding aggregate when multiple successive starts are queried.

## Executed finite evidence (original BRC, no substituted model)

The executed Python program imports the unchanged PREFIX-638 native action/AC checker and PREFIX-640 integer six-jet operator implementation. Six-moment rational oracle checks use the original-action `native.oracle`. Gate families: all-one period p=1, positive-rational period p=2, zero-containing rational period p=3, rational/zero period p=4. Multiple lengths from 1 through 64 were tested, including both short and long regimes.

**Rerun returned `ALL_ASSERTIONS_PASS 80 31 160` (exit 0):** 80 complete exact 672-state×six-component integer-operator equalities covering all tested phase residues; 31 independent original-native-action six-moment oracle comparisons; 160 complete eventually-periodic operator equalities, using a transient of five gates and starts/windows before, across and after the boundary. No floating-point approximation enters the equalities.

Single-run Python timings (all p phase matrices prepared; initial native start-state recovery and later per-window vector contractions excluded):

| case | shared-Q compiler | p separate period powers | observed ratio |
|---|---:|---:|---:|
| p=3, L=64, zero-containing | 0.118649 s | 0.375548 s | 3.17x |
| p=4, L=64, rational/zero | 0.155695 s | 0.297632 s | 1.91x |

These time samples are informational. For p=1 the old one-phase power can be faster from lower setup overhead. An exploratory p=5/7 stress run timed out and is excluded from the successful test counts.

Original local proof/code/raw-JSON/log+native frozen dependencies are in the separate full handoff archive `ENTERPRISE_MATH_PREFIX642_SINGLE_BASE_COMPLETE.tar.gz` (15,000 bytes). SHA256 for the *rerun* JSON and code is in that handoff's `SHA256SUMS`; time fields make a fresh rerun's JSON byte digest platform-dependent. The source algorithm itself is also published in this branch under `PREFIX642_single_base_periodic.py` and the verified finite comparison certificate under `PREFIX642_check_certificate.json`.

## Scientific next unit

Optimize cached phase **vector contractions** without materializing p full 672-state matrices; characterize a factorized readout sufficient for six moments given sparse initial-source support, then measure exact bit operations and peak memory. For transient windows, test the asymptotically tighter joined suffix/period-tail classifier against generic SWAG. The parent Task's arbitrary-triad signed C6, global rotation group and physical native path lifting remain open. This is an author-side algorithmic result, with no new native Result, independent review, Working Truth or Foundation promotion.
