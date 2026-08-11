# R013 Precision-Limit Closure — Closure Report

**Researcher-ID:** `EM-R013-0LCGPL`  
**Task:** `RS-R013-PRECISION-LIMIT-CLOSURE-FIBRE-PROOF-CALCULUS`  
**Taskbook base:** `agent/taskbook-scheduler-fast-path@74306d67ba3c6e8150e6152f1768221e4d0598c2`  
**Research branch:** `research/r013-precision-limit-closure-0lcgpl`  
**Date:** 2026-08-11 (Asia/Taipei)  
**Status:** `RESEARCH CLOSURE PACKAGE / NOT CANONICAL / DRIVER DECISION REQUIRED`

## 1. Executive closure verdict

The prior-art attack succeeds in the intended sense: **no new generic R013 mother theorem survives**.

1. Directed quotient/refinement towers, compatible theorem families, inverse-limit kernels and cofinal restriction are generic inverse/projective-system mathematics.
2. Language-relative exact quotient/refinement is already covered project-locally by A2/P023/FQ-004 and externally by completeness/strong-preservation theory.
3. Point-level exactness versus witness/back exactness is a real distinction, but its generic form is the classical back/lifting condition of bounded morphisms, bisimulation and relation lifting. A3/A4 own the Enterprise-specific relation/witness specializations.
4. Generic fibre aggregation is finite reindexing/Fubini over a partition; exact use of a compressed fibre certificate is a functional-kernel/factorization condition already native to A2/P023. Cross-fibre witness or carry state is an **interface specialization**, not a new generic calculus.
5. The generic residual `E_infinity = intersection E_lambda` is the kernel of the canonical map into the inverse limit. Its useful Enterprise content is only the task-language-relative classification of what the residual means.
6. The original C1–C4 Precision-Limit Closure proposal is **not theorem-grade**. It has at least two independent structural gaps: C2 lacks output/certificate realizability, and C4 is not invariant under arbitrary choice of cofinal tower unless the defect law is defined on the full directed system.

Accordingly, the original `PRECISION_LIMIT_CLOSED` criterion must **not** be promoted by this research session. A repaired `PLC*` can be retained as an Enterprise research/Driver certificate schema, not as a new mathematical principle.

There is no `R013_SPECIFIC_RESIDUE` generic theorem in this return.

---

## 2. Minimal task-relative precision object

Let the declared task be

`T = (D, O, F, L)`

with admissible domain `D`, observations `O`, allowed total/partial future operations or words `F`, and legality/witness requirements `L`.

Let `H_T` be the family of all semantic queries that the task contract actually allows to matter: observations, future-observation words, definedness queries for partial operations, and any declared witness/factor query.

Define the full task signature

`Sigma_T(x) = (h(x))_{h in H_T}`

and the intrinsic task equivalence

`x ==_T y  iff  Sigma_T(x) = Sigma_T(y)`.

For a finite query subfamily `A subset H_T`, define

`E_A = intersection_{h in A} ker(h)`.

Finite query sets are directed by union. If `A subset B`, then `E_B subset E_A`, hence there is a canonical quotient map

`rho_BA : D/E_B -> D/E_A`.

This gives a canonical task-generated precision system. It is preferable to a researcher-selected partition chain because its meaning is fixed by the declared semantic language.

### 2.1 Cofinal residual lemma

Let `J` be a cofinal subfamily of the finite-query directed system. Then

`intersection_{j in J} E_j = intersection_{A finite subset H_T} E_A = intersection_{h in H_T} ker(h) = ker(Sigma_T)`.

**Proof.** The left intersection contains the full intersection because `J` is a subfamily. Conversely, for every finite `A` choose `j in J` with `j >= A`. Then `E_j subset E_A`; hence membership in every `E_j` implies membership in every `E_A`. The second equality is immediate because every single query appears in a finite subfamily. `□`

This identifies the only defensible task-relative residual:

`E_infinity(T) = ker(Sigma_T)`.

If instead “admissible precision” means *all exact quotient refinements without a task-language restriction*, the identity partition `Delta_D` is admissible and the intersection is trivially `Delta_D`. Thus a nontrivial “intrinsic residual” is necessarily **relative to a declared semantic/refinement contract**; it cannot mean “indistinguishable under every imaginable refinement”.

### 2.2 Finite versus infinite state

