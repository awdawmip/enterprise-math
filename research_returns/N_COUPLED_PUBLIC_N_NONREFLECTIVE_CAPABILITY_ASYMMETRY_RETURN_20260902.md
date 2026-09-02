# N-Coupled Public-N Nonreflective Capability Asymmetry — Research Return

Researcher-ID: `EM-NCASCAP1-7A2F4C`  
Task: `RS-N-COUPLED-PUBLIC-N-NONREFLECTIVE-CAPABILITY-ASYMMETRY`  
Publication: `TP2-08FEE1835AC7CB784181`  
Claim: `chatgpt-ncascap1-20260902-0741-7a2f4c`

## 1. Terminal verdict

`NEGATIVE_BOUNDARY / EXTENSIONAL_NONREFLECTION_DOES_NOT_BLOCK_INTENSIONAL_PRESENTATION_COMPILATION`.

Hard-target disposition:

`PUBLIC_N_ONLY_NONREFLECTIVE_EFFECTFUL_TYPED_SUPPORT_EXACTLY_OBSTRUCTED_FOR_G_TRACE_LIN_BY_PUBLIC_TRACE_PRESENTATION_COMPILATION`.

This return freezes and kills one exact capability-limited class that is strictly outside the parent `G_reflect-FM` hypothesis:

`G_trace-lin = affine/linear one-use finite R_N-module handles + public presentation-transparent constructor transcript`.

Here `R_N=Z/NZ`, `N=pq` for distinct hidden primes. Runtime handles cannot be copied, replayed, compared, enumerated, membership-tested, quotient-equality-tested, standard-basis-probed, arbitrarily evaluated, cardinality-queried, or presentation-queried before the final boundary. Thus the previous complete-extensional-reflection argument does **not** apply to the runtime interface.

Nevertheless, every constructor in `G_trace-lin` has a public factor-blind finite-presentation compiler. Structural recursion on the public constructor transcript therefore reconstructs a presentation of the actual handle **without reading the handle at all**. For a presentation `C`, the maximal-minor determinantal divisor `Delta_r(C)` gives an exact CRT-support scalar:

`gcd(N,Delta_r(C))`.

If the hidden support is one-sided, this is already `p` or `q` before the declared terminal materialization/readout. Linear noncopyability blocks extensional reflection but does not block intensional reconstruction from public syntax.

The exact new boundary is therefore:

`EXTENSIONAL_NONREFLECTION != SUPPORT_HIDING`.

More sharply:

`EXTENSIONAL_NONREFLECTION + PUBLIC_PRESENTATION_TRANSPARENT_TRACE -> PRE_READOUT_SUPPORT_SCALARIZATION`.

This does not prove impossibility for a capability calculus containing a load-bearing transition whose realized output presentation is not effectively determined by the public transcript. It proves that **linear/one-use capability semantics alone are insufficient**.

No factoring lower bound, complexity lower bound, novelty, Working Truth, Foundation, L4, or canonical-promotion claim is asserted.

## 2. Why this is not the parent reflection theorem replayed

The accepted parent boundary `G_reflect-FM` scalarizes a finite module because the runtime interface is extensionally complete: enumerate a finite ambient set plus membership, enumerate quotient classes using total equality, deduplicate a complete iterator, or reconstruct a linear map by arbitrary basis probing.

`G_trace-lin` deliberately removes all of those powers.

The pre-readout client cannot:

- enumerate the elements of a handle;
- compare two elements or two handles extensionally;
- ask membership or quotient equality;
- probe a map on chosen elements;
- replay a consumed handle;
- duplicate a handle;
- ask cardinality;
- ask for a basis or presentation.

So there is no route from the **runtime handle** to `|M|` or to an explicit presentation.

The obstruction proved here is orthogonal. The source program and its public parameters are not secret. A finite constructor trace is public intensional data. If every constructor is presentation-transparent, the trace itself is a factor-blind presentation certificate. Resource linearity of runtime values does not erase the source-level construction DAG.

This distinction is the main mathematical contribution of the return:

