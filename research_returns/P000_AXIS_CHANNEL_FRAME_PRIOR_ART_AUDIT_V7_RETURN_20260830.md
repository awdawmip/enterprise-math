# P000 Axis-Channel Frame/Torsor/Connection 外部先例审计 V7 — Research Return

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

Researcher-ID: `EM-P0006DPA7-91C0E7`

Task-ID: `RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT`

Publication-ID: `TP2-5A7C1D9E3B6042F8D117`

Claim-ID: `chatgpt-p0006dpa7-20260830-0910-91c0e7`

Execution branch: `research/p000-axis-channel-frame-prior-art-v7-em-p0006dpa7-91c0e7`

Execution base: `cc69a1b72acba6e75deb590f2c857b425c7058e3`

Hard target:

`P000_AXIS_CHANNEL_FRAME_CONNECTION_EXTERNAL_DUPLICATION_BOUNDARY_CLASSIFIED`

Terminal class:

`CLASSICAL_FRAME_CONNECTION_CORE_DUPLICATED_P000_COMPOUND_SEMANTICS_UNMATCHED`

## 1. Executive result

The external-duplication boundary is sharp.

At the **abstract mathematical level**, nearly all of the Gen9/Gen10 frame machinery is classical:

- automorphism-invariance as an obstruction to definable/canonical choice;
- the natural `S6` pointwise-stabilizer sequence `(6-k)!` and the five-point base;
- the set of six-axis/six-channel bijections as an `S6` torsor;
- a frame/section as a torsor or principal-bundle trivialization;
- edge transports, path composition, parallel transport and loop holonomy;
- vertex-wise gauge changes and endpoint conjugation of edge transport;
- trivial-holonomy synchronization and reconstruction from one seed frame;
- re-expression of a channel-indexed two-index datum in an axis frame.

Those items must **not** be described later as new P000 mathematics.

The main residual P000-specific object is not the torsor/connection machinery itself. It is the **compound semantic guard** imposed on that machinery:

`opaque native Cell identity`
`+ globally named native-axis sort`
`+ local PF-10 presentation-channel sort`
`+ carrier/readout kept non-identifying`
`+ local channel S6 treated as presentation gauge`
`+ explicit no-quotient native-state rule`.

The audit found no material exact external duplicate of that exact compound package. This is only a `NO_MATERIAL_MATCH` boundary. It is **not** a novelty, inventive-step, patentability or originality conclusion.

A second important finding is terminological:

> In standard bundle/connection language, `flat` does **not** mean “all loop holonomies are identity”.

A flat connection may have nontrivial global monodromy. The condition actually equivalent to a single-valued globally parallel frame field is **trivial holonomy / synchronizability / pure-gauge transport**. Gen10's algebra is correct when its use of “flat” is read in that stronger project-local sense, but future text should not rely on that nonstandard shorthand without an explicit definition.

## 2. Mandatory claim map