For finite `D`, the task-generated residual is reached by finitely many queries: for each pair outside `ker(Sigma_T)`, choose one separating query; finitely many pairs require only finitely many choices. Hence some finite stage already has kernel `ker(Sigma_T)`.

For infinite `D`, the intersection can be well-defined without any finite stabilization. The canonical map

`eta_D : D -> lim_A D/E_A`, `x |-> ([x]_A)_A`

has kernel exactly `intersection_A E_A`. This is standard inverse-limit mathematics, not an Enterprise-specific theorem.

---

## 3. Precision-coherent theorem families: what coherence does and does not buy

Let

`X_lambda = X/E_lambda`

and let output objects `Y_lambda` have bonding maps `sigma_mu_lambda`. A function-valued theorem family

`T_lambda : X_lambda -> Y_lambda`

is precision-coherent when

`sigma_mu_lambda o T_mu = T_lambda o rho_mu_lambda`

for every `mu >= lambda`.

Relations, certificate sets and weighted outputs require the corresponding typed commuting condition rather than forced function notation.

This abstract condition is simply a morphism of inverse systems / a naturality condition. It creates an induced map on inverse limits. It does **not** by itself prove that the limit output is realizable in the originally declared output space.

### 3.1 Realizability counterexample: coherent modulo `2^n`, not realizable in `Z`

Take a singleton input, declared output space `Y = Z`, and finite output precisions

`Y_n = Z / 2^n Z`.

Let `a_n` be the inverse of `3` modulo `2^n`, and let `T_n` be the constant theorem with value `a_n`.

The family is coherent because reduction of `3^{-1} mod 2^{n+1}` is `3^{-1} mod 2^n`.

Suppose an integer `m` realized all finite theorems. Then

`3m == 1 (mod 2^n)`

for every `n`, so `2^n` divides the fixed integer `3m-1` for every `n`. Hence `3m-1 = 0`, i.e. `m = 1/3`, impossible in `Z`.

The compatible family is a legitimate element of the `2`-adic inverse limit because `3` is a unit there, but it is not in the image of `Z` inside that completion.

Therefore original C2 is insufficient even when C1 and C3 are trivial and C4 defect is identically zero.

### 3.2 Required repair to C2

If

`eta_X : X -> lim X_lambda`, `eta_Y : Y -> lim Y_lambda`

are the canonical maps and coherence induces `T_infinity`, theorem closure in the original output space requires

`T_infinity(eta_X(X)) subset eta_Y(Y)`.

Equivalent formulations may use an explicit global `T : X -> Y` whose reductions are all `T_lambda`.

For certificate-valued theorems the same requirement applies to the declared certificate space, not merely its completion.

Call this repaired condition:

**C2\*** = precision coherence **plus declared-output/certificate realizability**.

---

## 4. Point exactness and witness exactness are different gates

### Gate A — point semantics

A quotient is point-safe for an observable or deterministic transition precisely when the required semantics is constant on quotient fibres / factors through the quotient. This is already the functional-kernel and operation-compatible quotient layer owned by A2/P023/FQ-004, and externally it is the same abstraction-completeness/strong-preservation problem.

### Gate B — relation/factor semantics

For a relation `R subset X x Y` and quotients `q_X`, `q_Y`, let the coarse relation be the direct image. A generic back/witness condition is

`R_bar(q_X(x), y_bar) => exists y, q_Y(y)=y_bar and R(x,y)`.

This is the familiar bounded-morphism/relation-lifting shape. Multiplicity, weights, split completeness or exact witness identity can require stronger fibrewise bijection or conservation conditions.

### 4.1 Minimal point-safe but witness-unsafe example

Let

`X={a,b}`, `Y={u,v}`, `R={(a,u),(b,v)}`,

collapse `X` to one coarse point `*`, and keep `Y` exact.

The point query “does this state have some R-successor?” is true for both fine states and descends perfectly. But the coarse relation contains `(*,v)`. For fine state `a`, this coarse edge has no back-lift because `(a,v)` is absent.

Thus

`point-law-safe  !=>  factor/witness-safe`.

The distinction is important for Enterprise A3/A4 applications, but its generic theorem is prior art. R013 should not own another generic lifting primitive.

---

## 5. Fibre proof composition: exact generic core and its boundary

Let `p : X -> B` be a finite surjection and let `(S, +, 0)` be a commutative monoid. For finitely supported `w : X -> S`, define the fibre aggregate

