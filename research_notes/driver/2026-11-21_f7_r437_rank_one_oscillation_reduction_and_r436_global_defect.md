# CBRC F7 Driver r437 — rank-one involution, exact oscillation reduction, and global defect of the r436 certificate

Date: 2026-11-21 (+08:00). New auxiliary theorem/proof by the continuing Driver line `EM-DVR-DEBB5E`. Original F7 Task, mixing matrix, frozen Result `RR-AA38973D56330E59D315` and original scientific author `EM-CBRCF7-83A1D4` remain attributed to their original source. This mathematical note is not a Native Review or a change to frozen evidence.

## Theorem 1: exact four-input to one-dimensional oscillation reduction

For the **original F7** integer matrix
```
A = [[ 2,-2,-1, 2],
     [ 1,-1,-1, 2],
     [-1, 2, 2,-2],
     [-1, 2, 1,-1]]
```
write `u=(1,1,-1,-1)^T` and `v=(1,-2,-1,2)^T`. Direct multiplication gives `A=I+uv^T`, `v^Tu=-2`, and hence `A^2=I`. Thus F7's selected mixing transformation is an **integral rank-one involution**.

The reduction below holds for **any** real-valued `q: Z² -> R`; nonnegativity, parity and marks are unnecessary for the identity itself. Define
```
f_a(t) = q(t+a,t)
F_{a,b}(w) = f_a(w-b) - f_b(w-a)
           = q(w+a-b,w-b) - q(w+b-a,w-a).
```
For input `z=(n,m,p,l)`, put `a=n-m`, `b=p-l`, `r=m+b`, `s=l+a`. The exact F7 defect
```
D_q(z) = q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)
         -q(n,m)-q(p,l)
```
satisfies
```
                         D_q(z) = F_{a,b}(s)-F_{a,b}(r).                (1)
```
Proof: write `t=v^Tz=a-b-m+l`. Since `Az=(n+t,m+t,p-t,l-t)`, the two output pairs evaluate to `f_a(l+a-b)` and `f_b(m-a+b)`, while the two inputs evaluate to `f_a(m)` and `f_b(l)`. Rearranging gives (1).

For fixed integers `a,b`, the original variables `m,l` are independent and arbitrary. Therefore, with extended-real interpretation if an oscillation is unbounded,
```
sup_{z in Z^4} |D_q(z)|
       = sup_{a,b in Z} [ sup_{w in Z} F_{a,b}(w) - inf_{w in Z} F_{a,b}(w) ].  (2)
```
Consequently a global uniform error bound `|D_q|<=epsilon` is **equivalent** to the one-dimensional oscillation bound `osc F_{a,b}<=epsilon` for every pair `a,b`.

## Exact finite-cube oracle

For integer `B>=0`, define `I_d=[max(-B,-B-d),min(B,B-d)]∩Z`; only `|d|<=2B` occurs. Let `R=I_a+b` and `S=I_b+a`. Then
```
max_{z in [-B,B]^4 ∩ Z^4} |D_q(z)|
 = max_{|a|,|b|<=2B} max(
       max_{s in S} F_{a,b}(s)-min_{r in R} F_{a,b}(r),
       max_{r in R} F_{a,b}(r)-min_{s in S} F_{a,b}(s)).                  (3)
```
This is exact because `m∈I_a` and `l∈I_b` vary independently. Evaluating only each interval's minima and maxima takes `O(B^3)` scalar evaluations, instead of enumerating `(2B+1)^4=O(B^4)` input tuples. Each `q` evaluation is taken as `O(1)`; table construction and exact integer arithmetic remain separately accounted for.

Using the **unchanged** canonical r436 `q40=40q` table and the independent formula (3), the exact integer results are:

| B | Full four-tuple inputs | Evaluations of F | max |40D| |
|---|---:|---:|---:|
| 8 | 83,521 | 19,074 | 20 |
| 9 | 130,321 | 26,714 | 40 |
| 12 | 390,625 | 61,250 | 40 |
| 20 | 2,825,761 | 272,322 | 40 |
| 32 | 17,850,625 | 1,090,050 | 40 |

The B=8 result independently agrees with the published exhaustive r436 checker. The B=9 result evaluates the **same fixed r436 candidate**, not a new minimax over all admissible functions.

## Theorem 2: the r436 fixed candidate has exact global defect 1

For the immutable r436 `q40` certificate, `q(0,0)=0` and `1/2<=q(x,y)<=1` at every nonzero input. We prove
```
                          sup_{z∈Z^4}|D_q(z)| = 1.                     (4)
```
If both `a` and `b` are nonzero, neither argument of the two `q` terms in `F_{a,b}(w)` can be the origin. Hence `-1/2<=F_{a,b}(w)<=1/2` for all `w`, so the oscillation is at most 1.

When `a=0,b≠0`, `F_{0,b}(w)=q(w-b,w-b)-q(w+b,w)`. Only `w=b` can make the first term zero, and there `F_{0,b}(b)=-q(2b,b)`. Everywhere else `F∈[-1/2,1/2]`. If `q(2b,b)=1/2`, the whole oscillation is at most 1. The r436 finite exception table `T[(|x|,signed y)]` has `q(2b,b)>1/2` only for **b=-4,-1,4**. For these three b the *complete* possible nonbaseline `w` set is
```
W_b = {0,b}
      ∪ {b+t : (|t|,t) is an exception in T}
      ∪ {t : (k,t) is an exception in T and |t+b|=k}.
```
Outside `W_b`, both terms are the baseline value `1/2`, so `F=0`. Exact integer evaluation gives:

| b | candidate w values | 40 min F | 40 max F | 40 oscillation |
|---|---:|---:|---:|---:|
| -4 | 27 | -21 | 0 | 21 |
| -1 | 21 | -21 | 0 | 21 |
| 4 | 29 | -25 | 0 | 25 |

Also `F_{a,0}=-F_{0,a}` pointwise, and `F_{0,0}=0`; therefore all pairs `a,b` satisfy `osc F_{a,b}<=1`. Equation (2) establishes the global upper bound.

For the exact integer witness `z=(-9,0,9,0)`, `Az=(-27,-18,27,18)`. Both output pairs use r436's default off-axis `q=1/2`, while both input pairs are nonzero old-axis points with `q=1`. Hence `D_q(z)=-1`, attaining (4).

## Consequence and scope

The r436 **finite B<=8** equality `E_B=1/2` remains fully valid; its *particular* 524-exception candidate ceases to be a half-defect certificate at B=9 and has global defect exactly 1. This gives a concrete tail counterexample against simply extending that candidate. It does **not** disprove existence of some different global half-defect function; the unrestricted marked minimax remains `1/2<=E_infinity<=4/7` by the separate r435 construction.

The new oscillation oracle (2)–(3) is a reusable exact reduction for future scale-dependent F7 candidate design and dual-obstruction search. No change is made to P000, the F7 author's Result or currently unresolved original Native Review and manifest integrity discrepancy.

Source of the unchanged r436 table and original B8 certificate:
`research_checks/CBRC_F7_R436_B8_FINITE_CUBE_HALF_CERT_20261121.py` @ `f62febc5777c2b78f3b5edf3528f7f540000c88a`.
