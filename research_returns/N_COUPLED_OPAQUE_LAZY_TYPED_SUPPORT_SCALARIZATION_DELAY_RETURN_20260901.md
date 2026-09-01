# N-Coupled Opaque/Lazy Typed Support Scalarization Delay — Research Return

Researcher-ID: `EM-NCASOT1-91736F`  
Task: `RS-N-COUPLED-OPAQUE-LAZY-TYPED-SUPPORT-SCALARIZATION-DELAY`  
Publication: `TP2-6C1A4E92B7D3058F2A41`  
Claim: `chatgpt-ncasot1-20260901-1016-91736f`  
Execution record: `ER-53EE17EC0C5E1D9C1503`

## 1. Terminal verdict

`NEGATIVE_BOUNDARY / REFLECTION_COMPLETE_FINITE_TYPED_MODULES_SCALARIZE`.

Hard-target disposition:

`OPAQUE_TYPED_SUPPORT_ASYMMETRY_WITH_DELAYED_SCALARIZATION_EXACTLY_OBSTRUCTED_FOR_G_REFLECT_FM_BY_CARDINALITY_SUPPORT_SCALAR_AND_EFFECTIVE_PRESENTATION_RECOVERY`.

The task asked for one exact opaque/lazy typed carrier whose one-sided hidden support either survives all pre-readout scalarization attacks or is exactly killed. This return freezes and kills the following nontrivial opaque class:

`G_reflect-FM = finite R_N-module state with complete pre-readout extensional reflection`.

Here `R_N = Z/NZ`, `N=pq` with distinct hidden primes, and the typed state need **not** expose a basis, matrix, determinant, Fitting generator, Smith form, or factor. It may expose only a finite ambient representation plus total membership/equivalence, or an opaque finite iterator plus exact equality and module operations.

The obstruction is strictly earlier than the accepted explicit-presentation theorem. For every finite `R_N`-module `M`,

`support_card(M;N) := gcd(N, |M|)`

is exactly the product of those hidden primes on which `M` has nonzero CRT component. Hence a genuinely one-sided support state has

`support_card(M;N) in {p,q}`.

If the pre-readout interface is reflection-complete, `|M|` is effectively computable without `p`, `q`, candidate-prime schedules, or any classical factoring subroutine. Therefore the claimed scalarization delay fails even when no presentation matrix is exposed.

A second constructive theorem shows that the same complete reflection interface can, by finite exhaustive search, recover an ordinary finite presentation. Thus `G_exp-Fit` also applies after compilation. The cardinality scalar is simply the cheapest obstruction.

This does **not** prove impossibility for all opaque, lazy, implicit, effectful, oracle-like or non-ring computation. The smallest surviving capability is narrower:

`NONREFLECTIVE_EFFECTFUL_TYPED_SUPPORT_WITH_NONTRIVIAL_PRE_READOUT_COMPOSITION`.

No Working Truth, Foundation, L4, factoring lower bound, algorithmic speedup, or novelty claim is asserted.

## 2. Frozen typed grammar `G_reflect-FM`

Fix public `N=pq`, with distinct hidden primes `p,q`. The process receives only `N`.

A pre-readout typed state is one finite `R_N`-module object together with one of the following **complete reflection interfaces**.

### 2.1 Ambient-submodule form

`Sub(n, Mem)` denotes a submodule `M <= R_N^n`.

Public pre-readout operations:

- enumerate every ambient tuple in `R_N^n` from public `N,n`;
- evaluate the total predicate `Mem(x) in {false,true}`;
- exact module addition, negation and scalar multiplication on accepted tuples.

`Mem` may be implemented by arbitrary deterministic factor-blind public code. No basis or relation matrix is assumed available.

### 2.2 Ambient-quotient form

`Quot(n, EqQ)` denotes an `R_N`-module quotient of the public finite ambient set `R_N^n`.

Public pre-readout operations:

