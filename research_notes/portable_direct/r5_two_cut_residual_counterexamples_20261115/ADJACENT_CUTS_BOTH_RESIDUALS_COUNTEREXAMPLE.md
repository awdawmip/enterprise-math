# Adjacent length-three cuts can exhibit both optimizer residuals

Date: 2026-11-15. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Companion: TWO_CUT_RESIDUALS_THEOREM_AND_GEOMETRIC_COUNTEREXAMPLES.md, same directory, frozen science pin `435e77af0d180eac32bd1f9c4c464bc4010b7551`.

## Exact six-event certificate

In the derived one-dimensional integer-event radius-two indexed-center model, take n=6, K=4, original gaps `(3,3,3,2,2)` and close the **adjacent** original gap positions a=0 and b=1 (zero-based). Each selected gap changes length 3 to 2. The event coordinates for closure masks empty,a,b,ab are respectively:

- empty: (0,3,6,9,11,13)
- a: (0,2,5,8,10,12)
- b: (0,3,5,8,10,12)
- ab: (0,2,4,7,9,11)

All four optimal total nearest-center distances equal exactly 4. Writing 0124 for the center-index set {0,1,2,4}, the **complete** optimal families obtained by exhaustive enumeration of every 4-subset of six event indices are:

```
O_empty = {0124}
O_a     = {0124,0234,0235,0245,1234,1235,1245}
O_b     = {0124,0134,0135,0145,0234,0235,0245}
O_ab    = {0124,0134,0135,0145,0234,0235,0245,1234,1235,1245,1345}
```

Consequently the intersection surplus is

```
P = (O_a ∩ O_b) \ O_empty = {0234,0235,0245}
```

and the joint-only surplus is

```
Q = O_ab \ (O_a ∪ O_b) = {1345}.
```

Both are **nonempty**, even though cuts a and b are adjacent. Their exact cardinalities are |P|=3 and |Q|=1. The formula from the companion note gives |O_ab|=7+7-1-3+1=11, agreeing with enumeration. The directed minimal-center replacement maxima are H_a=2, H_b=2, H_ab=2; thus a nonempty Q does not by itself force a *strict* increase in the maxmin distance.

## Reproduction and conclusion

Run the adjacent Python verifier already in this directory and invoke `run_case([3,3,3,2,2],0,1,4)`; check the returned P, Q, optimizers and maxmin fields against the exact values above. The full computation evaluates 15 possible labeled 4-center sets under each mask, with integer distances and no tolerance. This is an explicit counterexample to **adjacency alone** being a sufficient geometric condition for the Boolean optimizer diamond. It also exhibits both distinct residual mechanisms in one layout.

The general task remains to identify stronger structural conditions, beyond gap adjacency, which make P=Q=empty in the previously frozen 954-event R5 case. This document is independent research evidence, not a formal Task/CLAIM/Review update.
