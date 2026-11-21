# R762IC — Universal Port-closure parity sufficiency in the frozen six-axis composite candidate

Date: 2026-11-21. Status: AUTHOR_PROVED / TWO INDEPENDENT EXACT FINITE CERTIFICATES / NOT_REVIEWED.

**Frozen scientific model:** RS-X6-TRIADIC-CLOSURE-DYNAMICS, scientific pin `a72226e2430ffa4786321ac86e7f0c599d5f0389`. Immediate antecedents: R762HT (independent Port/sign factorization), R762IB (complete three-orbit parity-core classification), R762IA (integer lattice). Native P000 remains the higher-priority primitive world model. This result is specifically about the **composite support-and-Port observer**, with no primitive `TRIADIC_CLOSURE_E` assertion.

## Theorem (all finite lengths and multiplicities)

Let `X={0,1,2,3,4,5}`, `T=binom(X,3)` (20 triad supports), and let `P=binom(X,2)` (15 Port states). A transition between distinct Ports `p,q` is allowed when `|p∩q|=1`; its triple support is `S=p∪q`. Let `n=(n_S)_{S∈T}` be any finite multiset of **named** support occurrences. Set `H_i=Σ_{S∋i}n_S`. Write `N_p(n)` for the number of legal closed Port histories using each named event once and starting/ending at `p`. Let `C(n)` count per-occurrence signs `ε∈{±1}` with `Σ_t ε_t h_{S_t}=0∈Z^6`. Then, for every `p` and `n`,

> **`N_p(n)>0  ==>  (C(n)>0  iff  all H_i are even)`.**

Equivalently, the joint signed zero-return count `J_p(n)=N_p(n)C(n)` is positive precisely when the legal closed Port history exists and the six coordinate-incidence counts are even. The forward implication `C(n)>0 ⇒ H_i even` follows immediately by reducing each signed coordinate sum modulo two.

This resolves the open **single fixed support histogram** parity-sufficiency question for the stated composite candidate. A sign assignment is allowed independently of Port edge choices, exactly as in R762HT. No uniform-in-`n` primitive native-force or time/rotation lift is asserted.

## 1. Compress an arbitrary multiplicity to a finite Boolean pair-presence set

Put `n_S=δ_S+2q_S`, where `δ_S∈{0,1}`. If every `H_i` is even, `δ` belongs to the binary incidence kernel. R762IB established by full, independently crosschecked finite enumeration that the 16,384 such cores contain exactly 230 nonsignable cores, forming three orbits under `S6`:

- 4-core: `024,035,125,134` (30 orbit members).
- 6-core: `012,015,025,034,123,124` (180 members).
- 10-core: `012,013,014,025,035,045,125,135,145,234` (20 members).

When `C(δ)>0`, balance `δ` and give the remaining `2q_S` events cancelling sign pairs. Thus `C(n)>0`.

For a nonsignable core define `Q={S:q_S≥1}` and `n^Q_S=δ_S+2·1_{S∈Q}`. If `C(n^Q)>0`, add cancelling sign pairs to obtain `C(n)>0`. Consequently `C(n)=0 ⇒ C(n^Q)=0`. This implication is valid for arbitrary, unbounded positive counts `q_S`.

**Exact Port parity reduction.** Each support `S` offers the three edges of its 3-Port triangle; their 15-bit endpoint-parity vectors `b_1,b_2,b_3` obey `b_1⊕b_2⊕b_3=0`. For `n_S=0`, the possible parity contribution is `{0}`; for `n_S=1`, it is `{b_1,b_2,b_3}`; for every `n_S≥2`, it is `{0,b_1,b_2,b_3}`. For `n_S=2` use repeated or distinct edges; for `n_S=3` use the triangle of three edges or three repetitions; for larger values add cancelling edge pairs. Therefore the set of *globally even Port degree* choices for `n` is nonempty iff it is nonempty for `n^Q`.

**Exact connectivity necessity.** Let `G_2(U)` have the distinct support types `U={S:n_S>0}=supp(δ)∪Q` as vertices and join two types when they share exactly two axes. Different support triangles share a Port vertex only if the supports are adjacent in `G_2`. Hence a connected Eulerian selected Port multigraph, required by any legal closed history using all events, forces `G_2(U)` connected. Both `n` and `n^Q` have the identical `U`.

We therefore need only rule out the following finite joint event for **each** of three cores and each of the `2^20` subsets `Q⊆T`:

`(A) C(n^Q)=0;  (B) G_2(supp δ ∪ Q) connected;  (C) even-degree Port edge assignment exists.`

