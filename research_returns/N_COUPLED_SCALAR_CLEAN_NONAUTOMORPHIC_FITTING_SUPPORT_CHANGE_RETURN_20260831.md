# N-Coupled Scalar-Clean Nonautomorphic Fitting-Support Change — Research Return

Researcher-ID: `EM-NCASFIT1-83A326`  
Task: `RS-N-COUPLED-SCALAR-CLEAN-NONAUTOMORPHIC-FITTING-SUPPORT-CHANGE`  
Publication: `TP2-2E7C91A54B60D83F1C25`  
Claim: `chatgpt-ncasfit1-20260831-1030-7e4c21`  
Execution record: `ER-4F06838FF6321D1C65DC`  
Result: `RR-E71A71AADBB2ACF55EFE`

## 1. Terminal verdict

`SUCCESS / DECLARED_EXPLICIT_PRESENTATION_GRAMMAR_OBSTRUCTED`.

Hard-target disposition:

`NONAUTOMORPHIC_SUPPORT_CHANGE_IS_POSSIBLE_BUT_ANY_ONE_SIDED_HIDDEN_RANK_EVENT_IN_A_FULLY_EXPLICIT_FINITE_PRESENTATION_SCALARIZES_TO_A_PROPER_DETERMINANTAL_GCD / EXPLICIT_PRESENTATION_SUPPORT_ASYMMETRY != SCALAR_CLEAN_TYPED_ASYMMETRY`.

This task does **not** prove that every non-automorphic or typed construction is impossible. It freezes a larger exact negative class than the accepted `G_hist-U` result: arbitrary factor-blind non-automorphic transformations may change dimensions and Fitting ideals, but if the resulting pre-collapse state is a **fully explicit finite presentation matrix**, then any one-sided hidden-channel rank/Fitting-support event has a canonical public scalarization by determinantal divisors. For `N=pq`, that scalarization is already a proper gcd with `N`.

Therefore the next missing capability is narrower than merely “leave unimodular transport”:

`NONAUTOMORPHIC_SUPPORT_CHANGE + PRECOLLAPSE_NONSCALARIZABLE_TYPED_REPRESENTATION`.

A genuinely surviving positive mechanism must keep the asymmetric support in an implicit/opaque typed object until the declared selective-collapse layer; materializing an ordinary finite presentation matrix before collapse is already too much information.

No Working Truth, Foundation, L4, novelty, complexity lower bound, or universal factoring claim is asserted.

## 2. Frozen grammar `G_exp-Fit`

Let `N=pq` with distinct hidden primes `p != q`.

A `G_exp-Fit` trajectory has:

1. public input `N` and no hidden-factor input;
2. arbitrary finite public transcript, including canonical representatives, floor/divmod, carry/borrow, history, variable stopping, and other factor-blind control;
3. at each pre-collapse data state an **explicit integer matrix**
   `A_t in Mat_{m_t x n_t}(Z)`, with dimensions allowed to vary;
4. an arbitrary deterministic factor-blind transition producing the next explicit matrix from public state.

The transition may be non-automorphic. In particular this grammar permits:

- singular left/right multiplication;
- fixed or transcript-dependent row/column restriction and compression;
- deleting or appending generators/relations;
- dimension-changing completion or quotient presentation;
- quotient/carry/history-derived relation rows;
- any other finite exact transformation whose output presentation matrix is explicitly materialized.

The only exclusions are the task-level guards: no `p,q`, factor-aware selector, candidate-prime schedule, operational branch on a proper gcd/nonunit, or hidden-factor injection.

### 2.1 Canonical support scalarization

For an explicit matrix `A` and `1 <= k <= min(m,n)`, define

`D_k(A) = gcd(|det A[I,J]| : |I|=|J|=k)`,

with positive gcd convention and `D_k(A)=0` when all `k x k` minors vanish.

This is the positive generator of the integer determinantal ideal `I_k(A)`.

Define the public support scalar

`sigma_k(A;N) = gcd(N, D_k(A))`.

The key semantic choice of `G_exp-Fit` is that an explicit public presentation makes its canonical determinantal scalarization available before selective collapse. `sigma_k` is not an extra hidden-factor oracle; it is a deterministic factor-blind scalar function of the already-materialized public matrix and `N`.

A construction that needs to forbid this scalarization is therefore **outside** `G_exp-Fit` and must declare an opaque/typed interface whose presentation is not materialized pre-collapse.

