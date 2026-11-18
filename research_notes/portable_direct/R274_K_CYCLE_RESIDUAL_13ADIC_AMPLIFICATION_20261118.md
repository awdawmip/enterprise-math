# R274 — K-way directed Port-cycle residual and 13-adic length amplification

2026-11-18. AUTHOR_PROVED / EXACT_INTEGER_AND_RATIONAL_CHECK / NOT_REVIEWED.

**Lineage:** R273 in branch `portable/r1-r273-mixed-cycle-20261118-1529`, continuing R272@ `bafca0cfdb4a7814cc5d74534ff9ade753029b4a`. Frozen science `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Exact foundation WBRC-T30/T31/T32 with retained visible, labeled Ports.

## Theorem A — exact K-way mixed-cycle observer

Let `K>=2` be an integer. Take K distinct labeled visible Ports and the nonnegative rational recurrent matrix W with precisely the K edges `i->(i+1 mod K)` of weights `a_i`, with `Q=product(a_i)<1`. All other entries are zero. Then

```
W^K = Q I_K,
S=(I-W)^(-1)=(I+W+...+W^(K-1))/(1-Q),
S_ii=1/(1-Q),     each labelled Port i.
```

**Proof.** Every K-step route returns to its initial Port with total weight Q, whereas no positive path shorter than K returns. Hence `W^K=QI` and the claimed finite resolvent follows by multiplication. The spectral radius of this nonnegative cycle matrix equals `Q^(1/K)<1`, proving strict recurrent stability.

If any nonempty **proper subset** of the K edges is kept, the retained subgraph is acyclic. Its matrix is nilpotent, its finite star is `I+W+...+W^(K-1)`, and every diagonal star observation is **exactly 1**. Thus every proper edge subfamily is invisible to this *selected diagonal observer*, while all K edges jointly produce `S_ii-1=Q/(1-Q)`. This is an exact K-way joint-relation direction in the allowed positive-rational visible-Port interface. Off-diagonal stars and retained source/Port labels are not identified by this one observer.

## Theorem B — 13-adic resonance amplified by v13(K)

For every integer `t>=1`, set `P=13^t` and let all K edges have positive rational weight `a_i=1/(1+P)`. Every row sum is <1 and the complete K-cycle is strictly stable. Its loop product and resonance denominator are

```
Q=(1+P)^(-K),
1-Q=((1+P)^K-1)/(1+P)^K.
```

The exact valuation formula is

```
v13((1+13^t)^K-1)=t+v13(K),
v13(1-Q)=t+v13(K),
v13(S_ii-1)=-(t+v13(K)).
```

So the cycle's length contributes **exactly v13(K) extra p-adic pole digits**; for `K=13^h` the gain is h. At `t=1`, cycles of lengths 13,169,2197 have 13-adic pole depths 2,3,4 respectively, while deleting any single edge makes every diagonal star identically 1.

**Complete valuation proof.** Write `K=13^h u` with `13∤u`. Since `u` is a 13-unit, the binomial expansion of `(1+P)^u-1` starts with `uP` of valuation t and all later terms have valuation at least 2t; hence the expression has valuation exactly t. If `x=1+13^r z`, where `r>=1` and `13∤z`, expansion of `x^13-1` has first term `13^(r+1)z`. Every intermediate term has valuation at least `1+2r>r+1` because `13` divides `binom(13,j)` for `2<=j<=12`, and the final term has valuation `13r>r+1`. Thus raising to the 13th power adds exactly one to the valuation; repeat h times. Finally, `Q` is a 13-adic unit, proving the third displayed equality.

This is a standard binomial/lifting-the-exponent argument embedded into the actual BRC labeled-Port context; it does not reclassify a K-edge feedback cycle as a primitive K-force equilibrium under P000.

## Exact evidence and declared limits

The companion stdlib `Fraction` and integer checker tests `t=1..4`, cycle lengths `2..40`, `169`, `2197` (164 integer valuation cases), plus the full rational matrix inverse and **every one-edge deletion** for `t=1..3`, `K=2..6` (15 complete matrix cases). It returns `PASS 164 matrix 15`. The complete generated `R274_verification.json` has SHA-256 `b90049a62c2c78e65b6e0e738bbd0d775e503313963f94e50f1f437982f2e0b9`. The unbounded t,K theorem rests on the symbolic proof, not finite extrapolation.

The permitted context covers rational nonnegative labeled visible Port edges. The exact full `W_eff` and provenance remain the WBRC-T32 unrestricted-context signature; this result only establishes the named diagonal observer's behavior. Native Heartbeat-X6 constraints and the mandatory joint-relation-preservation scope remain intact.

## Next scientific questions

1. With several cycles sharing vertices, expand the small feedback determinant as a **signed cycle-cover** expression and locate cancellation and 13-adic resonance strata in genuinely interacting Port modules.
2. Over a declared sequence of edge insertions, identify and prove the smallest retained mixed-cycle coordinate that makes a desired observer descend through the quotient.
3. Continue the R269 source/provenance-to-native-Port mapping question using explicit port labels, branch history and future-operation fiber constancy.

Artifacts: this MD, `R274_cycle_length_resonance_checker.py`, and `R274_verification_digest.json`. The full machine JSON is regenerated deterministically by the checker. Independent review is pending.
