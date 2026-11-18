# EC49FSL — Exact positive-volume three-independent-price saturation wedge

Research date: 2026-11-18. Scientific input pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This note extends the companion EC49FSL continuous ten-region theorem under the original 141-profile, 228-named-physical-observer BRC16943 exact native model.

## Domain, variables, and full theorem

Allow **three fully independent named observation discounts** `a,b,z` in [0,1], with costs
- q32: (1-a)t
- q34: (1-b)t
- q140: (1-z)t
- all remaining q: t, with t>0.

Write `H(a,b,z)=141V(a,b,z)/t` for the unrestricted global minimum of complete original named-observer identification trees with uniform prior. In any optimal nonredundant tree, no named observation repeats along a profile path.

The symmetric EC49FSL result is
`G(alpha,z)=H(alpha,alpha,z)=min_{(U,Q,K) in P10}(U-Q alpha-K z)`
for `alpha in [15/32,1/2]`, `z in [0,1]`, where
`P10` consists of:
```text
(304,169,32), (305,173,29), (306,182,10), (308,182,22),
(309,169,46), (311,151,69), (311,169,51), (312,186,31),
(315,151,77), (319,93,141).
```
All but the final type have a fully certified **q34-rooted** original complete decision tree; the last type has a q140 root.

Define `P34=P10\{(319,93,141)}` and the exact rational semialgebraic base region
```text
R34 = { (alpha,z) in [15/32,1/2] × [0,1] :
         min_{(U,Q,K) in P34}(U-Q alpha-K z) <=
                                      319-93 alpha-141 z }.
```
This is the union of the nine closed positive-area q34-optimal polygons in the EC49FSL rational certificate. Its boundaries, including ties with q140-optimal types, are included.

**Exact 3D wedge theorem.** For **all real**
```text
(alpha,z) in R34,     b in [alpha,1],     a = alpha,
```
the full three-price native Bellman optimum is

```text
H(a,b,z) = G(a,z) - 141(b-a)
          = min_{(U,Q,K) in P34} { U - (Q-141)*a - 141*b - K*z }.
```

This domain contains positive-volume open 3D regions (one above each strictly q34-optimal 2D region). Each nine corresponding three-price affine formula is globally optimal throughout its prism and realized by its original preserved q34-root tree. The nine three-dimensional gradients `(-(Q-141),-141,-K)` are pairwise distinct, so at least nine fixed full-tree cost types are necessary to cover the strict interiors of these nine wedges; the witness trees show sufficiency on the stated wedge domain. This statement is confined to the explicitly defined wedge, and makes no claim of a complete [0,1]^3 phase classification.

## Short proof: a sharp observation-saturation transfer lemma

For each complete legal nonredundant original native identification tree T, let `N_j(T)` count the uses of named observation j over the 141 full profile paths, so `0 <= N_j(T) <= 141`. For fixed discounts of all q other than q34, increasing q34's discount from b0 to b1>=b0 changes any tree cost by exactly `-(b1-b0) N_34(T)`, a decrease bounded below by `-141(b1-b0)`. Taking minima over all trees gives the universal sharp inequality

```text
H(a,b1,z) >= H(a,b0,z) - 141(b1-b0).
```

If some globally optimal tree T0 at (a,b0,z) uses q34 at the root, its q34 observation is paid once on **every** one of the 141 profile paths, so `N_34(T0)=141`. Therefore that same feasible T0 at b1 attains precisely `H(a,b0,z)-141(b1-b0)`, giving the matching reverse inequality. Hence *equality holds for the entire future discount ray* b1 in [b0,1].

At any (alpha,z) in R34, the EC49FSL exact ten-plane symmetric theorem identifies at least one q34-rooted optimal tree. Apply this lemma at (a,b0,z)=(alpha,alpha,z) and b1=b. Substitute the known G(alpha,z) and split its native witness count `Q=N32+N34` with `N34=141` and `N32=Q-141`. This proves both displayed equalities pointwise for all real parameters, with no new finite-grid assumptions or physical/Euclidean substitution.

The same argument proves the **global three-coordinate Lipschitz bound**, for all discounts p=(a,b,z), p'=(a',b',z') in [0,1]^3,
```text
|H(p)-H(p')| <= 141(|a-a'| + |b-b'| + |z-z'|).
```
This is a robust necessary bound and is not itself a global optimal-policy selection criterion.

## Independent off-diagonal exact native computation

The new source-pinned **primary** Bellman optimizer and **separate original-source** full 228-observation Bellman decoder were actually run at these **three** off-diagonal rational points, returning exactly matching global minima:

| (a,b,z) | Exact H(a,b,z) | (U,N32,N34,N140) of full optimal tree | Root |
|---|---:|---|---|
| (1/2,15/32,1/3) | 20455/96 | (312,45,141,31) | q34 |
| (15/32,1/2,1/3) | 5033/24 | (304,28,141,32) | q34 |
| (1/2,7/16,1/2) | 3307/16 | (319,18,75,141) | q140 |

All three have complete 141-state native tree witnesses; their depth is 4, 3, 3 respectively. The second anchor lies in the proved saturated wedge, and additionally checks the identity
```text
G(15/32,1/3)-141(1/2-15/32)
=20555/96-141/32
=5033/24.
```
The first and third anchors are exact explorations **outside the particular saturation orientation**; no wedge extension is inferred from them.

The full independently reproduced oracle numeric responses, original named-witness trees, runnable code, and inputs are in the local self-contained EC49FSL archive. This GitHub note is a full human-checkable proof of the wedge using existing immutable EC49FSL tree certificates.

Status: `AUTHOR_PROVED / EXACT_FINITE_CROSSCHECKED (3/3 anchors) / NOT_REVIEWED`. No formal new Task/CLAIM/Result/Review is asserted. No P000 changes, new native X6 mechanics, or source repinning.

**Next**: search a three-price point where none of the inherited ten symmetric-slice witnesses (possibly with mirrored q32/q34 roots) attains the unrestricted Bellman minimum, or prove a larger polyhedral neighborhood of stability by exact certificate geometry with a full native-observer optimizer.