## 3. Theorem A — determinantal divisor / hidden-rank criterion

For every integer matrix `A`, every prime `r`, and every admissible `k`,

`r | D_k(A)  <=>  rank_F_r(A mod r) < k`.

### Proof

`rank_F_r(A mod r) < k` exactly when every `k x k` minor vanishes modulo `r`. This is exactly the statement that `r` divides every integer `k x k` minor of `A`, hence divides their gcd `D_k(A)`.

Conversely, if `r | D_k(A)`, then `r` divides every `k x k` minor, so every such minor vanishes modulo `r`, forcing rank `< k`. QED.

This proof is independent of how `A` was produced. No CRT-naturality or automorphism assumption is used.

## 4. Theorem B — exact semiprime scalarization equivalence

Let `N=pq` with distinct primes. For every explicit matrix `A` and every admissible `k`:

- `sigma_k=1` iff both hidden ranks are at least `k`;
- `sigma_k=p` iff `rank_F_p(A)<k <= rank_F_q(A)`;
- `sigma_k=q` iff `rank_F_q(A)<k <= rank_F_p(A)`;
- `sigma_k=N` iff both hidden ranks are below `k`.

Hence

`rank_F_p(A) != rank_F_q(A)`
iff
`exists k: 1 < sigma_k(A;N) < N`.

### Proof

By Theorem A, divisibility of `D_k(A)` by `p` is equivalent to the `p`-rank being below `k`, and similarly for `q`. Since `N=pq` is squarefree, `gcd(N,D_k)` records exactly which of the two hidden primes divide `D_k`. The four cases follow immediately.

If the ranks differ, choose `k=min(rank_p,rank_q)+1`; exactly one hidden rank is below `k`, so `sigma_k` is `p` or `q`. Conversely, a proper `sigma_k` means exactly one prime divides `D_k`, hence exactly one hidden rank is below `k`. QED.

## 5. Corollary — balanced explicit state cannot become scalar-clean asymmetric

Assume the seed `A_0` has equal hidden ranks

`rank_F_p(A_0) = rank_F_q(A_0) = r`.

Then for every `k`:

- `sigma_k(A_0;N)=1` for `k <= r`;
- `sigma_k(A_0;N)=N` for `k > r` within the matrix range.

So the seed's canonical support scalars are gcd-clean.

Now let an arbitrary `G_exp-Fit` transition produce an explicit `A_t` with unequal hidden ranks. By Theorem B, at the **same explicit state** there is a canonical `sigma_k(A_t;N)` equal to `p` or `q`.

Therefore:

`BALANCED_EXPLICIT_PRESENTATION -> ONE_SIDED_FITTING_SUPPORT`
implies
`PRECOLLAPSE_PROPER_SUPPORT_GCD`.

This closes the entire declared explicit-presentation class under the task firewall, even though non-automorphic operations can genuinely change support.

The result is stronger than the parent unimodular obstruction in one direction and weaker in another:

- stronger: the transition itself may be arbitrary, singular, dimension-changing, history-dependent, and non-CRT-natural;
- weaker: the obstruction requires the resulting pre-collapse support-bearing state to be a fully explicit finite presentation.

## 6. Non-vacuity witness — fixed projection really changes support

Take

`N=15`, hidden factors `p=3`, `q=5`, and

`B_0 = [[1,1,0],[1,4,1],[0,2,1]]`.

Exact determinantal divisors are

`D_1(B_0)=D_2(B_0)=D_3(B_0)=1`.

Also

`det(B_0)=1`,

so

`rank_F_3(B_0)=rank_F_5(B_0)=3`.

Now apply the fixed factor-blind non-invertible projection/restriction that keeps the first two rows and first two columns:

`A = [[1,1],[1,4]]`.

Then

`D_1(A)=1`,
`D_2(A)=3`.

Hence

`rank_F_3(A)=1`,
`rank_F_5(A)=2`,

and

`sigma_2(A;15)=gcd(15,3)=3`.

All individual coordinate scalars appearing in `B_0` and `A` have gcd with `15` in `{1,15}`; the leak is genuinely a **relation/minor support scalar**, not an entry that was already a visible factor.

Thus a simple non-automorphic projection can indeed change full-carrier Fitting support from clean to one-sided. The task is not blocked because support change is impossible. It is blocked because once the projected presentation is explicit, the new one-sided support has already become a public scalar nonunit through `D_2`.