`EXTENSIONAL_REFLECTION` and `INTENSIONAL_PRESENTATION_COMPILABILITY` are independent reflection channels.

A serious delayed-scalarization candidate must close both.

## 3. Frozen capability calculus `G_trace-lin`

Exact machine-readable contract:

`research_artifacts/N_COUPLED_PUBLIC_N_NONREFLECTIVE_CAPABILITY_ASYMMETRY/trace_linear_capability_contract.json`.

### 3.1 Runtime carrier

A handle `H` denotes one finite `R_N`-module. Handles are affine/linear resources: every consuming constructor invalidates its inputs. The same runtime handle cannot be used twice.

The process receives public `N` only. No hidden `p`, `q`, CRT idempotent, candidate-prime schedule, named maximal ideal, or factor-aware selector is an input.

### 3.2 Pre-readout handle constructors

The frozen vocabulary is:

1. `NEW_FREE(r)` — create a fresh one-use handle denoting `R_N^r`;
2. `ATTACH_RELATION(H,v)` — consume `H=coker(C)` and return the quotient obtained by adjoining the public relation vector `v`, hence `coker([C|v])`;
3. `DIRECT_SUM(H1,H2)` — consume both handles and return their direct sum;
4. `TENSOR(H1,H2)` — consume both handles and return their tensor product over `R_N`.

This is nontrivial composition. A handle may pass through arbitrarily many consuming algebraic stages, and two independently produced handles may be combined.

Public relation vectors may be arbitrary effectively computed integer functions of public `N` and other public integers. They may not depend on hidden factors.

### 3.3 Forbidden pre-readout reflection

The following are absent by the formal capability contract, not by implementation convention:

`COPY_HANDLE`, `REPLAY_HANDLE`, `HANDLE_EQUALITY`, `ENUMERATE_ELEMENTS`, `MEMBERSHIP_QUERY`, `QUOTIENT_EQUALITY_QUERY`, `STANDARD_BASIS_PROBE`, `ARBITRARY_ELEMENT_EVALUATION`, `CARDINALITY_QUERY`, `PRESENTATION_QUERY`.

Thus `G_trace-lin` is genuinely nonreflective at the runtime-handle level.

### 3.4 Public intensional observations

The source program remains public. Before readout one may inspect and perform ordinary pure integer computation on:

- `N`;
- constructor tags;
- constructor arities and public type dimensions;
- public integer relation vectors;
- the finite public constructor transcript.

Treating these as secret would be implementation secrecy and would violate the task.

No scalar observation of the runtime handle state is primitive.

### 3.5 Exact terminal boundary

`MATERIALIZE(H)` consumes the final handle and returns one finite presentation matrix for its module. It does not return a factor, a nonunit, a CRT side, a hidden prime, or a factor-aware selector.

The declared terminal readout is then:

1. obtain a presentation `C`;
2. compute its maximal-minor determinantal divisor `Delta_r(C)`;
3. return `gcd(N,Delta_r(C))`.

This is a non-oracular presentation-returning boundary. The theorem below shows that in `G_trace-lin` the boundary is semantically too late: a presentation is already computable from the public transcript.

## 4. Theorem A — public trace compilation

For every closed finite `G_trace-lin` program `P` producing a handle `H_P`, there is a factor-blind effective compiler

`Compile(P,N) = C_P`

such that

`H_P ~= coker_R(C_P mod N)`.

The compiler never queries a runtime handle.

### Proof

Proceed by structural induction on the constructor transcript.

#### Base: `NEW_FREE(r)`

`R_N^r` is the cokernel of the empty map

`R_N^0 -> R_N^r`.

Compile to the `r x 0` empty presentation matrix.

#### Relation attachment

Suppose `H ~= coker(C:R_N^s -> R_N^r)` and the public relation is `v in Z^r`, reduced modulo `N` at runtime.

Quotienting by the cyclic submodule generated by `v` adds exactly one relation, so

`ATTACH_RELATION(H,v) ~= coker([C|v]:R_N^(s+1) -> R_N^r)`.

