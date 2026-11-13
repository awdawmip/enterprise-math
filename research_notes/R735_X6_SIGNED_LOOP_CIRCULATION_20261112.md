# R735 — Signed circulation and one-bit history repair for X6 triadic loop BRC

Date: 2026-11-12 (Asia/Shanghai). Research line: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`.
Frozen scientific Source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.
Prior author evidence: R734, Draft PR #2129, commit `c598be3c00b39bf8ddcbf70d2edef7b25dd1caa3`.
Status: an exact *coordinate/path N-BRC theorem*, not a native force-closure event or V39 verification.

## Question

R734 proved that a nonbacktracking six-step signed native-coordinate return on three axes has 240 ordered branches, with 30 branches for each first-appearance signed-source triad. Does the endpoint-only observation (always zero) hide a smaller, equivariant *signed circulation* observer? Given the source signs, what extra ordered-history information is sufficient to reconstruct the original branch exactly?

## Population and conventions

Fix any three distinct X6 native axes, labelled 0,1,2 solely to describe one chart. Let `W` consist of all 6! permutations of their six signed primitive steps `+e_i,-e_i` (each occurs once). Each word starts at an arbitrary chosen Cell `c`, and ends at that same Cell. Let `NB` exclude any pair of immediately successive inverse steps. R734 gives `|NB|=240` and first return at six for every NB word.

Write `x^{(t)} = Σ_{r≤t} Δx^{(r)} ∈ Z^3` for the relative location after step t. For i<j, define the **integer signed coordinate circulation**
[
J_{ij}(w)=sum_{t=1}^{6} x_i^{(t-1)},Delta x_j^{(t)}.
]
The pair `J=(J_01,J_02,J_12)` is a *candidate coordinate loop-flow readout*, not the real V39 flow `j`, for which no source-backed event correspondence is asserted. Unlike physical Euclidean area, the definition uses only signed X6 step provenance and integer arithmetic.

Define `Q(w)=(σ_0,σ_1,σ_2)` where `σ_i` is the sign of axis i's **first occurrence** in the word, exactly as in R734. This is a declared encoding convention. A branch includes full ordered step identities.

## Theorem 1 — Exact current type and symmetry

For every `w∈W` and pair i<j, `J_ij(w) ∈ {-1,0,1}`. The value is nonzero precisely when the two occurrences of axis i *interleave* the two occurrences of axis j in the projected four-event word. The sign is the orientation of this interleaving.

*Proof.* On a closed word, `Σ_t Δx_j^{(t)}=0`, so translating the chosen Cell anchor leaves `J_ij` unchanged. The summation-by-parts identity for a closed word gives `Σ x_i Δx_j = -Σ x_j Δx_i`; thus J is an antisymmetric integer 2-index tensor. Project to the four steps `+e_i,-e_i,+e_j,-e_j`. If the two axis occurrences do not alternate, the two j-steps encounter the same i-coordinate and cancel, yielding zero. If they alternate, exactly one j-step occurs while the i-coordinate is ±1, yielding ±1. A relabeling g∈S6 transports J by `J'_{g(i),g(j)}=J_{ij}` with the necessary antisymmetric sign when the indices are reordered. The full six-axis tensor is zero on pairs outside the chosen triple. This proves anchor invariance and S6 covariance on the declared coordinate carriers. □

## Theorem 2 — Sharp nonbacktracking current census

For every `w∈NB`, `J(w)≠(0,0,0)`. Every one of the 26 vectors
[
{-1,0,1}^{3}setminus{(0,0,0)}
]
occurs. Their exact multiplicities are determined solely by `s=|supp(J)|`:

| Nonzero current components s | Different J signatures | Words per signature | Total words |
|---|---:|---:|---:|
| 1 | 6 | 8 | 48 |
| 2 | 12 | 12 | 144 |
| 3 | 8 | 6 | 48 |
| Total | 26 | — | 240 |

