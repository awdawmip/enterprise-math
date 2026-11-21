# CBRC F7 Driver r435 — signed second-coordinate angular scalar: exact global defect 4/7 and class-sharpness

Date: 2026-11-21 (+08:00). New restricted-model author/proof contributor: Driver logical line `EM-DVR-DEBB5E`. Original F7 author `EM-CBRCF7-83A1D4` retains attribution for the exact `UNARY_DROP` matrix, F7 definitions, and the original no-J ablation. This note is an independently derived **mathematical construction and restricted-class minimax proof**; it is not a Native Review or an accepted frozen Result.

## 1. Original matrix and statement

Use the original F7 `GL_4(Z)` involution
```
A = [[ 2,-2,-1, 2],
     [ 1,-1,-1, 2],
     [-1, 2, 2,-2],
     [-1, 2, 1,-1]],    det(A)=-1, A^2=I.
```
Its old projection splits the first old basis input into nonzero components `(2,-1)`, meeting F7 A0. For `z=(n,m,p,l)`, define
```
D(z) = q((Az)[0],(Az)[1]) + q((Az)[2],(Az)[3])
       - q(n,m) - q(p,l).
```
Let `a=|n|`, `b=|m|`. Define the following *new*, direction-sensitive scalar on **all** integer pairs:
```
q(n,m) =
  0                  if a=b=0
  1                  if b=0 and a>0
  1/2                if b>0 and a<=b
  9/14               if m>0 and b<a<2b
  11/14              if m<0 and b<a<2b
  1/2                if m>0 and a=2b
  4/7                if m<0 and a=2b
  13/14              if b>0 and a>2b
```
This is exhaustive and disjoint. It is J-even under `(n,m)->(-n,m)`, nonnegative, `q(0,0)=0`, `q(t,0)=1` for every nonzero integer `t`, and has `q(n,m)>=1/2` on every nonzero pair. It fulfills **both original exact marks** `q(2,1)=q(-1,-1)=1/2`. The scalar need not be even in the *second* coordinate; that extra assumption was imposed in r434's narrower construction, not by the F7 `J` symmetry.

**Theorem (all integer inputs).**
```
                 sup_{z in Z^4} |D(z)| = 4/7.
```
This improves the r434 construction `3/5` while preserving the fixed A, A0, J-evenness, exact marks and uniform nonzero floor. The general infimum `E_*`, allowing arbitrary scalar variation within the same stated constraints, is therefore bounded by
```
                          1/2 <= E_* <= 4/7.
```
The lower `1/2` is the existing r434 witness `z=(1,-1,0,0)`: `Az=(4,2,-3,-3)`; input scalar `1/2` and both nonzero output scalars at least `1/2`.

## 2. Exact universal upper bound and attainability

On one pair `(x,y)`, use the six rational forms `x-y,x+y,x-2y,x+2y,x,y`. Evaluate these on each of the two input and two output slots through A. The resulting **24 integer linear forms on Z^4** determine the sign of `m`, both angular thresholds, coordinate axes, the zero pair, and hence all four scalar values and `D(z)` exactly.

An all-integer rational central-arrangement certificate constructs every rank-three cocircuit from every independent three-form intersection (using 3x3 cofactors), adds both signs, and closes under the standard conformal sign composition. Counts:
- **464 distinct signed cocircuits**.
- **5,793 sign covectors**, including the all-zero one.
- For the integer-valued `14D`, the complete histogram:
```
14D   -8  -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7   8
count  34 248 526 150 270 148 336 398 1573 398 336 148 270 150 526 248  34
```

**Why finite enumeration proves a universal result:** the 24 rational forms span the four-dimensional dual space. Every nonzero relatively open rational sign cell has a pointed closed cone whose extreme rays lie in rank-three form intersections. Conformal combinations of these rays realize its sign covector; sign composition reconstructs such combinations, and sufficiently small rational perturbations make each composition realizable. Positive integer scaling does not change the signs. Conversely, every integer input has exactly one of these sign covectors. Thus the enumeration is exhaustive for all Z^4, not an arbitrary finite input box. Its histogram proves `|14D|<=8`.

Both endpoints are attained; for instance, the six explicit exact witnesses in §3 have signed `14D=+8` after orientation, and therefore give `|D|=8/14=4/7`.

