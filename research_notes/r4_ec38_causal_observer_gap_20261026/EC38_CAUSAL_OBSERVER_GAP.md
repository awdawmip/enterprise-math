# R4-EC38 — Arbitrarily loose co-adapted source-coupling bound despite identical labelled-path laws

**Status:** AUTHOR_SIDE_PROOF_AND_EXACT_FINITE_CHECK. **Research scope:** positive-integer labelled BRC *auxiliary* source kernels, macro source-label observer. Not a P000-native X6 dynamics theorem, not independent review, not canonical acceptance.

## 0. Exact source and authority scope

GLOBAL_KNOWLEDGE_V1 read snapshot: `awdawmip/chatgpt-global-knowledge@3505cfab9caffaef02ec55bebc3e549d9e4a8389`, including 00_BOOTSTRAP, OPERATING_MANUAL, P000, ACTIVE worldview, code/math/BRC and activity rules. Project control read snapshot: `awdawmip/enterprise-math@cdbfbfdf64459c80354ed2ed084edededa0e129a`, including `docs/PORTABLE_RESEARCH_PROTOCOL.md`, `research_persistence_policy.json`, toolbox routing, and the BRC-only heartbeat constraint.

Precise predecessor: **R4-EC37**, immutable author-side draft `0a7e1d0baebfc648460c58cdc8b6fd99b675fe62:research_notes/r4_ec37_causal_source_20261026/EC37_CAUSAL_LABEL_COUPLING.md`. In that result a finite nonnegative **joint** kernel `P_t(s;label,next_state)` has common integral micro-source row total `M`. An adapted state-pair coupling chooses, conditionally on each currently coupled pair, a transportation coupling of the two exact rows. The Bellman survival value `h_0` yields the safe upper bound `TV(labelled-word laws) <= 1-h_0`; no equality was claimed.

Researcher-ID `EM-R004-A37B` is retained from this conversation, with a **locally assigned logical session key**, not a service-issued execution identity. Authenticated GitHub account was `awdawmip`, with repository push/admin permissions. Native `em_control_tasks` returned `CONTROL_QUOTA`; native `em_session_start` was rejected before execution with `STATIC_READONLY_SCOPE_DENIED`. Active task owner, session, CLAIM and a formal native run remain **unverified**. This note occupies only a noncanonical author-side draft branch.

BRC reuse: `T0_BRC` typed positive multiplicity/provenance and EC37's exact labelled-word histogram and finite transportation/Bellman law — **REUSE_APPLIED**. The existing positive-source total is *not* a signed/phase amplitude, and label-only observation does not preserve microscopic branch IDs. No pi/trigonometry/matrix exponential or physical residual attribution is involved.

## 1. The exact question

How loose can the **optimal** EC37 co-adapted state-pair Bellman bound be, even if the two models induce precisely the same distribution on every finite observable label word?

We answer: the discrepancy may approach **one**. The obstruction is a hidden-state filtration requirement of the *co-adapted* coupling, not a discrepancy in actual observed labelled-path laws.

## 2. Theorem EC38.1 — an arbitrarily large *certificate gap*

For any integer `K >= 2`, define two time-inhomogeneous positive integer micro-source kernels `P_K,Q_K`. Both start at state `O`. In every state and at every operation step the outgoing microscopic source multiplicity is `M=K`. The observable alphabet consists of `*`, the distinct symbols `0,...,K-1`, and `X`. The state labels below are hidden memory, not spatial axes.

**Step 0:** Both models emit `*` and choose hidden state `S_i`, `i=0,...,K-1`, by a single micro-source branch per `i`. (The two copies of `S_i` are separately typed.) Thus `P_K(*,S_i|O)=Q_K(*,S_i|O)=1/K`.

**Step 1:** In `P_K`, state `S_i` has exactly `K` distinct microscopic branches, all emitting label `i` and entering common state `Z`. In `Q_K`, every state `S_j` has exactly one branch emitting each of `0,...,K-1` and entering `Z`.

