# F7 Driver r427 — sharp fixed-separation defect dichotomy for all two-slot old-axis unimodular mixers

Date: 2026-11-21 (+08:00). Contributor: original Driver logical line `EM-DVR-DEBB5E`. Status: proved self-contained finite-dimensional mathematical subunit; no Native Review, Result admission, formal Task completion, or mother Objective closure is asserted.

## Precise scope and original provenance

This is an independent *extension* of the Driver's previously saved branching-gap lemma [2026-11-21_f7_branching_dilation_quantitative_gap_exact.md](2026-11-21_f7_branching_dilation_quantitative_gap_exact.md) (commit `480ecb69061cc4fc1a9034a21fddf6f63c9e5241`). That lemma handled arbitrary integer branching but specialized its F7 conclusion to the original author's particular old-axis matrix `[[2,3],[3,4]]`. The frozen F7 author's source remains `EM-CBRCF7-83A1D4`, original commit `c9bf0811f8cc17af1fa116af75911ed70b1f26b9`; no original claim or authorship is reassigned. The present theorem classifies the entire *block-separated old-axis* `GL_2(Z)` family, not arbitrary `GL_4(Z)` or every F7 marked-balance model.

Let `B=[[a,b],[c,d]] in GL_2(Z)`. For any finite-valued `f:Z^2 -> [0,infty)` satisfying `f(0,0)=0`, set `H(t)=f(t,0)` and suppose `H(t)>=s>0` for every `t != 0`. Define the block-separated map
```
A_B(n,m,p,l)=(a*n+b*p, m, c*n+d*p, l)
```
on `Z^4`, and its total additive-energy defect
```
D_{B,f}(n,m,p,l)
 = f(a*n+b*p,m)+f(c*n+d*p,l)-f(n,m)-f(p,l).
E(B,f)=sup_{(n,m,p,l) in Z^4} |D_{B,f}(n,m,p,l)|, possibly +infty.
```
Call a `2x2` matrix *monomial* if it is a signed permutation matrix (one nonzero entry, equal to `+1` or `-1`, in each row and column).

## Theorem (complete sharp two-slot dichotomy)

For every `B in GL_2(Z)` and `s>0`,
```
inf_{f >= 0, f(0,0)=0, f(t,0)>=s (t!=0)} E(B,f)
    = 0,  if B is a signed permutation;
    = s,  otherwise.
```
Moreover, for **every** admissible `f`, a nonmonomial `B` satisfies `E(B,f)>=s`, with no boundedness or evenness requirement on `H`.

### Proof of the lower bound

If both columns of `B` have at most one nonzero entry, invertibility forces one nonzero in each *different* row and column. Since `det B=+-1`, the nonzero entries must be `+-1`. Thus every nonmonomial unimodular `B` has a column with two nonzero coefficients.

For the first such column `(a,c)^T`, evaluate `D_{B,f}(t,0,0,0)` at `t != 0`:
```
|H(a*t)+H(c*t)-H(t)| <= E(B,f).
```
Both multipliers are nonzero integers. The exact branching lemma from the cited Driver source applies with `r=2`, yielding `E(B,f)>=s`. If instead the second column `(b,d)^T` splits, use `D_{B,f}(0,0,t,0)` and obtain the same conclusion. This also handles `E=+infty` without change.

The invoked branching lemma is independent of sign, column sizes and expansion: with `S_k=sum_{w in {1,2}^k} H(a_w*t_0)`, nonzero outputs imply `S_k>=2^k*s`; its upper recurrence from a defect bound `e` gives `S_{k+1}<=S_k+2^k*e`. Dividing `S_k<=H(t_0)+(2^k-1)*e` by `2^k` and taking `k->infty` proves `e>=s`. This restatement shows that no unspoken positivity on extra coordinates or noncolliding multiplication paths was used.

### Universal optimal witness

Set `f_s(n,m)=s*1_{n!=0}`, independent of `m`. Then
```
D_{B,f_s}/s = #{nonzero coordinates of B(n,p)}-#{nonzero coordinates of (n,p)}.
```
Because `B` is invertible, either `(n,p)=(0,0)` and both supports have size zero, or both vectors are nonzero and their support sizes lie in `{1,2}`. Thus `E(B,f_s)<=s` for every unimodular `B`.

If `B` is nonmonomial, a splitting column maps a vector of support one to support two, so `E(B,f_s)=s`. If `B` is monomial, every input has the same support size as its image, so `E(B,f_s)=0`. This proves both sharp values. QED.

## Exact finite regression and its logical role

A separate exhaustive arithmetic check enumerated all matrices `a,b,c,d in {-2,-1,0,1,2}` with `|ad-bc|=1` and all `(n,p) in [-4,4]^2` for the support witness. It found exactly **104** unimodular matrices: **8** signed permutation and **96** nonmonomial; the maximum support-change defect was respectively **0** and **1** for every matrix, with **zero mismatches**. The universal theorem above is proved algebraically and does not depend on this bounded regression.

## Relation to the F7 mother question and the remaining boundary

1. The author's original `B=[[2,3],[3,4]]` is nonmonomial, so its fixed-separation lower bound `E>=s` is one instance of the proved complete `GL_2(Z)` class. The statement is stronger than a single-axis test and does not require special residue identities.
2. The witness `f_s(n,m)=s*1_{n!=0}` need not obey F7's separate marked `f(1,0)=1`, `f(2,0)=f(3,0)=1/2` conditions for general `s`; therefore the universal minimax **sharpness** here is for the declared separation-only class. The preceding Driver note independently supplied marked-balance sharpness for the *specific original* `B` and `0<s<=1/2`. For an arbitrary `B`, the **lower bound** remains valid under additional marked constraints, but their optimal attainable defect is not classified here.
3. This dichotomy assumes `A_B` maps the second coordinate of each output slot unchanged. An arbitrary A0-compatible `GL_4(Z)` mixer may alter the other coordinates, so the two-slot axis test may fail to iterate in the same one-variable slice. A genuine next step is a certified invariant finite-ray/cone class, or an explicit `GL_4` counterexample, preserving all F7 assumptions.
4. A defect bound below `s` for a block-separated `B` therefore *forces* the old-axis mixing block to be monomial. Exact conservation is the `E=0` special case; no theorem here changes the independently frozen original Result, its manifest hash discrepancy, or review/authority status.

**Layered status:** one new mathematical proof subunit; Native Review admitted 0; Native Result admitted 0; formal Task DONE 0; parent Objective CLOSED 0.