The standalone standard-library pure-integer checker (no floating point, no additional axiom, no Lean/sorry) is fixed at:
`research_checks/CBRC_F7_R435_SIGNED_SECOND_COORDINATE_EXACT_FOUR_SEVENTHS_20261121.py`
on commit `514cad975427930cd7392c69aab7325f408da6b3`, Git blob `8f3977648b17a8fc45ef07b6df4bf0deb4aae161`.
It checks the arrangement closure, exact histogram, marks, and all six integer witnesses; local execution returned the counts above.

## 3. Six-witness analytic lower certificate: 4/7 is sharp *in this angular class*

Consider **any** scalar `q` constant on each sign-of-`m`, absolute-ratio sector
`a=0`, `0<a<b`, `a=b`, `b<a<2b`, `a=2b`, `a>2b`, with separately fixed `b=0` and origin. Enforce `q(t,0)=1`, `q(0,0)=0`, exact marks `q(2,1)=q(-1,-1)=1/2`, and J-evenness. No sign-of-`m` parity condition is imposed.

Write `H_±` for the values in `a>2b` with `m>0` / `m<0`; `M_±` for `b<a<2b`; `R_{2,±}` for `a=2b`, and `R_{1,-}` for `a=b,m<0`. The two exact marks set `R_{2,+}=R_{1,-}=1/2`.

For the indicated six integer inputs, direct substitution into the original matrix yields the following six inequalities whenever `E=sup|D|` is finite. The sign column determines whether `D` or `-D` is being bounded:
| `z` | signed defect lower expression `<= E` | weight numerator |
|---|---|---:|
| `(-46,17,-36,24)` | `-D=H_+ + M_+ - 2 R_{2,+}` | 1 |
| `(1,-1,4,1)` | `D=2 - R_{1,-} - H_+` | 1 |
| `(-3,-2,3,2)` | `D=2 - M_- - M_+` | 1 |
| `(0,0,-1,1)` | `D=R_{2,-}` | 2 |
| `(46,-17,36,-24)` | `-D=H_- + M_- - 2R_{2,-}` | 1 |
| `(-5,-1,-2,1)` | `D=2 - H_- - R_{2,+}` | 1 |

Summing with weights `(1,1,1,2,1,1)` cancels all unconstrained sector variables and produces
```
7E >= 6 - R_{1,-} - 3 R_{2,+}
   = 6 - 1/2 - 3/2 = 4,
```
hence **`E>=4/7` for the entire twelve-variable sign-sensitive angular-sector class**. The construction in §1 attains equality. The class theorem has a finite transparent lower certificate independent of the upper-bound enumeration.

Crucially, `D(0,0,-1,1)=R_{2,-}` cancels the two `a=b,m>0` values *because they are on the same homogeneous ray*. This cancellation is not licensed for arbitrary scale-dependent scalars; the unrestricted `E_*` therefore remains open.

## 4. Provenance and formal-state boundaries

- Matrix, original A0/F7 target and no-J ablation: original contributor `EM-CBRCF7-83A1D4`, frozen author commit `c9bf0811f8cc17af1fa116af75911ed70b1f26b9`.
- Prior Driver results: r432 defect 1; r433 defect 2/3; r434 sign-of-m-even class-sharp defect 3/5, fixed proof `292e6048e6ad06ae524d98214e47635d5ab53704`.
- This r435 is an **auxiliary fixed-matrix quantitative approximate-conservation theorem**. It neither supplies exact F7 conservation nor alters the original author's exact no-go result or retracted historical Lemma 3.3.
- Original Native first F7 review remains terminal `FAILED/NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED` ([Issue #2874](https://github.com/awdawmip/enterprise-math/issues/2874)); independent frozen Result manifest SHA256 divergence remains open. Do not replay this write, invent a review receipt or infer Task/parent completion.
- Local math checker executed exactly and Source GitHub file was independently read back at the fixed commit. Native Review admitted +0; Native Result admitted +0; formal Task DONE +0; parent Objective CLOSED +0.

**Next scientifically distinguishing question:** Can scale-dependent (not homogeneous) signed-angular corrections improve the `4/7` bound toward the universal `1/2` floor, or can a finite exact witness combination provide a stronger unrestricted lower bound?