- enumerate every ambient representative in `R_N^n`;
- evaluate total quotient equality `EqQ(x,y)`;
- exact induced zero, addition, negation and scalar multiplication on classes.

No quotient basis, relation matrix, annihilator or class-count primitive is exposed.

### 2.3 Opaque-handle iterator form

`Opaque(Iter, Eq, Add, Neg, Scale)` denotes a finite `R_N`-module whose elements are opaque handles.

Public pre-readout operations:

- `Iter()` is a terminating finite iterator that visits every element at least once and emits an end marker;
- `Eq` decides extensional equality of handles;
- module operations are exact.

The iterator may contain duplicates and need not be canonical.

### 2.4 Total linear-map form

A map `f:R_N^a -> R_N^b` may be exposed only by total evaluation `Eval_f(x)`.

Public transformations may form finite direct sums, kernels, images, cokernels, intersections, sums, pullbacks, pushouts or quotients **provided the resulting state again supplies one of the complete reflection interfaces above**.

### 2.5 Declared pre-readout observations

The primitive observation list intentionally excludes:

- `|M|`;
- a basis;
- a presentation matrix;
- determinants or minors;
- Fitting generators;
- Smith data;
- annihilator generators;
- a proper gcd with `N`.

This exclusion does not create semantic opacity if those quantities are effectively reconstructible by composing allowed observations. The task explicitly forbids implementation secrecy as a substitute for unavailable information.

### 2.6 Declared readout

A candidate may declare an arbitrary later `Readout(M)` intended to collapse typed one-sided support to a scalar factor witness.

The hard target requires that no equivalent scalar support witness be effectively available before this boundary. The theorems below show that `G_reflect-FM` fails that requirement.

## 3. Theorem A — cardinality is an exact CRT-support scalar

Let `R_N = Z/NZ` with `N=pq`, `p != q` prime, and let `M` be any finite `R_N`-module.

Define

`M_p := M tensor_R F_p`,
`M_q := M tensor_R F_q`.

Let

`a = dim_Fp(M_p)`,
`b = dim_Fq(M_q)`.

Then

`|M| = p^a q^b`

and therefore

`gcd(N, |M|) = p^[a>0] q^[b>0]`.

Equivalently:

- `gcd(N,|M|)=1` iff `M_p=M_q=0`;
- `gcd(N,|M|)=p` iff `M_p != 0` and `M_q=0`;
- `gcd(N,|M|)=q` iff `M_p=0` and `M_q != 0`;
- `gcd(N,|M|)=N` iff both hidden components are nonzero.

In particular,

`ONE_SIDED_HIDDEN_SUPPORT(M)`
iff
`1 < gcd(N,|M|) < N`.

### Proof

Chinese remaindering gives

`R_N ~= F_p x F_q`.

Let `e_p,e_q` be the two orthogonal central idempotents in the abstract CRT decomposition. Every `R_N`-module decomposes internally as

`M ~= e_p M x e_q M`.

Because `M` is finite, `e_p M` and `e_q M` are finite-dimensional vector spaces over `F_p` and `F_q`, with dimensions `a,b`. Hence their cardinalities are `p^a` and `q^b`, so

`|M|=p^a q^b`.

Since `N=pq` is squarefree, taking `gcd(N,|M|)` retains precisely the prime factors whose exponents in `|M|` are positive. QED.

No hidden idempotent is computed by the algorithm. The idempotents appear only in the proof of the cardinality identity.

## 4. Theorem B — complete reflection computes cardinality before readout

Every `G_reflect-FM` state makes `|M|` effectively computable before the declared readout.

### Ambient-submodule case

Enumerate the public finite ambient set `R_N^n` and count the tuples satisfying `Mem`.

This uses only `N,n` and the allowed total predicate.

### Ambient-quotient case

Enumerate `R_N^n`. Using total `EqQ`, partition the finite ambient set into quotient equivalence classes and count the classes.

This uses no presentation matrix.