This witness also separates two statements:

`NONAUTOMORPHIC_PROJECTION_CAN_CHANGE_FITTING_SUPPORT` — true.

`EXPLICIT_PROJECTED_FITTING_SUPPORT_CAN_REMAIN_SCALAR_CLEAN` — false in `G_exp-Fit`.

## 7. Coverage of the task's admissible candidate classes

### 7.1 Factor-blind non-invertible projection/compression

Covered whenever the projected/compressed object is materialized as an explicit finite matrix. Support may change, but any one-sided hidden-rank event yields proper `sigma_k`.

### 7.2 Dimension-changing completion or quotient

Covered whenever the completed/quotiented object is returned by an explicit finite presentation matrix. Matrix size is irrelevant to Theorems A and B.

### 7.3 Quotient/carry-derived module generator or relation

Covered even if the choice of new relation row depends on non-ring carry/history/quotient semantics. The post-state theorem does not require the update rule to descend through CRT.

### 7.4 Typed kernel/restriction semantics

Split boundary:

- if a basis/presentation matrix for the kernel/restriction is materialized pre-collapse, it is inside `G_exp-Fit` and scalarizes;
- if only an opaque/implicit typed object is retained and the canonical presentation/support scalarization is unavailable until collapse, it lies outside this theorem.

This is the smallest unresolved semantic capability isolated by the result.

## 8. Update-map naturality versus process stopping

The accepted sibling audit froze

`UPDATE_MAP_CRT_NATURALITY != PROCESS_STOPPING_CRT_ASYMMETRY`.

`G_exp-Fit` respects that distinction.

The transition function may fail CRT-product naturality through carry, canonical representatives, quotient/remainder, or other stateful control. The stopping time may also be arbitrary and history-dependent.

The present theorem is **post-state**:

> whenever the stopped pre-collapse state is a fully explicit finite presentation matrix, one-sided rank support at that state is equivalent to a proper determinantal gcd.

Therefore neither update-map non-naturality nor variable stopping rescues an explicit-presentation candidate. A process whose useful asymmetric event is not represented by an explicit finite presentation remains outside scope.

## 9. Mandatory classical-mechanism firewall

| Mechanism class | Relation to `G_exp-Fit` result | Disposition |
|---|---|---|
| Pollard `p-1` / Williams `p+1` / ECM | No group-order or smoothness annihilation is used in the theorem or witness. | `NOT_THE_MECHANISM` |
| Pollard rho collision/cycle | No collision, repeated-state equality, or cycle event is used. Variable history is allowed but irrelevant to the post-state proof. | `NOT_THE_MECHANISM` |
| Fermat / Lehman / Hart / CFRAC / Dixon / QS / NFS | The theorem does not claim these algorithms reduce to rank-support scalarization. If an explicit relation matrix itself acquires one-sided Fitting support, that support scalarizes; their classical success mechanisms remain separate square/relation routes. | `BOUNDARY_ONLY` |
| named-prime Hensel / p-adic lifting | No named prime/maximal ideal is supplied. | `NOT_THE_MECHANISM` |
| direct zero-divisor / nonunit / idempotent / nontrivial root | This is the exact obstruction endpoint: explicit one-sided Fitting support canonically reduces to a proper scalar nonunit `sigma_k`. | `REDUCES_TO_EXCLUDED_SUPPORT_GCD` |
| pure carry/quotient control | Allowed, including CRT-nonnatural control; it does not defeat post-state scalarization. | `CONTROL_ONLY_INSUFFICIENT` |

No novelty conclusion follows from this table.

## 10. Deterministic exact checker

Checker:

`research_checks/N_COUPLED_SCALAR_CLEAN_NONAUTOMORPHIC_FITTING_SUPPORT_CHANGE_CHECK_20260831.py`

Certificate:

`research_artifacts/N_COUPLED_SCALAR_CLEAN_NONAUTOMORPHIC_FITTING_SUPPORT_CHANGE/explicit_presentation_scalarization_certificate.json`

Executed result: `PASS`.

Finite regression envelope:

