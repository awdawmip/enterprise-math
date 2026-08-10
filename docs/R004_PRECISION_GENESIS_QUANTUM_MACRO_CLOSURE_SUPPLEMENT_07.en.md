# R004 precision genesis — Supplement 07: closed-form future-language representation compiler

Status: `PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_SPECIALIZATION + FOUNDATION_FEEDBACK_CANDIDATE`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_06.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 06 established the operation-relative representation principle:

`count / defect / exponent / repair` are not one universal coordinate system; a representation is legal only for the future language that actually descends through it.

This supplement advances that principle from a boundary into a first **closed-form representation compiler**. It does not re-own the generic P023 future-safe quotient theorem or the generic P024 translation-language program. Instead it solves one explicit finite arithmetic family.

## 1. Prime-power setup

Fix a prime `p`, a positive cap `K`, and the finite state space

`X = Z / p^K Z`.

The declared observable is the capped valuation

`q_K(x)=min(v_p(x),K)`,

with the zero residue assigned level `K`.

For a future translation language `T subset X`, the future signature is

`Sigma_T(x)=(q_K(x+t))_(t in T)`.

By P023, the coarsest safe representation is `ker(Sigma_T)`. The question here is whether that kernel has a direct arithmetic normal form, so no generic partition-refinement loop is needed.

## 2. Subgroup translation compiler

First take the translation subgroup

`H_s = p^s Z / p^K Z`,

where `0<=s<=K`.

### R004-COMP-T01 — low-level invariance

If `v_p(x)=a<s`, then every `t in H_s` has valuation at least `s>a`. Therefore

`v_p(x+t)=a`

for every allowed future translation. All residues with the same level `a<s` have the same complete future signature.

Hence below the subgroup threshold the valuation level alone is sufficient.

### R004-COMP-T02 — exactness inside the reachable subgroup

If `v_p(x)>=s`, write

`x=p^s u` modulo `p^K`.

Every allowed translation has the form `p^s h`, so

`x+p^s h = p^s(u+h)`.

After removing the common factor `p^s`, `h` ranges over every residue modulo `p^(K-s)`. Full translations on that reduced component distinguish every `u` exactly: choose `h=-u` to send one state to capped level `K`, while any distinct `u'` cannot also reach that level under the same translation.

Therefore inside `H_s` the future-safe quotient must retain the exact tail

`u = x/p^s mod p^(K-s)`.

### R004-COMP-T03 — closed-form minimal token

The coarsest future-safe token is

`R_(p,K,s)(x) = ("v",v_p(x))` if `v_p(x)<s`,

and

`R_(p,K,s)(x) = ("r",x/p^s mod p^(K-s))` if `v_p(x)>=s`.

The first family contributes exactly `s` valuation classes and the second contributes exactly `p^(K-s)` exact subgroup residues. Hence

`C(p,K,s)=s+p^(K-s)`.

This is both sufficient and minimal because every pair of distinct tokens has a future translation separating it.

The executable oracle confirms token equality iff full future-signature equality.

## 3. Translation depth gives an exact exponential repair law

Define the translation depth

`t=K-s`.

The allowed subgroup has exactly

`|H_s|=p^t`

translations, while the minimum state complexity is

`C_(p,K)(t)=K-t+p^t`.

The pure valuation baseline at `t=0` has `K+1` classes, so the exact additional repair cost is

`E_p(t)=p^t-t-1`.

The marginal cost of opening one further translation digit is

`E_p(t+1)-E_p(t)=(p-1)p^t-1`,

and the second finite difference is

`Delta^2 E_p(t)=(p-1)^2 p^t>0`.

Thus state complexity is discretely convex in future translation depth. Additional future capability becomes strictly more expensive at each layer, except for the unique plateau

`p=2, t=0 -> 1`,

where `E_2(1)=0`: the first binary translation digit introduces no new quotient classes because the top two capped valuation classes already name the two residues in that two-point subgroup.

This is an exact finite complexity law; it is not an entropy or information-theoretic limit theorem.

## 4. CRT product compiler

Now let

`M=prod_i p_i^(K_i)`

with distinct primes. By the Chinese remainder theorem,

`Z/MZ ~= prod_i Z/p_i^(K_i)Z`.

Let the future translation subgroup factor componentwise with levels `s_i`, equivalently depths `t_i=K_i-s_i`.

The observation is the vector of capped valuations on the prime-power components. Because both the state space and the declared subgroup language factor across CRT components, future-signature equality is coordinatewise.

Hence the minimal compiled state is the tuple of the one-prime tokens, and

`C_CRT = prod_i [s_i+p_i^(K_i-s_i)]`

or equivalently

`C_CRT = prod_i [K_i-t_i+p_i^t_i]`.

The branch exhaustively checks representative composite moduli and all small subgroup-level combinations against the literal full future signatures.

This is the first R004 compiler family whose state complexity can be written directly from a typed future-language description without enumerating the whole generic quotient first.

