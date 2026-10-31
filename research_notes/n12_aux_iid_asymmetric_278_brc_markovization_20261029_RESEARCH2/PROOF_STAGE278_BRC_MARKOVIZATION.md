# Stage278-B: exact BRC source-mass Markovization and a sharp future-observer obstruction

**Date:** 2026-10-29. **Status:** `PORTABLE_AUTHOR_PROOF / EXACT_CHECKED_FINITE_WITNESSES / UNREVIEWED / NOT_ADMITTED`. The algebraic theorem below is an external finite-horizon probability result. It neither modifies P000 nor proves native X6 Cell or heartbeat dynamics.

## Immutable reading pins and relation to existing work

- GLOBAL_KNOWLEDGE_V1 `awdawmip/chatgpt-global-knowledge main@6005f73f35bf71adf780aa5f34eab2a163e9018b`. Entry: `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`; project route and math/code/BRC/activity constraints as applicable. Protected `我眼中的世界.md` remains unchanged.
- Enterprise Math canonical control/source `awdawmip/enterprise-math main@cdfbccfdd26f74a9692b0f5281e3f505139416fd`; actual original `p000_reality_foundation.json` (P000-startup projection's earlier blob pin does not match the current canonical original), `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`, `docs/PORTABLE_RESEARCH_PROTOCOL.md` and `control_plane/current_control_authority.json` read as scope constraints.
- Immediate immutable author predecessor: `awdawmip/enterprise-math@982e37b4e95860e901b4a365acbe273ccd116113`, `research_notes/n12_aux_iid_asymmetric_276_277_r2_author_20261029_1606_RESEARCH2/NEXT_TASK_PACKET_278.md` in Draft PR #1571. Stage276/277's exact affine support regions are **consumed**, not recomputed or promoted. This is independent Stage278 task packet item 4; Stage278's next Bellman face (items 1–3) is **not** solved by this note.
- Current identity/authority: author of this execution only, not a borrowed native researcher. Native Site-scoped status at 2026-10-29 09:15:49 UTC reported `research_authority_granted=false`, `write_relay_enabled=false`, and `backend_connected=false` (connection was not checked by that status query). Current owner listing attempt `em_control_tasks` returned `CONTROL_QUOTA`; therefore active owner is **unverified**. No native CLAIM, activity checkpoint, Source Result, Driver review or admission is claimed. GitHub author storage is non-canonical research evidence.

## 1. Universal exact theorem: simultaneous multi-source count/action Markovization

Let `Σ={0,...,m-1}` be a finite alphabet; `N≥1` a finite horizon; `L` any finite (or arbitrary indexed) collection of IID source laws, with `p_z^(ℓ)≥0` summing to 1 for each source `ℓ`. A randomized stopping-and-declaration policy `π` may use its **full ordered history** `h∈Σ^{≤N}` and private randomization independent of the source. Available actions are `D_1,...,D_k,C` (declare or continue); continuing at `|h|=N` is disallowed. We interpret `π(a|h)` as the conditional action probability *given that prefix h was actually reached*. The policy observes no hidden source label.

For a word `h`, write `c(h)=(count_0(h),...,count_{m-1}(h))`. Let `w(ε)=1` and `w(hz)=w(h)π(C|h)` (`|h|<N`): the **policy-only reach factor** of that particular ordered word, conditional on its observation symbols. This factor does not include any source probability. For each count state `s` and action `a`, define the nonnegative rational/real quantities

`W_s = Σ_{h:c(h)=s} w(h)`; `M_s^a = Σ_{h:c(h)=s} w(h)π(a|h)`.

When `W_s>0`, set `\bar π(a|s)=M_s^a/W_s` for every action. When `W_s=0`, choose any legal fixed distribution (irrelevant to reached trajectories). **Then there is one count-only randomized policy `\bar π`, common to all sources simultaneously, with exactly the same `W_s` and `M_s^a` for every count state and action as `π`.** For any source `ℓ`, every count/action occupancy mass is consequently identical:

`Occ_ℓ(s,a)=p_ℓ(s)M_s^a`, where `p_ℓ(s)=∏_z (p_z^(ℓ))^{s_z}`.

In particular all source-indexed declaration errors, all source-indexed stopping-time expectations, and *any linear sum of count/action occupancy readouts* are exactly preserved. Rational source laws and rational original conditional probabilities produce rational quotient probabilities, with no approximation. This theorem holds for all finite `N`, not just `N=12`; it is constructive and applies to Stage277's exact two-source IID model with its 455 count states.

### Proof (full ordered-history induction; no Bellman optimality premise)

For every word `h`, its event of being reached and having symbols `h` has source-`ℓ` probability `p_ℓ(c(h))w(h)` by IID factorization and the policy-only continuation factors. Therefore aggregating actions over `c(h)=s` gives precisely `p_ℓ(s)M_s^a`. Since `W_s=Σ_a M_s^a`, the quotient distribution is legal and independent of `ℓ`; it uses the **separate ordered-word support and multiplicities before quotienting**.

At the root `W_0=1`. For any nonempty count state `s`, partition every ordered word counted by `W_s` by its *last* letter `z`; its prefix has count `s−e_z`. By the exact reach recursion,

`W_s = Σ_{z:s_z>0} M_{s−e_z}^C`.                                            `(1)`

The count-only policy has the same root occupation and, assuming `\bar W_t=W_t` at layer `|t|=n`, its contribution from predecessor state `t=s−e_z` to `s` is

`\bar W_t \bar π(C|t) = W_t (M_t^C/W_t) = M_t^C`

(with both sides zero when `W_t=0`). Summing over `z` in `(1)` proves `\bar W_s=W_s` for the next layer, and then `\bar M_s^a=\bar W_s\bar π(a|s)=M_s^a`. Induction through `N` proves the assertion.

For two declarations P and Q and two IID sources P and Q, the four Stage277 observers are precisely

`eP=Σ_s p_s M_s^Q`, `eQ=Σ_s q_s M_s^P`,

`tP=Σ_{|s|<N} p_s M_s^C`, `tQ=Σ_{|s|<N} q_s M_s^C`.

The stopping-time formulas count the expected number of observed symbols as one unit for each continuing action (including at the empty root). All sums are finite. This proves preservation of the objective `min max(tP,tQ)` and errors under Markovization, for **any** history-dependent admissible randomized policy. Consequently the *attainable four-observer set* of the finite IID sequential-decision problem equals that achievable by count-only randomized policies. The earlier ordered-word DFS remains useful for source/provenance audits and for exact reach counts of nested ties, but a count-only Markov policy exists for each such four-observer vector.

**Critical quantifier boundary:** This is an **existence of an equivalent policy for the declared aggregated observers**, not literal identity of the original strategy, path law or path-conditioned future response. It does not assert that the same random choice is applied to every word, nor that the original strategy factors through counts. It does not remove the ordered histories from the source certificate.

## 2. Sharp ordered-future-observer obstruction, even under IID

Take the same Stage277 ternary sources and a horizon-two policy that always observes two symbols. It declares `P` on all ordered length-two words except `10` and `11`, on which it declares `Q`. At count `(1,1,0)` the ordered words `01` and `10` have **equal** source probability, respectively `p_{01}=p_{10}=1/192`, `q_{01}=q_{10}=1/144`, but the policy declares differently. The above Markovization declares `P` with probability `1/2` on this count state, and otherwise copies the deterministic declarations.

The source-indexed aggregate terminal-P masses agree exactly: `P(declare P)=143/144`, `Q(declare P)=71/72`, and both stopping times equal two. Nevertheless the admissible **path-sensitive readout** `F=1_{(first observed symbol=0) AND (declare P)}` does not descend to the count/action quotient:

| Source | Full ordered policy `E[F]` | Count-only Markovization `E[F]` | Exact lost value |
|---|---:|---:|---:|
| P | `1/8` | `47/384` | `1/384` |
| Q | `1/12` | `23/288` | `1/288` |

No single count-only decision rule can reproduce the **joint conditional declaration** on both `01` and `10`: it would have to assign probability one and zero to action P at the very same count `(1,1,0)`. Thus the original full `(path,action)` observer cannot be preserved by a count-only representation, even though its Stage277 four-observer projection is preserved exactly.

**Typed X6 reading (conditional syntax only, not a native dynamics assertion):** map symbol `0` to one signed primitive `+E₁` step, symbol `1` to `+E₂` in the P000 `Z^6`-torsor chart. The two composite native-axis *word descriptions* `(+E₁,+E₂)` and `(+E₂,+E₁)` have the same final displacement `E₁+E₂` but different first-step/ordered-provenance observers. The counterexample demonstrates why an endpoint or unordered-count map alone cannot certify retention of all declared future operations in a proposed X6 bridge. It does **not** claim those words implement a real heartbeat trajectory or that a physical observer is already specified.

## 3. Necessity of source-fiber proportionality for universal source-indexed Markovization

The IID proof relies on **all source prefix likelihoods being constant within each count fiber**. There is a useful sharp necessary condition at a fully observed terminal layer. Let `C` be a fiber of full words and `P(C),Q(C)>0`; suppose one shared quotient randomized declaration is required to reproduce the source-indexed action mass *inside C* for **every** full-word declaration policy. Choose a deterministic declaration policy that declares P only on one word `h∈C` and Q on all other words of `C`. A quotient chooses P with one common probability `x`. Matching both sources requires

`x=P(h)/P(C)=Q(h)/Q(C)`.

Since `h` is arbitrary, **the two normalized within-fiber source distributions must coincide**. In the IID count fibers this is automatically true; without proportionality it can fail. For an exact positive finite counterexample on `Σ={0,1}`, `N=2`, take full-word laws

`P(00,01,10,11)=(1/2,1/4,1/8,1/8)` and `Q(00,01,10,11)=(1/2,1/8,1/4,1/8)`.

With the same count-`(1,1)` fiber `C={01,10}`, if only `01` declares P, the common quotient probability would have to be both `P(01)/P(C)=2/3` and `Q(01)/Q(C)=1/3`; impossible. All masses are strictly positive, and both source laws normalize to one. This is an exact obstruction for shared **count/action occupancy**, not a claim about every possible coarser four-scalar fitting problem.

## 4. Executed exact computation and limitations

`REPRO_STAGE278_MARKOVIZATION.py` uses only CPython standard-library `fractions.Fraction`, `itertools.product`, and `collections.defaultdict`. It constructs a nontrivial full-history randomized policy with `N=3`, enumerates all 40 ordered prefixes in its three-symbol tree, separately computes both original full-word reach/action masses and quotient full-word reach/action masses, and compares every one of the 60 count/action quantities across 20 count states exactly. It checks the two source distributions normalize exactly and that both source-indexed declaration masses and time expectations match. It independently computes the path-sensitive future observer and both separate `N=2` counterexamples. See the verbatim stdout file. The executed terminal marker is `STAGE278_BRC_COUNT_MARKOVIZATION_EXACT_PASS`.

For the nontrivial `N=3` witness, the exact aggregate Stage277-style readouts are:

`eP=2256023/3981312`, `eQ=73055/165888`, `tP=88985/41472`, `tQ=22193/10368`.

The witness's path-dependent readout `first_0_then_P` differs under P by `649/101184` and under Q by `103/25296`, while all four aggregate observers are identical. The numerical witness is finite; the arbitrary-finite-horizon theorem is justified by the symbolic induction above, **not** extrapolated from this test. The script's equality assertions check the specific rational witness and specified path readouts, not all possible policies or all source laws.

**BRC provenance discipline:** before aggregation we retain each ordered word, both separate exact positive source masses, its survival factor, and its decision mass. The homomorphism to count/action occupancies is proven for an explicitly named observer algebra; it is not a universal information-erasing identity. Signed amplitudes, phase, native X6 temporal dynamics and physical instrumentation are outside this model and are not inferred from positive rational masses.

## 5. Immediate research consequences and smallest next problem

1. **Stage278-B item 4 resolved at external IID level:** count-based randomized policies span exactly the same four-observer feasibility/optimization region as unrestricted ordered-history policies, even with nested stopping ties. Ordered path records remain necessary to audit the original witness and any richer future operations. The prior Stage276/277 results are not modified; their proofs' narrower language is simply strengthened at this declared observer scope.
2. **Stage278-A items 1–3 still open:** construct a strict outer point beyond a nonshared R277 edge, its exact Bellman dual, a matched primal policy, and a new all-real equality face, retaining ordered tie reach counts.
3. **Native bridge still open:** specify native X6 cells, clock/time type, relation state, source-process law, permitted future operation monoid and native observer. Prove a commutative descent `O∘U = \bar O∘\bar U∘q` (or provide a typed residual/repair coordinate) for each operation and composition. The two-path example forbids claiming universal descent from endpoint/count data alone; the source process and native operation/observer signatures are not yet defined.

This contribution is a reproducible *portable author* mathematical derivation. It does not assert source-owner transfer, native activity registration, review, acceptance, or protected P000 changes.