`W(b) = sum_{x in p^{-1}(b)} w(x)`.

Then

`sum_{x in X} w(x) = sum_{b in B} W(b)`.

For a chain

`X_H -> X_O -> X_L`,

associativity gives exact two-stage aggregation. This covers:

- cardinality (`S=N`, `w=1`);
- weighted sums and semiring-additive aggregates;
- additive defect when the defect itself decomposes fibrewise.

This is ordinary finite partition summation / Fubini-style reindexing.

### 5.1 Interface-sufficiency lemma

The non-additive case reduces to factorization.

Suppose fibre `b` has detailed datum `z_b in Z_b`, local summary `s_b : Z_b -> S_b`, and the desired global theorem is

`Phi : product_b Z_b -> G`.

The local summaries are sufficient for exact global composition iff `Phi` is constant on fibres of `product_b s_b`, equivalently

`ker(product_b s_b) subset ker(Phi)`,

or equivalently there exists `Phi_bar` with

`Phi = Phi_bar o product_b s_b`.

This is the ordinary functional-kernel factorization criterion. It is already aligned with A2/P023 rather than a new R013 theorem.

### 5.2 Certificates, witnesses and carry state

Local proof certificates compose without extra state only when the global checker factors through an associative/monoidal combination of the local certificate summaries. If a global theorem depends on cross-fibre witness identity, branch definedness, multiplicity coupling or arithmetic carry, the summary must be enlarged by exactly enough interface state to make the target factor.

Hence the useful Enterprise statement is methodological:

> fibre decomposition exposes where a minimal interface state is required; it does not create a new generic composition law.

The generic `FIBRE_COMPOSITION` candidate is therefore rooted in prior art / elementary reindexing plus existing functional-kernel machinery.

---

## 6. C1–C4 pressure test

### 6.1 C1+C2+C3 with C4 failure

Fix an exact finite precision system and a coherent identity theorem family, so C1–C3 hold. Give the declared defect contract the requirement `d_lambda -> 0`, but choose `d_n` alternating between `0` and `1`. C4 fails independently of the first three conditions.

If the phrase “declared asymptotic law” is allowed to accept any exact description of any sequence, then C4 becomes vacuous rather than repaired. A theorem-grade C4 must therefore declare its target, topology/order, error notion and accepted convergence mode before observing the data.

### 6.2 C1+C2+C4 with residual not intrinsic

Let `D={a,b}` and let the declared refinement *mechanism* contain only the universal equivalence. A constant theorem family and zero defect satisfy C2 and C4, and the one-stage family is complete relative to that mechanism. But if the task semantic contract contains an admissible observation `h` with `h(a) != h(b)` that the mechanism omitted, the residual is not intrinsic.

Thus C1 must be coupled to a canonical task-language-generated refinement system (or explicitly disclaim completeness beyond the scoped mechanism). C1 alone does not prove C3.

### 6.3 Numerical defect convergence with theorem incoherence

Take fixed `X_n=Y_n={0,1}` with identity bonding maps. Let `T_n` alternate between identity and Boolean flip, while `d_n=0` for all `n`.

The numerical defect converges perfectly; the theorem family is not coherent. C4 cannot replace C2.

### 6.4 Cofinal-family choice can change a naive C4 verdict

On `Lambda=N`, define

- `d_n=0` for even `n`;
- `d_n=0` for `n == 1 mod 4`;
- `d_n=1` for `n == 3 mod 4`.

Both the even and odd index subsets are cofinal in `N`. The even restriction is identically zero and stabilizes. The odd restriction oscillates and has no scalar limit.

Therefore “C4 holds on the chosen cofinal tower” is not an intrinsic predicate. If a freely declared periodic asymptotic formula is allowed to count as closure on the odd tower, the verdict depends on the researcher's chosen C4 mode instead; that is the same invariance failure in another form.

**Required repair:** define the defect on the full directed system and require a cofinal-invariant property: full-net convergence in a specified space, eventual stabilization over the full system, an exact compatible limit object, an order-monotone convergence law, or a uniform asymptotic law fixed independently of the chosen cofinal presentation.

Call this **C4\***.

---

## 7. Repaired closure certificate `PLC*`

The original four conditions are not sufficient. The strongest useful retained Enterprise schema is:

### C1\* — canonical precision completeness

The working family is cofinal in the precision system canonically generated by the declared task semantic language, or the claim is explicitly limited to a narrower declared mechanism.