**Steps `t>=2`:** Both models at `Z` have `K` distinct microscopic branches, all emitting `X` and returning to `Z`.

The observer retains the *entire finite label word* and counts positive microbranch multiplicity, but does not retain the microscopic branch IDs or hidden `S_i` values. The EC37 successor-state relation is universal; there are no terminal ports.

Let `C^P_n(w), C^Q_n(w)` be integer counts and `mu_n,nu_n` normalized word laws. Then

1. At depth `n=0`, the sole empty word has count `1`; at `n=1`, the sole word `*` has count `K`.
2. At every depth `n>=2` the **only** observable words are `*iX^(n-2)`, `i=0,...,K-1`. Each has count `K^(n-1)` in **each** model. In particular `C^P_n=C^Q_n` for *all* `n`, and `TV(mu_n,nu_n)=0`.
3. The **optimal EC37 state-pair co-adapted Bellman survival probability** for depth `n>=2` is exactly `h_0=1/K`, so its best upper bound for the actual TV is `1-h_0=1-1/K`.
4. Therefore the gap between the exact safe EC37 bound and actual TV is `1-1/K`, tending to `1` as `K→infinity`, although the observable word laws and unnormalized word counts agree at **every depth**.

**Proof.** Both models have the stated `K` outgoing microbranches per state. At step 0, `P_K` and `Q_K` choose `S_i` uniformly, with the sole label `*`. In `P_K`, at step 1 the visible label equals `i`, while in `Q_K` it is uniform over all `K` labels independent of its hidden `j`. Thus the depth-2 observable word has uniform label `i` for both models, with count `K` (one choice in P then K microbranches; or K choices of hidden `j` in Q then one microbranch). Every later step appends `X` with `K` distinct branches, establishing item 2 and all word counts.

Under an EC37 admissible **state-pair** transition coupling, conditional on a particular step-0 coupled pair `(S_i,S_j)`, the two stage-1 *marginals must remain the specified source rows*, even when the coupling knows both `i` and `j`. The P label is deterministically `i`; the Q label is conditionally uniform over `K` possibilities. Hence the maximal probability of label agreement in this pair is exactly `1/K`, irrespective of the pair and regardless of the transport coupling. Step 0 always agrees in the observed label, and after step 1 all later labels are identical `X`. Thus the Bellman recursion gives `h_1(S_i,S_j)=1/K` and `h_0(O,O)=1/K`. An arbitrary valid step-0 transport followed by any valid step-1 transport attains this success probability; it is not just an upper estimate on the optimum adapted value. Combining with item 2 proves items 3–4. QED.

**Key interpretation.** Ordinary maximal coupling of the two already-marginalized *observed-word laws* has success probability 1. The EC37 state-pair coupling optimizes a **stronger, co-adapted joint-kernel preservation rule**. A global path coupling can correlate Q's future output with P's hidden choice while preserving each complete model's marginal law; it need not preserve Q's row kernel conditional on the **joint** hidden-state pair. Such an anticipative/weak coupling is outside the EC37 Bellman admissible class. Hence a conservative bound is not evidence of actual observer distortion.

## 3. EC38.2 — explicit primal–dual certificates at every step

For each state pair and continuation values `h_{t+1}`, aggregate identical outcomes `a=(label,nextP)`, `b=(label,nextQ)`, with probabilities `p_a,q_b`, and define `c_ab=1_(labels equal)*h_(t+1)(nextP,nextQ)`. The EC37 Bellman transport primal and its rational dual are

`MAX sum_ab gamma_ab*c_ab, subject gamma>=0, sum_b gamma_ab=p_a, sum_a gamma_ab=q_b`,

`MIN sum_a p_a*u_a+sum_b q_b*v_b, subject u_a+v_b>=c_ab`.

The finite transportation LP has rational optima. A rational feasible gamma and rational dual u,v **with identical objectives** constitute a complete exact local optimum certificate (by weak duality, without floating point or a bare solver-status claim).