## 2. Exact finite certificate and independent algorithms

Let `h_S=Σ_{i∈S}e_i`. For a fixed core `δ`, construct the finite target set

`A_δ={ -(1/2)Σ_{S∈δ}ε_S h_S : ε_S∈{±1} }`.

Every target is integral because the core has even axis degree. For `Q` define

`R_Q={Σ_{S∈Q}z_S h_S : z_S∈{-1,0,1}}`.

Then `C(n^Q)>0 ⇔ A_δ∩R_Q≠∅`. This is an exact integer test retaining source support and sign, not a floating-point approximation.

Let `B_δ` be the set of XOR sums of one selected Port edge-boundary per odd core support. Let `V_Q` be the `F_2`-span of the three edge-boundaries for each `S∈Q`. Then condition (C) is exactly `B_δ∩V_Q≠∅`. The Python checker independently tests it using connected components of the 15-vertex Port graph induced by `Q`: a desired parity mask is in `V_Q` iff its set bits have even cardinality in each such component. The C++ checker computes a binary row-reduced basis directly.

Each row enumerates **all 1,048,576** Boolean `Q` masks; exactly 3,145,728 cases over the three orbit representatives:

| Odd-core orbit representative | Distinct targets `|A_δ|` | Distinct core boundary masks `|B_δ|` | (A) nonsignable `Q` | (A)+(B) | (A)+(B)+(C) |
|---|---:|---:|---:|---:|---:|
| 4-event Pasch orbit | 16 | 81 | 3,824 | 64 | **0** |
| 6-event orbit | 64 | 621 | 1,056 | 0 | **0** |
| 10-event orbit | 656 | 6,081 | 1,024 | 0 | **0** |
| **Total** | | | **5,904** | **64** | **0** |

The 64 connected nonsignable `Q` for the Pasch core have cardinality 3/4/5/6 with counts 8/24/24/8. For all 64, the even-Port-degree condition is impossible. The two programs agree on the full per-core levels (see JSON evidence and program output).

**Completeness of the optimized enumerations.** The C++ program checks every one of the 2^20 masks, exploiting monotonicity only to avoid a redundant signed-sum computation. The independent Python program descends only through nonsignable prefixes: if a prefix is signable, every superset is signable, so no nonsignable `Q` can be pruned. The two implementations use different sum enumeration and Port parity methods. Both use fixed-width *integer* bit masks for the finite graph and exact six-coordinate integer sums; no randomness, real approximation, or formal proof assistant is involved.

## 3. Deduction and preserved representation

Assume for contradiction `N_p(n)>0`, all `H_i` even, and `C(n)=0`. The odd core must be one of the three R762IB orbits. Passing to `Q` preserves nonsignability of the minimal histogram `n^Q`, preserves the necessary connected support graph, and preserves feasibility of even Port degrees. Thus `Q` satisfies (A),(B),(C), contradicting the exhaustive zero count. Hence `C(n)>0`.

This Boolean reduction is **observer-specific**: it certifies the existence of some signed assignment under the fixed support histogram and *necessary* even-degree Port feasibility. It does not identify full Port walks by a parity mask, erase named event identities from an actual history, or claim a lossless representation for other observers, native time, field, phase, momentum, branch, or subsequent operations. The original full Port witness remains unchanged; after proving existence, a valid sign assignment can be attached event-by-event without modifying it.

The exact program checks are finite combinatorial theorem certificates for this composite model; they do not compute P000 primitive heartbeat evolution, physical residuals, or external numerical `π`/trigonometric values. The mandatory BRC provenance/sign distinction is preserved at the claim boundary. Independent mathematical review and primitive `TRIADIC_CLOSURE_E` realization remain open.

## Next mathematical unit

1. Extract a *constructive* signing algorithm taking `n` and one legal Port circuit as input, using the finite Boolean classification to produce a certificate `ε` without a fresh exponential search for each case.
2. Attempt a human-checkable orbit/graph proof replacing the 3×2^20 exhaustive step (the C++/Python certificates already settle its exact finite six-axis statement).
3. Investigate the genuinely native `TRIADIC_CLOSURE_E` force/Cell/Link/Port/time and rotation lift separately; do not promote composite Port closure to a primitive native equality.

**Files:** `R762IC_PORT_PARITY_SUFFICIENCY.md` (this proof), `R762IC_CHECK.cpp` (exhaustive C++), `R762IC_VERIFY.py` (independent monotone DFS), and `R762IC_EVIDENCE.json` (counts and controls). Historical result R762IB is a stated load-bearing finite classification, not an independently reviewed theorem.