### C2\* — coherence plus realizability

Finite-level theorems/certificates form a compatible family **and** the induced limit output is realized in the declared output/certificate space rather than only in its completion.

### C3\* — intrinsic task-relative residual classification

The residual is identified with `ker(Sigma_T)` and every remaining collapsed pair is proved indistinguishable by every semantic query allowed by the task contract.

### C4\* — cofinal-invariant defect law

The defect is defined on the full directed precision system and satisfies a predeclared, presentation-independent stabilization/limit/asymptotic contract.

`PLC*(T) = C1* and C2* and C3* and C4*`

is a useful **research certificate schema**. This report does not claim it as a new generic mathematical theorem, and it does not assign the canonical status `PRECISION_LIMIT_CLOSED`.

---

## 8. k=4 symmetric multiplication prototype

The prototype identity is

`(c^2-x^2)(c^2-y^2) = c^4 - (x^2+y^2)c^2 + x^2 y^2`.

Write

`n = x^2+y^2`, `P=x^2 y^2`, `A=c^4-n c^2`.

For the normalized shell

`S_n = {(x,y) in Z_{>=0}^2 : x<=y, x^2+y^2=n}`,

`P` is strictly increasing as a function of `s=x^2` on `s<=n/2`: if `s1<s2`, then

`P(s2)-P(s1) = (s2-s1)(n-s1-s2) > 0`.

Hence `(n,P)` identifies a normalized shell state.

For output precision `r`, define

`b = floor((A+P)/r)`.

At fixed `n`, the output fibres partition `S_n`. If

`N_n = |S_n|`, `N_{n,b}=#{(x,y) in S_n : output=b}`,

then exactly

`N_n = sum_b N_{n,b}`

and the collision defect is

`delta_r(n) = N_n - #{occupied b} = sum_b (N_{n,b}-1)_+`.

This is precisely the generic fibre-count identity, not a new k=4 calculus.

### 8.1 Carry/interface law

Write Euclidean decompositions

`A = r q_A + a`, `P = r q_P + p`, with `0<=a,p<r`.

Then

`floor((A+P)/r) = q_A + q_P + kappa_r(a,p)`

where `kappa_r(a,p)=1` iff `a+p>=r`.

Thus generic cross-level output composition needs a remainder/carry interface unless it is already determined by the coarse state.

On the equal-coarse prototype used here, `r | c`. Therefore `r | A`, so `a=0` and the carry term vanishes:

`floor((A+P)/r) = A/r + floor(P/r)`.

This is a strong negative result for novelty: the k=4 equal-coarse fibre law is an especially clean instance of ordinary fibre binning plus existing arithmetic remainder machinery. It does not leave an R013-specific generic residue.

The companion finite explorer checks shell injectivity, fibre-count/defect decomposition, the carry identity, the equal-coarse carry collapse, the cofinal-C4 counterexample and the witness-lifting counterexample.

---

## 9. Seven-candidate closure matrix — human-readable verdict

| # | Candidate | Primary verdict | Routing consequence |
|---|---|---|---|
| 1 | Precision as directed refinement system | `ROOTING_SUCCESS / PRIOR_ART` | Use inverse/projective-system language; no mother theorem. |
| 2 | Reachable/admissible domain before minimum precision | `EXISTING_ENTERPRISE_OWNER` | Return to A2/P023/FQ-004 task/future/partial-operation quotient layer. |
| 3 | Directed conversion width `omega(P->Q)` | `REJECT / UNDERDEFINED` | `OMEGA_PROVENANCE_INCOMPLETE / DO_NOT_BACKFEED`; retain only sourced comparable `w_P(Q)` under its P023 bridge provenance. |
| 4 | Exact compiler needs witness lifting beyond point commutation | `EXISTING_ENTERPRISE_OWNER` | Gate A to A2/P023; generic Gate B rooted in bounded-morphism/relation-lifting prior art; Enterprise witness specializations to A3/A4. |
| 5 | Precision Tower / fibre proof composition | `ROOTING_SUCCESS / PRIOR_ART` | Generic theorem is partition sum/Fubini + factorization; retain only application/checklist use. |
| 6 | Residual kernel / intrinsic residual collapse | `ENTERPRISE_SPECIALIZATION` | Generic intersection/inverse-limit kernel is prior art; retain task-language-relative `ker(Sigma_T)` classification, not a new theorem. |
| 7 | Original C1–C4 Precision-Limit Closure | `REJECT / UNDERDEFINED` | C2 realizability and C4 invariance gaps kill theorem status; retain repaired `PLC*` as research methodology only. |