### Opaque-handle case

Run `Iter()` to the end marker. Deduplicate the finite handles using total `Eq` and count the distinct classes.

The runtime may be enormous; that is irrelevant here. The task asks whether scalarization is effectively available, not whether exhaustive reflection is efficient.

Combining this theorem with Theorem A gives a public factor-blind pre-readout algorithm:

1. compute `c=|M|`;
2. compute `g=gcd(N,c)`;
3. if `1<g<N`, the typed state already exposes one-sided hidden support as a proper factor.

Therefore:

`COMPLETE_EXTENSIONAL_REFLECTION + ONE_SIDED_FINITE_MODULE_SUPPORT`
implies
`PRE_READOUT_PROPER_GCD`.

The declared readout is semantically too late.

## 5. Theorem C — complete reflection also reconstructs a finite presentation

Even if cardinality were removed from consideration, `G_reflect-FM` does not escape the accepted explicit-presentation boundary.

Given a complete finite module interface for `M`:

1. enumerate all distinct elements
   `M={m_1,...,m_h}`;
2. use all elements as a finite generating family;
3. define the public surjection
   `phi:R_N^h -> M`,
   `phi(a_1,...,a_h)=sum a_i m_i`;
4. enumerate the finite coefficient space `R_N^h`;
5. test `phi(a)=0_M` by the exposed exact operations/equality;
6. collect the finite kernel
   `K=ker(phi)={k_1,...,k_t}`;
7. form the relation matrix `C in Mat_(h x t)(R_N)` whose columns are the `k_j`.

Because every kernel element itself appears among the listed relation generators,

`im(C)=K`

and therefore

`M ~= coker(C)`.

Choosing canonical integer representatives of entries and adjoining the relations `N e_i=0` gives an explicit finite integer presentation

`[ C | N I_h ]`.

This compiler is factor-blind and requires no `p,q`. Its cost can be exponential or worse; no complexity claim is made.

Consequences:

- an explicit finite presentation is recoverable;
- relation matrices are recoverable;
- determinant/minor families and Fitting ideals become recoverable;
- integer Smith data becomes recoverable from `[C | N I_h]`;
- the accepted `G_exp-Fit` determinantal scalarization theorem applies after compilation.

Thus complete extensional reflection is not genuine representation-level support hiding.

## 6. Theorem D — total black-box linear evaluation is not opaque

Let a public map

`f:R_N^a -> R_N^b`

be hidden behind only a total evaluation interface `Eval_f(x)`.

Query the public standard basis vectors `e_1,...,e_a`.

The vectors

`Eval_f(e_j)`

are exactly the columns of the matrix of `f`. Therefore `a` evaluations reconstruct the full matrix.

Hence an arbitrary-basis-query linear black box is already an explicit-presentation source. Kernels, images and cokernels built from it are not protected merely because the implementation calls the map “opaque”.

The smallest possible black-box survivor must therefore restrict reflection/evaluation itself, not only suppress a printed matrix.

## 7. Exact scalar-clean-coordinate witness: lazy quotient still leaks by cardinality

Reuse the accepted factor-blind projection witness only as a non-vacuity control:

`N=15`, hidden factors `3,5`,

`A = [[1,1],[1,4]]`.

Every coordinate satisfies

`gcd(15,A_ij)=1`.

So no entry itself is a factor witness.

Now forget the matrix presentation at the interface and expose only the typed quotient

`Q = coker(A:R_15^2 -> R_15^2)`

through ambient representatives, quotient equality and module operations.

Hidden ranks are

`rank_F3(A)=1`,
`rank_F5(A)=2`.

Therefore

`dim_F3(Q_3)=1`,
`dim_F5(Q_5)=0`.

The typed quotient has genuine one-sided support.

But the quotient equality interface permits complete class enumeration, and exactly

`|Q|=3`.

Hence

`gcd(15,|Q|)=3`.

This is a strict opacity test:

