# Causal Recursive Dimension Generator — Minimal Continuation State, Binary Coherence, and Arbitrary-Dimensional Generation

Status: `ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT FINITE THEOREMS + EXECUTABLE REFERENCES`

Ownership: derivation source is A3 `research/core/relation-quotient`. General future-equivalence/quotient theory remains A2/P023; carry/scale corollaries should flow to P018; geometry corollaries to P012/P022.

This note corrects an over-strong reading of higher-order coupling: pairwise factorization plus a triple failure does **not** by itself prove an absolute ternary primitive. For any fixed finite horizon one may sequentialize an arbitrary rule by storing enough prefix history. The meaningful question is how complicated the minimum future-safe continuation state must become if the *same* lower-dimensional causal law is to generate arbitrary dimensions.

## 1. Typed binary join kernel

Let `T` be the continuation types obtained after quotienting current witnesses by complete remaining-future signature. Define

\[
K(\alpha,\beta;\nu,\delta)\in\mathbb N_0,
\]

meaning that one `alpha` witness joined with one `beta` witness produces that many joint witnesses of continuation type `nu` and integer grade shift `delta`.

For type-grade inventories `F,G`, exact witness counting gives

\[
(F\star G)(\nu,E)=
\sum F(\alpha,E_1)G(\beta,E_2)K(\alpha,\beta;\nu,\delta)
\mathbf 1[E=E_1+E_2+\delta].
\]

No matrix, tensor, convolution or semiring is primitive here.

## 2. Exact associativity is the three-body compatibility gate

For singleton types `a,b,c`, left and right binary bracketings give

\[
L_{abc}^{\nu,d}=\sum_{\mu,d_1+d_2=d}K(a,b;\mu,d_1)K(\mu,c;\nu,d_2),
\]

\[
R_{abc}^{\nu,d}=\sum_{\mu,d_1+d_2=d}K(b,c;\mu,d_1)K(a,\mu;\nu,d_2).
\]

A binary law is bracket-independent exactly when

\[
L_{abc}^{\nu,d}=R_{abc}^{\nu,d}
\quad\text{for every exact typed outcome.}
\]

When this fails, retain positive left-only and right-only multiplicity defects separately; a signed scalar can hide two causally distinct failures.

If the equality holds, inventory composition is associative, hence every finite number of factors has the same result under every parenthesization. This is the exact condition under which one typed binary law can recursively generate arbitrary slot counts without adding an n-body composition rule.

## 3. Coupling order is state-language relative

Minimal nonfaces of the current causal-independence complex remain useful, but their order means only `factorization-failure order in the currently exposed state language`.

The even-parity states

\[
000,011,101,110
\]

have pairwise-factorized marginals but a non-factorized triple in the marginal-only language. Yet a two-state continuation variable

\[
\tau\in\{0,1\},\qquad \tau_{ab}=a\oplus b
\]

with the same binary XOR update and final acceptance `tau=0` generates even parity in arbitrary dimension. Thus exposed order 3 does not imply an absolute ternary composition primitive.

## 4. Contextual continuation types are compiled, not declared

If binary composition itself is an allowed future operation, ordinary continuation equivalence must include composition contexts. For every raw partner `p`, add the actions

\[
L_p(x)=p*x,\qquad R_p(x)=x*p.
\]

Repeatedly refine current observation classes by the classes reached under every such action. The stable classes are the contextual continuation types.

If raw composition is associative, this stable partition is a composition congruence, the induced type join is well-defined, and the induced type join is associative. Hence quotient-monoid structure is a shadow of

\[
\text{raw associative LEGO composition}
+\text{future contextual indistinguishability}.
\]

## 5. Pair grade coherence

For deterministic type join `a*b` and integer pair grade shift `gamma(a,b)`, bracket-independent three-body grade requires

\[
\gamma(a,b)+\gamma(a*b,c)=\gamma(b,c)+\gamma(a,b*c).
\]

The difference between the two sides is the exact three-body grade compatibility defect. The equation has the same form as the standard additive 2-cocycle condition with trivial action; here the causal reason is bracket-independence and traditional cocycle language is a proof/coordinate shadow.

## 6. Base carry is a canonical coherent pair grade

For base `B>=2`, define residue type join

\[
a*_Bb=(a+b)\bmod B
\]

and local carry grade

\[
\gamma_B(a,b)=\left\lfloor\frac{a+b}{B}\right\rfloor.
\]

The pair grade is coherent. Every composed block preserves the exact invariant

\[
\text{integer total}=\text{residue}+B\times\text{accumulated carry}.
\]

So carry can be read as the local pair correction that lets residue composition generate arbitrary-size integer sums without bracket ambiguity.

If stored grades are re-based by an integer `h(type)`, the pair shift changes by

\[
\gamma'(a,b)=\gamma(a,b)+h(a*b)-h(a)-h(b),
\]

while the three-body coherence defect is unchanged.

## 7. Continuation complexity across dimension

Fix an alphabet `A`, horizon `N`, and terminal observation `O:A^N->V`. For a length-`d` prefix `p`, define its full suffix-response signature

\[
R_{N,d}(p)=\bigl(O(ps)\bigr)_{s\in A^{N-d}}.
\]

Let `C_(N,d)` be the number of distinct such signatures and

\[
C_N=\max_d C_{N,d}.
\]

This is the minimum number of anonymous finite continuation labels needed at the fixed horizon/task.

Examples:

- parity: `C_N<=2` for all `N`, hence a genuine uniform finite-type law;
- full word identity: `C_(N,N)=|A|^N`, hence no fixed finite type set can preserve arbitrary-dimensional full identity;
- binary integer sum: `C_(N,d)=d+1`, so finite label count grows, while the same fixed integer accumulator update `s'=s+x` still generates every dimension.

Therefore distinguish:

- **finite-type uniformity**: `sup_N C_N` is finite;
- **fixed integer-schema uniformity**: label cardinality may grow, but the integer state schema/update law is independent of `N`.

The second notion is broader and remains an open formalization target.

## 8. Absolute n-body claims require a state-complexity restriction

Without a restriction on intermediate causal-state complexity, every fixed finite-horizon rule can be sequentialized by storing enough history. A meaningful higher-order claim should therefore report at least

\[
(\text{exposed coupling order},\ \text{minimum continuation complexity},\ \text{join-coherence defect}).
\]

Only after declaring state-schema/locality/dimension-uniformity constraints does an irreducible n-body primitive become a well-posed claim.

## 9. Consequence for close packing / FCC-HCP research

This note does not derive physical FCC/HCP selection. It changes the entry point: equal local packing/contact observations may still carry different continuation signatures if buried stacking relations change future admissible operations or observations. Absolute registry labels can remain coordinate shadows. The actual test is whether a small, dimension-uniform continuation state plus a local join/grade law generates the full stacking family.

## 10. Executable assets

- `causal_recursive_join.py`
- `causal_contextual_join.py`
- `causal_grade_coherence.py`
- `causal_prefix_complexity.py`
- corresponding `tests/test_*`

Related existing assets include `causal_continuation_refinement.py`, `causal_continuation_kernel.py`, `causal_type_inventory.py`, `graded_lego_fiber.py`, and `coupled_graded_fiber.py`.

## 11. Promotion boundary

These are research-branch exact finite/integer derivations plus executable references. Full clean-integration CI, Lean formalization, and novelty review remain outstanding. Finite continuation refinement/congruence is adjacent to classical automata theory, and the grade coherence equation is adjacent to traditional 2-cocycle theory; those general tools are not claimed as project inventions.
