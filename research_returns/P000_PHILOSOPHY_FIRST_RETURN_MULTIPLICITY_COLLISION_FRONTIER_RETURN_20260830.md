# P000 Philosophy-First Q16 — Return Multiplicity Collision Frontier Return

Task: `RS-P000-PHILOSOPHY-FIRST-RETURN-MULTIPLICITY-COLLISION-FRONTIER`  
Publication: `TP2-46C9AF42B85B2C948F8D`  
Researcher: `EM-P000-6B3CB6`  
Claim: `chatgpt-p000q16-20260830-2258-3f8c21`  
Execution branch: `research/p000-phil-q16-return-multiplicity-collision-frontier-em-p000-6b3cb6`  
Hard target: `P000_RETURN_MULTIPLICITY_COLLISION_FRONTIER_EXACTLY_CLASSIFIED`

## Terminal verdict

`SUCCESS / FIRST_EQUAL_MULTIPLICITY_NONISOMORPHIC_PAIR_CLASSIFIED`

The anonymous primitive-return multiplicity packet survives strictly beyond the four-Cell class `U_BR4`, but it is **not** a general reconstructive invariant even on the smallest natural connected subcubic branching size-order tested here.

Freeze

\[
\mathcal U_{BR}(n)
\]

to be finite connected simple native-Cell adjacency graphs on exactly `n` Cells, every Cell of degree `2` or `3`, with at least one degree-`3` Cell, modulo Cell relabeling / graph isomorphism. Scan the family by increasing `n`.

Then:

1. `n<4` cannot branch.
2. Exact exhaustive enumeration proves the anonymous return-multiplicity packet is injective on every `U_BR(n)` for `n=4,5,6,7`.
3. At `n=8` there is an explicit equal-packet nonisomorphic pair.
4. Therefore the **first collision size in this declared family is exactly eight Cells**.
5. The witness shows what multiplicity forgot: not another per-root count, but the one-step native adjacency correlation between anonymous root-multiplicity profile classes. A single scalar edge-class count already separates the pair.

No claim is made that this adjacency-correlation repair is globally complete, nor that eight Cells is the first collision in every conceivable larger graph class. The minimality statement is exactly for the frozen `U_BR(n)` size-order above.

## 1. Frozen primitive-return semantics

Q13 is consumed without changing its definitions.

A primitive return through root `x` is an **unoriented simple native-adjacency cycle** containing `x`. For `k>=3` define

\[
\mu_X(x,k)
=
\#\{\text{unoriented primitive returns of length }k\text{ through }x\}.
\]

The root profile is the finite map

\[
m_X(x):k\longmapsto \mu_X(x,k),
\]

and the anonymous packet is

\[
\mathcal M(X)
=
\multiset_{x\in Cell(X)} m_X(x).
\]

Cell identity, canonical labels, adjacency matrices, full cycle bases, spectra and Ihara-zeta data are not probe output.

The task asks whether this first Q13 repair is genuinely reconstructive beyond `U_BR4`, so the search order is countermodel-first.

## 2. Exact collision-free prefix `n=4..7`

The deterministic checker enumerates **every labeled simple graph** satisfying the frozen degree and connectivity constraints, computes `M`, and only then tests whether any equal-packet pair can be nonisomorphic.

The exact counts are:

| n | labeled models in `U_BR(n)` | isomorphism types | representable multiplicity packets | collision? |
|---:|---:|---:|---:|:---|
| 4 | 7 | 2 | 2 | no |
| 5 | 100 | 3 | 3 | no |
| 6 | 1,690 | 10 | 10 | no |
| 7 | 34,440 | 20 | 20 | no |

Thus `M` is injective on the exact bounded union

\[
\mathcal U_{BR}^{\le7}
=
\bigcup_{n=4}^{7}\mathcal U_{BR}(n).
\]

This is not sampling. For each `n`, the checker uses the handshaking constraint: if exactly `r` vertices have degree `3`, then `r` is even and

\[
|E| = n+\frac r2.
\]

