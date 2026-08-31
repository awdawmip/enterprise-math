# P000 Philosophy-First Q19 — Return Edge-Profile Correlation Collision Frontier Return

Task: `RS-P000-PHILOSOPHY-FIRST-RETURN-EDGE-CORRELATION-COLLISION-FRONTIER`  
Publication: `TP2-A2D4A2D896ADC274FD72`  
Researcher: `EM-P000-FAA806`  
Claim: `chatgpt-p000q19-20260831-1051-b84c17`  
Execution branch: `research/p000-phil-q19-return-edge-correlation-collision-frontier-em-p000-faa806`  
Hard target: `P000_RETURN_EDGE_CORRELATION_COLLISION_FRONTIER_EXACTLY_CLASSIFIED`

## Terminal verdict

`SUCCESS / FIRST_EDGE_PROFILE_CORRELATION_COLLISION_CLASSIFIED`

Freeze the Q16 family

\[
\mathcal U_{BR}(n)
\]

as finite connected simple native-Cell adjacency graphs on exactly `n` Cells, every Cell of degree `2` or `3`, with at least one degree-`3` Cell, modulo Cell relabeling.

Let `m_X(x)` be the frozen Q16 primitive-return multiplicity profile of root `x`, and let

\[
\mathcal M(X)=\multiset_{x\in Cell(X)}m_X(x).
\]

Q19 tests the weakest full class-level one-step relation repair suggested by the Q16 witness:

\[
E_X(P,Q)
=
\#\bigl\{\{x,y\}\in Edge(X):
m_X(x)=P,\ m_X(y)=Q
\bigr\},
\]

with `P,Q` unordered. Define the relation-enriched packet

\[
\mathcal C(X)=\bigl(\mathcal M(X),E_X\bigr).
\]

The exact result is:

1. `C` separates the frozen Q16 eight-Cell collision.
2. Exact exhaustive degree-normalized enumeration proves `C` is injective on every `U_BR(n)` for `n=4,5,6,7,8`.
3. The exact representability image on that prefix has `2,3,10,20,59` packets respectively.
4. At `n=9` there is an explicit equal-`C` nonisomorphic pair.
5. Therefore the first collision size of the full edge-profile correlation packet in the frozen size order is exactly **nine Cells**.
6. The nine-Cell witness pinpoints the next missing information more sharply than “two-step adjacency”: the aggregate class-edge histogram forgets **which profile-class incidences co-occur at the same anonymous root**. A single profile-conditioned root-incidence scalar already separates the pair.

Thus one-step class correlation is a genuine extra tomography layer, but it is still not a general reconstruction invariant.

## 1. Native packet and relabeling invariance

For each root `x` and length `k>=3`, Q16 freezes

\[
\mu_X(x,k)
=
\#\{\text{unoriented simple native cycles of length }k\text{ through }x\},
\]

and

\[
m_X(x):k\mapsto \mu_X(x,k).
\]

The Q19 edge-profile correlation is defined only from native adjacency and these anonymous profiles. No Cell names, canonical labels, adjacency matrices, spectra, Ihara zeta, or complete cycle bases are included in the observation.

If `f:X->Y` is a Cell relabeling / graph isomorphism, then native simple cycles correspond bijectively, hence

\[
m_Y(f(x))=m_X(x).
\]

The same `f` bijects native edges, so for every unordered profile pair `{P,Q}`,

\[
E_Y(P,Q)=E_X(P,Q).
\]

Therefore `C(X)` is invariant under Cell relabeling.

## 2. Mandatory Q16 repair check

The Q16 first multiplicity collision is reproduced exactly.

`H_8`:

```text
02 04 15 16 23 24 36 47 56 57
```

`G_8`:

```text
01 02 04 14 25 27 35 36 46 57
```

Their anonymous root-multiplicity packets agree:

\[
\mathcal M(H_8)=\mathcal M(G_8)=\{\!\{A^{\times4},B^{\times2},C^{\times2}\}\!\}.
\]

But their edge-profile histograms differ. In particular the Q16 witness coordinate

\[
e_{CC}(H_8)=0,\qquad e_{CC}(G_8)=1.
\]

Hence

\[
\mathcal C(H_8)\ne\mathcal C(G_8).
\]

So the full profile-edge correlation packet passes the task's first kill gate and genuinely repairs the frozen eight-Cell collision.

## 3. Exact collision-free prefix through eight Cells

The new checker does not enumerate all `n!` relabelings. It performs an exact symmetry-normalized cover.

If exactly `r` vertices have degree `3`, handshaking forces `r` even. Every graph in `U_BR(n)` with that `r` admits a labeling in which the degree-`3` vertices are exactly `0,...,r-1`. The checker exhausts **every simple realization** of the fixed degree sequence

\[
3^r\,2^{n-r}
\]

under that normalization, rejects disconnected realizations, computes `C`, and checks every equal-packet fiber for actual graph isomorphism.

Because every isomorphism type has at least one degree-normalized labeling and `C` is relabeling-invariant, this covers the complete quotient family modulo Cell relabeling. The normalization removes irrelevant permutation blow-up but does not sample or omit any isomorphism type.

