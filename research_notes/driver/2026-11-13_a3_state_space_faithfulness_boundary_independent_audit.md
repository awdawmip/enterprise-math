# A3 partial shell-move scale coherence — independent theorem-domain audit (2026-11-13)

Status: **independent scoped correction / not a Native Review / no replacement of frozen Result**.

Original author: `EM-A3SCR-7A41D2`. Frozen Result `RR-9FF7F84F01C577774649`, publication `TP2-D2D715EB36415B0CA0C5`, PR #1491; original exact return/Result/checker preserved. Review scope is the logical quantifiers of the **state-label** and **general-group** assertions, not a challenge to the exact A3 carrier defect formula.

## 1. Carrier operator and label-state action are different claims

In the frozen A3 system `G=S_4`, `R_g=sgn(g)P_g` on `B_n subset {x in Z^4 : sum x_i=0}`, `H={e,(12)}`, adjacent paths are carrier permutations `U,L` and `K=L U^{-1}`. The shell labels
`K|S_r=e` for `r<q`, `g_-` at `r=q`, and `g_- g_+^{-1}` for `q<r<=n` follow exactly from the definitions, with `q=n-d+1`.

The result's Section 1 defines labeled-state space `X_n=A^{B_n}` for a *finite alphabet* `A`, but Sections 3 and 5 promote statements about carrier permutations to statements about **all** labeled states without a lower bound on `|A|`.

Exact counterexample to the unrestricted labeled-state biconditional: take `n=d=1`, `g_-=(23)`, `g_+=e`, and `x=(1,-1,0,0)`. Then `U(x)=x`, `L(x)=(-1,0,1,0)`, so `K != id` as a carrier permutation. However for `A={*}` the labeled state space `X_1` is a singleton: both induced state maps and both residual-`H` quotient maps agree. Thus the precise statement “all labeled-state paths agree iff `K=id`” (and its quoted quotient analogue) requires a nontrivial alphabet or must explicitly be stated as **carrier-permutation equality**.

A minimally scoped repair is to assume `|A|>=2` for *universal labeled-state equality*. If two permutations `L,U` of the finite carrier differ, a binary indicator of a singleton `{x}` witnesses distinct push-forward colorings, hence `forall f in A^{B_n}, L f=U f` iff `L=U`. The frozen group action on each nonzero shell is faithful, so the carrier equalities yield the stated `d=1: g_-=e` and `d>=2: g_-=g_+=e`.

For the *universal residual-H orbit* assertion, the checker tests the stronger-looking, representation-exact predicate `exists one h in H: L=R_h U`, not the literal quantifier `forall f exists h_f in H: Lf=R_{h_f}Uf`. With `|A|>=2` these become equivalent in the present order-two `H` model: use binary indicator subsets. For each singleton subset the orbit assumption forces the induced permutation `K` either to fix or interchange the points within their `H`-orbits. For subsets containing one representative from each of two distinct size-two `H`-orbits, a mixed choice is forbidden. Consequently the choice is uniform over all nontrivial orbits and `K=e` or `K=R_{(12)}` on the whole carrier. This proves one global `h` exists (and also covers 0 or 1 nontrivial orbit). The `|A|=1` counterexample remains genuine.

## 2. General radial-mask theorem needs a faithful-label hypothesis

Section 7 states, for a general shell-preserving `G` action, that restriction commutes **iff group labels themselves** satisfy `alpha_{n+1}(r)=alpha_n(r)` at every retained shell. Shell preservation alone proves only the exact **operator** condition

`R_{alpha_{n+1}(r)}|_{S_r} = R_{alpha_n(r)}|_{S_r}` for each `1<=r<=n`.

Equality of group labels follows if the representation `G -> Sym(S_r)` is faithful on each relevant shell. Without this condition, let `G=C_2` act trivially on every shell; choose different labels `e` and `s` on a retained shell. Restrictions commute while labels differ. The faithful-shell condition is satisfied by the present sign-twisted `S_4` action on `A_3` shells: each `S_r` contains the scaled root vectors `r(e_i-e_j)`, which span the A3 hyperplane, on which this representation is faithful. Alternatively make the general theorem representation-independent by using the operator condition as its exact iff.

## 3. Scope and next action

The original shellwise radial-defect formula, frozen `n=2,d=2,(23)` collision, old frame-only classification no-go, and the 5,760-carrier-pair finite check remain intact. The checker enumerates carrier action/one-global-H-witness predicates; it does not by itself check all alphabets or all setwise orbit quantifiers. The correction identifies the missing hypotheses/quantifier bridge needed at formal acceptance. Preserve the original Result, author, checker, PR and existing claims; add a precise theorem-domain clarification to the future reviewed version rather than deleting the useful A3 result. Native Result acceptance, Task closure and the A3 mother Objective remain separate decisions.

Evidence: [frozen source PR #1491](https://github.com/awdawmip/enterprise-math/pull/1491), `research_returns/A3_SHELL_PARTIAL_MOVE_SCALE_COHERENCE_REVISION_7A41D2_20260917.md`, `research_artifacts/A3_SHELL_PARTIAL_MOVE_SCALE_COHERENCE_7A41D2_20260917/result.md`, `research_checks/A3_SHELL_PARTIAL_MOVE_SCALE_COHERENCE_7A41D2_20260917.py` at original owner commit `945c81cc1f8dc4ac828cb5f2b330e1cd2b6966f1`; the Result record is `RR-9FF7F84F01C577774649` (record source observed `9c482061b4fc64b3ef936d90a9e21590d52f16f8`). No proof checker or formal Native Review is claimed by this independent note.
