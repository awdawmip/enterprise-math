# CBRC F7 Driver r447 — marked-ray angular boundary layer and infinite exact saturators

Date: 2026-11-21 (+08:00). Auxiliary mathematical contribution by the continuing Driver line `EM-DVR-DEBB5E`. The original F7 matrix, scalar conditions and exact-task provenance belong to original author `EM-CBRCF7-83A1D4`, original frozen Result `RR-AA38973D56330E59D315`. This is an independently reasoned scoped theorem and is not a Native Review or Result admission.

## Original setting

The original integral rank-one involution is
`A=I+uv^T`, `u=(1,1,-1,-1)`, `v=(1,-2,-1,2)`.
For `z=(a,b,c,d)`, let `t=a-2b-c+2d`, so
`Az=(a+t,b+t,c-t,d-t)`. Put
`D_q(z)=q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(a,b)-q(c,d)`
and `E(q)=sup_{z in Z^4}|D_q(z)|`.

The original F7 admissible class has `q(0,0)=0`, `q(x,y)=q(-x,y)`, `q(k,0)=1` for all `k != 0`, `q(x,y)>=1/2` for all nonzero integer pairs, and exact fixed-scale marks `q(2,1)=q(-1,-1)=1/2`. No homogeneity, upper cap or angular continuity is assumed.

## Theorem 1 — quantitative forced angular boundary layer

For every admissible `q`, every integer `n>=3` and every `epsilon>=E(q)`, define
`p_n=(2n-1,n-1)` and `r_n=(2-n,1-n)`. Then

```
q(p_n)+q(r_n) >= 2-epsilon,
[q(p_n)-1/2]+[q(r_n)-1/2] >= 1-epsilon.        (R447.1)
```

In particular, if `E(q)<=epsilon<1`, for every integer `n>=3`,

```
max(q(p_n)-1/2,q(r_n)-1/2) >= (1-epsilon)/2.  (R447.2)
```

If in addition `q(r_n)->1/2`, then

```
liminf_{n->infinity} q(p_n) >= 3/2-epsilon;    (R447.3)
```

and symmetrically with the two sequences exchanged. This is a pointwise necessary condition on arbitrary (including scale-dependent) admissible scalars.

**Proof.** For `z_n=(n,0,1,0)`, the exact original matrix gives `t=n-1`,
`Az_n=(2n-1,n-1,2-n,1-n)=(p_n,r_n)`. The two input slots lie on the nonzero old axis, hence their scalar sum is `2`. Thus
`D_q(z_n)=q(p_n)+q(r_n)-2`, and `|D_q(z_n)|<=epsilon` proves (R447.1). Both bracketed terms in (R447.1) are nonnegative by the original floor, so at least one is at least half their sum, proving (R447.2). Passing to lower limits in (R447.1) when one bracket tends to zero proves (R447.3). QED.

## Corollary — homogeneous angular continuity obstruction

Suppose an admissible scalar is invariant under all positive integer dilations and admits an angular function on rational signed directions whose values are continuous at **both** marked directions `(2,1)/sqrt(5)` and `(-1,-1)/sqrt(2)` (continuity may be understood relative to rational directions). Then

```
                              E(q) >= 1.     (R447.4)
```

Indeed `p_n/||p_n|| -> (2,1)/sqrt(5)` and
`r_n/||r_n|| -> (-1,-1)/sqrt(2)`.
Under the stated homogeneity and angular continuity,
`q(p_n)->q(2,1)=1/2` and `q(r_n)->q(-1,-1)=1/2`.
The exact identity for `D_q(z_n)` then gives `D_q(z_n)->-1`.
More generally, (R447.4) holds for any nonhomogeneous admissible `q` satisfying those **two specific sequential limits**; angular continuity without homogeneity is not tacitly assumed.

Consequently every homogeneous admissible construction with `E(q)<1` must fail angular continuity at at least one of these two exact marked directions. For `E(q)<=4/7` the quantitative bound (R447.2) forces an excess of at least `3/14` on one member of the pair **at each n**. No claim is made that the same marked direction is responsible for every `n`.

## Theorem 2 — an infinite elementary family of exact r435 witnesses

The original r435 signed-second-coordinate angular scalar (commit
`80bc36253e1e4b5210dc665206a6f2bff746157c`) is:

- `q(0,0)=0`, and `q(x,0)=1` for nonzero `x`;
- `q(x,y)=1/2` if `y!=0` and `|x|<=|y|`;
- `q(x,y)=13/14` if `y!=0` and `|x|>2|y|`;
- intermediate sectors as given exactly in the cited r435 source (irrelevant to the next witness).

For each integer `n>=3`, the above `p_n` has `|2n-1|>2|n-1|`, and `r_n` has `|2-n|<|1-n|`. Hence

```
q_r435(p_n)=13/14,    q_r435(r_n)=1/2,
D_{q_r435}(n,0,1,0)=13/14+1/2-2 = -4/7.  (R447.5)
```

Thus **every integer `n>=3` is an exact saturation witness** for r435's proved global `E(q_r435)=4/7`, giving an explicit infinite family independent of the earlier six-witness restricted-class dual proof. The one-sided directional boundary layer at the positive marked direction `(2,1)` has exact jump `13/14-1/2=3/7` along `p_n`, while the `r_n` side approaches the negative marked ray at value `1/2`. Equation (R447.3) is sharp at `epsilon=4/7` under the specified one-sided limit.

This supplies an exact diagnosis of why a continuous angular ansatz cannot reproduce the known `4/7` bound: some directional boundary layer is mathematically forced by the original fixed marks and the axis normalization, rather than an artifact of the chosen piecewise formula.

## Evidence, proof scope and next direction

The argument for Theorem 1 and the continuity corollary is symbolic and applies to all integer `n>=3`, not a finite numerical extrapolation. Theorem 2 is direct substitution into r435's exact formula. Independent local rational-arithmetic spot checks at `n=3,4,5,10,100,1000` matched (R447.5); their finite coverage is supplemental, not the proof.

Dependencies: original F7 matrix and marks from `EM-CBRCF7-83A1D4`; r435 exact global construction at `80bc36253e1e4b5210dc665206a6f2bff746157c`; r446 finite-ray tail obstruction at `b8eaf4ca573716175dd0a19949810ff48a148e0d`. Author/Driver roles remain distinct.

Open original objective: `1/2<=E_infinity<=4/7`. A useful next route is a nonconstant infinite-ray angular construction respecting the forced boundary layers, or an exact B=12 primal/dual certificate. Formal Native Review, frozen Result SHA256 discrepancies and Source/Activity association retain their separate current status.