Machine-readable details are in `experiments/r013_precision_limit_closure_candidate_matrix.json`.

---

## 10. Targeted prior-art ledger

Deep Research was used only as an attack/de-dup instrument.

1. **Giacobazzi, Ranzato, Scozzari — “Making Abstract Interpretations Complete” (JACM, 2000).** Complete refinement/shell/core machinery roots generic claims that a precision domain should be refined until semantic operations become complete.
2. **Ranzato, Tapparo — “Generalized Strong Preservation by Abstract Interpretation” (2004 preprint / later publication).** Language-relative strong preservation is characterized via completeness and minimal refinement, directly attacking any generic claim that Enterprise invented the coarsest exact quotient for a declared language.
3. **Ranzato, Tapparo — “Generalizing the Paige–Tarjan Algorithm by Abstract Interpretation” (2006).** Partition-refinement algorithms for strong preservation further root finite effective refinement claims.
4. **Standard inverse/projective-limit theory; Stacks Project, limits/cofinal systems.** Compatible quotient towers, cofinal subsystem invariance for inverse limits, and `Z_p = lim Z/p^n Z` are standard. This also supplies the ambient home for the C2 realizability counterexample.
5. **Bounded morphism / p-morphism back conditions in modal semantics.** Forward preservation alone is weaker than the back condition needed to reproduce fine witnesses from coarse edges.
6. **Bílková, Kurz, Petrişan, Velebil — “Relation Liftings on Preorders and Posets” (2012).** Functorial relation lifting and weak-pullback/exactness conditions root the generic witness/relation-lifting layer.
7. **Standard finite Fubini/partition reindexing and commutative-monoid aggregation.** The additive fibre composition law is elementary. Its non-additive exactness boundary is functional factorization, already represented by Enterprise A2/P023.

The prior-art ledger does **not** imply that the Enterprise task-relative packaging is useless. It implies that the project should keep its value in precise specialization, ownership and proof interfaces rather than renaming established generic mathematics.

---

## 11. `omega(P->Q)` provenance decision

The recovered checkpoint source for the historical refinement-width bridge defines only the comparable-partition invariant

`w_P(Q) = max_{P-block C} #{Q-blocks contained in C}`

for `Q <= P`, together with:

- minimum local detail alphabet `w_P(Q)`;
- one-shot transport specializations;
- nested composition bound `w_R(Q) <= w_R(P) w_P(Q)` for `Q <= P <= R`.

No exact definition or theorem source was recovered for an arbitrary/non-comparable “directed conversion width” `omega(P->Q)`, nor for its advertised mixed repair, zero criterion or triangle law.

Verdict:

`OMEGA_PROVENANCE_INCOMPLETE / DO_NOT_BACKFEED`.

This does **not** invalidate the sourced comparable `w_P(Q)` results; it prevents them from being silently generalized into an unsourced mother invariant.

---

## 12. Final routing recommendations to Driver

1. **Do not promote R013 as a new generic limit/closure theory.** Rooting/de-dup has succeeded.
2. **Return point-exact quotient/refinement material to A2/P023/FQ-004.** No second owner.
3. **Return relation/witness arithmetic specialization to A3/A4.** Keep generic back/lifting language explicitly prior art.
4. **Keep comparable refinement width `w_P(Q)` with its existing P023 bridge provenance.** Do not backfeed `omega(P->Q)` unless a precise independent source is later recovered.
5. **Retain task-relative residual classification `ker(Sigma_T)` only as an Enterprise specialization.** Its intrinsic claim is always relative to a declared semantic language.
6. **Retain `PLC*` only as a research/Driver closure checklist/certificate schema.** It must include realizability and full-system/cofinal-invariant defect semantics.
7. **Treat the k=4 equal-coarse prototype as negative novelty evidence.** Its fibre composition is exact but reduces to ordinary fibre counts plus a carry law that vanishes when `r|c`.
8. **No child taskbook is created by this return. No promotion is performed. No CI polling is requested.**

The Driver can now decide whether to archive R013 as a successful rooting/closure exercise, retain `PLC*` as methodology, or issue a separately authorized follow-up if a genuinely task-specific arithmetic interface question remains.