| # | Gen9/Gen10 claim | Classification | External boundary |
|---|---|---|---|
| 1 | Primitive-preserving automorphisms move every candidate channel, so no canonical definable unique axis-channel choice exists. | `EXACT_DUPLICATE` | Standard model-theoretic principle: definable data are invariant under automorphisms fixing parameters. Gen9 uses only the necessary direction. |
| 2 | Natural `S6` action: after `k` distinct anchors the residual stabilizer has order `(6-k)!`; five anchors are necessary/sufficient in the worst symmetric case. | `EXACT_DUPLICATE` | Ordinary pointwise-stabilizer/base-size computation for `Sym(6)`. |
| 3 | A six-element unlabeled local channel frame is an `S6`-torsor choice/trivialization. | `EXACT_DUPLICATE` | `Bij(A,C_x)` is a principal homogeneous `Sym(C_x)`-set by postcomposition. Choosing one frame chooses a torsor point and identifies the torsor with `S6`. |
| 4 | Per-Cell frame field versus one seed frame + invertible edge connection. | `EXACT_DUPLICATE` | Classical graph synchronization/local-system/principal-bundle pattern, with global reconstruction exactly under trivial loop holonomy. |
| 5 | Graph/discrete connection, inverse edge transport, path composition and loop holonomy. | `EXACT_DUPLICATE` | Standard connection/parallel-transport machinery. |
| 6 | Gauge change `T_xy' = g_y T_xy g_x^{-1}`; based holonomy changes by conjugation; identity/nonidentity and conjugacy class are invariant. | `EXACT_DUPLICATE` | Standard vertex-gauge/vertical bundle-automorphism law, up to orientation convention. |
| 7 | A global parallel frame exists exactly when the independently supplied connection has trivial loop holonomy. | `EXACT_DUPLICATE` with terminology guard | The equivalence is classical for trivial holonomy/synchronizability. `flat => global frame` is false in standard terminology without the extra trivial-monodromy condition. |
| 8 | Partial actions / groupoids / inverse semigroups can model typed/domain-sensitive local transport. | `PARTIAL_ANTECEDENT` | Strong standard antecedents exist, but they do not generate the project-specific missing P000 relation or semantic guard. |
| 9 | `PASS_x(E_i,E_j)=M_x[f_x(E_i),f_x(E_j)]` is the framed rewrite of `M_x`. | `EXACT_DUPLICATE` | Standard pullback/reindexing. If `M_x` is an endomorphism matrix, this is permutation similarity/change-of-basis; for a count/relation table, “reindexing/pullback” is the precise statement. |
| 10 | P000 no-quotient + opaque native Cell + native-axis typing + carrier-readout separation. | `NO_MATERIAL_MATCH` | Components are standard separately (many-sorted typing, vertical gauge, representation/frame separation), but no exact duplicate of the compound project ontology was found. `NO_MATERIAL_MATCH != NOVELTY`. |

The machine-readable form is frozen in:

`research_artifacts/P000_AXIS_CHANNEL_FRAME_PRIOR_ART_AUDIT_V7/claim_map.json`.

## 3. Claim 1 — definability under automorphisms

Gen9's obstruction has the following form.

Let the present primitive structure contain:

- a fixed Cell `x`;
- fixed named axes `A={E_1,...,E_6}`;
- a six-element presentation-channel set `C_x`;
- no primitive relation selecting a particular `E_i <-> c`;
- an automorphism/reindexing group acting transitively on `C_x` while fixing the P000 parameters used in the attempted definition.

If a formula over those fixed parameters defined a unique channel `c`, every automorphism fixing those parameters would preserve the formula and therefore fix `c`. A transitive nontrivial action contradicts this.

This is standard model-theoretic reasoning. Hodges' automorphism treatment supplies the general framework; Berkeley model-theory notes state the stronger definable-closure/orbit criterion in their monster-model setting. The P000 argument only needs:

`definable over A => fixed by Aut(-/A)`.

It does **not** need the converse “automorphism-invariant => definable” in arbitrary structures.

Therefore the Gen9 no-canonical-choice argument is not a new theorem form. The P000-specific content lies in proving that the selected finite PF-10 countermodel really has the claimed primitive-preserving `S6` reindexing symmetry while native axes and Cell identity remain fixed.

## 4. Claim 2 — `(6-k)!` and the five-anchor bound

For the natural action of `S_6` on six points, the pointwise stabilizer of `k` distinct fixed points is canonically `S_{6-k}`. Hence:

| `k` | pointwise stabilizer | order |
|---:|---|---:|
| 0 | `S6` | 720 |
| 1 | `S5` | 120 |
| 2 | `S4` | 24 |
| 3 | `S3` | 6 |
| 4 | `S2` | 2 |
| 5 | `S1` | 1 |
| 6 | `S0`/trivial | 1 |

This is exactly the Gen9 sequence.

Permutation-group terminology calls a set with trivial pointwise stabilizer a **base**. For the natural action of `S_n`, `n-1` points form a base and fewer do not. Thus the Gen9 “five anchors plus bijectivity force the sixth” is exactly the `n=6` instance of the natural-action base-size fact.