Thus the compiler appends the public column `v`.

#### Direct sum

If

`H1 ~= coker(C:R_N^s -> R_N^r)`,
`H2 ~= coker(D:R_N^v -> R_N^u)`,

then

`H1 direct_sum H2 ~= coker(blockdiag(C,D))`.

The block diagonal matrix is computable from the two compiled presentations.

#### Tensor product

Right exactness of tensor product gives a presentation of

`coker(C) tensor_R coker(D)`

with free codomain `R_N^(ru)` and relation matrix

`[ C tensor I_u | I_r tensor D ]`.

The first block imposes the relations of `H1` in each second-factor free coordinate; the second imposes the relations of `H2` in each first-factor free coordinate. This matrix is effectively computable from `C,D`.

These cases exhaust the frozen grammar. Therefore every finite public transcript compiles by structural recursion. QED.

### Resource-linearity point

The compiler duplicates neither a runtime handle nor its elements. It consumes only the public syntax tree and public integer parameters, which are ordinary classical data. Hence one-use/affine typing does not obstruct the compiler.

## 5. Theorem B — maximal minors are an exact hidden-support scalar

Let `C` be an integer `r x s` matrix and let

`M_C = coker(C mod N : R_N^s -> R_N^r)`

for `N=pq`, distinct primes.

Define the top determinantal divisor:

- if `r=0`, set `Delta_r(C)=1`;
- if `s<r`, set `Delta_r(C)=0`;
- otherwise set `Delta_r(C)` equal to the gcd of all `r x r` minors of `C`.

Then for each hidden prime `ell in {p,q}`,

`ell | Delta_r(C)`
iff
`rank(C mod ell) < r`
iff
`M_C tensor_R F_ell != 0`.

Consequently

`gcd(N,Delta_r(C))`

is exactly the product of the hidden primes on which `M_C` has nonzero CRT component.

In particular,

`ONE_SIDED_HIDDEN_SUPPORT(M_C)`
iff
`1 < gcd(N,Delta_r(C)) < N`.

### Proof

Base change is right exact, so

`M_C tensor_R F_ell ~= coker(C mod ell)`.

This vector space is nonzero exactly when the row rank of `C mod ell` is less than `r`.

For `s>=r`, a matrix over a field has row rank `<r` exactly when every `r x r` minor vanishes. Thus

`rank(C mod ell)<r`
iff
`ell` divides every integer maximal minor
iff
`ell | Delta_r(C)`.

If `s<r`, rank is automatically `<r` for both hidden primes and the convention `Delta_r=0` makes both divide it. If `r=0`, the cokernel is zero and `Delta_0=1` has no hidden prime divisor. Since `N=pq` is squarefree, taking `gcd(N,Delta_r(C))` retains precisely the supported hidden primes. QED.

No CRT idempotent, hidden prime, or hidden-channel computation is performed by the scalarizer. Hidden factors occur only in the proof of correctness.

## 6. Main theorem — linear nonreflection is not delayed scalarization

For every `G_trace-lin` program `P`, combine Theorem A and Theorem B:

1. before `MATERIALIZE`, compute `C_P=Compile(P,N)` from the public transcript;
2. compute `Delta_r(C_P)` using ordinary integer arithmetic;
3. compute
   `g_P=gcd(N,Delta_r(C_P))`.

If the runtime handle has one-sided hidden support, then `g_P` is exactly `p` or `q`.

Therefore every putative positive `G_trace-lin` construction violates the task's pre-readout scalar-clean requirement. The final `MATERIALIZE` operation adds no support information that was not already effectively present in the public construction trace.

Freeze:

`LINEAR_ONE_USE_HANDLE != INTENSIONAL_TRACE_ERASURE`.

`NO_EXTENSIONAL_HANDLE_REFLECTION + PRESENTATION_TRANSPARENT_PUBLIC_TRACE != SUPPORT_HIDING`.

`ONE_SIDED_SUPPORT_IN_G_TRACE_LIN -> PRE_READOUT_PROPER_GCD`.