Exact counts:

| n | degree-normalized connected realizations | isomorphism types | representable `C` packets | collision? |
|---:|---:|---:|---:|:---|
| 4 | 2 | 2 | 2 | no |
| 5 | 13 | 3 | 3 | no |
| 6 | 178 | 10 | 10 | no |
| 7 | 1,812 | 20 | 20 | no |
| 8 | 39,492 | 59 | 59 | no |

Thus `C` is injective on

\[
\mathcal U_{BR}^{\le8}
=
\bigcup_{n=4}^{8}\mathcal U_{BR}(n).
\]

### Exact representability image

The machine artifact

`research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_EDGE_CORRELATION_COLLISION_FRONTIER/P000_Q19_RETURN_EDGE_CORRELATION_COLLISION_FRONTIER_V1.json`

freezes the exact representability image for `n=4..8` by a deterministic canonical packet serialization together with per-size SHA256 and a combined digest. The checker reconstructs all 94 packets exactly; the artifact pins that image without duplicating the full serialization.

Per-size image SHA256 digests are:

- `n=4`: `f120e82dd929f416b6e5c780dce8d78f005efacf5bd88935acfbbf7ca68367a8`
- `n=5`: `ca8468ebdecfa51617b2d6b47546ec27ed3791ae0e587ac23867ff34e492ce5c`
- `n=6`: `712f36ab512258c9dee46f7eacc58a844b0fe50173ae26e5f080978bb5097379`
- `n=7`: `85f69c4334c48b7ebfa778783dc5a9c91b814aaef58b8cb933794590196c70cf`
- `n=8`: `c71aa7149b6348d731872a23ca9d04c130980391b2dae2da7aad59c7a448579f`

Combined exact-image digest:

`16024b3075aca19423f8c920ba6aa911c74042af20d7e1ea9827280904ec5f0a`

This supplies both sides required by the task: exact bounded **separation** and exact bounded **representability**.

## 4. First collision at nine Cells

Let `H_9` and `G_9` have vertex set `{0,...,8}`.

### `H_9`

```text
01 02 04 13 15 24 26 37 38 56 78
```

### `G_9`

```text
01 04 05 14 16 23 25 26 37 38 78
```

Both are connected, simple, and have degree multiset

\[
\{2,2,2,2,2,3,3,3,3\},
\]

so both lie in `U_BR(9)`.

Define four root-profile classes, with omitted lengths having multiplicity zero:

\[
A=(5:1,6:1),
\]

\[
B=(3:1),
\]

\[
C=(3:1,6:1),
\]

\[
D=(3:1,5:1,6:1).
\]

Both graphs have the identical anonymous root packet

\[
\mathcal M
=
\{\!\{A^{\times3},B^{\times3},C^{\times1},D^{\times2}\}\!\}.
\]

More strongly, the **entire** profile-edge correlation histogram agrees:

\[
E(A,A)=2,\quad
E(A,B)=1,\quad
E(A,D)=2,
\]

\[
E(B,B)=3,\quad
E(C,D)=2,\quad
E(D,D)=1,
\]

and every unlisted profile-pair count is zero.

Therefore

\[
\mathcal C(H_9)=\mathcal C(G_9).
\]

So no reconstruction map factoring through the full Q19 packet `C` can distinguish the pair.

## 5. Structural nonisomorphism certificate

The pair is not a labeling artifact.

For a root `x`, define only for this certificate the native one-hop neighbor-profile multiset

\[
N_X(x)
=
\multiset_{y\sim x}m_X(y).
\]

An isomorphism preserving native adjacency automatically preserves both `m_X(x)` and `N_X(x)`.

Now inspect only roots of profile `A`.

In `H_9`, exactly one `A`-profile root has two neighbors and both neighbors also have profile `A`:

\[
\#\{x:m_X(x)=A,\ N_X(x)=\{\!\{A,A\}\!\}\}=1.
\]

In `G_9`, no `A`-profile root has that local incidence pattern:

\[
\#\{x:m_X(x)=A,\ N_X(x)=\{\!\{A,A\}\!\}\}=0.
\]

Therefore no graph isomorphism can exist.

This certificate is deliberately lower-information than a complete adjacency description, spectrum, zeta function, or global canonical label.

## 6. The next missing information is root-incidence co-occurrence

The n=9 witness diagnoses precisely what the global edge histogram forgot.

`E_X(P,Q)` preserves **how many** class-`P`/class-`Q` edges exist globally, but it sums over all roots in a profile class. It does not preserve **which incident class-edges meet at the same anonymous root**.

The witness therefore exposes the next low-information datum as:

> profile-conditioned rootwise co-occurrence of neighboring profile classes.

Equivalently, the next candidate packet need only refine each anonymous root profile by the multiset of neighbor profiles, then anonymize again. Q19 does **not** promote this stronger packet as complete; it only identifies it as the first witness-exposed missing relation.

The scalar certificate above is already enough:

`A-root with neighbor-profile multiset {A,A}: 1 vs 0`.