The five-anchor encoding also does not reduce information:

`6P5 = 6! = 720`.

So Gen10's statement that five anchors are tuple-smaller but not information-smaller is an elementary finite reparametrization of the same torsor.

The checker independently enumerates all `720` permutations and reproduces the stabilizer counts.

## 5. Claim 3 — `AXIS_CHANNEL_FRAME` as torsor/frame data

Fix the named axis set `A` and the local channel set `C_x`. Define

`Frames_x = Bij(A,C_x)`.

`Sym(C_x)` acts on `Frames_x` by postcomposition:

`g · f = g ∘ f`.

For any `f,h in Frames_x` there is a unique

`g = h ∘ f^{-1}`

with `g∘f=h`. Hence the action is free and transitive: `Frames_x` is a torsor.

This is exactly the principal-homogeneous-space pattern. The Stacks Project gives the standard simply-transitive torsor definition, and standard bundle notes identify a section with a trivialization of a principal bundle. In the present finite/discrete setting no smooth structure is needed.

Consequences:

1. “There are `6!` frames” is the cardinality of the torsor.
2. “No preferred frame exists before symmetry breaking” is the absence of a distinguished torsor point.
3. “Choose one frame” is “choose one torsor point/trivialization”.
4. A per-Cell frame field is naturally a section of the family of frame torsors over Cells.

The P000-specific restriction is not the torsor notion. It is what the two sides of the bijection mean: globally named **native P000 axes** versus **local PF-10 presentation channels**, with explicit prohibitions on changing Cell identity or promoting channel gauge to native rotation.

## 6. Claims 4–7 — connection, synchronization, gauge and holonomy

### 6.1 Frame-induced edge transport

Given frames `f_x:A->C_x` and `f_y:A->C_y`, define

`T_xy = f_y ∘ f_x^{-1}: C_x -> C_y`.

Then automatically:

`T_yx = T_xy^{-1}`.

For a path `gamma=(x_0,...,x_n)`,

`T_gamma = T_{x_{n-1}x_n} ∘ ... ∘ T_{x_0x_1}`

telescopes to

`T_gamma = f_{x_n} ∘ f_{x_0}^{-1}`.

For a loop at `x_0` this is the identity.

Nothing here is P000-specific as abstract mathematics.

### 6.2 Converse: one seed frame + transport

Take one seed frame at `x_0`. Define a candidate frame at `x` by transporting the seed along a path.

This is single-valued exactly when two different paths from `x_0` to `x` give the same transport, equivalently when every based loop has identity holonomy.

Gao–Brodzki–Mukherjee formulate the corresponding graph synchronization problem in principal-bundle language and state that triviality of holonomy dictates synchronizability. This is a very close external antecedent to Gen10, not merely an analogy.

Thus the correct classical boundary is:

`global parallel frame extending a seed`
`<=>`
`trivial holonomy / synchronization consistency`.

### 6.3 Important terminology guard: flat is weaker

Standard geometry distinguishes:

- local flatness / zero curvature;
- global holonomy/monodromy.

A flat connection can have nontrivial holonomy around noncontractible loops. In graph settings this distinction is especially important because a graph is one-dimensional: local curvature language may be vacuous or be imposed only after adding 2-cells, while cycle holonomy can still be nontrivial.

Therefore the phrase

`flat connection <=> global frame`

is too strong under ordinary terminology.

Future P000 text should prefer one of:

- `TRIVIAL_HOLONOMY_CONNECTION`;
- `SYNCHRONIZABLE_EDGE_TRANSPORT`;
- `PURE_GAUGE_EDGE_TRANSPORT`;
- or explicitly define `P000_FLAT := all loop holonomies identity`.

The accepted Gen10 proof itself already uses the stronger all-loops-identity condition, so this is a terminology correction, not a mathematical refutation of the construction.

### 6.4 Gauge transformation

Under local presentation changes `g_x in Sym(C_x)`,

`f_x' = g_x ∘ f_x`.

Compatibility gives