This is an exact no-go for the declared calculus, not a universal no-go for all capability-limited computation.

## 7. Nonvacuity witness — two consuming relation attachments

Take public

`N=15`.

Run the one-use program

`H0 = NEW_FREE(2)`;

`H1 = ATTACH_RELATION(H0,(1,1))`;

`H2 = ATTACH_RELATION(H1,(1,4))`.

Both input handles are consumed, so no runtime replay or copying occurs.

The public trace compiler gives

`C = [[1,1],[1,4]]`.

Every displayed relation coordinate is gcd-clean with `15`:

`gcd(15,1)=gcd(15,4)=1`.

Hidden ranks, used only to audit the semantics, are

`rank_F3(C)=1`,
`rank_F5(C)=2`.

Thus the cokernel has one-dimensional `F_3` component and zero `F_5` component: genuine one-sided hidden support.

But

`Delta_2(C)=det(C)=3`,

so the public trace already yields

`gcd(15,Delta_2(C))=3`.

This example proves the no-go is not vacuous. The linear capability interface can carry genuine one-sided support while exposing no element-level reflection; the failure is specifically that the public construction trace compiles to the same support-bearing presentation.

## 8. Adversarial audit

### 8.1 Not implementation secrecy

The handle internals are not used. The public semantic specification of every constructor is sufficient for compilation. Hiding the constructor parameters or source trace would be an implementation-secrecy move and is outside the task.

### 8.2 Not complete extensional reflection

No enumeration, equality, membership, quotient-equality, standard-basis probing, arbitrary evaluation, cardinality, or presentation query exists before readout. The proof never calls any of them.

### 8.3 Not a direct factor oracle

The terminal primitive returns a presentation, not a factor/nonunit/CRT side. The pre-readout factor appears only because the public trace gives an equivalent presentation and Theorem B converts its maximal-minor support to a gcd.

### 8.4 Not an order/smoothness mechanism

There is no group-order schedule, exponent annihilation, curve-family search, or smoothness event.

### 8.5 Not collision/history equality

There is no equality test between runtime states, no cycle detector, and no rho-style stopping event.

### 8.6 Not congruence-of-squares / relation collection

The relations in `ATTACH_RELATION` are module-presentation relations, not collected smooth-number relations used to manufacture a square congruence. The extraction theorem is the explicit maximal-minor/Fitting support boundary already accepted in this N-coupled line.

### 8.7 Not named-place p-adic lifting

No hidden prime/maximal ideal is supplied or selected.

### 8.8 No novelty claim

The accepted external prior-art audit remains the comparison firewall. This return is a task-local mathematical boundary and makes no novelty inference.

## 9. Representation / information-flow audit

| Information channel | `G_trace-lin` pre-readout status | Consequence |
|---|---|---|
| runtime element enumeration | `FORBIDDEN` | parent cardinality enumeration proof unavailable |
| runtime equality / quotient equality | `FORBIDDEN` | no extensional class counting |
| runtime standard-basis probing | `FORBIDDEN` | no black-box matrix reconstruction |
| runtime presentation query | `FORBIDDEN` | no direct handle reflection |
| handle copying / replay | `FORBIDDEN` | genuine affine/linear resource discipline |
| public constructor trace | `AVAILABLE` | source program cannot be treated as secret |
| presentation from public trace | `RECOVERABLE` | Theorem A structural compiler |
| maximal-minor support scalar | `RECOVERABLE` | Theorem B |
| one-sided support factor | `RECOVERABLE` | proper `gcd(N,Delta_r(C))` |

Hence the capability class passes the **extensional** nonreflection test but fails the stronger **intensional** nonreflection test.

## 10. Tool-reuse gate resolution

Current toolbox coverage was checked after the task structure was understood and before any new general-purpose mechanism was introduced.