*Proof of nonvanishing.* Draw the three matched axis pairs as chords between their two occurrences in the linear order 1,…,6. `J_ij=0` exactly when the pair-i and pair-j chords do not cross. A noncrossing perfect matching of six ordered sites necessarily contains a matched adjacent pair (take a pair of minimum interval length). Such an adjacent matched pair is an immediate inverse step, excluded by NB. Hence some J component is nonzero. The complete finite multiplicity statement and realization of each of the 26 signatures follow from exhaustive permutation enumeration: the attached verifier iterates all 720 distinct ordered words, checks the NB condition and computes each J by exact integer accumulation. There are no discarded or sampled inputs. The independent Python enumeration in the research session agrees with all 26 signature counts. □

## Theorem 3 — One-bit repair with the signed source observer

The joint observation `(Q(w),J(w))` has exactly **192 fibers** on `NB`:
- 144 fibers containing one ordered branch;
- 48 fibers containing two ordered branches.

Consequently its largest fiber contains two words, and **exactly one auxiliary bit is necessary and sufficient** in this fixed labelled chart to recover the whole six-step ordered word from `(Q,J)`. For comparison, the current J alone has a maximum fiber of 12, requiring four bits for guaranteed reconstruction.

*Proof.* The same finite exhaustive verifier groups the 240 NB words first by Q and J, records 144 singleton and 48 double fibers, and asserts that no other size occurs. Distinct words in a double fiber establish the lower bound of one bit; assigning indices 0/1 within each finite double fiber establishes the upper bound. This is an exact finite classification over the declared 720-word population. It is not a claim that a chart-specific 0/1 index automatically remains invariant under S6; source axes and any repair index must be transported with their declared encoding. □

An explicit double fiber with `Q=(+,+,+)` and `J=(1,1,0)` is
[
(+0,+1,+2,-0,-2,-1)
quad	ext{and}quad
(+0,+2,+1,-0,-1,-2).
]
Both endpoint observations, the full signed-source observer and the three components of J coincide, but the ordered histories differ. The repair bit distinguishes the two.

## BRC observation lease and future operations

The branch population is `NB`, the representation is an explicit positive integer N-BRC count of *signed, ordered primitive paths*, the observer is `(Q,J)`, and the intended future operations are any deterministic operations that consume the *full branch word* after decoding. Within this finite carrier and a fixed labelled chart, retaining one additional bit gives an exact lossless encoding; discarding the bit in the 48 double fibers is not history-safe for every future branch-sensitive operation. Current signatures describe oriented combinatorial circulation, not signed physical force cancellation or phase amplitudes.

This is a concrete improvement from R734's zero-endpoint readout to a signed loop-flow candidate and a minimal typed history repair. It preserves P000's distinction between six-dimensional native Cell returns and `TRIADIC_CLOSURE_E` force events.

## Verification

Run `node research_notes/R735_X6_SIGNED_LOOP_CIRCULATION_VERIFY.js` (standard Node.js, no dependencies). It independently constructs all 720 permutations, asserts 240 NB, confirms R734's 480 first-return-six count, groups J and (Q,J), and emits `R735_X6_SIGNED_LOOP_CIRCULATION_EXACT_PASS`. The sibling JSON certificate records the same exact integer counts and an explicit collision. A separate Python `itertools.permutations` enumeration in this run matched 240, all 26 J signatures, support totals 48/144/48 and joint-fiber sizes 144/48.

## Unfinished native bridge

An actual event-level claim requires a Source-backed `TRIADIC_CLOSURE_E` certificate, Cell/Link/Port incidence with signed source IDs, a legal V29 PASS schedule, and V39's real `j` update law. The pinned P000 material fixes arity/orthogonality and native Cell adjacency, not these event-level rules. The next discriminating task is to obtain one genuine admissible event and compare its V39 output against `J` for two R735 words in a shared (Q,J) fiber, or derive a provable event-to-J correspondence.

Formal TASK CLAIM, Source semantic checkpoint, independent review and mathematical promotion remain separate from this author-side GitHub record.
