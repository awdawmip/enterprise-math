# R004 precision genesis — Supplement 08: product factorization and the true joint-coupling boundary

Status: `PROVED_WIP + EXECUTABLE_CHECKED + NEGATIVE_BOUNDARY + FOUNDATION_FEEDBACK_CANDIDATE`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_07.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

This supplement corrects the provisional frontier stated at the end of Supplement 07. A correlated, non-product action language does **not** by itself force a joint representation when dynamics and observation remain componentwise/product-valued. The actual obstruction is coupling in the observable or dynamics.

## 1. Product-signature factorization theorem

Let

`X = prod_i X_i`.

For every joint future action `a=(a_i)`, assume the transition acts componentwise:

`a.x = (a_i.x_i)_i`.

Assume the declared observable is the full product vector

`O(x)=(O_i(x_i))_i`.

Let `A` be any nonempty set of joint actions. It may be highly correlated and need not be a Cartesian product of its coordinate projections.

Define the joint future signature

`Sigma_A(x)=(O(a.x))_(a in A)`.

For axis `i`, let

`A_i=pi_i(A)`

and define the marginal signature

`Sigma_i(x_i)=(O_i(a_i.x_i))_(a_i in A_i)`.

### R004-COMP-T05 — correlation-invisible product kernel

For two product states `x,y`,

`Sigma_A(x)=Sigma_A(y)`

if and only if

`Sigma_i(x_i)=Sigma_i(y_i)`

for every axis `i`.

Hence

`ker(Sigma_A) = prod_i ker(Sigma_i)`.

### Proof

If the joint signatures agree, then for every joint action `a in A` and every axis `i`, the `i`-th observable coordinates agree. Every `a_i in A_i` appears in at least one joint action, so all marginal signature coordinates agree.

Conversely, if every marginal signature agrees, then for each joint action every coordinate of the full product observable agrees, hence the complete joint observable vector agrees.

No independence or Cartesian-product assumption on the action labels is needed. ∎

This is elementary product-kernel mathematics and should not be claimed as a new generic theorem.

## 2. Consequence for the CRT translation compiler

For

`Z/MZ ~= prod_i Z/p_i^(K_i)Z`,

let `T subset Z/MZ` be any nonempty finite translation set, not necessarily a subgroup and not necessarily a product of its CRT projections.

Observe the full vector of capped prime-power valuations. Translation is componentwise under CRT. Therefore R004-COMP-T05 applies.

The exact joint compiler is:

1. project `T` to every prime-power component;
2. compile each projected translation language using the one-axis p-adic trie compiler from Supplement 07;
3. take the tuple of those axis tokens.

The exact class count is therefore

`C_T = prod_i C_(pi_i T)`,

where each factor is the one-axis trie class count

`|C_i| + # deficit nodes_i`.

Thus action-label correlation is invisible to the safe quotient as long as the observable exposes the complete coordinate vector and the dynamics remains componentwise.

The executable module `precision_crt_translation_compiler.py` checks this directly against literal joint future signatures for arbitrary bounded correlated translation sets.

## 3. Why the provisional open problem in Supplement 07 disappears

Supplement 07 ended with the concern that a correlated action subset might make an axiswise compiler over-refine because some joint action combinations never occur.

That concern is false under the declared full-vector observation semantics.

Future equivalence asks whether **every observable coordinate** agrees for every actually allowed joint action. If a marginal action value appears anywhere in the joint language, the corresponding coordinate equality is already required. The missing Cartesian combinations do not remove that marginal requirement.

Therefore the correct boundary is not

`correlated action labels -> joint state`.

It is

`cross-axis coupling in required future outputs or dynamics -> potentially joint state`.

This correction is important because it prevents the compiler architecture from introducing relation state merely because action metadata is correlated.

## 4. Minimal coupled-observation counterexample

Take the two-bit product state

`X=(Z/2Z)^2`.

Actions act componentwise by XOR. Replace the full product observation by the coupled scalar

`O(x_1,x_2)=x_1 x_2`.

Consider two joint action languages:

`A={(0,0),(1,1)}`

and

`B={(0,1),(1,0)}`.

They have:

- the same action count `2`;
- the same first-axis marginal action set `{0,1}`;
- the same second-axis marginal action set `{0,1}`.

Nevertheless their future-safe partitions are different.

For `A`:

`{{00},{01,10},{11}}`.

For `B`:

`{{00,11},{01},{10}}`.

Thus the marginal action languages and action cardinality are insufficient once the observable couples axes.

The distinction comes entirely from which joint actions are paired with which other-axis actions.

Hence

`same action marginals + same action count != same safe quotient`

for coupled observations.

## 5. Compiler architecture consequence

The current R004 representation compiler now has a clean layering rule.

### Axiswise compiler is exact when

- state is a Cartesian/CRT product;
- dynamics acts componentwise;
- declared observable exposes the complete product of component observables.

Then action correlation can be discarded after taking marginal action languages.

### Joint repair is potentially required when

- an observable mixes multiple axes;
- a transition updates one axis using another axis;
- the future language asks for relation/witness identity across axes rather than independent coordinate values.

At that point the missing information is not another valuation digit. It is a **coupling state**.

This is precisely where A3 structured relation-state and A4 witness/correspondence machinery become relevant candidates. R004 must consume those owners rather than silently encoding joint coupling inside an exponent tuple.

## 6. Validation

New executable assets:

- `precision_crt_translation_compiler.py`;
- `precision_product_language_factorization.py`;
- matching regression files.

Checks include:

- every nonempty joint action set on the two-bit product for the full product observable;
- every nonempty translation language modulo `6` for the CRT compiler;
- all translation languages of size up to `3` modulo `12` in the bounded regression;
- explicit coupled-observation counterexample with equal action count and identical marginal action sets.

Independent exploratory search first attempted to find an over-refinement counterexample under full-vector observation and failed across multiple small CRT moduli. The theorem above explains why no such counterexample exists.

These are finite proof/executable checks, not Lean formalization or fresh full-repository CI.

## 7. Revised compiler frontier

The R004 compiler frontier is now:

`one p-power axis + arbitrary translations -> exact p-adic trie compiler`;

`multiple CRT axes + arbitrary correlated translations + full vector observation -> exact product of marginal trie compilers`.

The genuinely open problem is narrower:

> **Given a finite coupled observable or coupled dynamics, can the project compile the coarsest joint repair state into a structured relation/witness normal form instead of an opaque partition table?**

That question is no longer purely R004-local. It touches P023 minimal repair, P024 action-language precision, A3 relation-state algebra and A4 witness/correspondence semantics. Any mother theorem must therefore be routed through the appropriate owner/Foundation process.