- `T0_BRC`: `NOT_APPLICABLE`. Its Boolean/provenance support typing is not the CRT finite-module support used here. Importing it would conflate distinct support notions.
- `T6_OPERATION_SAFE_QUOTIENT`: `NOT_APPLICABLE`. The cokernels in this proof are algebraic finite-module presentations, not a chosen semantic observation quotient/coarse-graining problem.
- New general-purpose tool family: `NOT_CREATED`.

The work is a task-local theorem and exact checker, not a new toolbox direction.

## 11. Deterministic exact checker

Checker:

`research_checks/N_COUPLED_PUBLIC_N_NONREFLECTIVE_CAPABILITY_ASYMMETRY_CHECK_20260902.py`

Certificate:

`research_artifacts/N_COUPLED_PUBLIC_N_NONREFLECTIVE_CAPABILITY_ASYMMETRY/trace_linear_capability_certificate.json`

Exact finite regression envelope:

- hidden prime pairs `(2,3),(2,5),(3,5),(3,7),(5,7)`;
- matrix shapes `1x0,1x1,1x2,2x0,2x1,2x2,2x3`;
- entry alphabet `{0,1,2}`;
- `4,165` exact presentation matrices;
- `790` one-sided support cases;
- `0` maximal-minor support-law mismatches;
- `196` tensor-presentation component-dimension checks;
- `196` direct-sum component-dimension checks;
- the sequential `N=15` two-attachment witness independently checked;
- all ten forbidden extensional-reflection primitives absent from the pre-readout handle vocabulary.

Expected deterministic terminal line:

`PASS G_TRACE_LIN_INTENSIONAL_PRESENTATION_SCALARIZATION matrix_cases=4165 one_sided=790 tensor_checks=196 direct_sum_checks=196 witness=N15_two_linear_ATTACH_Delta3_gcd3 forbidden_reflection_ops=10`

The finite checker is a regression certificate. The all-`p,q` support theorem and the trace-compiler theorem are symbolic proofs in Sections 4–6.

## 12. Exact surviving frontier

The parent task showed:

`COMPLETE_EXTENSIONAL_REFLECTION -> SUPPORT_SCALARIZATION`.

This return adds:

`PUBLIC_PRESENTATION_TRANSPARENT_CONSTRUCTION_TRACE -> SUPPORT_SCALARIZATION`,

even when runtime extensional reflection is absent and handles are strictly one-use.

Therefore a future positive capability candidate must satisfy at least both:

1. **extensional nonreflection** — no complete enumeration/equality/probing/cardinality/presentation recovery from the runtime interface; and
2. **intensional presentation noncompilability** — at least one load-bearing realized transition must not admit a factor-blind effective presentation transformer from the public constructor transcript and input presentations.

Call this necessary gap, without asserting existence:

`DOUBLE_NONREFLECTION = EXTENSIONAL_NONREFLECTION + INTENSIONAL_PRESENTATION_NONCOMPILABILITY`.

The second condition cannot be satisfied merely by hiding implementation details. A legitimate future calculus must give a public semantics explaining why the realized transition is not determined by a replayable public presentation transformer — for example because of a formally modeled one-use/generative effect — and must still prove that its terminal readout is not a factor oracle or a reviewed classical mechanism.

This return does **not** prove such a survivor exists and does not authorize one by fiat.

## 13. Driver recommendation

Recommended disposition:

`ACCEPT / EXACT_NEGATIVE_BOUNDARY / LINEAR_ONE_USE_TRACE_TRANSPARENCY`.

Freeze the two independent scalarization channels:

- `EXTENSIONAL_REFLECTION_CHANNEL` — closed by the parent `G_reflect-FM` theorem;
- `INTENSIONAL_PUBLIC_TRACE_COMPILATION_CHANNEL` — closed here for `G_trace-lin`.

If the parent objective remains open, any successor should be narrower than generic “nonreflective capability”. It should target a **publicly specified but trace-noncompilable realized effect** and must adversarially prove that the effect is neither hidden factor authority nor a renamed order/smoothness, collision, square-relation, named-place p-adic, or direct nonunit mechanism.

Do not interpret this return as a universal lower bound or as evidence that such an effect exists.
