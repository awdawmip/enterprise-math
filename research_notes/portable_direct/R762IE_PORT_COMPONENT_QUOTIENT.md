# R762IE — Port-component quotient and five symmetry classes of bad masks

Date: 2026-11-22 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Frozen science: RS-X6-TRIADIC-CLOSURE-DYNAMICS, pin `a72226e2430ffa4786321ac86e7f0c599d5f0389`.
Model: six-axis **composite** support/Port/sign observer; no native P000 force, Link, Cell, time or rotation lift claimed.

Dependencies: R762IB@a3b465e76af541de223fcf7773477fbd224be8b4 (three odd-core S6 orbits), R762IC@40945d2ccef1d6d691ba88a85930e9d9276c9123 (signing sufficiency), R762ID@f75988f529eace287a11b217130fc239e4c3b592 (fifteen maximal bad masks). Their finite-classification completeness is reused, **not** re-proved here.

## 1. Exact Port-component quotient theorem (any finite multiplicities)

Let X={0,...,5}, V=binom(X,2) (15 Port vertices), T=binom(X,3) (20 support labels). Each support S gives triangle Δ(S) on the three Ports binom(S,2), with three allowed Port-transition edges. An occurrence chooses one edge e={u,v}, contributing boundary ∂e=1_u+1_v in F₂^V.

For multiplicities n_S=δ_S+2q_S, define D={S:δ_S=1} and Q={S:q_S≥1}. Construct graph G_Q on all 15 Port vertices with the entire triangle Δ(S) for each S in Q; isolated vertices count as components. Write c(v) for its component, κ(Q) for the number of components, and e_j for basis vectors of F₂^{κ(Q)}.

**Theorem.** There is an assignment of one permitted Port edge per named event making every Port degree even iff one can choose an edge {u_S,v_S} of Δ(S) for each S in D such that

    ⊕_{S in D} (e_{c(u_S)} + e_{c(v_S)}) = 0   in F₂^{κ(Q)}.

The even-pair boundary subspace has rank exactly 15−κ(Q).

**Proof.** Two occurrences of a support S may choose the same triangle edge, giving total boundary 0. If they choose distinct edges, their F₂ boundary sum equals the boundary of the third edge. Thus one pair realizes exactly {0} plus all three nonzero triangle-edge boundaries, a two-dimensional F₂ subspace; extra pairs do not enlarge it. Independent pair supports sum their subspaces, giving B_Q=span{∂e:e∈E(G_Q)}. For any finite graph, its F₂ incidence image equals the vectors whose coordinate sum is even on each connected component: every generating edge is component-even, and spanning-tree paths generate every difference within each component. Consequently dim B_Q=15−κ(Q). The compulsory unpaired events choose one edge each; their sum can be cancelled by pairs precisely when its image under the component-sum quotient is zero. QED.

This criterion concerns Port *degree parity*. A single connected Euler circuit also needs connected used edges. Both mechanisms are checked separately below.

## 2. Pasch four-event core: two geometrically different bad-mask orbits

Fix D4={024,035,125,134}. Its stabilizer under all six-axis permutations has order 24. Acting on the twelve maximal nonsignable Q masks in R762ID yields precisely two orbits of sizes **8** and **4**.

**Orbit A (8 masks):** Representative `0x13301`, Q={012,035,045,125,134,234}. The Port graph G_Q has three components, five Ports each:

- A={01,02,12,15,25};
- B={03,04,05,35,45};
- C={13,14,23,24,34}.

Of the four obligatory core supports, 035,125,134 each has all its Ports inside one component. But 024 has Port vertices 02,04,24 in A,B,C respectively. Its chosen edge necessarily crosses two *different* components, contributing nonzero quotient boundary. All other core contributions and all available pairs have zero quotient boundary. The theorem therefore forbids even Port degrees for any mask in this orbit. This is the intrinsic explanation of the eight earlier parity failures.

**Orbit B (4 masks):** Representative `0x5b525`. G_Q has component sizes 12 and 3. Its support-overlap graph on D4∪Q (supports adjacent if they share a Port, i.e. two axes) has two components with obligatory core supports on both sides: {035} is isolated from the other core supports. Any circuit using all named events would have to connect these components, which is impossible. The three other masks are symmetry images. Their component-parity tests pass, so the obstruction is connectivity, not degree parity.

## 3. The remaining three bad-mask representatives

For D6={012,015,025,034,123,124}, the stabilizer has order 4; its two maximal bad masks `0x6ccc9` and `0x80cc8` are each invariant (singleton orbits). For D10={012,013,014,025,035,045,125,135,145,234}, the stabilizer has order 36; `0x1d347` is a singleton orbit. In each of these three cases the support-overlap graph on D∪Q splits compulsory core supports among distinct components, hence no single legal closed circuit exists.

| Odd-core size | Stabilizer | Bad-mask orbit sizes | Port degree obstruction | Mandatory-support disconnection |
|---|---:|---|---:|---:|
| 4 | 24 | 8, 4 | 8 | 4 |
| 6 | 4 | 1, 1 | 0 | 2 |
| 10 | 36 | 1 | 0 | 1 |
| Total | | 15 masks in **5 symmetry classes** | **8** | **7** |

Thus the R762ID Port no-go certificate has five structural symmetry witnesses, conditional on the preceding exact classification of the maximal nonsignable masks. This also supplies a general-purpose quotient algorithm: construct G_Q, contract its components, then solve a small F₂ parity-choice problem on the odd-core triangles.

## 4. Validation and scope

`R762IE_PORT_COMPONENT_QUOTIENT_CHECK.py` (Python 3 stdlib; integer bitmasks only) independently implements (a) component parity and (b) F₂^15 boundary-span elimination. It checks all fifteen R762ID masks, their complete stabilizer orbits, the exact 8/7 obstruction split, and 1,506 additional deterministic Q inputs across the three odd cores (empty/full plus 500 seeded pseudorandom choices per core). It generates `R762IE_EVIDENCE.json`; observed local result: `PASS R762IE port-component quotient and orbit certificate`.

The all-multiplicity quotient theorem follows from the above graph-incidence proof, not numerical sampling. The five-orbit proof uses an exact finite six-axis permutation check plus the independently supplied list of fifteen R762ID masks. R762IB orbit-completeness, R762ID nonsignability classification, native P000 lifting and independent mathematics review remain distinct obligations. This research note does not assert a current TASK CLAIM, Activity identity or PROGRESS.

## 5. Next research units

Derive the five maximal nonsignable masks directly from ternary signed-support reachability without using the R762ID exhaustive classifier; combine the Port quotient with connected-edge selection to build a positive circuit algorithm from histograms; and seek an explicit typed P000-native embedding preserving Cell, Link, force, time and rotation observers.

Control observation: original continuation read `r3-20261122-0025-x6-cont-read-01` concluded FAILED / SOURCE_TREE_TRUNCATED, affecting current owner/CLAIM verification. Scientific portable publication is independent of that read failure.