It enumerates all edge sets of those cardinalities, rejects degree/connectivity failures, computes every unoriented simple cycle, forms the anonymous packet, and performs exact isomorphism backtracking inside each packet fiber.

### Exact representability image

The machine artifact

`research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_MULTIPLICITY_COLLISION_FRONTIER/P000_Q16_RETURN_MULTIPLICITY_COLLISION_FRONTIER_V1.json`

lists all representable formal packets for `n=4,5,6,7`: exactly `2+3+10+20=35` packets.

Per-size image digests are:

- `n=4`: `7f3e64e5aa1bc09ca670921483ec634bc185c0ccf49055968857aeb62c0f9a24`
- `n=5`: `32c14a8c2d811c910733bbca5f29fafde34b6a73df7d4a02f312c53560fc6e93`
- `n=6`: `6cb627ace9d539b96cb9953ee773dbcc68e6bb96004bf958db76ede1bcf9103e`
- `n=7`: `f7ee6ecaaf16dba6c0da8e1f08182a431abedb0ab82358004ecf048a0655133b`

Combined exact-image digest:

`e3c294c684bf89d62646510eefe945f5ab2f1b92fbba3ef7e70a02496f9c3ceb`

So the bounded positive theorem is simultaneously a separation theorem and an exact representability-image classification.

## 3. First collision at eight Cells

Let `H_8` and `G_8` have vertex set `{0,...,7}`.

### `H_8`

Edge set:

```text
02 04 15 16 23 24 36 47 56 57
```

### `G_8`

Edge set:

```text
01 02 04 14 25 27 35 36 46 57
```

Both are connected simple graphs with degree multiset

\[
\{2,2,2,2,3,3,3,3\},
\]

so both lie in `U_BR(8)`.

Their total primitive-cycle counts also agree:

\[
\#C_3=2,\qquad
\#C_6=1,\qquad
\#C_7=2,\qquad
\#C_8=1,
\]

with no primitive returns of lengths `4` or `5`.

More strongly, their anonymous **rootwise multiplicity packets agree exactly**.

Define three root-profile types, with omitted lengths carrying multiplicity zero:

\[
A=(3:1,\;6:1,\;7:2,\;8:1),
\]

\[
B=(3:1,\;7:1,\;8:1),
\]

\[
C=(6:1,\;7:2,\;8:1).
\]

Then

\[
\mathcal M(H_8)
=
\mathcal M(G_8)
=
\{\!\{A^{\times4},B^{\times2},C^{\times2}\}\!\}.
\]

Therefore no reconstruction map which factors only through `M` can distinguish the two states.

## 4. Structural nonisomorphism certificate

The collision is not a labeling artifact.

The profile `C` occurs at exactly two Cells in each graph. Because root multiplicity profile is an isomorphism invariant, any graph isomorphism must map the two-element `C`-class of one graph onto the two-element `C`-class of the other.

But:

- in `H_8`, the `C` Cells are `3` and `7`, and `37` is **not** an edge;
- in `G_8`, the `C` Cells are `3` and `6`, and `36` **is** an edge.

Hence the number

\[
e_{CC}(X)
=
\#\{\text{native edges whose two endpoints both have profile }C\}
\]

satisfies

\[
e_{CC}(H_8)=0,\qquad e_{CC}(G_8)=1.
\]

An isomorphism must preserve both the profile class and native adjacency, so no isomorphism can exist.

This is a direct structural certificate; no canonical labeling, spectrum or almost-complete graph description is needed.

## 5. The first missing information after multiplicity

Q13 showed that return-support loses **how many** equal-length returns occur. Q16 now shows that even after restoring all per-root multiplicities, the anonymous multiset forgets **where those root profiles sit relative to one another**.

The witness isolates the missing datum at the lowest relation level needed here:

> one-step native adjacency correlation between anonymous return-multiplicity profile classes.

For the exact pair, the single scalar `e_CC` is already sufficient.

Equivalently, if one forms the task-local edge-profile histogram

\[
E_X(P,Q)
=
\#\{\{x,y\}\in Edge(X):m_X(x)=P,\;m_X(y)=Q\},
\]