## 5. Arbitrary one-axis translation languages: the p-adic trie compiler

Subgroup closure is not required on a single prime-power axis.

For any nonempty finite translation set `T subset Z/p^K Z`, define the center set

`C=-T mod p^K`.

Then

`q_K(x+t)=min(v_p(x-c),K)`

for the corresponding center `c`.

Read residues in p-adic digit order: least significant digit first. Two residues agree modulo `p^j` exactly when their first `j` p-adic digits agree. The center set therefore defines an occupied p-adic prefix trie.

For a state `x` there are exactly two cases.

1. **Center:** `x in C`. Its own signature contains value `K`, so this center is a singleton future-safe class.
2. **Trie exit:** `x notin C`. Follow the low-digit prefix of `x` as long as some center shares it. At a unique deepest occupied parent prefix, the next digit of `x` enters an unoccupied child branch.

All states exiting through the same occupied parent prefix have identical future signatures:

- centers outside that parent already differ at an earlier digit, so their valuations are fixed by the shared parent prefix;
- centers inside that parent all differ from the exiting state at the next digit, so their valuation is exactly the parent depth.

Conversely, different exit parents are future-distinguishable by a center lying below one of the two trie positions; center tokens are also mutually distinguishable.

Therefore the coarsest safe representation is exactly

`center token OR deepest occupied exit-parent token`.

### R004-COMP-T04 — arbitrary-language class-count formula

Let a **deficit node** be an occupied trie node at depth `<K` with at least one unoccupied child. Then

`C_T = |C| + # deficit nodes`.

The first term counts exact center leaves; the second counts one merged wildcard class for all empty child branches of each occupied parent.

This is a closed form on the finite p-adic center trie, not a normalized measure.

The subgroup theorem is recovered immediately. For `C=H_s`, the first `s` nodes form one occupied path with empty siblings, while the subtree below depth `s` is completely filled. Hence there are exactly `s` deficit nodes and

`C_T=p^(K-s)+s`.

## 6. Same action count can require different state complexity

The trie theorem proves a new negative boundary:

`number of future actions != representation complexity`.

For `p=2`, `K=4`, two-center languages already give different class counts:

- centers `{0,8}` -> `5` classes;
- `{0,4}` -> `6` classes;
- `{0,2}` -> `7` classes;
- `{0,1}` -> `8` classes.

All four languages contain exactly two centers. Only their p-adic separation changes.

For two distinct centers `c_1,c_2`, let

`r=v_p(c_1-c_2)<K`.

Their p-adic trie shares one path through depth `r` and then splits. Counting center leaves and incomplete occupied parents gives

`C_2 = 2K-r` for `p=2`,

and

`C_2 = 2K-r+1` for `p>2`.

Equivalently,

`C_2=2K-r+1_(p>2)`.

Thus operations that are p-adically closer are more redundant as future distinguishers. Future-language **geometry**, not merely cardinality, controls the minimum present-state complexity.

## 7. Validation

Two executable compilers are added:

- `precision_representation_compiler.py` — subgroup and CRT closed forms;
- `precision_translation_trie_compiler.py` — arbitrary one-prime translation sets.

Committed regressions compare compiler tokens against literal full future signatures on bounded families.

Independent research enumeration additionally checked:

- every nonempty translation subset of `Z/2^4 Z`: **65,535 / 65,535** exact;
- every nonempty translation subset of `Z/3^2 Z`: **511 / 511** exact;
- subgroup and CRT families across multiple small prime powers and composite moduli.

This is exact finite validation, not a Lean proof and not fresh full-repository CI.

## 8. Ownership and prior-art boundary

The generic theorem

`future language -> coarsest safe quotient = future-signature kernel`

belongs upstream to P023/FQ-004. Translation-language precision belongs to P024. p-adic valuation, cyclic p-groups, CRT and prefix-tree reasoning are established mathematics.

R004's contribution here is therefore deliberately narrower:

- one closed-form compiler for capped valuation under subgroup translations;
- its exact exponential/discrete-convex state-cost law;
- a CRT product specialization;
- an arbitrary one-axis p-adic trie normal form;
- the negative boundary that equal action counts can have different state cost because future-language geometry matters.

Historical novelty of this precise package remains `NOVELTY_UNVERIFIED`.

## 9. Next frontier

The compiler frontier is now sharply split.

Solved at WIP level:

`one p-power axis + arbitrary finite translations -> trie compiler`,

and

`multiple CRT axes + product-closed translation subgroups -> product compiler`.

Still open:

> **multiple prime-power axes with a correlated, non-product translation language.**

In that case the action set is a subset of the CRT product rather than a Cartesian product. Independent axis compilation can over-refine because correlations among future actions may remove combinations that never occur.

That is the next meaningful compiler problem. It asks for the minimal joint repair state induced by correlated finite future operations, without falling back immediately to an opaque generic partition table.