- prime set: `3,5,7,11`;
- `6` semiprimes;
- dimensions: `1x1, 1x2, 2x1, 2x2, 2x3, 3x2, 3x3`;
- entry alphabet: `{-1,0,1}`;
- `21,243` explicit integer matrices;
- `127,458` semiprime/matrix cases;
- `372,888` determinantal-rank threshold checks;
- `1,728` hidden-rank-asymmetric cases;
- exactly `1,728` cases with a proper `sigma_k`;
- `0` rank-criterion failures;
- `0` asymmetry/scalarization equivalence failures;
- the `N=15` fixed-projection witness is independently asserted;
- every coordinate scalar in that witness remains gcd-clean while the projected `D_2` becomes the proper factor `3`.

The checker is regression evidence only. The all-`p,q`, all-matrix theorem is Sections 3–5.

Execution environment for this run: Python `3.13.5`.

## 11. Tool/method reuse resolution

### `T0_BRC`

- coverage: support/result/provenance-valued composition;
- reuse state: `REUSE_APPLIED`;
- application: keeps the typed carrier/support event separate from the scalar collapse readout and prevents inferring hidden support from erased provenance;
- boundary: no claim that BRC itself supplies a selector.

### `T6_OPERATION_SAFE_QUOTIENT`

- coverage: quotient/projection/descent and preserved-observation semantics;
- reuse state: `REUSE_APPLIED_AS_GUARD`;
- application: the theorem explicitly declares which observation is preserved/available — the canonical determinantal support scalarization of an explicit presentation — and treats an opaque type that forbids this observation as a genuinely different semantic interface;
- boundary: the tool does not decide that determinantal scalarization must be semantically available; that availability is part of the frozen `G_exp-Fit` grammar.

No new reusable global tool family is introduced. The checker is task-specific. Method-harvest classification: `RESULT_ONLY`.

## 12. Smallest surviving capability

The accepted parent result said:

`NONRING_CONTROL + AUTOMORPHIC_DATA_TRANSPORT -> FITTING_SUPPORT_INVARIANT`.

This result adds:

`EXPLICIT_NONAUTOMORPHIC_FITTING_SUPPORT_ASYMMETRY -> CANONICAL_SCALAR_SUPPORT_GCD`.

Together they sharpen the open residue to:

`OPAQUE_OR_LAZY_TYPED_SUPPORT_CHANGE_BEFORE_SCALARIZATION`.

A future positive construction must therefore provide all of:

1. factor-blind public `N`-only semantics;
2. a genuinely non-automorphic support-changing operation;
3. a pre-collapse state whose one-sided support is not materialized as an ordinary explicit finite presentation with accessible determinantal divisors;
4. no order/smoothness, collision/cycle, congruence-of-squares/relation, named-place p-adic, or direct nonunit mechanism;
5. a declared selective-collapse map that turns the typed asymmetry into a scalar only at the readout boundary.

The key new distinction is:

`SUPPORT_CHANGE != SUPPORT_HIDING`.

Leaving `GL(Z)` is necessary but not sufficient. The representation type must also delay canonical scalarization.

## 13. Scope firewall

This return does **not** prove:

- impossibility of all public non-ring factorization processes;
- impossibility of all non-invertible projections or quotients;
- impossibility of implicit kernels, black-box modules, lazy relation objects, sheaf/groupoid-like typed states, or other non-materialized carriers;
- that determinantal-divisor computation is the only possible readout;
- a polynomial-time factoring lower bound;
- novelty or prior-art absence beyond the accepted sibling audit;
- Working Truth, Foundation, L4, or canonical theorem status.

It proves exactly:

> For squarefree semiprime `N=pq`, once a pre-collapse support-bearing state is materialized as a public finite integer presentation matrix, hidden-channel rank asymmetry is equivalent to the existence of a canonical proper determinantal gcd with `N`. Therefore a scalar-clean one-sided Fitting-support event cannot live in that explicit-presentation grammar.

## 14. Driver recommendation

Review this Result at the exact declared strength.

If accepted:

1. freeze `EXPLICIT_PRESENTATION_SUPPORT_ASYMMETRY != SCALAR_CLEAN_TYPED_ASYMMETRY`;
2. retain the non-vacuity fact that non-automorphic projection can change Fitting support;
3. close fully materialized finite presentation matrices as the pre-collapse carrier for a scalar-clean one-sided support mechanism;
4. route any successor specifically to an **implicit/opaque typed support carrier** whose scalarization is delayed until collapse, rather than to another explicit projection/compression search;
5. preserve the accepted external mechanism firewall and do not infer novelty;
6. defer Lean formalization and independent replication until Driver decides this obstruction is stable enough to justify them.