`T_xy' = g_y ∘ T_xy ∘ g_x^{-1}`.

For a loop based at `x`:

`Hol_x'(gamma)=g_x ∘ Hol_x(gamma) ∘ g_x^{-1}`.

Thus:

- exact holonomy element depends on the chosen local presentation;
- identity versus nonidentity is invariant;
- conjugacy class is invariant.

This is standard gauge behavior. Standard principal-bundle notes define the gauge group as automorphisms covering the identity on the base. That observation is useful for P000: keeping opaque native Cell identity fixed while changing channel presentation is not an exotic gauge rule; it is the usual vertical-gauge pattern specialized to the P000 sorts.

## 7. Claim 8 — partial actions, groupoids and inverse semigroups

The prior Gen6 audit already found these as standard adjacent frameworks. V7 sharpens their role.

Exel's classical result constructs an inverse semigroup `S(G)` whose actions correspond to partial actions of `G`. The symmetric inverse semigroup is the standard algebra of partial bijections. Groupoids likewise encode source/target-aware arrows with partial composition.

Therefore the following design move is standard in abstract form:

> replace globally total transformations by explicitly domain-typed partial arrows and compose only where source/target data match.

But that standard formalism does **not** answer the P000-specific existence question:

- which Cells/axes/channels constitute the domain;
- what native relation supplies a mixed-support arrow;
- what payload is transported;
- whether the arrow preserves opaque native Cell identity;
- whether it is a presentation morphism or a native spatial rotation;
- whether carrier equality is allowed to identify native states.

So claim 8 is `PARTIAL_ANTECEDENT`, not `EXACT_DUPLICATE` of the P000 semantics.

## 8. Claim 9 — `PASS` is ordinary change of frame

Gen10 defines

`PASS_x(E_i,E_j)=M_x[f_x(E_i),f_x(E_j)]`.

This is exactly the pullback/reindexing of the two-index channel datum `M_x` along the frame bijection.

Under a presentation reindexing `g_x`:

`f_x' = g_x∘f_x`

and

`M_x'(g_x(c),g_x(d))=M_x(c,d)`,

so:

`PASS_x'(E_i,E_j)=PASS_x(E_i,E_j)`.

This is standard coordinate/frame invariance.

There is one wording guard. If `M_x` is only a passage-count matrix or a binary two-index relation, the precise language is **simultaneous reindexing / pullback**. If an additional linear-operator semantics is authorized, then in matrix notation this becomes the familiar permutation similarity/conjugation formula. The MIT change-of-basis reference covers that stronger linear case.

Hence `PASS` itself cannot support a novelty claim.

## 9. Claim 10 — what is actually P000-specific?

The audit separated the compound package into standard ingredients and project-specific assembly.

### 9.1 Standard ingredients

The following are standard individually:

1. **Many-sorted typing.** Model theory routinely uses separate sorts with typed functions/relations. So merely declaring `Cell x Axis x Channel` is not novel.
2. **Gauge fixes the base.** Principal-bundle gauge transformations are automorphisms over the identity base. So changing a local frame while fixing the underlying Cell is standard.
3. **Abstract object versus coordinates/frame.** Bundle, tensor and representation theory routinely distinguish the object from its chosen local trivialization or coordinates.
4. **No preferred torsor point.** Standard torsor theory already captures “many equivalent frames with no canonical one”.

### 9.2 Compound P000 residue

What the audited sources did **not** duplicate exactly is the full operational package:

- a native Cell has an opaque project-level identity;
- that identity is not a six-coordinate tuple and is not defined by the FCC carrier;
- the six native axes are a globally named P000 sort;
- the six PF-10 channels are local presentation slots, not those axes;
- a frame is a downstream cross-sort relation, not a change in root ontology;
- channel `S6` is presentation/gauge symmetry, not a native `S6` spatial rotation group;
- FCC carrier/readout equality cannot quotient or identify native Cells;
- native adjacency/rotation claims must be proved independently of local channel-state symmetry.

This exact conjunction is `NO_MATERIAL_MATCH` in the audited literature.