- the entries are gcd-clean;
- the presentation may be withheld from the interface;
- no determinant/minor primitive is called;
- total quotient equality alone still makes the support scalar available by finite reflection.

So merely replacing an explicit matrix by a lazy quotient wrapper does not cross the scalarization boundary.

## 8. Mandatory representation audit

| Candidate support witness | Pre-readout status in `G_reflect-FM` | Reason |
|---|---|---|
| finite presentation | `RECOVERABLE` | Theorem C exhaustive generator/relation compiler |
| basis | `NOT_ALWAYS_EXISTS / EFFECTIVELY_TESTABLE` | enumerate tuples and test the induced finite map; non-freeness is not opacity |
| relation matrix | `RECOVERABLE` | columns are the exhaustively enumerated kernel relations |
| annihilator | `RECOVERABLE` | enumerate `r in R_N` and test `r m=0` on all reflected elements |
| determinant/minor family | `RECOVERABLE_AFTER_COMPILATION` | computed from the recovered presentation |
| Fitting generator | `RECOVERABLE_AFTER_COMPILATION` | determinantal ideals of recovered presentation |
| Smith data | `RECOVERABLE_AFTER_INTEGER_LIFT` | apply Smith reduction to `[C | N I_h]` |
| resultant | `NOT_INTRINSIC` | if a polynomial/operator presentation is supplied, its finite data is compilable; no separate hiding is obtained |
| norm / trace | `NOT_INTRINSIC` | any exposed finite linear operator with total basis evaluation is reconstructible |
| order | `EFFECTIVELY_ENUMERABLE_WHEN_DEFINED` | and group-order/smoothness use remains separately excluded |
| equivalent scalar support witness | `RECOVERABLE_DIRECTLY` | `gcd(N,|M|)` already gives exact hidden support set |

The audit therefore fails at two independent levels:

`CARDINALITY_SCALARIZATION`

and

`FINITE_PRESENTATION_RECOVERY`.

## 9. Why this is not a classical factoring mechanism relabel

The proof does not use:

- Pollard `p-1`, Williams `p+1`, ECM, smooth group orders or annihilating exponents;
- collision/cycle detection or rho-style stopping;
- congruence of squares, relation collection, CFRAC, Dixon, QS or NFS;
- a named hidden prime/maximal ideal or Hensel lifting;
- a supplied CRT idempotent or hidden selector;
- candidate-prime trial schedules;
- a direct scalar nonunit inserted as input.

The `N=15` witness is not proposed as a factoring algorithm. It is an adversarial test showing that a typed quotient with gcd-clean coordinates still fails the declared opacity interface because extensional reflection computes its cardinality.

This return consumes the accepted prior-art mechanism map as a frozen firewall and makes no new novelty claim.

## 10. Deterministic checker

Checker:

`research_checks/N_COUPLED_OPAQUE_LAZY_TYPED_SUPPORT_SCALARIZATION_DELAY_CHECK_20260901.py`

Certificate:

`research_artifacts/N_COUPLED_OPAQUE_LAZY_TYPED_SUPPORT_SCALARIZATION_DELAY/reflection_complete_typed_module_scalarization_certificate.json`

Executed result:

`PASS REFLECTION_COMPLETE_TYPED_MODULE_SCALARIZATION matrix_cases=2500 support_checks=2504 one_sided=1094 eval_reconstruction=2500 equality_class_counts=1 relation_enumeration=1 witness_relations=1125 witness=N15_A[[1,1],[1,4]]_card3_gcd3`

Finite regression envelope:

- hidden prime pairs `(2,3),(2,5),(3,5),(3,7)`;
- `2x2` matrices over entry alphabet `{0,1,2,3,4}`;
- `2,500` semiprime/matrix cases;
- exact quotient cardinality from public image enumeration;
- exact hidden-component dimensions used only by the checker oracle to verify the theorem;
- `1,094` one-sided coker-support cases;
- every one-sided case produced a proper cardinality gcd;
- `2,500` total linear-map evaluators were reconstructed exactly by standard-basis probing;
- the `N=15` lazy-quotient witness was independently class-counted from quotient equality;
- the generic all-elements-as-generators presentation compiler was instantiated on that witness:
  `3` extensional elements, `1,125` exhaustively enumerated relation tuples, quotient cardinality recovered as `3`.

