# P000 Philosophy-First Q23 — all-finite-arity forward XOR independence

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

Researcher-ID: `EM-P000-79CA40`
Task-ID: `RS-P000-PHILOSOPHY-FIRST-FORWARD-XOR-ALL-N-INDEPENDENCE`
Publication-ID: `TP2-5D06C7F7782AB19751E8`
Execution-Record-ID: `ER-60D301E690740902816C`
Claim-ID: `chatgpt-phq23-20260901-1016`
Execution branch: `research/p000-phil-q23-forward-xor-all-n-em-p000-79ca40`
Execution base: `ba1396656ac3f8d935d653c58b6080803f1bdbaf`

Hard target: `P000_FORWARD_XOR_ALL_FINITE_ARITY_ZERO_SUPPORT_INDEPENDENCE_PROVED_OR_REFUTED`

## 1. Terminal result

`SUCCESS / ALL_FINITE_ARITY_NONCOPYING_XOR_NORMAL_FORM_AND_ZERO_SUPPORT_INDEPENDENCE_PROVED`

Q20 的三环 `(n+1)^m` 现象是任意有限 arity 的结构定理，不是有限枚举巧合。

For every finite `m,n>=0`, the frozen grammar generates exactly the maps
`f:C2^m -> C2^n` encoded by

`alpha:{1,...,m}->{0,1,...,n}`,

where `alpha(i)=0` discards input `i`, and `alpha(i)=j>0` sends that input to output `j`.
Hence

`f(x)_j = XOR_{i:alpha(i)=j} x_i`.

Equivalently, the `F2` matrix of `f` has every source column equal to `0` or one standard basis vector.
Therefore

`|Hom(C2^m,C2^n)|=(n+1)^m`

for all finite `m,n`, and every generated map preserves zero.

Define

`Z_n(x) := (x=0)` and `A_n(x) := true`.

Both satisfy every frozen backward-free forward structural law, but they disagree on every nonzero state.
Thus the frozen forward theory does not force any nonzero holonomy effective at any finite arity.

## 2. Universal normal-form proof

Let `N(m,n)` be the class of matrices in `F2^(n x m)` whose columns lie in
`{0,e_1,...,e_n}`.

### Generator inclusion

Every allowed primitive lies in `N`:

- coordinate permutation: one standard basis vector per column;
- restriction/deletion: deleted source columns become `0`;
- zero insertion: target coordinates may be unused, but source columns remain basis vectors;
- noncopying XOR fusion: several distinct source columns may hit the same target basis vector, while no source column hits two outputs;
- identity: a permutation special case.

### Closure under composition

Take `f in N(m,n)` and `g in N(n,p)`.
A source column of `f` is either `0` or `e_j`.
Under `g`, it becomes either `0` or the `j`-th column of `g`.
That column is again `0` or some `e_k`.
So `g o f in N(m,p)` for arbitrary finite dimensions.

### Converse generation

Given any assignment `alpha`, construct it by four stages:

1. delete all inputs with `alpha(i)=0`;
2. permute retained inputs so equal nonzero `alpha`-fibres form consecutive blocks;
3. XOR each block to one output; if only binary XOR is primitive, induct on block size;
4. insert zero outputs for empty target fibres.

The fibres are disjoint, so this factorization never copies an input.
It realizes the prescribed action on every source basis vector.
Therefore the generated grammar is exactly `N(m,n)`.

## 3. Counting and standard-structure dedup

Each of the `m` source coordinates independently has `n+1` choices: discard, or choose one of `n` targets.
Hence

`|Hom(C2^m,C2^n)|=(n+1)^m`.

This also covers `m=0` and `n=0`.

Under the assignment encoding, composition is ordinary composition of partial functions on source/target basis-index sets, with `0` meaning undefined.
So the morphism category is a standard finite partial-function structure represented linearly on `F2` bases.
This is not claimed as Enterprise novelty.

Prior-art dedup after the native proof:
J.R.B. Cockett and Stephen Lack, *Restriction categories I: categories of partial maps*,
Theoretical Computer Science 270 (2002), 223-259,
DOI `10.1016/S0304-3975(00)00382-0`.

## 4. Zero-support model for every finite arity

Every generated map has `f(0)=0`.
Consequently `Z_n(x):=(x=0)` satisfies:

- forward preservation along every generated morphism;
- permutation invariance;
- restriction/deletion forward preservation;
- neutral zero insertion/deletion, in fact `Z(x) <=> Z(insert_zero(x))`;
- glue, in fact `Z(x,y) <=> Z(x) AND Z(y)`;
- every declared XOR fusion-forward law;
- unit truth and unit naturality;
- associativity and fusion coherence, because those are equalities of forward structural maps.

The all-effective family `A_n` satisfies the same laws trivially.

For any `n>=1` and any `v!=0`, `Z_n(v)=false` while `A_n(v)=true`.
Because both are models of the same backward-free theory, semantic entailment of `E_n(v)` fails.

