# HODGE H0N — Non-Split Weil Sixfold Exceptional `ch_3` Seed Object Gate — Research Return

Researcher-ID: `EM-HODGEH0N-6A4C2F`  
Task-ID: `RS-HODGE-H0N-NONSPLIT-WEIL-EXCEPTIONAL-CH3-SEED-OBJECT`  
Publication: `TP2-9A71D4C6E2B5083F16CD`  
Claim: `chatgpt-hodgeh0n-20260902-1034-6a4c2f`  
Execution record: `ER-E30109282875D92161A7`  
Execution branch: `research/hodge-h0n-exceptional-ch3-seed-em-hodgeh0n-6a4c2f`  
Date: `2026-09-02`

## Verdict

Primary classification:

`REUSABLE_NATURAL_SOURCE_FAMILY_NO_GO_WITH_EXACT_EXCEPTIONAL_PROJECTOR__GENERAL_SEED_EXISTENCE_OPEN`.

Terminal verdict for this task return:

`NEGATIVE_BOUNDARY`.

The hard target is satisfied at the permitted **natural-source-family no-go** strength. No target-side object with nonzero exceptional `W_K` component of `ch_3` is constructed, and no non-algebraicity or Hodge-conjecture claim is made.

The strongest frozen mathematical statements are:

1. the non-split `[-3]` Weil-sixfold carrier and divisor-algebra separation needed from H0M survive independent re-verification;
2. there is an explicit rational polynomial in a target algebraic endomorphism whose action on `H^6` is the exact projector onto the exceptional two-dimensional Weil space `W_K`;
3. every semihomogeneous vector bundle on the very-general target has `ch_3` in the divisor line `Q[theta^3]`, hence zero exceptional projection;
4. the same zero-projection statement is stable under finite shifts, finite direct sums, and finite exact-triangle/cone/extension constructions generated from such objects;
5. every Fourier–Mukai output that is independently verified to remain semihomogeneous (up to shift) is killed by the same theorem;
6. divisor-generated classes remain divisor-generated under target `K`-endomorphisms; and expected-codimension-three determinantal classes built from bundles whose Chern classes lie in `Q[theta]` are also killed;
7. arbitrary direct summands/Karoubi completion and arbitrary algebraic correspondences are **not** covered by these no-go results.

## Independent premise audit

The task grants no Working Truth from H0M. The following premises were therefore re-derived from the pinned model rather than inherited as authority.

Let

`K = Q(i)`, `U = K^6`, `Lambda = Z[i]^6`

and take the Hermitian form

`h = diag(1,1,1,-1,-1,-3)`.

Its signature is `(3,3)` and its determinant class is `[-3]` in

`Q^*/Nm_{Q(i)/Q}(Q(i)^*)`.

The split six-dimensional class is `[-1]`; their ratio is `3`. If `3=Nm(a+bi)` with `a,b in Q`, clearing denominators produces coprime integers

`x^2 + y^2 = 3 z^2`.

Modulo `3`, the only way a sum of two squares is zero is `x=y=0 mod 3`, after which the equation also forces `z=0 mod 3`, contradicting coprimality. Hence `3` is not a norm and `[-3] != [-1]`.

The alternating form

`E(x,y) = (1/2) Tr_{K/Q}( i h(x,y) )`

is integral on `Lambda`. Taking the complex structure acting by `+i` on the first three `K`-coordinates and `-i` on the last three gives a positive Riemann form, so the corresponding `(3,3)` unitary period component is nonempty. The target is a very-general member `A_gen` in the fixed `[-3]` component.

Write

`V = H^1(A_gen,Q)`,

viewed as a six-dimensional `K`-vector space. Then

`W_K = wedge_K^6 V`

has rational dimension two. After complexification,

`V_C = V_sigma direct-sum V_sigma_bar`

and

`W_{K,C} = wedge^6 V_sigma direct-sum wedge^6 V_sigma_bar`.

Because the Weil signature is `(3,3)`, these two determinant lines have Hodge type `(3,3)`.

For the chosen very-general target,

`NS(A_gen)_Q = Q theta`.

Thus the degree-six divisor-generated subspace is `Q theta^3`. Introduce the embedding-count decomposition

`B_p = wedge^p V_sigma tensor wedge^(6-p) V_sigma_bar`, `0 <= p <= 6`.

Then

`theta^3 in B_3`

while

`W_{K,C} = B_0 direct-sum B_6`.

The `B_p` are distinct direct summands of `wedge^6 V_C`; therefore

`W_K intersect Q theta^3 = 0`.

Only this exact carrier/separation strength is used below.

## Exact exceptional projector

The target already carries multiplication by every Gaussian integer as an algebraic endomorphism. Choose

`u = 1 + 2 i`, with `Nm(u)=5`.

On the block `B_p`, the pullback `u^*` acts by

`lambda_p = u^p conjugate(u)^(6-p)`.