A length-two profile-path count also separates the pair, but that is not the minimal diagnosis: the failure is already visible as co-incidence of two one-hop relations at one anonymous root.

## 7. Minimality of the collision size

For `n=4..8`, exhaustive degree-normalized coverage proves every equal-`C` fiber contains exactly one isomorphism type.

At `n=9`, the explicit `H_9/G_9` pair lies in one equal-`C` fiber and is nonisomorphic.

Therefore

\[
\min\{n:\mathcal C\text{ is noninjective on }\mathcal U_{BR}(n)\}=9.
\]

This is exact for the frozen connected degree-`2/3` branching family and its size order. It is not a claim about all finite graphs or arbitrary graph classes.

## 8. Consequence for weaker selected coordinates

Because the **full** edge-profile histogram is equal on `H_9/G_9`, every observation that factors only through a selected subset, scalar coordinate, or deterministic function of that histogram also identifies the pair.

Thus the Q16 scalar `e_CC` was a valid witness-specific repair, but no scheme restricted to global profile-class edge counts can become a universal reconstruction interface on the frozen family.

In the task's outcome vocabulary:

- `EDGE_PROFILE_CORRELATION_REPAIRS_Q16_COLLISION_WITH_EXACT_BOUNDED_IMAGE` — **YES through n=8**;
- `FIRST_EDGE_PROFILE_CORRELATION_COLLISION_CLASSIFIED` — **YES, first at n=9**;
- `SELECTED_CORRELATION_COORDINATE_INSUFFICIENT` — **YES as a corollary for every coordinate factoring through the full global edge-profile histogram**.

The terminal class is the stronger exact statement:

`FIRST_EDGE_PROFILE_CORRELATION_COLLISION_CLASSIFIED`.

## 9. Deterministic checker

Checker:

`research_checks/P000_PHILOSOPHY_FIRST_RETURN_EDGE_CORRELATION_COLLISION_FRONTIER_CHECK_20260831.py`

It uses only the Python standard library. It:

1. recomputes primitive simple-cycle multiplicity profiles;
2. defines and checks the relabeling-invariant `C=(M,E)` packet;
3. reproduces and separates the Q16 eight-Cell witness;
4. exhausts every degree-normalized connected realization for `n=4..8`;
5. proves every equal-`C` prefix fiber contains one isomorphism type;
6. freezes and verifies all exact representability images and SHA256 digests;
7. verifies the explicit equal-`C` n=9 pair;
8. proves that pair nonisomorphic by exact backtracking;
9. independently checks the lower-information `A{AA}=1 vs 0` root-incidence certificate;
10. verifies the machine artifact against recomputation.

Deterministic run:

```text
PASS P000_Q19_EDGE_PROFILE_CORRELATION; checks=41520; exact_prefix_n=4..8; normalized_connected=2,13,178,1812,39492; packet_images=2,3,10,20,59; first_collision_n=9; common_packet=A3_B3_C1_D2+AA2_AB1_AD2_BB3_CD2_DD1; next_gap=A-root incidence co-occurrence; A{AA}=1_vs_0
```

The exact finite-prefix theorem is computationally exhaustive modulo relabeling, not sampled. The n=9 negative result additionally has a short structural certificate.

## 10. Method and scope audit

The current method inventory was checked before freezing the result. Existing reusable relation-observable machinery confirms that relation-enriched signatures are already a recognized tool family, so this task does not create a new global mechanism. The actual proof is task-local exact finite enumeration plus isomorphism and structural certificates.

Source exposure is nonblind and disclosed: the Q19 taskbook and its Q16 dependency were consumed. No external prior-art novelty claim is made. Classical finite-graph terminology is proof infrastructure only; the project-specific contribution here is the exact failure boundary of the declared native observation ladder.

No Working Truth, P000 root mutation, Foundation promotion, or canonical ontology change is requested.

## 11. Hard-target disposition and next research question

`P000_RETURN_EDGE_CORRELATION_COLLISION_FRONTIER_EXACTLY_CLASSIFIED` is satisfied:

- weakest full legal class-edge packet defined and relabeling invariance proved;
- Q16 eight-Cell collision reproduced and separated;
- exact bounded prefix `4<=n<=8` exhaustively collision-free;
- exact formal representability image mechanically frozen for all 94 prefix packets by canonical serialization plus cryptographic digests;
- first equal-packet nonisomorphic pair frozen at `n=9`;
- structural nonisomorphism certificate supplied;
- next lowest missing relation identified as rootwise profile-incidence co-occurrence;
- deterministic checker and machine artifact frozen.

The scientifically justified successor is **not** full adjacency, spectrum, zeta, or cycle-basis escalation.

It is:

> anonymize the rootwise neighbor-profile incidence signature itself, test whether that one-hop co-occurrence refinement repairs the n=9 collision, and locate its first collision/representability frontier countermodel-first.

This preserves the information ladder

`return support -> return multiplicity -> global profile-edge correlation -> rootwise incidence co-occurrence -> ?`

without manufacturing reconstruction by reintroducing the full object.