This proves

`ZERO_SUPPORT_EFFECTIVITY_INDEPENDENCE_PROVED_FOR_ALL_FINITE_ARITIES`.

The proof is structural, not a bounded census.

## 5. Exact obstruction boundary

The fully general criterion is simple:

> the zero-support obstruction is crossed only by adding an axiom or primitive that `Z` does not satisfy.

Within the current structural/Horn vocabulary, the minimal one-premise mechanisms are:

1. **Nonzero-generating forward primitive.**
   Some `f` has `f(0)!=0`.
   A constant `1` or nonzero affine shift is the canonical example.
   Forward preservation then carries the effective zero/unit state to a nonzero effective state.

2. **Backward reflection across a nontrivial zero fibre.**
   Some `x!=0` has `f(x)=0`, together with `E(f(x)) => E(x)`.
   The minimal frozen witness is XOR:
   `mu(1,1)=0`.
   From effective `0`, `FUSION_BACKWARD_2` yields effective `(1,1)`, and restriction yields effective `1`.

3. **Direct or equivalent nonzero-effectivity assertion.**
   Any axiom already implying some `E_n(v)` with `v!=0` kills `Z` by definition.

These are classifications inside the current one-premise structural/Horn vocabulary; they are not claimed to exhaust arbitrary logical syntax.

## 6. Stronger boundary: copying is not enough

Noncopying is needed for the exact `(n+1)^m` normal form.
It is not needed for zero-support independence.

For example the diagonal

`delta:C2->C2^2`, `delta(x)=(x,x)`

copies one source coordinate, so its matrix column has two `1`s and the noncopying normal form fails.
But `delta(0)=(0,0)`, so `Z` still satisfies forward preservation.

More generally, arbitrary additional `F2`-linear maps still preserve zero.
Therefore any extension that remains zero-preserving and forward-positive still leaves the zero-support countermodel alive.

This separates two issues:

- exact morphism normal form: depends on noncopying;
- effectivity obstruction: depends only on zero preservation plus forward-positive semantics.

## 7. Regression checker

Task-local checker:

`research_checks/P000_PHILOSOPHY_FIRST_FORWARD_XOR_ALL_N_INDEPENDENCE_CHECK_20260901.py`

Default `m,n<=4` run:

`PASS P000_Q23_FORWARD_XOR_ALL_N; checks=2789; max_dim=4; morphisms=1279; factorized=1279; zero_preserving=1279; hom_matrix=1,1,1,1,1/1,2,3,4,5/1,4,9,16,25/1,8,27,64,125/1,16,81,256,625; q20_prefix=144; normal_form=(target_dimension+1)^source_dimension; category=finite_partial_functions_on_basis_indices; matched_models=zero_support,all_effective; escape=backward_nontrivial_fibre_or_nonzero_generating_primitive_or_direct_nonzero_axiom; copying=breaks_noncopying_normal_form_but_preserves_zero_support; terminal=ALL_FINITE_ARITY_NONCOPYING_XOR_NORMAL_FORM_AND_ZERO_SUPPORT_INDEPENDENCE`

The checker independently generates permutations, deletions, zero insertions, pair XOR fusions and their composition closure.
It verifies 1279 morphisms, reconstructs all 1279 by delete -> permute -> block-fuse -> zero-insert, checks all 1279 preserve zero, and reproduces the Q20 `m,n<=3` prefix count `144`.

The checker is regression evidence only; Sections 2-6 are the universal proof.

Machine-readable certificate:

`research_artifacts/P000_PHILOSOPHY_FIRST_FORWARD_XOR_ALL_N_INDEPENDENCE/P000_Q23_FORWARD_XOR_ALL_N_CERTIFICATE_V1.json`

## 8. Hard-target disposition and control recommendation

Hard target disposition: `PROVED`.

Frozen subresults:

- `ALL_FINITE_ARITY_NONCOPYING_XOR_NORMAL_FORM_PROVED`;
- `ZERO_SUPPORT_EFFECTIVITY_INDEPENDENCE_PROVED_FOR_ALL_FINITE_ARITIES`;
- no higher-arity escape exists under the unchanged frozen grammar;
- the minimal semantic information boundary that can kill `Z` is classified.

If Driver accepts this Result:

- stop four-loop/five-loop enumeration under the unchanged forward zero-preserving grammar except as regression;
- reopen only for a genuinely new primitive or semantic relation;
- require every successor to state explicitly whether and how the new information invalidates `Z`;
- do not treat copying alone as sufficient;
- do not rename `FUSION_BACKWARD` as a derived old law;
- do not promote this Result to bare P000 / Working Truth / Foundation before Driver review.

Unresolved parent residue:
whether native P000 geometry/rotation/slice semantics contains an independently justified, non-circular relation that actually invalidates the zero-support countermodel.

Method harvest: `RESULT_ONLY / task-local checker only; no new global tool family`.
