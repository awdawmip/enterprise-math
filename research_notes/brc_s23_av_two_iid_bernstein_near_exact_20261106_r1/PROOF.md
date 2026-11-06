# S23 conditional AV: near-optimal two-trial reconstruction certificate

Date: 2026-11-06. Author exact computer-assisted rational certificate; independent mathematical review pending. Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Continues exact indistinguishable-fiber theorem at `4aa996135989aa84297a0a47db3dd8728e320146:research_notes/brc_s23_av_two_iid_exact_fiber_diameter_20261106_r1/PROOF.md` (Draft PR #1777).

## Precise theorem

Let `a,c` range independently over the entire real interval `[1/2,7/8]`. Set `z=(1-a)c`, `u=1-a-z`, and define the full conditional AV stop law `A=(a,z,u)` on `{1,3,4}` and binary event law `B=(z,1-z)` on `{Y,N}`. Both trials are independent *conditional on the same* hidden `(a,c)`. The original separate parameter `b` may be any value in `[1/8,1/2]` and does not change this conditional AV observer. For one parameter-independent `4x9` row-stochastic kernel `L`, set

`delta2 := inf_L sup_{a,c in [1/2,7/8]} TV(A(a,c)^tensor2, B(a,c)^tensor2 L)`, with `TV(P,Q)=sum_j |P_j-Q_j|/2`.

**New exact certified bound over the entire continuous parameter domain:**

`9/49 <= delta2 <= 9/49 + 1/1500000 = 13500049/73500000`.

The new upper is about 0.18367413605; the lower is about 0.18367346939. The remaining gap is **at most exactly 1/1500000**. The preceding proved upper from `6a00e023af967e99fe459d72b2e7d2dc1b861430` was `387769986271/2048000000000` (about 0.1893408136).

## Lower certificate (reused)

The two legal parameters `(a,c)=(1/2,1/2)` and `(5/7,7/8)` share the identical binary probability `z=1/4`, but their full two-trial laws have total variation exactly `18/49`. Any common kernel reconstructs the same law at these two parameters; TV triangle inequality gives a worst error >=`9/49`. The verifier independently checks the exact nine-coordinate Kronecker TV equality.

## New constructive upper: explicit symmetric 4x9 kernel

Group the nine ordered output pairs into six swap orbits in this order:

`11 | (13,31) | (14,41) | 33 | (34,43) | 44`.

An orbit mass is distributed equally across the two ordered outcomes when the orbit has size two. The input rows for `YY`, either of `YN/NY`, and `NN` are the following integer vectors divided by `D=1000000`:

```
YY     0       0       0       996872  3128   0
mixed  88614   435270  375797  521     91861  7937
NN     711899  154264  133837  0       0      0
```

Each row is nonnegative and sums to D. Using the same symmetric mixed row for YN and NY defines a lawful parameter-independent **random kernel for the auxiliary observer experiment**. The full law aggregated into the six output orbits is

`T(a,c)=(a^2,2az,2au,z^2,2zu,u^2)`;

the reconstructed orbit law is `Q(a,c)=(z^2,2z(1-z),(1-z)^2) K`. Full and reconstructed ordered-pair laws are swap invariant, so their nine-coordinate TV equals the six-coordinate TV between T and Q.

## Proof of the upper for every real parameter

Write `a=1/2+3s/8`, `c=1/2+3t/8`, with `(s,t) in [0,1]^2`. Each coordinate of signed error `E(s,t)=T(a,c)-Q(a,c)` is of degree at most 2 separately in s,t: both A(a,c) and B(a,c) are separately affine in a,c, and their two-trial squares are biquadratic.

Use the exact tensor Bernstein expansion

`E(s,t) = sum_{i,j=0}^2 B_i^2(s) B_j^2(t) E_ij`

where `B_0^2=(1-x)^2`, `B_1^2=2x(1-x)`, `B_2^2=x^2`. Its nine six-coordinate coefficient vectors are determined exactly by the function values on `{0,1/2,1}^2` using the interpolation matrix

```
M = [ 1       0        0   ]
    [-1/2     2       -1/2 ]
    [ 0       0        1   ].
```

The identity `sum_k E_k(s,t)=0` holds identically; uniqueness of Bernstein coefficients gives `sum_k E_ij,k=0` at each control point. The half-L1 seminorm of each coefficient is therefore `sum_k max(0,E_ij,k)`. On any rectangle, Bernstein basis weights are nonnegative and sum to one. By convexity, its entire continuous TV error is bounded by the largest of the nine local coefficient seminorms.

If a rectangle has a local bound exceeding `13500049/73500000`, subdivide it at both midpoints, using exact quadratic de Casteljau on every coordinate: from `(x0,x1,x2)` the left control triple is `(x0,(x0+x1)/2,(x0+2*x1+x2)/4)` and the right is `((x0+2*x1+x2)/4,(x1+x2)/2,x2)`. The four children exactly cover the parent.

The included `VERIFY.py` performs this finite branch-and-bound with Python `fractions.Fraction` only, verifying all row normalizations, exact fiber witness, each local coefficient zero sum, and every accepted rectangle's bound. It visits exactly **49 nodes**, accepts **37 leaves**, has **maximum depth 11**, and leaves no rectangle unresolved at cutoff 16. The largest accepted coefficient TV is `1577748772836239/8589934592000000`, strictly below the claimed upper. Hence the claimed upper holds for **all real** parameters in the full domain. This is a finite exact covering proof, not a sampling extrapolation.

## Evidence, relation to mother question and next test

The verifier is executable with Python 3 standard library only; `RUN_EVIDENCE.txt` preserves one actual execution. The kernel originated from exploratory finite linear programming but its universal guarantee is proved by the exact rational certificate independently of that numerical search.

The theorem concerns the auxiliary conditional-AV observer. It does not itself establish a lawful strategy mapping from the frozen six-source/ten-label S23 experiment to this observer, or determine the mother minimax `R_beh(k,10)`. Its exact value `delta2` remains to be determined within a gap `1/1500000`; independent mathematical review and project admission remain open.

BRC existing positive-mass observer/fiber and preservation of tagged source distinctions are **REUSE_APPLIED** at their precise scope. This is an exact local certificate, not a new general BRC toolbox family. Next: test exact attainability `delta2=9/49` by a rational universal kernel and global signed-event polynomial inequalities, or find an exact multi-hypothesis dual >`9/49`. Independently verify any transfer to original lawful encoder/decoder and quantifier order.