That is a meaningful engineering/ontology boundary, but the permitted statement is only:

> “This audit found no material exact external duplicate of the compound P000 semantic package.”

It is **not** permitted to infer:

> “Therefore the package is mathematically novel.”

## 10. Negative-search discipline

Searches included direct terms around:

- `AXIS_CHANNEL_FRAME`;
- `opaque Cell identity`;
- `native axis typing`;
- `carrier readout`;
- `no-quotient Cell identity axis channel`.

No material mathematical duplicate was found. Unrelated telecommunications and biology uses of “cell identity” were excluded.

This exact-phrase result has low independent novelty weight. The more important negative boundary comes from concept decomposition: standard literature covers the separate mechanisms very well, but none of the audited sources imposed the exact P000 conjunction described above.

The search ledger records the exact queries and sources at:

`research_artifacts/P000_AXIS_CHANNEL_FRAME_PRIOR_ART_AUDIT_V7/source_ledger.json`.

## 11. Source ledger — load-bearing references

### S01 — Hodges, Model Theory

Wilfrid Hodges, *Model Theory*, Cambridge University Press, 1993, Chapter 4 “Automorphisms”.

DOI: `10.1017/CBO9780511551574.006`

Use: standard automorphism framework for definability/canonicality.

### S02 — Berkeley model-theory notes

Leonard Tomczak, *Model Theory – Lecture Notes*, 2023, Proposition 7.5.

URL: `https://math.berkeley.edu/~ltomczak/notes/Lent2023/ModelTheory_Notes.pdf`

Use: precise definable-closure / automorphism-orbit statement in the stated setting; especially the universally safe direction “definable implies automorphism invariant”.

### S03 — Godsil–Meagher

Christopher Godsil and Karen Meagher, *Erdős–Ko–Rado Theorems: Algebraic Approaches*, CUP, 2015, Chapter 14.

DOI: `10.1017/CBO9781316414958.015`

Use: pointwise stabilizer of `t` distinct elements in `Sym(n)` has size `(n-t)!`.

### S04 — Bailey–Cameron base-size survey

Robert F. Bailey and Peter J. Cameron, *Base sizes, metric dimension and other invariants of groups and graphs*.

URL: `https://maths.qmul.ac.uk/~pjc/preprints/bsod.pdf`

Use: standard definition of a permutation-group base as a set with trivial pointwise stabilizer.

### S05 — Stacks Project torsors

The Stacks Project, Section 39.11, Principal homogeneous spaces.

URL: `https://stacks.math.columbia.edu/tag/0499`

Use: torsor as simply transitive action; trivial torsor iff section.

### S06 — Cohen fiber-bundle notes

Ralph L. Cohen, *The Topology of Fiber Bundles / Math 215B notes*.

URL: `https://math.stanford.edu/~ralph/math215b/book.pdf`

Use: principal bundle trivial iff section; gauge group as bundle automorphisms over the identity base.

### S07 — Gao–Brodzki–Mukherjee

Tingran Gao, Jacek Brodzki, Sayan Mukherjee, “The Geometry of Synchronization Problems and Learning Group Actions”, *Discrete & Computational Geometry* 65(1) (2021), 150–211.

DOI: `10.1007/s00454-019-00100-2`

URL: `https://eprints.soton.ac.uk/id/eprint/430926`

Use: connected-graph synchronization as flat principal `G`-bundle geometry; trivial holonomy determines synchronizability.

### S08 — Exel

Ruy Exel, “Partial actions of groups and actions of inverse semigroups”, *Proceedings of the American Mathematical Society* 126(12) (1998), 3481–3494.

DOI: `10.1090/S0002-9939-98-04575-4`

URL: `https://arxiv.org/abs/funct-an/9511003`

Use: partial action / inverse-semigroup correspondence.

### S09 — Munn

W. D. Munn, “The characters of the symmetric inverse semigroup”, *Mathematical Proceedings of the Cambridge Philosophical Society* 53(1) (1957), 13–18.

