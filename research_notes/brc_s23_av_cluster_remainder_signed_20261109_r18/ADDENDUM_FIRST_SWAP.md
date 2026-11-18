# First single-cluster crossing: a local risk-increment lemma and S23 n=226

2026-11-09 · continuation of ADDENDUM_POSITIVE_GAP.md and PROOF.md; author-side exact mathematics.

## General first-crossing lemma

For the signed rational-cluster observer, work after phase reflection with theta_+=k/q+eta, delta=q*eta and m>=q. Suppose at time t-1 (t>m) every circular boundary gap G_s(t-1)>0, so the q phase clusters are cyclically ordered and their interior gaps have length delta. Suppose the new cut with source index i=t-1 belongs to residue r, and at time t its unique negative boundary is G_r(t)=-x where

```
0 < x < delta,
```

while the cyclic location it crosses is the first point of the next cluster r_plus. Assume that next cluster already contains its first two cut points at the historical time m (equivalently m>r_plus+q), and no other boundary crossing occurs in this insertion. Then the new cut lies inside that next cluster's first historical intra-cluster arc, of length delta, at distance x clockwise from its first endpoint; this arc was an unrefined n-cut subarc at time t-1. The exact optimal whole-future-block risk increment is

```
R_theta(m,t-m)-R_theta(m,t-1-m) = min(x,delta-x).       (3)
```

**Proof.** Before insertion, the target historical intra-cluster arc contains no internal refined cuts. The new phase point crosses the next cluster's first cut by x, and x<delta places it before that cluster's second cut; all other arcs are unchanged. Hence the maximum length in this historical arc decreases from delta to max(x,delta-x), and the global risk increases by delta-max(x,delta-x)=min(x,delta-x). The mirror theta ↔1-theta preserves risks and lengths. QED.

This result is local to a single first boundary crossing with a two-cut historical target cluster; its exact hypotheses identify the arc and rule out a hidden second crossing. It is compatible with (1), which applies up to the positive-gap boundary, and is an explicit next carrier transition beyond that boundary.

## Frozen S23 exact first crossing

For theta in the certified strict interval, p/q=16/61, eta=16/61-theta, and reflected k=45 with inverse 19 modulo 61, the first negative cluster gap occurs when the cut of index i=225 (t=226) extends residue r=42 beyond the next cluster r_plus=0. At n=225 all gaps are positive. At n=226 exactly G_42 is negative, and every other G_s remains positive. The new point lies between cuts i=0 and i=61, both present in the original m=128 history.

```
G_42(226)=1/61-225*eta=-x,
x=225*eta-1/61=59-225*theta,
delta=61*eta=16-61*theta.
```

The strict rational theta enclosure proves 0<delta-x<x<delta. Thus (3) gives

```
Delta R(128, L=98) = delta-x
                   = 1/61-164*eta
                   = 164*theta-43.
```

Combining this exact local update with the previously proved n=225 endpoint yields

```
R_theta(128,98)=-2090+7972*theta.
```

This explains, by an explicit cut transfer from the boundary of cluster 42 to the historical short arc of cluster 0, why the increment at n=226 remains the prior value even though the uncorrected positive-gap cluster formula no longer applies.

`VERIFY_FIRST_SWAP.py` separately checks both strict rational enclosure endpoints, all 61 gaps at n=226, the unique crossing, ordered cut location, the shortest-side relation, and the independent exact phase subdivision risk. `RUN_FIRST_SWAP.txt` contains its executed stdout.

Next: classify the maximal sequence of single-boundary transfers before the next multi-cluster interaction, preserving the exact historical-arc labels, and test a local-event rank/select implementation against the existing Farey event stream.