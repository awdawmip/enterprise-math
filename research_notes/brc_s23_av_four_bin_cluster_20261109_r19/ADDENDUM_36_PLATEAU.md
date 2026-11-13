# S23: structural proof of the first 36-step risk plateau and exact restart

Date: 2026-11-09. Frozen science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Mathematical predecessor: this directory's `ADDENDUM_67_TRANSFERS.md` and r18's positive-gap theorem. All assertions use the auxiliary uniform-phase Bayes circle observer with m=128 and theta in the previously certified strict 24-digit interval.

Put `beta=1-theta=45/61+eta`, `eta=16/61-theta`, `delta=61*eta`, `x=225*eta-1/61`; the verified strict relation is `0<delta-x<x<delta`.

## Exact finite-interval theorem

For **every** theta in the certified interval and every integer n from 293 to 328,

```
R_theta(128,n-128) = -4928 + 18796*theta.                   (I)
Delta R_theta(128,n-128) = 0.                              (J)
```

At n=329 the exact growth resumes:

```
Delta R_theta(128,201)=164*theta-43=delta-x,
R_theta(128,201)=-4971+18960*theta.                       (K)
```

This identifies, in terms of labeled historical arcs, the **mechanism** of the previously computed first 36-step flat block: each insertion splits a delta-sized gap while leaving another delta-sized gap in its *same historical arc*, so that its Bayes-optimal maximum remains unchanged.

## Proof

At m=128=2*61+6, each residue h=6,...,60 has exactly two historical cuts, with source indices h,h+61. Its original historical boundary arc starts at index h+61. For h=6,...,41, the positive-gap r18 theorem through n=225 shows that later cuts h+122 and h+183 both belong to this historical boundary arc, at successive clockwise spacings delta. The remaining terminal gap is `1/61-164*eta=delta-x`, strictly smaller than delta. Thus by n=225 this historical arc has two internal refined gaps of length delta and a terminal gap delta-x, so its maximal refined gap is delta.

The preceding 67 steps n226,...,292 all inserted cuts into historical *short* arcs (not these boundary arcs). They leave the stated maxima intact.

For every h=6,...,41, set `i=286+h` (so i=292,...,327 and n=i+1=293,...,328). Since `i-(h+61)=225`,

```
{(i-(h+61))*beta}={225*beta}=x,  0<x<delta.
```

The new cut therefore splits the first delta gap in historical boundary arc h+61 into lengths x and delta-x, but the **second delta gap** between h+122 and h+183 survives. All 36 h target different historical arcs. Every other historical-arc maximum is unaffected, and the targeted arc's maximum remains delta. Therefore every associated risk increment is zero, giving (I)-(J) from the prior certified R at n292.

At h=42, the new index is i=328 and its target historical boundary arc starts at index 42+61=103. The predecessor positive-gap epoch left an inserted cut 42+122=164 at distance delta from index103, followed by a terminal subgap of length delta-x. Its next same-residue index 42+183=225 already crossed into the *short historical arc of residue 0* (the r18 first swap), so there is **no second delta gap** in the historical boundary arc of index103. At n329, cut i328 lies x inside its sole delta subgap, splitting it into x and delta-x. Its historical-arc maximum falls from delta to x (since x>delta-x); all other historical arc maxima stay unchanged. The risk increases by delta-x=164 theta-43. This proves (K). QED.

## Verification and next question

`VERIFY_36_PLATEAU.py` ran exact `Fraction` checks on each of the two certified theta enclosures. It individually computed maxima of all 128 historical arcs at every insertion n293,...,329 and checked the target-arc winner, global success mass, interval risk, and first restart. Output `RUN_36_PLATEAU.txt` reports PASS. The strict linear inequalities used in this argument hold at both endpoints, hence throughout the certified theta interval.

The new exact arc-based explanation joins the r19 four-bin positive-gap segment, 67 transfer steps and 36-step plateau into a single provenance-labeled finite history of risk. Next derive the next family of positive increments n329 onward and identify the next *different* maximizer event (not a repeat of the first cycle). Independent mathematical review and project admission remain pending.