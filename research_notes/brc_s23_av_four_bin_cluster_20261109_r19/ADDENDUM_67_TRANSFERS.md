# S23: 67 distinct historical-short-arc transfers after the first cluster crossing

Date: 2026-11-09. Same frozen S23/AV circle-risk input `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Predecessors: r18 positive-gap theorem, its exact first crossing at n=226, and r19 four-bin risk formula.

## Exact theorem

Let `m=128`, `q=61`, `p/q=16/61`, `theta` in the previously certified strict interval
`262204504569236716045286/10^24 < theta < 262204504569236716045287/10^24`.
Put `beta=1-theta=45/61+eta` with `eta=16/61-theta>0`, `delta=61*eta`, and `x=225*eta-1/61`. The predecessor r18 certified `0<delta-x<x<delta`.

For every new cut index `i=225,...,291` (cut counts `n=i+1=226,...,292`), set `j=i-225`, `h=j mod 61`, and choose historical arc start/end indices

```
a_i=h+61*[j>=61],     b_i=a_i+61.
```

Then `a_i,b_i` belong to the original 128 cuts; `0<=a_i<b_i<128`. In the reflected clockwise circle order, the historical arc `[a_i,b_i]` has length `delta`, and the new cut `i` lies exactly `x` clockwise from its start:

```
{(b_i-a_i)*beta}=delta,     {(i-a_i)*beta}=x.
```

These 67 historical arcs are pairwise distinct: first 61 occupy the **first** intra-cluster short arc of residues h=0,...,60, and the next six occupy the **second** intra-cluster short arc of residues h=0,...,5.

At n=225 all these historical short arcs remain unrefined by future cuts (r18 positive-gap theorem). No previously inserted new cut lands inside a later target arc. Thus each insertion splits one previously unrefined historical arc of length delta into x and delta-x. Its Bayes risk increase is exactly

```
Delta R_theta(128,n-128) = min(x,delta-x)
                           =delta-x
                           =164*theta-43   (>0)
                      for EVERY n=226,...,292.        (F)
```

Together with `R_theta(128,225-128)=-2047+7808*theta`, this gives the complete **67-step post-boundary affine continuation**

```
R_theta(128,n-128)=-2047+7808*theta+(n-225)*(164*theta-43),
                                          225<=n<=292. (G)
R_theta(128,164)=-4928+18796*theta.                       (H)
```

## Proof of location, uniqueness and increment

For `j=0,...,60`, `i=225+j`, `a_i=j`, so `i-a_i=225`. For `j=61,...,66`, `i=225+j`, `a_i=j-61+61=j`, hence again `i-a_i=225`. In both layers, `b_i-a_i=61` and `(225*beta) mod 1=x` because `225*45/61 =165+60/61`; `(61*beta) mod 1=delta`. The strict inequalities locate each new cut in its target historical arc.

The first layer's starts are 0,...,60 and the second layer's starts are 61,...,66, all unique and contained in `[0,67)`, with ends at most 127. r18's positive-gap regime through n225 means no new cut before i225 entered any original intra-cluster short arc. Each of the 67 added cuts lands in a fresh such arc, so its largest subdivided gap changes from delta to max(x,delta-x)=x. The global success mass decreases by delta-x, proving (F). Summing (F) from the certified r18 endpoint proves (G)-(H). QED.

## Independent finite corroboration and next frontier

`VERIFY_67_TRANSFERS.py`, run using exact `Fraction` arithmetic, checks both certified theta interval endpoints. For all i225,...,291 it verifies the congruence, short historical arc membership, 67 unique arc starts, and each exact Bayes increment by independently reconstructing all circular cut intervals. At n293 it additionally observes `R_theta(128,165)=R_theta(128,164)` at both endpoints; the *general* risk-plateau interval beyond n292 remains a separate next unit. Actual stdout is in `RUN_67_TRANSFERS.txt`.

This is a proof of a concrete finite but parameter-interval-uniform 67-transfer family, and a reusable disjoint-target method for local phase-cut risk. It refines the structural mechanism underlying an earlier numerically certified constant-increment segment; it neither redefines P000 nor asserts native X6 dynamics or independent theorem admission.