The exact eigenvalues are

- `lambda_0 = 117 - 44 i`,
- `lambda_1 = -35 + 120 i`,
- `lambda_2 = -75 - 100 i`,
- `lambda_3 = 125`,
- `lambda_4 = -75 + 100 i`,
- `lambda_5 = -35 - 120 i`,
- `lambda_6 = 117 + 44 i`.

Over `Q`, the conjugate-pair factors are

`F_0(t) = t^2 - 234 t + 15625`,
`F_1(t) = t^2 + 70 t + 15625`,
`F_2(t) = t^2 + 150 t + 15625`,
`F_3(t) = t - 125`.

Define

`P(t) = -(t-125)(9881t-609029)(t^2+70t+15625)(t^2+150t+15625) / 57000000000000000`.

Direct exact substitution gives

`P(lambda_0)=P(lambda_6)=1`

and

`P(lambda_p)=0` for `1 <= p <= 5`.

Hence

`Pi_W := P(u^* | H^6(A_gen,Q))`

is an exact rational projector with

`im(Pi_W)=W_K`.

Because `u` is an algebraic endomorphism, every rational polynomial in `u^*` is induced by a rational linear combination/composition of algebraic graph correspondences. Thus `Pi_W` is an algebraic correspondence at the cohomological level.

This is a **separator, not a seed**. It does not imply that any nonzero element of `W_K` is algebraic: one still needs an algebraic input class `alpha` with `Pi_W(alpha) != 0`.

For the polarization,

`u^* theta = 5 theta`

and therefore

`u^* theta^3 = 125 theta^3`.

Consequently

`Pi_W(theta^3)=0`.

There is also a useful amplification fact. The discriminant of `F_0` is

`234^2 - 4*15625 = -7744 = -88^2`,

so `u^*|W_K` has no rational eigenline. Therefore, if **one** nonzero rational algebraic class `w in W_K` is ever constructed, then

`{w, u^*w}`

is automatically a rational basis of `W_K`. Since `u` is algebraic, a single algebraic seed would generate algebraicity of the full two-dimensional rational Weil space under this action. This conditional amplification does not provide the initial seed.

## Semihomogeneous source-family no-go

For a semihomogeneous vector bundle `E` of rank `r>0` on an abelian variety, Mukai's semihomogeneous Chern-class structure gives, in rational cohomology,

`ch(E) = r exp(c_1(E)/r)`.

Therefore

`ch_3(E) = c_1(E)^3 / (6 r^2)`.

On the very-general target `A_gen`,

`c_1(E) in NS(A_gen)_Q = Q theta`.

Hence there exists `q in Q` with

`ch_3(E) = q theta^3`.

By the direct-summand separation and the exact projector,

`Pi_W(ch_3(E)) = 0`.

Thus:

**Theorem (semihomogeneous no-go).**  
No semihomogeneous vector bundle on the declared very-general non-split `[-3]` Weil sixfold can itself supply the required exceptional `ch_3` seed.

This is an unbounded theorem over the whole declared semihomogeneous family; the checker below validates only its symbolic algebra and projector certificate, not the theorem by finite enumeration.

## Finite extension/cone closure

The Chern character factors through `K_0`. Thus:

- shifts multiply the class by `-1`;
- finite direct sums add classes;
- exact sequences and exact triangles give additive Chern characters.

Starting with semihomogeneous bundles whose degree-six Chern-character components lie in `Q theta^3`, every object obtained by a **finite** sequence of shifts, finite direct sums, extensions, cones, and exact triangles still has

`ch_3 in Q theta^3`

and therefore zero exceptional projection.

This statement intentionally excludes arbitrary direct summands/idempotent completion. A relation

`[F]=[E]+[G]`

with only the total class controlled does not justify control of an unknown summand in a Karoubi envelope. Extending the theorem to the entire thick subcategory would risk assuming away precisely the exceptional source object being sought.

## Fourier–Mukai subfamily

The Fourier–Mukai route is treated by output type, not by name.

Whenever a target-side Fourier–Mukai construction is independently known to produce a semihomogeneous bundle (possibly followed by a shift)—including the standard WIT transforms of nondegenerate line bundles/semihomogeneous inputs in the classical Mukai–Orlov setting—the preceding semihomogeneous theorem applies on the target:

`Pi_W(ch_3(FM(E)))=0`.

This yields a reusable no-go for the **verified-semihomogeneous FM subfamily**.

No blanket statement is made for an arbitrary Fourier–Mukai image whose target object is not known to be semihomogeneous or whose support/Chern data are not controlled. Such a blanket extension would exceed the audited hypotheses.

## Polarization and target `K`-endomorphism constructions

Since `NS(A_gen)_Q=Q theta`, every divisor-generated degree-six class is a scalar multiple of `theta^3`.

