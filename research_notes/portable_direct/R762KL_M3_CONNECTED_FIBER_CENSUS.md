# R762KL — Exact connected-fiber census and an observer non-injectivity witness for M3

Date: 2026-11-23. Status: AUTHOR_EXACT_FINITE_CHECKED / NOT_REVIEWED.
Scientific provenance: continuation of R762KK at `awdawmip/enterprise-math@036ad56598da5e5abd5e6901f0ffa100735abd35:research_notes/portable_direct/R762KK_PROJECTION_PAIR_ADAPTIVE_THEOREM.md`.
Original lane's historical researcher: `EM-X6-B1684F` (Activity `RA-6F2C09233DC4F142A2F7795A`); this portable Source publication by itself neither renews a native RUN nor changes ownership.
Frozen P000: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`.

## Model, domain, and exact question

Work **only in the unsigned auxiliary Port–Euler observation model** of R762KH–KK. Fix inactive Ports `01,23,45`. The twelve active pair Ports in increasing order are
`02,03,04,05,12,13,14,15,24,25,34,35`.
There are twelve forced three-axis supports, each allowed one fixed edge internal to one of the three four-Port components, and eight flexible supports
`024,025,034,035,124,125,134,135`, forming a Boolean cube. In the choice census **each of the eight flexible supports has multiplicity exactly one**. The twelve forced-support multiplicities are represented by their GF(2) boundary parameter `b`; their positive values can vary. The special baseline with every one of the twenty supports occurring once has forced boundary `b=0` and twenty events total. At cube support `ijk`, define its projected Ports
`A=(i,j)`, `B=(i,k)`, `C=(j,k)`. Choose exactly one of the edges `AB, AC, BC`; order the corresponding choices `0,1,2`.

Let `F` be the GF(2) span of forced-edge boundary masks, a nine-dimensional subset of `GF(2)^12` with `|F|=512`. For `b in F`, let `Q(b)` be the number of distinct eight-support choices whose flexible boundary equals `b` and whose union with the twelve forced edges is connected. The forced edges have positive integer multiplicities. For any actual forced inventory whose aggregate boundary is `b`, a connected flexible choice realizing `b` gives an even-degree connected graph and hence an Euler circuit with any active Port as start. The fiber count does not conflate different forced multiplicity inventories.

## Theorem KL.1 — exact connected realization fiber census

The image of `Q` has **465** reachable forced parity boundaries; the other **47** boundaries have `Q(b)=0`, agreeing with the hole set of R762KJ/KK. The full exact fiber-size histogram is

| Connected realizations `Q(b)` | Number of forced boundaries |
|---:|---:|
| 0 | 47 |
| 2 | 132 |
| 3 | 112 |
| 4 | 135 |
| 5 | 36 |
| 6 | 35 |
| 7 | 12 |
| 8 | 3 |

Consequently **every reachable forced boundary has at least two different connected legal edge-event realizations**; no reachable boundary has a unique realization. In total there are **1,638** connected assignments with a forced-compatible parity and **1,641** assignments before connectivity filtering.

At zero boundary specifically, there are nine parity-compatible flexible assignments, three disconnected (the constant `AB`, constant `AC`, and constant `BC` choices) and six connected. All other forced-compatible assignments are connected.

### Exact finite proof

1. The twelve forced supports are exactly those three-axis subsets whose non-inactive Port pairs number two. Their forced-edge boundary vectors span `F` of size `512`; they connect every four-Port component internally as a square.
2. There are `3^8=6,561` ordered flexible choice vectors, each fully identified by its eight entries. XORing the appropriate two-port masks produces its exact twelve-bit boundary. Filtering by `F` is a complete enumeration: there are no other legal choices in this one-event-per-support model.
3. The only intercomponent edges are `AB`, `AC`, and `BC`. The quotient on components `A,B,C` is connected iff at least two of these edge *types* occur. Exactly three assignments have only one edge type. For any constant type, each selected projected Port occurs exactly twice as the cube coordinate omitted by the other grid varies; its total parity is therefore zero, so precisely these three fail connectivity among forced-compatible assignments.
4. The companion standard-library program computes (a) the complete direct enumeration with connectivity filter, and independently (b) the coefficient recurrence `D_{r+1}(x)=sum_{e in E_r} D_r(x xor e)` on integer masks. It asserts pointwise equality of all `512` forced-boundary counts, and the complete histogram above. Each algorithm uses exact integer counts and bitwise GF(2) XOR; there is no approximation or sampling.

Thus this is an exhaustive finite classification of the stated 20-event auxiliary model. The 47 zero fibers confirm predecessor geometry, while the positive multiplicity distribution is an additional quantitative result.

## Theorem KL.2 — explicit residual/non-injectivity certificate

For the **actual twenty-event all-supports-once inventory**, the forced-edge boundary is `b=0` (the twelve forced edges form three four-cycles). The following two *distinct* legal choice vectors (cube order above) both realize `b=0` and connect all three components:

`(0,0,2,2,0,0,2,2)` and `(1,0,1,0,1,0,1,0)`.

They have the **same** frozen support-count inventory (one event per each of twenty supports), forced boundary, active Port set, even-degree requirement and connectivity/Euler-existence result. But their `024` event uses `AB` versus `AC`, hence their edge identities and provenance differ.

Therefore the auxiliary observer `(support multiplicities, forced/flexible boundary, connectedness)` has a nontrivial fiber, and **cannot by itself answer a future query for the legal edge selected at a named support**. This is a concrete scoped residual-fidelity obstruction to discarding edge-event provenance; importantly the two witnesses are **actual complete twenty-event Euler solutions**. It does not assert that native signed Cell/Link/Port or BRC dynamics have the same fiber until a typed source-preserving bridge is proved.

## Reproduction and evidence

Execute `python R762KL_FIBER_CENSUS_VERIFY.py` with Python standard library. The program independently enumerates all 6,561 choices and computes the integer-coefficient recurrence; it checks the forced space size, every count, all boundary histograms and the explicit two-vector witness. Generated companion file: `R762KL_EXACT_EVIDENCE.json`. Local verification (2026-11-23) passed all assertions.

### Frontier

A natural next quantity is the **connected fiber-size spectrum with one or two upgraded flexible supports**, conditioned on the frozen event counts, and whether a source-preserving observer can factor the Euler feasibility and count without erasing support-edge identities. Independently pursue a combinatorial proof of the minimum positive fiber size two instead of the finite-census proof. The native signed `TRIADIC_CLOSURE_E`, time ordering, branching and BRC information remain a separate transfer obligation.

Review: NOT_REVIEWED. Mathematical claim scope: exact, finite, unsigned auxiliary M3 Port–Euler, **20 events**. No official Result/Working Truth/Foundation promotion.
