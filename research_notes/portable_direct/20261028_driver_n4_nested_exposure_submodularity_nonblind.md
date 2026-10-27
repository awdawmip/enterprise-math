# N4 nested-exposure theorem — submodular signed-support loss for disjoint collisions

Date: 2026-10-28 (Asia/Taipei). **SOURCE-EXPOSED / NONBLIND / AUTHOR-LEVEL PORTABLE PROOF / UNREVIEWED / NOT_ADMITTED**. This is *not* a native Driver Review, reference pass, synthesis, follow-up, V2 task publication, or clean-independent assessment. The present recurring Driver conversation has previously seen author work on R5/F7; this proof retains the N4 original author's separate contribution.

## Exact motivation and provenance

The original R1-author N=4 strictly-positive two-law stopping tree and its exact dynamic calculation are in `research_notes/brc_n4_dynamic_two_collision_support_nonadd_20261028_r1t11/PROOF.md`, read at Enterprise Math `main@43ff8342a26b580f07bd009ca54de5128495b52a`. That author established an example with strict *subadditivity* of two support losses, but did not assert a universal inequality. The present note proves a bounded structural theorem explaining why this N4 exposure pattern is always subadditive for **every** signed direction, not merely the displayed numerical direction. The numerical tree and its exact values belong to the R1 author; only this abstract inequality and its sufficient strictness criterion are claimed here as new source-exposed derivations.

This is an **external finite P/Q sequential experiment**. Its four-dimensional observer is `O=(P(D=Q), Q(D=P), E_P[tau], E_Q[tau])`. The user-fixed P000 native discrete X6 and separately typed time, ACTIVE residual-fidelity worldview, and all original BRC task assumptions remain untouched. No correspondence to native X6 dynamics is proved.

## Scope: nested, disjoint exposure and additive Bellman costs

Fix any real signed direction `lambda in R^4` and minimize `lambda · O` over all real behavioral probabilities. Assume the finite stopping tree has two initially distinguishable histories/roots A and B, each permitting immediate stop (with already optimized stop cost `s_A,s_B`) or continuation. Under full-history policies, continuing these roots has separately optimized additive costs `c_A,c_B` (these numbers include the original positive P/Q path masses). Further assume two **different** signature-compression restrictions:

* X identifies one action interface in a descendant subtree of A with one in a descendant subtree of B. X has no effect unless **both** roots continue. When both continue, replacing independently optimized X-actions by a shared action increases the combined minimized cost by a fixed `d_X >= 0`.
* Y identifies action interfaces entirely inside a different descendant subtree of A, disjoint from both X subtrees. Y has no effect unless A continues. After optimizing its own subtree, it increases A's continuation cost by a fixed `d_Y >= 0`, independently of X.
* Apart from X and Y, continuation objectives decompose additively into the named subtrees; no other action constraint couples those subtrees or their root stops. At other same-signature terminal interfaces, their common optimal terminal decision may be folded into the subtrees without additional signed-support cost.

The nonnegative increments exist because shared-action feasible sets are subsets of their unrestricted counterparts. The theorem does **not** cover overlapping collision descendants, a later shared seed coupling two subtrees, or a restriction that changes the root action interfaces themselves. In the original N4 tree, X is the `t=2` AU/BU collision, Y is the `t=3` AV0/AV1 collision, and the remaining identical BV0/BV1 signature has no extra signed-support penalty.

Define `V_00=V_full`, `V_10=V_X`, `V_01=V_Y`, and `V_11=V_XY` as the exact minima, where subscripts say which of X/Y are imposed.

## Theorem (nested-disjoint collision submodularity)

Under the stated exact hypotheses, for **every** signed direction,

```
0 <= V_10 - V_00,       0 <= V_01 - V_00,
max(V_10,V_01) <= V_11 <= V_10 + V_01 - V_00.
```

Equivalently, the incremental support loss of Y cannot increase after imposing X:

```
V_11 - V_10 <= V_01 - V_00.
```

No finite rational grid, positive-sign restriction on lambda, Gaussian approximation, or special numerical tree is used.