DOI: `10.1017/S0305004100031947`

Use: classical partial-bijection analogue of the symmetric group.

### S10 — MIT change of basis

MIT 18.700 Linear Algebra, Day 10, Proposition 19.

URL: `https://math.mit.edu/~sschiavo/18-700/Lectures/LessonPlan10.pdf`

Use: standard matrix change-of-basis / conjugation formula.

### S11 — Tent–Ziegler many-sorted structures

Katrin Tent and Martin Ziegler, *A Course in Model Theory*, CUP, 2012, §1.2.

DOI: `10.1017/CBO9781139015417`

Use: standard many-sorted typed relation/function semantics.

## 12. Independent exact finite checks

Checker:

`research_checks/P000_AXIS_CHANNEL_FRAME_PRIOR_ART_AUDIT_V7_CHECK_20260830.py`

Frozen checks:

1. claim-map vocabulary and all ten mandatory rows;
2. all source references resolve inside the source ledger;
3. exhaustive enumeration of all `720` elements of `S6`;
4. exact pointwise-stabilizer counts `720,120,24,6,2,1,1`;
5. natural-action base size `5`;
6. `6P5=720=6!`;
7. sampled exact simple-transitivity check for `Bij(A,C)` as an `S6` torsor, with uniqueness searched across all `720` permutations;
8. exhaustive gauge-reindexing regression for an asymmetric six-by-six passage table over all `720` channel permutations;
9. terminology guard explicitly contains both `flat` and `trivial holonomy`;
10. novelty guard is exactly `NO_MATERIAL_MATCH != NOVELTY`.

Local execution result before publication:

`PASS P000_AXIS_CHANNEL_FRAME_PRIOR_ART_AUDIT_V7_CHECK`

with:

`S6 stabilizers: [720, 120, 24, 6, 2, 1, 1]`

and:

`full frames: 720 five-anchor presentations: 720`.

## 13. Required synthesis

The requested synthesis is:

\[
\boxed{
\begin{array}{l}
\text{Gen9/Gen10 的 automorphism obstruction、S_6 五锚点、torsor/frame、}\\
\text{edge connection、parallel transport、gauge、holonomy、trivial-holonomy}\\
\text{synchronization 与 PASS 换框，均属于经典数学。}\\[2mm]
\text{P000 剩余的特殊性主要在这些经典对象被施加的 native typed / no-quotient}\\
\text{/ opaque-Cell / carrier-readout-separation 复合语义，而非经典对象本身。}
\end{array}}
\]

A future P000 manuscript may legitimately say:

> “We instantiate standard torsor/frame/connection and synchronization mathematics inside a P000-specific many-sorted native-identity discipline, and impose a no-quotient separation between native Cell state and carrier/readout presentation.”

It may **not** say, on the basis of Gen9/Gen10:

> “P000 introduces a new theory of torsors, frames, gauge connections, holonomy, permutation-group bases, or change of frame.”

For the exact compound P000 semantics, the strongest allowed statement after this audit is:

> `NO_MATERIAL_MATCH_IN_AUDITED_SOURCES; NOVELTY_UNDECIDED`.

## 14. Driver recommendation

Recommended disposition:

`ACCEPT / FREEZE_CLASSICAL_BOUNDARY_WITH_TERMINOLOGY_GUARD`.

Recommended control-plane consequences:

1. Freeze C01–C07 and C09 as standard mathematical antecedents.
2. Carry C08 only as a standard partial-transport toolkit, not as a P000 theorem.
3. Preserve C10 as project-specific semantics with `NO_MATERIAL_MATCH != NOVELTY`.
4. Replace ambiguous “flat iff global frame” wording with “trivial holonomy/synchronizable iff global parallel frame”, or explicitly define the stronger project-local meaning of `flat`.
5. Do not spend successor research re-proving torsor, gauge, holonomy or the five-anchor `S6` base.
6. If novelty-oriented work continues, search the **compound ontology/semantic separation** and any concrete native base-Cell automorphism criterion, not the classical frame/connection machinery.
