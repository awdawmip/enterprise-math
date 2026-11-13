# R745 — Oriented three-force port closure: an S6-equivariant candidate and a sharp one-bit provenance bound

Date: 2026-11-12 (Asia/Shanghai). Status: author-side mathematical construction and theorem, exact finite verification. Parent Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`. Frozen science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Current P000, ACTIVE worldview and project research method remain unchanged. This is a **candidate specialization** of `TRIADIC_CLOSURE_E`, not an assertion that the original P000 already determines all of its incidence dynamics.

## 1. Mother question and a new local question

P000 specifies three nonzero primitive forces as the minimal stable atom, canonical equal-quantum triads at pairwise Enterprise `PERP_E` (native 120°), and no primitive two-force balance. The published Task asks for an explicit Cell/Link/Port closure and rotation-compatible updates with BRC provenance. Prior R743/R744 show that path-current and low-order word observers may lose source order.

**Local question:** Can one define an exact finite three-force port incidence closure which respects the existing `S6` axis-permutation skeleton, and what additional source state is mathematically necessary to retain the directed closure wiring?

## 2. Typed Cell / Link / Port candidate (C1)

Let `C` be the affine torsor for `Z^6` from the frozen X6 Cell foundation; choose a chart only for calculation. Fix a Cell `c`, a three-element subset `A={i,j,k}` of the six distinct native axes, a sign `s_i ∈ {+1,-1}` for each `i∈A`, and a nonzero common quantum `q∈Z_{>0}`. Define the three primitive *coordinate links*

`L_i: c -> c+s_i e_i,quad i∈A`,

with attachment ports `p_i=(c,i,s_i)`. The three links are separate primitive actions; the composite port wiring below is **not** an additional primitive spatial direction or a 3-step spatial return.

An oriented port witness is a relation `W⊂P×P` on `P={p_i:i∈A}`, consisting of one directed three-cycle. Equivalently, it is a cyclic ordering `ω=[i,j,k]` modulo cyclic rotation. Exactly two such witnesses exist: `[i,j,k]` and `[i,k,j]`. Define the candidate event

`E(c,A,s,q,W) = (three force quanta (p_i,q), three coordinate links L_i, internal balance-port relation W)`.

Define `TRIADIC_CLOSURE_E^port(E)=true` exactly when there are three nonzero distinct-axis quanta, equal positive q, and `W` is a directed 3-cycle on their three ports. Without the witness, a raw triple of quanta is not yet a specified *oriented* closure event. For every equal-q three-distinct-axis input, both valid witnesses exist. This is a constructive, internally relational realization of the P000 canonical equal-quantum case: no Euclidean vector-sum-zero condition is used. The closure circuit lives in **port incidence at c**, while the three external links each still end at distinct neighboring Cells.

For later BRC work, assign the three link events distinct provenance labels `b_i`, and preserve the full branch/event tuple `(c,A,s,q,W,b)`; the following minimality theorem is stated for the **source-only observer** which omits `W` and carries no extra asymmetric port-order label.

## 3. Equivariance and exact state count

For `π∈S6`, let `π(c)` be the permuted Cell chart, `π(e_i)=e_{π(i)}`, and act on `s,W`, links and ports by relabeling. Then:

`π(T^s_i(c))=T^s_{π(i)}(π(c))`, and `π(W)` is again a directed 3-cycle. Consequently

`TRIADIC_CLOSURE_E^port(πE)=TRIADIC_CLOSURE_E^port(E)`.

For any fixed Cell and common q, the unordered signed-triad observations number

`binom(6,3)*2^3 = 160`.

There are precisely two oriented witnesses above each observation, so **320 oriented event states**. By the count of positive signs k, these form four `S6` orbits of sizes `40,120,120,40` for `k=0,1,2,3` respectively. This is exact finite classification of the candidate carrier, not a census of all actual P000 force events.

## 4. No-go theorem: no canonical oriented wiring from a signed unordered triple

**Theorem.** There is no `S6`-equivariant function assigning one of the two oriented three-cycles `W` to each of the 160 unordered signed triple configurations `(A,s)`. This remains true for every fixed common nonzero q, even if the function may inspect the sign configuration.

**Proof.** In any set of three signs `(+/-)`, at least two axes `u,v∈A` have the same sign. The transposition `τ=(u v)∈S6` fixes the entire unordered signed configuration `(A,s)`, while reversing the orientation of each directed three-cycle on A. If an equivariant selector `f` existed, then `f(A,s)=f(τ(A,s))=τ f(A,s)`, but no directed three-cycle on three distinct ports is fixed by `τ`. Contradiction. This applies independently to every signed configuration. QED.

The **oriented source-state fiber has size exactly two**. Therefore one binary choice is necessary and sufficient to recover an oriented witness from the declared source-only observation. Relative to sorted axis labels, write the two choices as `ε∈{+1,-1}`. Under `π`, ε transforms by the parity of the induced reordering of the selected three axes; it is a *covariant orientation coordinate*, not an invariant global scalar. This is a mathematical lower bound for the stated observation/future-operation scope, not for a Boolean stability detector that deliberately forgets orientation.

## 5. Future-operation significance

The observable `Next_W(p_i)` gives the successor port in the directed balance circuit. It is `S6`-covariant:

`Next_{πW}(πp_i)=π Next_W(p_i)`.

The two allowed witnesses have different successors for every source port. Thus, any later update that routes signal/source flow via `Next_W` must retain one orientation bit (or equivalent information) to be exactly reconstructible. A coarser observer that merely asks whether *some* valid three-cycle exists can safely collapse the two witnesses for that narrower Boolean use.

Translations `T_v` move the Cell and its attached three links and ports together, leaving `W` and source labels intact; this supplies a typed chart-independent spatial transport. `S6` relabeling supplies finite-axis rotation covariance. Dynamics beyond the frozen axis-permutation skeleton remain a separate task dependency.

## 6. A direct R743/R744 BRC-to-port bridge

Take the R743 connector family with four axes `I={0,1,2,3}` and loop axes `a=4,b=5`:

`w_σ=c_σ(+4,+5,-4,-5)c_σ^{-1}`, `σ∈S4`, `c_σ=(+σ_1,+σ_2,+σ_3,+σ_4)`.

All 24 rooted length-12 paths are closed, non-backtracking, and have exactly the same directed coordinate edge current `j` (the connector and its reverse cancel). Their connector endpoint is the same Cell `c_* = c_0+e_0+e_1+e_2+e_3`.

Choose the separate *triad port candidate* attached at `c_*` with signed source triple `A={0,1,2}`, all signs positive and q=1. Define `F(w_σ)` to be the cyclic orientation of these three axes in their **first-occurrence order along `c_σ`**. This map is `S6`-covariant when the loop pair and selected triple are relabeled together. The 24 paths split exactly `12+12` between the two port orientations, although they have identical `j`, the same triad Cell, and the same unordered signed triad.

In particular `σ=(0,1,2,3)` and `σ'=(1,0,2,3)` give opposite `F` but identical spatial edge current. This demonstrates a concrete *provenance-sensitive lift* from previously constructed signed-axis BRC branches to an oriented port-closure choice. It is a proposed encoding, not proof that native V29 PASS or V39 frame flow already implements `F`.