The algebraic `K`-endomorphism action preserves this divisor line; for `u=1+2i`, it acts on `theta^3` by the scalar `125`. Thus applying target-side `K`-endomorphisms to divisor-generated input cannot create an exceptional component:

`Pi_W(Q[K] . theta^3)=0`.

So the polarization plus the existing `K`-endomorphism algebra does not by itself solve the seed problem.

## Determinantal/degeneracy subfamily

Let a target-side expected-codimension-three degeneracy locus be defined from an explicit map of vector bundles/complexes whose relevant Chern classes all lie in `Q[theta]`.

By Thom–Porteous, its codimension-three class is a universal Schur polynomial in the Chern classes of the virtual difference. Since every degree-two generator is proportional to `theta`, every degree-six term is a scalar multiple of `theta^3`.

Therefore this declared determinantal subfamily also satisfies

`Pi_W([D])=0`.

The hypothesis is essential. If one defining bundle already carries exceptional codimension-three Chern data, then the construction has imported the missing seed rather than generated it from divisor algebra.

## Counterexample search and exact failure boundaries

The following overclaims were actively tested and rejected.

1. **"All objects generated by semihomogeneous bundles are killed."**  
   Rejected at arbitrary direct summands/Karoubi completion. The proven closure is finite additive/triangulated construction before uncontrolled idempotent splitting.

2. **"All Fourier–Mukai objects are killed."**  
   Rejected. The theorem covers only outputs whose target-side semihomogeneous type (or equivalent divisor-Chern confinement) is established.

3. **"All algebraic correspondences have zero exceptional image."**  
   Rejected strongly: `Pi_W` itself is an algebraic correspondence whose cohomological image is exactly `W_K`. The unresolved issue is producing an algebraic input class on which this projector is nonzero.

4. **"Failure of these natural families proves non-algebraicity."**  
   Rejected. Family-level failure has no such implication.

5. **"The projector constructs an algebraic Weil class."**  
   Rejected. A projector onto a Hodge subspace does not by itself furnish a nonzero algebraic vector in that subspace.

These boundaries are part of the result, not caveats to be silently removed.

## Literature/frontier audit

The H0M literature ledger was not adopted as Working Truth. Its routing conclusion was rechecked at the level needed here.

The relevant current primary-source picture remains:

- Markman's sixfold result treats the split/discriminant `-1` Weil case through secant-sheaf constructions;
- the later secant-sheaf framework remains tied to the split source geometry used there;
- Mostaed's 2026 sixfold analysis isolates points where existing algebraicity mechanisms do not supply the missing classes;
- no primary result located through `2026-09-02` supplies an all-discriminant theorem that would make the chosen very-general `[-3]` benchmark obsolete.

This is only a current routing statement. It is not evidence of non-algebraicity.

## Checker / certificate

Task-local checker:

`research_checks/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_CHECK_20260902.py`

Frozen local run:

`HODGE_H0N_CHECKS=20`  
`HODGE_H0N_FAILURES=0`  
`HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_CHECK: PASS`

It checks the elementary norm obstruction, exact Gaussian eigenvalues, rational factorization data, projector values, divisor-line annihilation, the irreducibility/no-rational-eigenline discriminant certificate, and the symbolic semihomogeneous `ch_3` coefficient identity. It does not replace any unbounded geometric theorem.

## Tool-reuse resolution

The current Enterprise toolbox and method inventory were queried after the task structure was understood. No reusable Hodge–Weil exceptional projector or semihomogeneous-Chern mechanism is registered there.

No new general-purpose Enterprise tool is proposed. The checker is task-local evidence only.

Method-harvest classification:

`NO_TOOL_PAYLOAD`.

## Unresolved residue

The exact remaining object-level frontier is now narrower:

construct either

- a genuinely target-side algebraic/derived object outside the killed semihomogeneous / finite additive-cone / verified-semihomogeneous-FM / divisor-generated determinantal families with
  `Pi_W(ch_3(E)) != 0`, or
- an algebraic source class/correspondence whose target image has nonzero `Pi_W` projection.

Arbitrary direct summands, genuinely non-semihomogeneous stable objects, and new correspondences remain live possibilities.

If a single nonzero rational algebraic `W_K` seed is found, the explicit algebraic endomorphism `u=1+2i` then generates the full two-dimensional rational Weil space.

## Recommendation

Driver-review this return as a reusable negative boundary, not as a proof of non-algebraicity.

If accepted:

- freeze the semihomogeneous and finite extension/cone no-go;
- freeze the verified-semihomogeneous Fourier–Mukai subfamily no-go;
- retain `Pi_W=P(u^*)` as an exact target-side exceptional detector;
- preserve the single-seed amplification lemma;
- route at most one successor to a genuinely non-semihomogeneous target seed family or a separately falsifiable algebraic source/correspondence construction.

Do not promote to H1 and do not claim the Hodge conjecture or its negation.

Freeze boundary reached.
