# R762BR — Equivariant Link observation and robust BRC source recovery on the six-Port triad fiber

Date: 2026-11-16 (Asia/Shanghai). **AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED; NOT_REVIEWED.**

Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`. Frozen inputs: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` P000 V5, signed X6 Cell torsor and native triadic balance. Follows conditional R762BP (PR #2517) and R762BQ (PR #2520). This **conditional directed-Link incidence model** has not itself been admitted as the native `TRIADIC_CLOSURE_E` law.

## Carrier and exact observer

Let `B₂` be the 40 permutations of six named force Ports with cycle type `(3,3)`, a pair of unordered oriented triads. Set `U={σ∈B₂:σ(1)=2}`; then `|U|=8`. Each branch is an explicit source-labelled BRC basis element `e_σ`. A directed-Link membership observation is the exact diagonal selector `P_(a,b)(e_σ)=1{σ(a)=b} e_σ`; the individual Boolean readout is `Q_(a,b)(σ)=1{σ(a)=b}`. The carrier keeps branch identity and multiplicity, with no signed force cancellation. The known `Q_(1,2)=1` is not charged.

The stabilizer `G=S_{3,4,5,6}≅S₄` fixes named Ports 1 and 2, transports `σ` by conjugation and sends query names `(a,b)` to `(g(a),g(b))`. A nonadaptive *G-invariant* panel consists of complete query-name orbits. In this theorem each named Link query can be used at most once. For the signed extension, four independent hidden signs on Ports 3..6 are separately queried, with individually charged repeated sign reads allowed.

## Theorem 1 — All equivariant Link panels and their distances

Of 30 possible ordered named Links, twenty are nonconstant on U and decompose into precisely three G-orbits:

- `A={Q_(2,c):3≤c≤6}`, four names;
- `B={Q_(c,1):3≤c≤6}`, four names;
- `C={Q_(a,b):a,b∈{3,4,5,6},a≠b}`, twelve names.

For every state in U, `Q_(2,c)=Q_(c,1)`: the known three-cycle is `1→2→c→1`. The two query names remain distinct measurement calls.

| G-invariant panel | Calls | Distinct codewords (of eight) | Minimum distance | Pairwise distance histogram |
|---|---:|---:|---:|---|
| A or B | 4 | 4 | 0 | 0:4, 2:24 |
| A∪B | 8 | 4 | 0 | 0:4, 4:24 |
| C | 12 | 8 | **4** | 4:12, 6:16 |
| A∪C or B∪C | 16 | 8 | **6** | 6:16, 8:12 |
| A∪B∪C | 20 | 8 | **6** | 6:4, 8:12, 10:12 |

Therefore a nonadaptive G-invariant panel reconstructing the eight labelled BRC branches requires **12** named Link calls (C), compared with five unrestricted named calls proved for R762BQ. C corrects one arbitrary corrupt Boolean answer, including one additional known erasure. Two arbitrary corrupt answers require at least **16** named calls, achieved by A∪C or B∪C. Under the distinct-name restriction, no such panel can correct three arbitrary answer errors, since even the twenty-query panel has distance six. The exact error/erasure condition is `2t+e<d`.

**Proof.** Every `σ∈U` has form `(c,ε)`: choose `c=σ(2)` from four options and one orientation `ε` of the complementary three-cycle on `R_c={3,4,5,6}\\{c}`. A and B are the same one-hot c vector, so their distances are 0 if c agrees, 2 otherwise. C records three directed edges of the complementary cycle. For the four pairs with identical c and opposite orientation, the edge sets are disjoint and their distance is six. For distinct c,c', `R_c∩R_c'` has exactly two Ports. Among the four orientation pairs, two share exactly one directed edge (distance four), two share no directed edge (distance six). There are six unordered pairs c,c', yielding twelve cross-c pairs at distance four and twelve at six. Thus `C:4:12,6:16`. Adding A or B adds two distance units to cross-c pairs and zero to same-c pairs, yielding all histograms. G-invariant panels are unions of the three orbits; only C can distinguish opposite orientations at fixed c, hence 12 is minimal. To increase min distance from 4 to at least 5, A or B must be added, hence 16 is minimal. The maximum with all three orbits is six, proving the correction ceiling by standard minimum-distance coding theory. ∎

**Symmetry of query order.** There is no deterministic *first single informative query* equivariant under all G: every nonconstant query name has orbit size 4 or 12, while an equivariant choice without additional input would have to be G-fixed. An equivariant batch panel such as C is well-defined.

## Theorem 2 — Exact signed BRC fault-tolerance cost

Extend the branch-labelled BRC carrier to `U×{±1}⁴`, 128 states, retaining the four independently observable hidden signs and all Link provenance. If Link panel H has minimum distance d(H) and sign i is separately queried `r_i` times, the full source code has precisely

`d_signed = min(d(H), r₃,r₄,r₅,r₆)`.

Indeed, a pair differing only in the cycle realizes d(H), and a pair differing only in sign i realizes r_i. Every distinct pair differs in at least one component and has no smaller distance. G-invariance forces equal sign repetitions r.

| Arbitrary answer flips t | Link panel | Sign calls per hidden Port | Total atomic queries | Achieved min distance |
|---:|---|---:|---:|---:|
| 0 | C (12) | 1 | **16** | 1 |
| 1 | C (12) | 3 | **24** | 3 |
| 2 | A∪C or B∪C (16) | 5 | **36** | 5 |

All three bounds are attained and optimal under the declared model. Each independent sign requires at least 2t+1 calls, while the Link panel must attain distance greater than 2t. Three arbitrary faults remain uncorrectable under the distinct-Link-name limit, whatever the sign repetition count. The unrestricted seven-bit BRC index and R762BQ's nine unrestricted noiseless atomic queries refer to different resource models.

## Finite proof witness and exact validation

`R762BR_SYMMETRIC_LINK_OBSERVER_VERIFY.js` enumerates all 720 six-Port permutations and selects the 40 labelled `(3,3)` permutations and eight conditional states. It computes all seven nonempty orbit unions and their exact 28-pair Hamming histograms; checks all 24 S₄ conjugations and 3,840 named-query covariance identities; and verifies three signed panels on all 128 states each, comparing `C(128,2)=8128` codeword pairs each time. The evidence is `R762BR_SYMMETRIC_LINK_OBSERVER_EVIDENCE.json`. Exact Boolean/integer branch-incidence operations only; no physical time or classical trigonometric dynamics is simulated.

The general mathematical proof is independent of finite testing. Current review: **NOT_REVIEWED**; no Lean/formal checker is claimed.

## Provenance and next question

- P000 frozen Source: `a72226e2430ffa4786321ac86e7f0c599d5f0389`; fixed three-force arity, signed X6 axes, pairwise PERP_E = native 120 degrees.
- R762BP author-side PR #2517@`131bd4d77341d0fc16e9a25c85fe44ac4d5ce726`; original Source HANDOFF `emr3-20261116-0042-r762bp-native-source-handoff-v1` is `SUCCEEDED / SOURCE_HANDOFF_PUBLISHED` at `8cdd69ab56c8e1ac5d099ace518fc824ffa1073e`.
- R762BQ author-side PR #2520@`b8599c9dd36fac458a7c0f6b23010aa5d5f07295`.
- Applicable current protocol `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`; current rules do not repin frozen scientific inputs.

**Next:** obtain the genuine permitted native signed Cell/Port/Link `TRIADIC_CLOSURE_E` event and V17/V29/V39 transports. Compute the *actual event-preserving subgroup*, restrict the state fiber and query orbits to admitted native events, and recompute optimal recovery costs and observer-safe BRC residual. Confirm whether an explicit time-typed rotation update acts on directed triads while preserving native Cell identity and ordered-path provenance.

Control state: the conditional author-side science is publishable to GitHub independently; operational Source Activity, formal PROGRESS/Result and independent Review require their own current authenticated authority.