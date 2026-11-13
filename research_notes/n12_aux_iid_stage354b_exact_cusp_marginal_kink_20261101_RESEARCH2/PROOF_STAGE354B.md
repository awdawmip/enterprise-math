# Enterprise Math Stage354-B — an exact upward marginal kink in the 16-tag right-arc optimum

Date: 2026-11-01 (Asia/Shanghai). Status: PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Research-author context continues the Stage353-B mathematical result. **The theorem is restricted to the right r1=0 arc.**

Pinned canonical inputs: GLOBAL_KNOWLEDGE_V1 main@1daf16db2f3a1168adb1574ff3e365fbb9d7d418, Enterprise Math main@77047bba6703aa333a7d2b2f483ac5a80815e21e, original P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Native control status: research_authority_granted=false. The attached inherited Stage353 proof below supplies the original sixteen independently labeled source-word laws, exact right-arc allocation theorem, and all-real concavity, not an unreviewed P000 X6 bridge.

## New exact theorem

Keep the original Stage353 definitions, including B_k(z)=z^k(1-z)^(3-k), w=(1,3,3,1), m=(61,21,9,9), and the **four source-port comparisons times four word laws**. Write q_s for the right r1=0 point with b(q_s)=beta_*+s, phi(s)=c(q_s), and let E_c be its unique y-source label cusp: y_c=(1+sqrt(13))/8. Stage351's exact root isolator proves 0.0021814072266<E_c<0.0021814072275. Stage353's restricted-arc minimization establishes V(E)=phi(0)+phi(E) for E<=E_c, and V(E)=phi(E_c)+phi(E-E_c) for E_c<E<=11/5000.

The unique switching label is (source y, anchor 3/4, word k=2). Since w_2=3, its term in c equals (21/512)*abs(B_2(3/4)-B_2(y)); B_2'(y)=y(2-3y). Crossing the cusp increases c_y by 21 B_2'(y_c)/256, with all other 15 tag comparisons unchanged. Along the smooth implicit r1=0 graph y=Y_1(x), with B(x)=b(x,Y_1(x)) and B'(x_c)>0,

  U := phi'_+(E_c)-phi'_-(E_c)
     = (21/256)*y_c*(2-3y_c)*Y_1'(x_c)/B'(x_c).

All derivative bounds are exact rational interval evaluations at certified Stage351 root rectangles, not point sampling. The new checker proves:

  0.11665 < U < 0.11666;
  0.03392 < A := phi'_+(E_c)-phi'(0) < 0.03393;
  0.08273 < J := phi'(0)-phi'_-(E_c) < 0.08274.

By Stage353's all-real minimization formula, V is continuous at the cusp and has one-sided derivatives V'_-(E_c)=phi'_-(E_c) and V'_+(E_c)=phi'(0). Thus **V has a rigorously positive upward marginal kink of size J**. The exact identity U=A+J splits the raw tag jump into a reallocation benefit and the remaining optimized-value jump. Stage351/353's strictly negative smooth-piece curvatures also imply V is strictly concave on both open pieces while **neither convex nor concave on the whole [0,11/5000]**: positive derivative jump violates global concavity and strict concavity on an open piece violates global convexity.

For E_c<E<=11/5000 let G(E)=phi(0)+phi(E)-V(E). Then G(E_c)=0 and G'(E)=phi'_+(E)-phi'(E-E_c). Stage351's certified entire post-cusp derivative lower interval R.lo and near-star upper L.hi, rechecked by Stage354, give R.lo-L.hi>3/100 for every such real E. Integration gives the new 50%-stronger strictly positive bound

  G(E) > (3/100)*(E-E_c).

Its right-hand onset derivative lies between 0.03392 and 0.03393. All these claims are about the **full continuum of allocations restricted to the right r1=0 arc**, with source provenance preserved. They neither rule out off-arc competition nor establish native X6 dynamics, the third slice coordinate, triadic closure, independent time, or final Cell addresses.

## Verification and next problem

