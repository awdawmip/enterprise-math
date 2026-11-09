# R5 — a nine-parameter physical / eight-dimensional statistical 14-edge Blackwell chamber

Date: 2026-11-09 (Asia/Shanghai). Proof status: **author-side exact algebra and locally executed SymPy Rational/Fraction certificate; independent review pending**.

This is a stronger continuation of this branch's explicit three-parameter theorem in `RESEARCH.md`. Frozen scientific inputs are inherited from PR #1845's immutable `VERIFY_2D.py` at commit `0fe08cc4c1a30b9c5e898eedb01f2e0ba7238c7f` (historical GLOBAL pin `a01383f825ef9d43b4b754254303298c64041568`, EM pin `86149263e38c22292c9def1e0f69092efa1be77e`). The current normative context is not treated as a frozen science pin.

## Statement and exact construction

Use the frozen seven likelihood ratios `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`, seven-dimensional physical flow coordinates `f=(g,a,b,u,v,w,z)`, frozen affine mass map `M(f)`, stopping-time map `T(f)=(T_P,T_Q)`, and the fixed 14-edge A support `SA` in the predecessor.

Set `lambda=1/4`, `delta=1/240`, `DX2=DX-K` with the exact predecessor observer-kernel lift, and define the *exact rational interior point*

```text
x* = (X0+3*X1)/4 + DX2/240,
y* = (Y0+3*Y1)/4 + DY/240,
E* = (A0+AH)/2 + D/240,   on the 14-entry support SA.
```

**Correction to notation:** the intended interpolation coefficient is `x*=(3*X0+X1)/4`, `y*=(3*Y0+Y1)/4`. In the formulas above, `(X0+3*X1)/4` and `(Y0+3*Y1)/4` are *not* the basepoint; use the corrected formulas here and the executable `VERIFY_9D.py`. The coupling formula `(A0+AH)/2` is correct.

Let `A` be the 26×28 rational homogeneous matrix acting on increments `(dx_7,dy_7,dE_{14})`, whose rows require:
* seven target-mass row sums `sum_j dE[i,j]=dM_i(y)`;
* seven source-mass column sums `sum_i dE[i,j]=dM_j(x)`;
* seven likelihood-ratio moment sums `sum_i r_i*dE[i,j]=r_j*dM_j(x)`;
* the source `dg=db`;
* the two target F-face identities `dz'=da'/10`, `dv'-dz'=9*db'/40`;
* equality of the two stopping-time increments.

The sparse support `SA` and every coefficient of `A` are constructed from the frozen exact maps in `VERIFY_9D.py`. Exact row reduction gives

```text
rank(A)=19, nullity(A)=9.
```

Let `v_0,...,v_8` be the nine rational nullspace basis columns computed in increasing free-column order by the exact SymPy matrix nullspace routine. For each real vector `t=(t_0,...,t_8)` satisfying

```text
|t_j| <= 1/100000  for all j=0,...,8,
```

define `(x(t),y(t),E(t))=(x*,y*,E*)+sum_j t_j*v_j`, with `E(t)` kept on the same 14 support positions.

**Theorem.** Every `t` in this entire closed 9-cube gives physically lawful FULL_HIST source flow `x(t)` with `g=b`, lawful seedless F-face LR target flow `y(t)`, identical P/Q stopping times, and a declaration-independent, strictly positive **14-edge** Blackwell transport `E(t)`. The family of physical source/target flow pairs `(x(t),y(t))` has affine dimension **nine**. The corresponding statistical observation image `(M(x),M(y),T_P,T_Q)` has affine dimension **eight**. All quantifiers range over real parameters in this box, including irrational parameters.

## Exact verification and proof

The frozen A-support basepoint has 14 strictly positive edge weights, the smallest `4897/832000`. Among the physical slack expressions, exactly the three defining face inequalities have zero at the basepoint (indices `4,23,25` in the joint 26-slack list); the nine directions preserve those identities exactly. Every other slack is strictly positive at the base.

For each strict physical slack and every edge weight, calculate its base value `s_0` and the sum of absolute rational directional derivatives `L=sum_j |ds/dt_j|`. The exact minimum of all `s_0/L` is

```text
1181037643981 / 2086671428467200  > 1/100000.
```

Consequently `s(t)>=s_0-(1/100000)*L>0` for every nonforced inequality and every edge weight. This single exact l¹ coefficient bound proves nonnegativity throughout the entire nine-dimensional real cube, without enumerating 512 vertices. All 26 affine homogeneous equations hold because `A v_j=0`, and they hold at the exact basepoint by the frozen certificate.

For the **physical-flow projection** from the nine basis columns to the 14 source/target coordinates, a selected 9×9 minor (rows `0,1,3,4,5,6,7,8,9`, zero-indexed) has determinant

```text
-83980800000 / 1111424393  != 0.
```

Thus the physical pair family has dimension nine.

For the **statistical observation projection**, take the 16-coordinate vector `(M(x)_0,...,M(x)_6,M(y)_0,...,M(y)_6,T_P,T_Q)`. Its nine-direction matrix has rank eight, and the selected 8×8 minor using observation rows `0,1,2,3,7,8,9,10` and nullspace columns `1,...,8` has determinant

```text
1/6 != 0.
```

The ninth independent physical direction lies in the kernel of the declared marginal/time observer; its exact physical difference is retained in the 9D representation. This is an observer-scope statement, consistent with the project's residual-fidelity distinction between hidden flow and statistical observation.

Reproduction: `python VERIFY_9D.py` with SymPy and Python standard-library `fractions.Fraction`. The executable exact matrix construction is the proof certificate and independently reports all three ranks, the `l¹` bound and both nonzero determinants. The code imports the immutable predecessor formulas from the adjacent checked-in directory; the parent PR #1845 must be present in the working tree.

## Implications and next unit

The fixed A-support 14-edge region now has a **9D physical open neighborhood** with an **8D statistical image**, strengthening both the former one-dimensional chart gluing and the 3D subbox. A further route is to characterize overlap with the distinct B-support region by solving a joint interface feasibility condition in the common 12-edge support, then attempt global finite-atlas coverage or construct a lawful 15-edge lower-bound witness. Separately, PR #1831's full R5 coverage author proof still requires independent audit.

These exact rational calculations are author-side mathematical evidence; no independent review, formal Task CLAIM, Result admission or protected Foundation modification is asserted.
