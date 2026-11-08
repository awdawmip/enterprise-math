# Exact first collision of translated eleven-point cascades at H=9,821,806

Date: 2026-11-08. Frozen science remains `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Direct extension of `PROOF.md` in this folder. Status: author-side proof with exact scaled-model execution, independent review pending.

## Exact onset theorem

Use the previous definitions `u=(79,431)`, `d=|u|_1=510`, `w=(380295,2074774)`, `M=|w|_1=2455069`, `q_b=u+b*w`, `H3=2d+4M=9821296`, `r=ln7/ln(10/7)`. At **H=H3+d=9,821,806**, the six-point local starts `0,u,2u` form one connected component. They occupy the following **16 consecutive old integer-key positions**:
```text
OLD:
[2w,w,0, q4,q3,q2,u+w,u,
 2q2,2u+3w,2u+2w,2u+w,2u,
 3u+4w,3u+3w,3u+2w]
```
Their exact increasing true-threshold order is:
```text
NEW:
[q4,2w,q3,w,2q2,q2,0,2u+3w,u+w,
 3u+4w,2u+2w,u,3u+3w,2u+w,3u+2w,2u]
```
Equivalently the new order lists the old indices (zero based):
`[3,0,4,1,8,5,2,9,6,13,10,7,14,11,15,12]`.
The sixteen-point permutation contributes **exactly 20 inverted pairs** (nine `q2`, six `q3`, three `q4`, two `2q2`).

Outside this single component, apply the preceding eleven-/six-/four-/pair local permutations with the following start sets:

- Eleven-blocks at `x in S_d \ {0,u}`: exactly `T(d)-2=130814`.
- Six-blocks at `x in S_(2d) \ (S_d union (u+S_d))`: exactly `T(2d)-2T(d)+1=260100`.
- Four-blocks at `y in S_(M+2d) \ (S_(2d) union (w+S_(2d)))`: exactly `T(M+2d)-2T(2d)=3016189228633`.
- Isolated pair swaps at `b in S_(2M+2d) \ (S_(M+2d) union (w+S_(M+2d)))`: exactly `M^2=6027363794761`.

These operations are pairwise disjoint and correct the entire order of `S_H`. The total number of inverted point pairs is exactly
```text
T(2M+2d)+T(M+2d)+T(2d)+T(d)
  = 15075934741862.
```
The preexisting exact L rank/select oracle therefore retains a finite, O(1)-overhead local correction at this new exact H.

## Proof

The previous proof's complete inverted difference classification remains valid at `H=H3+d`: `(A,B)=(1,2),(1,3),(1,4),(2,4)`, because `(3,4)` has positive true value `3epsilon-4eta>0`, and the first feasible `B=5` requires `H>=d+5M>H3+d`. The old integer key `K=2074774v-380295j` gives four consecutive fibers `K=0,1,2,3`. Their boundary pieces have sizes `3,5,5,3` respectively and concatenate to the sixteen OLD positions above. Every omitted predecessor or successor is either coordinate-negative or exceeds H.

As in the preceding paper, the exact rational logarithm enclosure yields `3eta/2<epsilon<2eta`; sorting the 16 affine forms `Aepsilon-Beta` gives precisely the NEW permutation. A finite inversion count gives 20, matching the four displacement classes within the component.

All six-block starts lie in `S_(2d)`. Two distinct such blocks overlap precisely if their starts differ by `u`; the only three-start chain fitting in `S_(2d)` is `0,u,2u`. Its two adjacent eleven-point cascades intersect in six positions, so their union contains `11+11-6=16` positions. The other eleven and six blocks are disjoint. The predecessor's extremal-fiber criterion partitions all remaining `q3` and `q2` inverted pairs into the listed four- and two-point blocks. Completeness follows from the exhaustive inversion-type classification. Counts follow from the inclusion-exclusion formulas; the exact total is their `20,13,6,3,1` weighted sum. QED.

## Independent executable check and next

`VERIFY_FIRST_OVERLAP.py` exhaustively sorts all 1326 or 1485 thresholds in two different scaled unimodular models at their first overlap horizon and checks every block is old-order contiguous, disjoint and transforms to the full exact true order, with precise count identities. `RUN_FIRST_OVERLAP.txt` preserves its stdout. The large-H theorem is the symbolic argument, with scaled enumerations as implementation checks.

Next seek a **translated 16-point window** for `H3+d <= H <= H3+2d-1`: candidate 16 starts `S_(a-d)`, residual eleven starts `S_a\(S_(a-d) union (u+S_(a-d)))`, and the previous six/four/pair residuals, where `a=H-H3`. Test the full interval in scaled models before claiming a universal theorem.