The attached Stage354 checker imports and executes the immutable Stage351 Fraction source and then checks the new exact rational derivative enclosures, the source-tag jump formula, interval decomposition and strengthened all-budget derivative gap. Two local executions of that checker were byte-identical; actual concise stdout is stored alongside it. No independent Driver review, canonical CLAIM, Source Result or mathematical admission is implied by publication. The next unit is an exact all-continuum off-arc rival check, prioritizing r3=0 and r0=0 plus Stage346 b-floor and Stage336/342 r3>=0 author lemmas. BRC resolution: REUSE_EXECUTED for original labeled Bernoulli comparisons and root checker, COMPOSE_APPLIED for the derivative jump and budget phase transition.

---

# Inherited complete Stage353-B right-arc proof (immutable scientific dependency)

The following source is reused exactly from commit 48bcbd2135526204586f661411b0de27031caedb and retains its own original author/proof classification.


# Enterprise Math Stage353-B — exact optimal post-cusp split on the full right r1=0 arc

Date: 2026-11-01 (Asia/Shanghai). Classification: **PORTABLE_AUTHOR_RESTRICTED_ARC_THEOREM / EXACT_FRACTION_INTERVAL_EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. The local author context is the ongoing 进取数论研究2 research conversation; it has no newly issued native Researcher/Driver identity, formal CLAIM, Result or independent review.

## 1. Pinned sources, model, and exact question