then the equal root-packet fiber splits immediately. In fact:

- `H_8`: `E(A,A)=2`, `E(A,B)=4`, `E(A,C)=4`, `E(C,C)=0`;
- `G_8`: `E(A,A)=3`, `E(A,B)=4`, `E(A,C)=2`, `E(C,C)=1`.

This does **not** promote the entire histogram as a universal next ontology. The scientifically justified statement is narrower: the first exact multiplicity collision is caused by erasure of relational placement/correlation, and one native adjacency-class bit/count witnesses it.

Any probe that still factors only through the anonymous root multiset necessarily identifies `H_8` and `G_8`.

## 6. Why eight is the first collision in the frozen family

A branching Cell in a finite simple graph requires three distinct neighbors, so `n>=4`.

The exact enumeration proves that every equal-`M` fiber for `n=4,5,6,7` consists of a single isomorphism type.

The explicit `H_8/G_8` fiber contains at least two nonisomorphic types.

Therefore

\[
\min\{n:\mathcal M\text{ is noninjective on }\mathcal U_{BR}(n)\}=8.
\]

This is a theorem about the declared connected min-degree-two subcubic branching family and its exact size order, not about arbitrary finite graphs.

## 7. Deterministic checker

Checker:

`research_checks/P000_PHILOSOPHY_FIRST_RETURN_MULTIPLICITY_COLLISION_FRONTIER_CHECK_20260830.py`

It uses only the Python standard library. It:

1. exhausts every labeled model in `U_BR(n)` for `n=4..7`;
2. recomputes every primitive simple cycle and root multiplicity profile;
3. proves every equal-packet prefix fiber is one isomorphism type;
4. freezes the exact 35-packet representability image and SHA256 digests;
5. verifies both eight-Cell witnesses are connected and degree-valid;
6. verifies the common packet `A^4 B^2 C^2`;
7. verifies the witnesses are nonisomorphic;
8. verifies the profile-`C` adjacency certificate `0` versus `1`;
9. verifies the machine artifact against the independently recomputed exact image.

Deterministic run:

```text
PASS P000_Q16_RETURN_MULTIPLICITY; checks=36276; prefix_labeled=7,100,1690,34440; prefix_iso_packets=2,3,10,20; first_collision_n=8; packet=A4_B2_C2; C_edge=0_vs_1
```

The exhaustive computation supports the exact finite prefix and first-size minimality. The nonisomorphism and missing-information conclusions also have the short structural proof above.

## 8. Hard-target disposition

`P000_RETURN_MULTIPLICITY_COLLISION_FRONTIER_EXACTLY_CLASSIFIED` is satisfied by:

- `FIRST_EQUAL_MULTIPLICITY_NONISOMORPHIC_PAIR_CLASSIFIED` — **YES**;
- exact first collision size in the frozen `U_BR(n)` order — **8**;
- `RETURN_MULTIPLICITY_INJECTIVE_ON_DECLARED_BOUNDED_FAMILY` — **YES on the exact prefix `4<=n<=7`**;
- `MULTIPLICITY_REPRESENTABILITY_GAP_EXACTLY_CLASSIFIED` — **YES for the exact prefix image**, with all 35 representable packets machine-frozen;
- lowest witness-exposed missing information — **native adjacency correlation between anonymous root-profile classes**, with `e_CC=0` versus `1`.

The candidate interface is therefore falsified as a general reconstruction invariant before importing stronger classical graph spectroscopy.

## 9. Residue and next research question

The next justified question is not “add a full adjacency matrix.”

It is:

> How little relational placement information over anonymous return-multiplicity profiles is enough to survive the first eight-Cell collision, and where does that relation-enriched packet first fail?

A natural successor may test a one-step edge-profile correlation packet or an even smaller selected correlation coordinate, countermodel-first and under another exact bounded size order.

No Working Truth, Foundation status, canonical ontology mutation, or novelty claim is requested. Classical finite-graph enumeration and cycle counting are used as proof infrastructure only; the project-specific result is the exact native-observation failure boundary and the low-information relation datum exposed by the first collision.
