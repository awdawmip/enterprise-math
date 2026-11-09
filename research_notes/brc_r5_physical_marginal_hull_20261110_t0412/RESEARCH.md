# R5 — Exact eight-dimensional physical marginal hull and generic 13-edge lower bound

Date: 2026-11-10 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING.

## Frozen inputs and scope

Continue R5 PR #1894 (`b4d0594d3f9705dbe403b607741871ec9ff97842`) and PR #1905 (`252a5e5689157fec254c72a2673e833c7a62fe65`) without changing their frozen scientific pins: account `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. The seven likelihood-ratio statistical labels are an auxiliary P/Q-BRC observation carrier, not P000 spatial dimensions. Native X6/time, P000, and protected worldview are untouched.

Set the ordered likelihood ratios `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. The *frozen* affine physical mass map `M(g,a,b,u,v,w,z)` and two stopping-time functionals `T1,T2` are copied exactly into `VERIFY.py`, originally read from PR #1894. Let `X` be a FULL_HIST source and `Y` a seedless-F target. Write `nu=M(X)`, `mu=M(Y)`. The selected physical equalities are

```text
X_g = X_b
Y_g = 1
Y_z = Y_a / 10
T1(X) = T1(Y)
T2(X) = T2(Y).
```

They define an affine subset `P` of the 14 physical-flow coordinates `(X,Y)`. Capacity inequalities are the 13 frozen slacks for each side. Transport feasibility uses the 21 Blackwell equations `sum_j E_ij=mu_i`, `sum_i E_ij=nu_j`, and `sum_i r_i E_ij=r_j nu_j`, with all `E_ij>=0`.

## Theorem A: exact rank eight, not nine

The equality matrix for `P` has exact rank 5, so `dim P=14-5=9`. The linear marginal observer `(X,Y) -> (mu,nu)`, restricted to the nine-dimensional physical tangent space, has exact rank **8**, and its kernel is one-dimensional.

Pure rational row reduction in `VERIFY.py` produces an explicit nonzero 8-by-8 minor of the restricted 14-by-9 marginal matrix, in the standard RREF free-variable basis:

```text
free physical variables = (Xu,Xv,Xw,Xz,Yb,Yu,Yv,Yw,Yz)
minor rows (0-based, mu then nu) = (0,1,2,3,4,7,8,9)
minor columns (0-based free-variable list) = (0,1,2,4,5,6,7,8)
determinant = -19799371/47239200.
```

For the matching upper rank bound, the full 14-dimensional marginal coordinates satisfy these **six independent affine relations**: `sum(mu)=1`, `sum(nu)=1`, `sum_i r_i(mu_i-nu_i)=0`, `nu_4=0`, together with the two physical-family-specific relations

```text
36 mu_0+28 mu_1+23 mu_2+18 mu_3+13 mu_4+8 mu_5 = 18;
-36 mu_0-36 mu_1-31 mu_2-18 mu_3-5 mu_4
    +36 nu_0+36 nu_1+31 nu_2+18 nu_3 = 0.
```

The exact rational rank of the six row functionals is 6; both additional affine identities hold for every point of `P` by the frozen mass/time formulas. Thus their common affine solution set has dimension 8 and is *exactly* the affine hull of the physical marginal image.

The unique invisible physical tangent direction, written as an integral primitive vector with source coordinates first and target coordinates last, is

```text
(-98800,-98800,-98800,-33345,264290,-33345,591026;
 0,0,0,0,0,0,0).
```

It preserves all five physical equalities and both complete 7-component statistical marginals. In BRC observer terms this is a precisely typed one-dimensional physical fiber residual: physical source-flow configurations can change along this direction without changing the declared seven-node statistical observation. The vector describes a local flow coordinate change within the capacity-positive neighborhood, not a new axis.

## Theorem B: a nonempty relatively open physical Blackwell chamber

The exact rational physical pair from PR #1894 (reproduced in `VERIFY.py`) satisfies the five equalities, all remaining source/target capacity inequalities strictly, `nu_4=0`, and four strict deficits `nu_j>mu_j` for `j=1,2,3,5`. The independent reproduction builds a 30-edge strictly positive rational Blackwell coupling `E0` with `min(E0)=1/10000000`; every one of the 21 equations is checked.

The six independent observable relations prove the image of the relative nine-dimensional physical neighborhood contains an open eight-dimensional set. All nonmandatory physical slacks and all four deficits remain strict for sufficiently small perturbations. Since the frozen full 30-edge Blackwell column matrix has rank 15 and `E0` is strictly positive, any sufficiently small compatible perturbation of its target vector remains realized by a positive perturbation of its coupling (choose a linear right inverse on the rank-15 column space). Therefore **a nonempty eight-dimensional relatively open neighborhood of legal matched-time `g=b` physical pairs is Blackwell feasible and lies in `nu_j>mu_j` for all four internal columns**.

## Theorem C: almost every physical marginal in that chamber needs at least 13 positive edges

For a realization with support `S` of size `k`, each column `j=1,2,3,5` must use an off-diagonal edge; otherwise `mu_j>=nu_j`, contrary to its strict deficit. The four columnwise martingale-defect rows `sum_i(r_i-r_j)E_ij=0` are therefore nonzero and mutually independent, because their variable supports are disjoint. Their zero set in the `k` edge weights has dimension `k-4`; normalization of total mass to 1 cuts a further independent dimension, leaving **at most `k-5` affine degrees of freedom** in the marginal image.

For `k<=12`, every such support contributes an image of dimension at most 7. There are finitely many subsets of the 30 allowed edges, so their union has zero eight-dimensional measure in the physical affine hull from Theorem A. Thus, **almost every feasible physical marginal in the open chamber of Theorem B requires at least 13 positive Blackwell edges**. The current global 15-edge vertex bound from PR #1894 remains available: the possible generic physical minima here are 13, 14, or 15. This is a generic measure-theoretic lower bound, not yet a certificate that PR #1894's particular rational physical pair requires 15.

## Reproduction and next discriminating question

Run `python3 VERIFY.py`. It uses only Python standard-library `Fraction`, checks the five physical equations, Jacobian ranks, exact 8-minor, six independent invariants, explicit source kernel, positive capacities, all 21 Blackwell equations, the 30-edge witness, and strict deficits. `EXACT_OUTPUT.txt` stores the actual executed stdout.

New question: classify **which 13- and 14-column spans contain the exact 8D physical affine hull**, then test the nonnegative regions of those charts. An 8D-open positive 13- or 14-edge chart would give an improved construction; a complete exact exclusion of all such charts would promote the generic physical lower bound accordingly. An exact rational certificate for the original PR #1894 point remains a separate promising unit.

No R5 formal Owner/CLAIM, independent review, or mathematical promotion is asserted by this author-side proof. The source notes are durable research evidence; native activity/checkpoint linkage is reported separately using the actual service receipt.