### Proof

A finite-horizon stopping tree with each time-indexed signature visited at most once along a path has a multi-affine expected linear cost in its per-signature behavioral action probabilities. Therefore each minimum is attained at a deterministic vertex, and the four root stop/continue configurations suffice. The branch separation assumptions give the **exact**, not upper-bound, costs

```
A=S,B=S:  s_A+s_B
A=S,B=C:  s_A+c_B
A=C,B=S:  c_A+j*d_Y+s_B
A=C,B=C:  c_A+c_B+i*d_X+j*d_Y,
```

where `i,j in {0,1}` denote imposing X and Y. Hence

```
K = s_A + min(s_B,c_B),
L_i = c_A + min(s_B,c_B+i*d_X),
V_ij = min(K,L_i+j*d_Y).                                    (1)
```

Since `d_X>=0`, `L_1>=L_0`. For every `d>=0` and all real `K,L`,

```
min(K,L+d)-min(K,L)=min(d, max(K-L,0)).                      (2)
```

The right-hand side of (2) is nonincreasing in `L`. Apply it first with `L=L_1`, then with `L=L_0`, and `d=d_Y`:

```
V_11-V_10=min(d_Y,(K-L_1)_+)
          <=min(d_Y,(K-L_0)_+)=V_01-V_00.
```

This proves subadditivity. Set inclusion of policy classes yields `V_11>=max(V_10,V_01)>=V_00` and the remaining inequalities. QED.

### Sufficient strictness condition

Suppose the unrestricted optimum continues both roots and, with `M=s_A-c_A`, one has

```
c_B+d_X<s_B,       0<max(d_X,d_Y)<M<d_X+d_Y.
```

Then `V_00=c_A+c_B`, `V_10=V_00+d_X`, `V_01=V_00+d_Y`, and `V_11=V_00+M`. Consequently

```
(V_10-V_00)+(V_01-V_00)-(V_11-V_00)=d_X+d_Y-M>0.
```

These conditions are sufficient, not necessary, for strict subadditivity. They show that the strict loss reduction comes from a **single upstream early-stop clipping threshold** rather than from numerical coincidence.

## Exact application to the published N4 tree

For the R1 author's signed direction `lambda=(100,2501/100,0,1/10)`, consume (without recrediting) the already proved subtree costs and collision penalties:

```
c_A=5011/400, c_B=9603/800,
s_A=s_B=2511/200,
d_X=d_Y=1/60.
```

The original optimal root A continuation margin is `M=s_A-c_A=11/400`; root B continuation margin is `s_B-c_B=441/800`. Therefore

```
1/60 < 11/400 < 1/30,        c_B+1/60 < s_B.
```

Our sufficient strictness criterion applies. Formula (1) yields, exactly,

```
V_full=785/32,
V_X=V_Y=11783/480,
V_XY=19647/800,
V_X+V_Y-V_XY-V_full=7/1200.
```

An independently written rational Bellman calculator in the present turn reproduced those four values directly from the 2/4/8/16-node tree with the root stop choices included. The general inequality follows from the algebra above; this single exact instance is only a cross-check.

## Inference boundary and next executable mathematical question

This theorem concerns **minimum signed linear support costs** only; it does not determine joint TV minimax, equal convex hulls, or equality of all-real behavioral observation *images*. For other collision topologies—overlapping descendants, time-recursive signature reuse, shared root interfaces, or cross-subtree control coupling—the `d_X+d_Y` decomposition need not hold, so subadditivity is **not** asserted. Those topologies are the discriminating next targets for a possible superadditive-support witness or genuinely equal-hull/unequal-image mother candidate.

This is portable and source-exposed; preserve the original N4 author's priority, P000, original Result/reviews, and all Source control gates. The Site connected in this turn has `source:read/control:read` only, no own native Driver DA. Do not treat this note as a native review, substitute a research selector for authorization, or publish an automatic successor task. Actual independent admission must start from its own current Driver authority and the exact frozen Result/review set.