The checker is regression evidence only. The all-`p,q`, all-finite-module statement is Theorem A.

## 11. Smallest surviving capability

The accepted predecessor left:

`OPAQUE_OR_LAZY_TYPED_SUPPORT_CHANGE_BEFORE_SCALARIZATION`.

This result removes every **reflection-complete finite module** implementation of that slogan.

A successor must now provide a genuinely stronger semantic capability:

`NONREFLECTIVE_EFFECTFUL_TYPED_SUPPORT_WITH_NONTRIVIAL_PRE_READOUT_COMPOSITION`.

At minimum it must deny all of the following before readout for reasons intrinsic to the interface, not because the implementation declines to call them:

1. no finite complete iterator of extensional elements plus decidable equality;
2. no finite public ambient domain plus total membership/equivalence predicate;
3. no arbitrary standard-basis probing of a total linear evaluator;
4. no finite descriptor AST with an effective compiler to presentation;
5. no other exact procedure that computes cardinality/support before readout.

Yet it must still have **nontrivial pre-readout compositional semantics**. A mere sealed token with one final `reveal()` method does not establish that one-sided support was carried in a mathematically meaningful operational state; it simply moves the entire mechanism into the readout oracle.

A future positive task must therefore explain how pre-readout operations can interact with the typed support while remaining non-reflective, and must separately prove that the final readout is not a renamed classical mechanism.

This return does not assert that such a capability exists.

## 12. Tool/method reuse

### `T0_BRC`

`REUSE_APPLIED`.

The proof keeps typed support, provenance and scalar readout as distinct objects. It does not infer support after erasing the interface that carried it.

### `T6_OPERATION_SAFE_QUOTIENT`

`REUSE_APPLIED_AS_ADVERSARIAL_GUARD`.

The lazy quotient witness makes the preserved observation contract explicit. Total quotient equality is sufficient to reconstruct class cardinality, so the quotient is not safe as an opacity boundary merely because a matrix is hidden.

Method-harvest classification:

`RESULT_ONLY`.

No reusable global tool family is introduced.

## 13. Scope firewall

This return proves only the declared `G_reflect-FM` boundary. It does **not** prove:

- impossibility of arbitrary implicit or lazy computation;
- impossibility of infinite typed states;
- impossibility of partial/nonterminating iterators;
- impossibility of capability-secured or effectful interfaces;
- impossibility of black boxes whose query set is intrinsically restricted;
- a complexity lower bound for reconstructing cardinality or a presentation;
- that every non-reflective interface is useful or factor-blind;
- that any surviving interface factors integers;
- novelty or absence of prior art beyond the already-reviewed firewall.

The exact frozen conclusion is:

`REFLECTION_COMPLETE_FINITE_TYPED_SUPPORT != DELAYED_SCALARIZATION`.

For finite `R_N`-modules, one-sided support plus complete extensional reflection already exposes the public support scalar `gcd(N,|M|)`, and the same interface can reconstruct an explicit finite presentation.

## 14. Control recommendation

Driver should review this Result at exact negative-boundary strength.

If accepted:

- freeze the cardinality support-scalar theorem for reflection-complete finite `R_N`-modules;
- freeze the exhaustive finite-presentation compiler as the second obstruction;
- do not generalize to all implicit computation;
- any successor should target one exact `NONREFLECTIVE_EFFECTFUL_TYPED_SUPPORT` interface with meaningful pre-readout composition and attack it for hidden oracle/classical-mechanism equivalence.

No automatic successor publication is requested from the Researcher lane.