For the EC38 family at **step 1**, for every `(S_i,S_j)`: the P side has one aggregate outcome with mass 1 and label `i`; Q has `K` outcomes with mass `1/K` and labels `b`. The primal coupling has `gamma_(i,b)=1/K` for all `b`. Take `u_i=0`, `v_b=1_(b=i)`. Both objectives are `1/K`; all dual inequalities are equalities.

At **step 0**, the `K×K` cost matrix is constant `c_ij=1/K`; both marginals are uniform. A diagonal coupling `gamma_ij=1_(i=j)/K` is primal feasible, and `u_i=1/K, v_j=0` is dual feasible. Both objectives equal `1/K`. Subsequent deterministic `X` stages have continuation value 1. This is a symbolic primal–dual certificate for **every integer K>=2**. Its finite exact verifier is `EC38_verify.js`.

## 4. EC38.3 — a sufficient condition when the Bellman bound is exact

Fix a finite horizon `n>=1` and the **label-word-only observer**, universal successor-state relation and no terminal port. Suppose:

(A) For each of the two kernels, on all prefixes of lengths `0,...,n-1` having positive mass, the hidden state after the prefix is uniquely determined by that visible prefix (observable-state determinacy; a reachable unifilar presentation suffices).

(B) Their distributions on `(n-1)`-letter visible prefixes agree exactly.

Then the optimal EC37 state-pair co-adapted Bellman success is **exactly**
`h_0 = 1-TV(mu_n,nu_n)`.

**Proof.** Equality of the `n-1` prefix laws implies equality of every shorter prefix law. Under (A), each positive visible prefix uniquely fixes each model's next state, so their conditional next-label distributions depend only on the common prefix. For times strictly before the final step these conditional next-label distributions coincide by (B). Couple each next emitted label identically with probability 1; the successor states are then the unique states determined by the new common prefix, so this is a valid joint-kernel coupling of the micro-branches. At the final step, given a common length-`n-1` prefix `u` of probability `p(u)`, choose a maximal coupling of the two conditional last-label distributions. Its agreement probability is `sum_a min(mu(a|u),nu(a|u))`. Total success equals
`sum_u p(u)*sum_a min(mu(a|u),nu(a|u)) = sum_w min(mu_n(w),nu_n(w)) = 1-TV(mu_n,nu_n)`.
No coupling can exceed the latter observable maximal-coupling bound. Thus Bellman attains it. QED.

This is sufficient, not necessary. Assumption (A) fails in EC38's witness because the visible first label `*` does not determine its successor hidden state. If the observation additionally includes microscopic branch IDs or a terminal port, the statement needs the corresponding refined-prefix assumptions and cannot be imported as written.

## 5. Exact computation, limitations, continuation

The portable JavaScript source `EC38_verify.js` executes self-contained BigInt exact microbranch histogram counts and checks the explicit rational transport primal/dual witnesses using denominator-`K` integer scaling. The saved `EC38_REPORT.json` is its actual return, not an imagined experiment. Tested `K=2,...,12` and operation depths `0,...,6`. Its computational coverage does **not** prove the all-`K), all-depth statements; the preceding constructive proofs do.

**Not shown:** a generic production LP optimizer, a general necessary-and-sufficient characterization of equality, preservation of microscopic branch labels, any native X6 update/third-coordinate map/independent time, physical residual measurement, current native Task owner or CLAIM, independent Driver review, or canonical mathematical acceptance.

**Next EC39 discriminating unit:** Characterize when a predictive observer quotient (rather than hidden-state pairwise synchronization) yields a *compositional* exact coupling with word-law overlap. In particular, distinguish prefix-compatible conditional disintegrations from global future-dependent couplings and construct a finite rational certificate for equality/strictness beyond the strong sufficient condition in EC38.3. Apply any eventual native-X6 transfer only after the P000 program, three-dimensional slice, third coordinate, source labels, update and independently typed time are explicitly supplied.