R744's order-four word coefficients recover the full `σ`, and hence `F`; the direct port witness stores only the one bit needed for this specific three-port successor observer. Thus full route recovery and local three-force oriented closure are two distinct, task-relevant future-operation targets.

## 7. Exact verification and independent proof basis

The supplied standard JavaScript finite checker enumerates all 20 three-axis subsets, all 8 sign assignments, both directed port orientations and all 720 six-axis label permutations, testing **230,400** covariance instances. It checks a same-sign stabilizer-transposition witness in each of the **160** signed configurations, verifies the four orbit sizes and re-enumerates all 24 R743 length-12 connector words, their common nonzero edge current and their 12/12 orientation split. A separate Python standard-library enumeration in the author environment reproduced the same counts.

`R745_X6_TRIADIC_PORT_ORIENTATION_EXACT_PASS`. Counting is finite, uses integers and permutations and has no approximate arithmetic. The no-equivariant-section result additionally has the general proof above, independent of the enumerator.

## 8. Scientific frontier and limits

**Established here:** an explicit typed C1 Cell/Link/Port closure **candidate**, a rotation-covariant update of its port data, exact 160/320 state classification, a sharp one-bit orientation bound, and an explicit R743/R744 route-provenance-to-port-wiring bridge.

**Still open for the parent task:** validate C1 against the remaining current X6 triadic rotation generators and actual V17/V29/V39 native update definitions; decide which legal `TRIADIC_CLOSURE_E` events require directed wiring and whether P000 permits additional incidence geometries; define physical action/response laws; classify larger triadic decompositions and construct the projected apparent-two-force lift; obtain the task's formal CLAIM, native Result and independent Driver review.

The new proof does not alter P000, the frozen scientific input, or source provenance. It can be used as a sharply scoped candidate construction within the published mother objective.
