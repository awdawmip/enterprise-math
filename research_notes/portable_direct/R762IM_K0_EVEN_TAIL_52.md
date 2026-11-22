# R762IM — 52-event constructive compression of every even upper-tail zero-critical Port terminal histogram

Date: 2026-11-22 (Asia/Shanghai). **AUTHOR_PROVED / EXHAUSTIVE_EXACT_CHECKED / NOT_REVIEWED**.

## Model and pinned scientific source

Frozen scientific Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; frozen P000 science `a72226e2430ffa4786321ac86e7f0c599d5f0389`. This is the six-axis **composite Port Euler observer** of R762IK/R762IL: Port vertices — the 15 two-element subsets of six native axes; each support `S` — one of the 20 three-element subsets; an event of type `S` selects one of the three edges among the pair-Ports in `S`. A closed legal Port trace is an Euler tour of its connected even-degree assigned multigraph. The observable includes the support histogram's positivity and parity, exact active Port set, and an arbitrarily specified active start Port.

Immediate predecessor: [R762IL proof](https://github.com/awdawmip/enterprise-math/blob/f83b9cc3ac2b852ca56d8b0b8938dc7dbc55024c/research_notes/portable_direct/R762IL_PORT_54_EVENT_KERNEL.md) and [exact checker](https://github.com/awdawmip/enterprise-math/blob/f83b9cc3ac2b852ca56d8b0b8938dc7dbc55024c/research_notes/portable_direct/R762IL_CHECK.py); its R762IK terminal-reduction dependency is [pinned](https://github.com/awdawmip/enterprise-math/blob/a8d8488b137cd090dbde3d3c07c3d5ffa6a9c57c/research_notes/portable_direct/R762IK_PORT_55_EVENT_KERNEL.md).

## Exact new theorem (the k=0 even upper tail)

Let `n=(n_S)` have exactly 20 indexed support entries, each `n_S∈{0,1,2,3}`, with an **even** total `|n|∈{54,56,58,60}`. For any original legal Euler realization of `n` whose active Port set is `V`, and every prescribed `p∈V`, there exists a support histogram `h≤n` with

```
sum_S h_S = 52,
h_S > 0  iff  n_S > 0,
h_S ≡ n_S (mod 2) for every S,
active Ports = V,
a connected all-even-degree edge realization of h with start p.
```

Consequently all deleted named events may be restored as same-support event pairs along an edge still occupied by that support. Thus a `k=0` pair-removal terminal history (the previous proof's zero critical-four regime) with an even length at least 54 admits a reversible **52-event** Port-Euler witness. Together with R762IL's odd upper-tail witnesses and its `k=0` terminal reduction, **all `k=0` terminal histories admit a 53-event-or-smaller witness**. This is a *proper subclass strengthening* of the established universal 54-event bound; the `k≥1` regimes remain separate.

## Finite constructive proof and exact completeness

Write `U,E,M,F` for the supports with multiplicity `1,2,0,3` respectively, with `|U|=u, |E|=e, |M|=m`. Relative to the all-three baseline (60 events) the deficit is exactly `D=2u+e+3m`. The hypothesis requires `D∈{0,2,4,6}`. Solving this finite nonnegative equation gives **exactly the 14 mutually exclusive support-histogram families** below. For every disjoint choice of indexed supports in every family the checker creates a concrete 52-edge assignment, including the appropriate chosen single-edge replacements of `(|n|-52)/2` three-event supports; all extra edges retain their original support identity.

| Family | D | Complete histograms | S6 orbits | Possible omitted-Port instances |
|---|---:|---:|---:|---:|
| T20 | 0 | 1 | 1 | 0 |
| E2 | 2 | 190 | 3 | 0 |
| U1 | 2 | 20 | 1 | 0 |
| E4 | 4 | 4,845 | 21 | 15 |
| U1E2 | 4 | 3,420 | 12 | 0 |
| U2 | 4 | 190 | 3 | 0 |
| M1E1 | 4 | 380 | 3 | 0 |
| E6 | 6 | 38,760 | 94 | 1800 |
| U1E4 | 6 | 77,520 | 152 | 1200 |
| U2E2 | 6 | 29,070 | 69 | 90 |
| U3 | 6 | 1,140 | 7 | 0 |
| M1E3 | 6 | 19,380 | 48 | 60 |
| M1U1E1 | 6 | 6,840 | 18 | 0 |
| M2 | 6 | 190 | 3 | 0 |
| **Total** | | **181,946** | **435** | **3,165** |

For active set `V` containing all 15 Ports, the program partitions each family's complete histogram population into actual orbits of all **720** axis permutations. For each of the **435** representatives, it constructs a witness and explicitly transports it to **every** labeled histogram in the orbit. For every transported witness the program checks supportwise count `0<h_S≤n_S` whenever `n_S>0`, even count difference, exactly 52 edges, legal Port edges, parity at all 15 Ports, connectivity and exact active set.

An original 54–60-event terminal histogram has at most six non-three support types. Every pair-Port lies in exactly four support triangles. Two different pair-Ports have at least seven distinct incident support types, hence they cannot both be inactive in any legal realization under this hypothesis. Therefore `V` can only contain 15 or 14 Ports. In the 14-Port case the omitted Port cannot belong to any three-event support. The checker enumerates **all 3,165** resulting `(n, omitted Port)` instances across all families, and independently constructs a connected, even-degree, exactly-14-active-Port 52-edge witness for each.

Every output is accepted by an *independent exact graph check*, and the source enumerators are explicit finite `S6` permutations and disjoint combinations, using no floating point. This constitutes a finite exhaustive constructive proof of the stated 14-family theorem. The checker may use non-equivariant search for one representative; only actually verified witnesses are transported under explicitly enumerated automorphisms. A failed direct search on a nonrepresentative therefore is not treated as a mathematical obstruction.

## Algorithms / evidence

Run `node research_notes/portable_direct/R762IM_CHECK.js` using standard JavaScript integers. It prints the full evidence including a literal 52-edge realization of the all-three baseline. The proof follows each run's actual enumeration and graph validation. Exact evidence file: `R762IM_EVIDENCE.json`. The results here are independent of native Task authorization; source proofs retain their historical authorship.

**Mathematical scope:** existential Euler Port observer with source/support presence, parity and active Port identity. It is neither a count-of-Euler-tours invariant nor a native P000 time/force/Cell/rotation lifting statement. The earlier R762IK/R762IL terminal-reduction lemmas remain load-bearing for the global k=0 corollary and are not independently reviewed here.

**Next unresolved:** eliminate or realize 54-edge terminal configurations with `k=1,2,7` under the old bridge-count bounds; determine whether the global 54 can be reduced to 53 or construct a sharp lower example. Separately implement a histogram-only algorithm returning a Port Euler tour or an exact infeasibility certificate, preserving original support/Port labels.
