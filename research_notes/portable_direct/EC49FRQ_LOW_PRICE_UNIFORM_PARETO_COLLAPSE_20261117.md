# EC49FRQ: Uniform three-tree Pareto domination on the complete low-price BRC strip

Date 2026-11-17; scientific input pin \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\` (unchanged).
Predecessor: EC49FRP, PR #2639, commit \`37535e08bdf99e888d432b5b4f4952d37c6bb316\`.
Evidence: AUTHOR_PROVED / EXACT_FINITE_CHECKED_WITH_TWO_IMPLEMENTATIONS / NOT_REVIEWED.

## Exact typed setting

Use the original BRC class 16943, its 310 configurations represented by 141 complete **named physical-response profiles** with positive integer multiplicities \`m_i\` summing to 310, and the **228 original named physical observations**: 144 terminal and 84 root. Every tree is a full, finite, adaptive identifying tree on all original profiles.

For a tree Q, let \`U_R,U_T\` count root/terminal observations summed over the 141 named-state paths, and \`M_R,M_T\` the original multiplicity-weighted counts. Set \`U_x=U_T+x U_R\`, \`M_x=M_T+x M_R\`, for a real root/terminal unit-price ratio \`x\`. The normalized cost at the original one-parameter prior is

\[
C_Q(x,\lambda)/t=\frac{1-\lambda}{141}U_x(Q)+\frac{\lambda}{310}M_x(Q),\quad 0\le\lambda\le1,\quad t>0.
\]

The three inherited, original **fixed physical decision trees**, all replayed on the 141 named profiles against the frozen response vectors, have the following exact cost vectors:

| Tree | (U_R,U_T,M_R,M_T) | (U_1,M_1) | (U_3,M_3) |
|---|---|---|---|
| A | (6,290,6,751) | (296,757) | (308,769) |
| B | (5,293,5,704) | (298,709) | (308,719) |
| C | (5,295,5,685) | (300,690) | (310,700) |

These are native response-tree witnesses, not abstract cost vectors unbacked by complete identifying actions. Their original complete tree data are retained in the accompanying self-contained evidence archive.

## Theorem — one fixed dominator across the entire price-prior rectangle

**For every legal original complete deterministic identifying tree Q, there exists one T in {A,B,C} such that C_T(x,lambda) <= C_Q(x,lambda) simultaneously for every real 1<=x<=3 and every real 0<=lambda<=1.**

The existential choice of T depends on Q, but *not* on price or prior within the entire rectangle. Thus {A,B,C} is a pointwise Pareto-dominating basis of the unrestricted original decision-tree set. The theorem is stronger than the previously established pointwise Bellman identity \`V=min(A,B,C)\`.

### Finite exact premises

The first new parity-lifted Bellman calculation at integer price x=1 gives:

| Exact integer objective over every original identifying tree | U_1 even | U_1 odd |
|---|---:|---:|
| 24 U_1 + M_1 | **7861** | **7886** |
| 19 U_1 + 2 M_1 | **7080** | **7099** |

Both rows were calculated directly from the frozen original data by (i) a 209-unique-same-price-partition DP, and (ii) an independently implemented 228-all-named-actions DP which re-parses the 94-family BRC master and root-cost CSV. Each DP visited 12,922 Bellman state subsets for each row; the first also constructed and replayed the four exact parity-optimal witness trees. Only exact integer arithmetic was used.

Inherited finite native Bellman evidence from EC49FRP and EC49FRI/FRJ gives the *unrestricted* scalar lower bounds

\[
U_1\ge296,\quad M_1\ge690,\quad U_3\ge308,\quad M_3\ge700.
\]

At integer price x=3, inherited unrestricted parity Bellman gives \`19 U_3+2 M_3 >=7290\` for even U_3 and \`>=7311\` for odd U_3. The original terminal-response signature fibers include exactly two nonsingleton pairs \`{8,139}\` and \`{46,140}\`, all of multiplicity one. Identifying both pairs forces at least one root observation on each of these four state paths. Therefore \`U_R>=4\` and \`U_R=4 => M_R=4\`. All weights being positive integers also gives \`M_R>=U_R\`.

The parity DP recurrence is mathematically exhaustive. If \`S\` is the current named-state subset and \`w_i=alpha+beta*m_i\`, let \`B_p(S)\` be the minimum total weighted future observation cost among full identifying subtrees for which the **unweighted** sum of state-path query counts has parity p. For an informative physical query q of cost \`c_q\`, let its actual named response fibers be \`S_{q,y}\`. Then

\[
B_p(S)=\min_q\left(c_q\sum_{i\in S}w_i+
 \min_{\bigoplus_y p_y=p\oplus(c_q |S|\bmod2)}
 \sum_y B_{p_y}(S_{q,y})\right).
\]

For singleton S, \`B_0=0, B_1=+infinity\`. Every informative query strictly decreases the possible-state subset on each branch; induction on subset size proves unrestricted exactness. A positive-cost noninformative query may be deleted. The second implementation does not quotient any of the original 228 named observations; the first coalesces only *equal response partitions with the same query price*, which is cost-equivalent for this declared decision problem.

### Complete integer classification proof

For arbitrary Q abbreviate \`u=U_1(Q)\`, \`m=M_1(Q)\`, \`r=U_R(Q)\`, \`s=M_R(Q)\`. These are integers, \`u>=296\`, \`m>=690\`, \`r>=4\`, \`s>=r\`. Also \`U_3=u+2r>=308\`, \`M_3=m+2s>=700\`, and if \`r=4\` then \`s=4\`. We now find **one** T that is no more costly than Q for **both populations at both prices x=1 and x=3**.

1. **u=296 or 297.** The condition \`u+2r>=308\` forces \`r>=6\`. New x=1 parity bounds force \`m>=757\` at u=296 and \`m>=758\` at u=297. Since \`s>=6\`, \`U_3>=308\`, \`M_3>=769\`, so **A** dominates Q at both price endpoints in both populations.

2. **u=298 or 299.** The x=3 uniform lower bound forces \`r>=5\`. The new even 24:1 bound forces \`m>=709\` at u=298; the new odd 19:2 bound forces \`m>=709\` at u=299. Therefore \`U_3>=308\` and \`M_3>=719\`; **B** dominates both price endpoints.

3. **u=300 or 301, r=4.** The fiber certificate gives \`s=4\`. Thus \`U_3=308\` or 309. Inherited x=3 even/odd bounds force \`M_3>=719\` or 720, respectively. Then \`m=M_3-8>=711\` or 712. In both cases **B** dominates Q at x=1 and x=3.

4. **u=300 or 301, r>=5.** Because \`s>=5\`, the scalar bounds give \`U_3>=310\`, \`M_3>=m+10>=700\` and \`m>=690\`; **C** dominates both endpoints.

5. **u>=302.** Because \`r>=4\`, \`U_3>=310\`; \`M_1>=690\` and \`M_3>=700\` follow from the unrestricted scalar bounds. **C** dominates both endpoints.

These cases exhaust all integer \`u>=296\` and \`r>=4\`. For the chosen T, both differences \`U_x(Q)-U_x(T)\` and \`M_x(Q)-M_x(T)\` are affine in x and nonnegative at x=1 and x=3. Consequently both are nonnegative throughout the real interval [1,3]. Their nonnegative prior combination proves the theorem for all real lambda in [0,1]. QED.

### Consequences

The three-tree basis is **minimal in the number of distinct affine cost-vector classes**. At x=1, A, B, C are strictly exposed Bellman-optimal on three nonempty open prior chambers separated by \`155/1847\` and \`620/3299\`. Any single affine cost vector matching the unrestricted optimum on an open chamber must coincide with that chamber's exposed affine piece, so no two chambers with distinct affine pieces can share one basis vector.

Any prior-blind randomized mixture of arbitrary original identifying trees can be replaced tree-by-tree with a mixture of A/B/C, pointwise no more costly on the *entire* low-price rectangle. Combined with EC49FRP's analogous \`∀Q ∃T∈{D,E} ∀x>=3 ∀lambda\` high-price theorem, the original model has a **three-tree low-price** and a **two-tree high-price** uniform Pareto basis. At price x=3 the pairs B/D and C/E have exactly equal (U_3,M_3) costs. Each strip retains its own correct quantifier order.

The theorem is internal to the original finite frozen *typed BRC response/observation model*. It does not collapse any underlying X6 state, provenance, joint relation direction or future observer. P000, the ACTIVE worldview, frozen inputs, and mathematical admission statuses remain unchanged.

## Evidence, verification and next scientific question

Original master SHA256: \`cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e\`.
Original physical-cost CSV SHA256: \`a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f\`.
The complete companion archive in this research conversation includes both source files, full original A/B/C trees, all four new parity-optimal witness trees, two independently written exact DP programs, original inherited x=3 Bellman certificate, exact machine results, logs and SHA256 manifest. The archive has been decompressed and all 18 listed files hash-verified; archive SHA256: \`5336a97f56e2d6408a8e03e8ffc72ed27fb486ed9bd8122e0c96fb9d7843561f\`.

The new theorem uses no floating-point interpolation. Author-computed finite checks and the full integer case proof establish the stated model-internal result; independent mathematical review and formal Source Result/Review remain open.

**Next question**: price individual named observations nonuniformly and determine which exact perturbation domains preserve a finite uniformly dominating Pareto basis, while retaining the original joint-relationship observer semantics. Control publication/CLAIM/Activity are separate from the portable research artifact.