This run read the GLOBAL_KNOWLEDGE_V1 canonical `main@0535430c6666f6bc032014cb0ca309e3c1ea632c` (both normative entries, EM project TASK router, P000 startup/full original, ACTIVE worldview, mathematical/code/BRC/registration and journal policies) and Enterprise Math canonical `main@c81693f40e81c1d640d4dd0caa54a680a93bce0a` (AGENTS, original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`, Heartbeat X6 and joint-observer contracts, portable/autonomous protocols). In particular, the startup projection's original GK P000 blob is `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`, equal to the GK original at this snapshot. The external model and its mathematical obligations remain distinct from P000 native X6.

The previously published Stage351 right-arc statement and checker are at project PR #1736, immutable commit `cef9ad60c0c4a81d8cc86b1235917aba2ad45e06`, file `research_notes/n12_aux_iid_stage351b_exact_cusp_onset_20261101_RESEARCH2/REPRO_STAGE351B.py`. Stage352 handed off a new question at PR HEAD `31703da2d364a24d6a632649824bec319648557c`: does the cusp split merely improve on the old endpoint, or is it itself the **true restricted right-arc minimizer**? This Stage353 answers the second question for *every real budget through* `11/5000`.

Retain all original source-word laws. For `k=0,1,2,3`, set `w=(1,3,3,1)`, `m=(61,21,9,9)`, `B_k(z)=z^k(1-z)^{3-k}`, and

\[
 r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160},\qquad
 b(x,y)=\frac5{32}\sum_{k=0}^3 w_k|r_k(x,y)|,
\]
\[
 D_3(a,z)=\frac12\sum_{k=0}^3w_k|B_k(a)-B_k(z)|,\qquad
 c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

These are **four individually labeled comparisons of four three-visit word laws**, not one merged source histogram. Let `q_*=(x_*,y_*)` solve `r0=r1=0` in the Stage351 rational root box and `β_*=b(q_*)`. On the right-hand `r1=0` graph, `q_s` is uniquely determined by `b(q_s)=β_*+s` for `0≤s≤Emax=11/5000`; put `φ(s)=c(q_s)`. The full two-source objective would be `T=33/1024+c(q_1)+c(q_2)` subject to `b(q_1)+b(q_2)≤2β_*+E`. **This theorem deliberately constrains both q_i to that right arc**; it does not say that the unrestricted global minimizer lies on the arc.

Define the unique source-tag cusp by

\[
 y_\dagger=\frac{1+\sqrt{13}}8,\quad r_1(x_\dagger,y_\dagger)=0,\quad
 E_\dagger=b(x_\dagger,y_\dagger)-\beta_*.
\]

The exact rational isolator, reused and re-executed from Stage351, proves

\[
 0.0021814072266<E_\dagger<0.0021814072275,
 \quad E_\dagger<E_{\max}<2E_\dagger. \tag{1}
\]

## 2. New complete theorem (not merely a better competitor)

**Stage353 right-arc allocation theorem.** For every real `E` in `[0,11/5000]`, among all `s,t≥0` satisfying `s+t≤E`, the minimum of `φ(s)+φ(t)` has the following exact and **unique, modulo swapping**, allocation:

\[
\boxed{
\begin{array}{c|c|c}
 E&\operatorname*{argmin}_{s+t\le E}[\phi(s)+\phi(t)]&\min[\phi(s)+\phi(t)]\\\hline
 E=0&(0,0)&2\phi(0)\\
 0<E\le E_\dagger&(0,E),(E,0)&\phi(0)+\phi(E)\\
 E_\dagger<E\le 11/5000&(E_\dagger,E-E_\dagger),(E-E_\dagger,E_\dagger)&\phi(E_\dagger)+\phi(E-E_\dagger)
\end{array}}
\tag{2}
\]

In the last interval the cusp split beats the old endpoint quantitatively:

\[
 \phi(0)+\phi(E)-\phi(E_\dagger)-\phi(E-E_\dagger)>
 (E-E_\dagger)/50>0.\tag{3}
\]

Thus Stage351's cusp competitor is not just *some* improving split: it is the **entire exact optimal allocation** within the declared full right-hand arc up to `E=0.0022`. This makes the post-cusp active-budget law a one-source cusp pin plus one source close to the star, and fully excludes interior stationary allocations **inside this arc**, without any grid-search claim. The full model's post-cusp optimizer remains a separate question; an off-arc source may beat (2).

## 3. NEW post-cusp exact curvature certificate

The Stage351 certificate establishes for the entire pre-cusp arc that `B'>0`, `C'<0`, and `N_-=C''B'-C'B''<-4/5`, where `B(x)=b(x,Y_1(x))`, `C(x)=c(x,Y_1(x))` and `Y_1(x)` solves `r1=0`. It also establishes `φ'(u)<-119/100` for `0≤u≤Emax−E_dagger`, and `-117/100<φ'(v)<0` for `E_dagger<v≤Emax`.

For the **new** post-cusp chamber, the 16 source-word tag signs are retained. Only `D3(3/4,y)` at `k=2` changes sign, at the exact algebraic cusp. The right-chamber derivatives obtained from all original labels are

\[
 c_x=-\frac{3(x-1)(61x-63)}{256},\qquad
 c_y^+=-\frac{3y(25y-18)}{256},\qquad
 c_{yy}^+=-\frac{3(50y-18)}{256}.\tag{4}
\]

The accompanying code verifies the `c_y^+` identity by an *exact symbolic expansion of all eight y-word source contributions* (`9D3(1/4,y)+7D3(3/4,y)`), while the pinned Stage351 checker verifies the original 16 tag-sign regions and `r1` graph isolators. Along `r1=0` let

\[
 Y'=-r_{1,x}/r_{1,y},\quad
 Y''=-(r_{1,xx}+r_{1,yy}(Y')^2)/r_{1,y},
\]
\[
 B'=b_x+b_yY',\quad B''=b_{xx}+b_{yy}(Y')^2+b_yY'',\quad
 C'=c_x+c_yY',\quad C''=c_{xx}+c_{yy}(Y')^2+c_yY''.
\]

The previously certified exact root bounds place the **whole** post-cusp arc `E_dagger≤s≤Emax` in the rational rectangle

\[
 X=[0.23780,0.23788],\qquad Y=[0.57569,0.57591].\tag{5}
\]

Exact outward `Fraction` interval propagation on this entire rectangle yields

\[
 \boxed{N_+:=C''B'-C'B''<-\frac75,
 \quad B'>\frac3{10},\quad C'<0.}\tag{6}
\]

In fact the checker prints exact fractions with decimal values `N_+ upper≈−1.47219450669` and `B' lower≈0.312509081918`. It follows for each smooth post-cusp `s` that

\[
 \boxed{\phi'(s)=C'/B'<0,\qquad \phi''(s)=N_+/(B')^3<0.}\tag{7}
\]

This is the missing post-cusp strict-concavity certificate. The breakpoint itself is deliberately handled by one-sided derivatives; the proof does not extend (7) across the kink as if smooth.

## 4. Complete real-continuum allocation proof

Both smooth pieces of `φ` are strictly decreasing and strictly concave by Stage351 and (7). Hence any feasible split with `s+t<E` can increase one coordinate along the declared right arc and strictly decrease total cost; **all minimizers exhaust the budget**.

When `0<E≤E_dagger`, `φ` is strictly concave throughout `[0,E]`. Consequently `F_E(s)=φ(s)+φ(E−s)` is strictly concave on `[0,E]` and has precisely its two endpoints as minimizers; the `E=0` case is immediate.

Now fix `E_dagger<E≤Emax`. By (1), the breakpoints are strictly ordered

\[
 0<E-E_\dagger<E_\dagger<E.\tag{8}
\]

Partition the **entire** possible split interval exactly into

\[
 [0,E-E_\dagger],\quad [E-E_\dagger,E_\dagger],\quad [E_\dagger,E].\tag{9}
\]

On the first and third pieces one argument of `F_E` is pre-cusp and the other post-cusp; on the middle piece both are pre-cusp (because `E<2E_dagger`). Each restriction of `F_E` is therefore **strictly concave**, regardless of the derivative jump at the two boundaries. A strictly concave function on a closed interval has its minimum at an endpoint. Thus only the four endpoints of (9) can minimize globally:

\[
 s\in\{0,E-E_\dagger,E_\dagger,E\}.\tag{10}
\]

Symmetry makes the two cusp endpoint costs equal and the two old endpoints equal. Let `H(E)=φ(E_dagger)+φ(E−E_dagger)−φ(0)−φ(E)`. Stage351's exact separated derivative enclosures give

\[
 H'(E)=\phi'(E-E_\dagger)-\phi'(E)
 <-\frac{119}{100}+\frac{117}{100}=-\frac1{50},
 \quad H(E_\dagger)=0.\tag{11}
\]

Hence `H(E)<−(E−E_dagger)/50<0`. Equations (10)–(11) exclude both old endpoints, and strict concavity on all three pieces excludes every interior point except the two cusp breakpoints. This proves (2)–(3) including all uniqueness clauses.

No finite collection of sample points was used to infer an all-real claim: (9) is an exact partition of every feasible real split; the numerical kernel verifies bounds on continuous rational rectangles.

## 5. Execution, BRC usage, scope and next obligation

`REPRO_STAGE353B.py` imports the published exact Stage351 program (the import executes all its root, sign and pre-cusp assertions) and adds the independent post-cusp polynomial derivative and exact interval checks. `EM_STAGE351B_CHECKER` may point to that prior program; otherwise the relative sibling research path in PR #1736 is used. Run with assertions enabled and SymPy available. The program was executed twice locally with byte-identical stdout; successful ending marker is `STAGE353B_POST_CUSP_RESTRICTED_GLOBAL_SPLIT_EXACT_PASS`. A fully standalone equivalent local checker was also run and gives the same post-cusp upper bounds, but it is not needed to reproduce the PR-delivered theorem.

BRC resolution: `REUSE_EXECUTED` for the Stage351 typed original 16-label Bernoulli comparison and rational root/interval checker; `COMPOSE_APPLIED` for the post-cusp curvature, exact source sign switch and three-piece active-budget combinatorics. No word tags or source ports have been erased; the operations form an **external auxiliary observer** with declared domain `s,t∈[0,11/5000]`. No X6 third slice coordinate, triadic closure, independent time, future-operations observer guarantee or final Cell address is claimed.

**Open:** prove or refute that every unrestricted global two-source minimizer for `E_dagger<E≤0.0022` is on this arc; independently inspect the Stage346 global `b` floor and Stage336/342 strict `r3≥0` Pareto domination, including equality boundaries, before removing the conditional qualifier from Stage352. The native research service reported `research_authority_granted=false`, `executor_binding_configured=false`, and owner list returned `CONTROL_QUOTA`; no formal CLAIM, activity registration, Result, independent Driver or acceptance is inferred from this authored theorem or GitHub storage.