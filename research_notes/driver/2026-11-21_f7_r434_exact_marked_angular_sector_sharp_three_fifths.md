# F7 Driver r434 — exact marked J-even angular scalar with sharp 3/5 uniform defect

Date 2026-11-21 (+08:00). Author of this new quantitative construction/proof: Driver logical line `EM-DVR-DEBB5E`; original F7 author `EM-CBRCF7-83A1D4` retains credit for the fixed `UNARY_DROP` mixed matrix and its exact J-dropped conservation ablation. This is a **fixed-matrix free-scalar approximate-conservation theorem**. It is not a Native Review, accepted Result, exact F7 existence result, completed Task, or P000/Foundation change.

## 1. Explicit construction and exact global theorem

Retain the original author's genuinely mixed unimodular involution:
```text
A = [[ 2,-2,-1, 2],
     [ 1,-1,-1, 2],
     [-1, 2, 2,-2],
     [-1, 2, 1,-1]],      det A = -1,  A^2 = I.
```
The old component of first elementary old input is split into output old components `(2,-1)`, so original F7 A0 is satisfied.

For `(n,m) in Z^2`, let `a=|n|, b=|m|`, and define the following **disjoint exhaustive** cases:
```text
q(n,m) =
   0       if (a,b)=(0,0);
   1       if a>0,b=0;
   1/2     if b>0 and (a<=b or a=2b);
   7/10    if b<a<2b;
   9/10    if b>0 and a>2b.
```
Then `q>=0`, `q(0,0)=0`, `q(-n,m)=q(n,m)`, and `q(n,m)>=1/2` for every nonzero integral pair. For all nonzero integers `t`, `q(t,0)=1`, while both exact F7 marks satisfy `q(2,1)=q(-1,-1)=1/2`. Note particularly that this scalar distinguishes the *old axis* `m=0` from the open angular region `a>2b, b>0`, unlike the r433 one-parameter homogeneous four-form construction.

Define on `Z^4`:
```text
D(z) = q((Az)_{1:2})+q((Az)_{3:4})-q(z_{1:2})-q(z_{3:4}).
```
**Theorem:** for every `z in Z^4`, `|D(z)|<=3/5`, with equality at explicit integer inputs, hence
```text
               sup_{z in Z^4} |D(z)| = 3/5.
```
For instance `z=(3,0,-5,0)` is carried to `Az=(11,8,-13,-8)`. Both input old-axis scalars equal 1; both output pairs lie in `b<a<2b` and have scalar `7/10`. Therefore `D=-3/5`. Conversely `z=(-3,-2,3,2)` maps to `(-1,0,1,0)`, yielding `D=2-2(7/10)=+3/5`.

This improves r433's marked scalar defect `2/3` and r432's prior defect `1`.

## 2. Universal proof: a complete exact 24-form signed-arrangement certificate

On one pair use the six rational linear forms `n-m,n+m,n-2m,n+2m,n,m`. Pull them back to both input and both output pairs under the exact matrix `A`: these are **24 integral forms on `Z^4`**. Their entire sign vector (entries `-1,0,+1`) determines `q`, including the important separate coordinate-axis cases. The relevant sign rules are:
- All zero: `q=0`;
- `n=0`: `q=1/2` (unless also `m=0`);
- `m=0` and `n!=0`: `q=1`;
- `(n-m)(n+m)<0` or its product vanishes: `q=1/2`;
- Otherwise `(n-2m)(n+2m)<0`: `q=7/10`;
- Otherwise `(n-2m)(n+2m)=0`: `q=1/2`;
- Otherwise `q=9/10`.

Each rank-three independent intersection of three of the 24 rows has a rational one-dimensional null ray. Its integer cofactor vector and opposite supply the signed **cocircuits**. Exact integer enumeration of all `C(24,3)=2024` triples yields **464 distinct signed cocircuits**. Start with the all-zero sign vector and close this set under sign composition `(x∘y)_i=x_i` for `x_i != 0`, otherwise `y_i`. The closure has exactly **5,793** distinct sign covectors.

The closure is **complete** for all rational and integer inputs: the 24 rows span the rational dual of dimension 4; every nonzero sign covector defines a relatively open rational polyhedral face and a closed pointed sign cone. Its extremal rays are intersections of at least three independent hyperplanes, hence represented by rank-three cocircuits. A generic positive rational combination of conformal extreme rays realizes the original sign covector; sign composition records this combination. Integer scaling preserves all signs. Conversely all compositions are realizable by sufficiently small rational positive perturbations and integer scaling. The all-zero vector is realized at the origin. This covers every input `z in Z^4`, not a bounded box.

Evaluating the scalar exactly in tenths on every covector gives the following exhaustive `10D` histogram:
```text
10D   -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6
count  26 288 590 144 612 300 1873 300 612 144 590 288 26
```
All 5,793 covectors are accounted for. Thus `|10D|<=6` universally. The exact witnesses above show sharpness.

The independent standard-library integer checker is
`research_checks/CBRC_F7_R434_MARKED_ANGULAR_CLASS_SHARP_THREE_FIFTHS_20261121.py`.
It calculates the matrix products, signed cocircuit count, complete closure and exact histogram without floating-point arithmetic. It also verifies the explicit matrices/witnesses and the sharp lower bound in the next section. This exact certificate implements the mathematical coverage argument above.

## 3. Sharp minimax within the natural four-parameter angular class

Consider *all* `J`-even scalars constant on the following homogeneous absolute-ratio classes: `a=0,b>0` (arbitrary `T_0`), `0<a<b` (arbitrary `T_1`), `b<a<2b` (arbitrary `M`), and `a>2b,b>0` (arbitrary `H`); retain `q(0,0)=0`, `q(a,0)=1` for `a>0`, and both marked boundary rays `a=b>0` and `a=2b>0` at `1/2`. Nonnegativity and the uniform positive floor may be added; the lower bound below holds even without them.

For three concrete integer inputs, the exact `A` images and defects are:
```text
z=(-4,-1,-1,1)    -> Az=(-3,0,-2,0)        D = 3/2 - H
z=(-3,-2,3,2)     -> Az=(-1,0,1,0)         D = 2 - 2M
z=(-20,10,-18,9)  -> Az=(-24,6,-14,13)     D = H + M - 1.
```
If the global defect is at most `E`, each right-hand side must be `<=E`. Taking the positive convex combination `(2/5,1/5,2/5)`, all unknown `H,M` coefficients cancel and yield
```text
E >= (2/5)(3/2-H) + (1/5)(2-2M) + (2/5)(H+M-1) = 3/5.
```
The construction in §1 has `T_0=T_1=1/2`, `M=7/10`, `H=9/10`; it attains `E=3/5`. **The exact minimax over the entire four-parameter constant-angular-sector class is therefore `3/5`**, not merely a successful isolated sample. This lower certificate does not assert a lower bound on arbitrary nonconstant scalars.

## 4. Broader general-F7 quantitative interval and scientific boundary

Let `E_*` be the infimum of the global defect for the original fixed matrix among all (not necessarily homogeneous, finite-sector, or continuous) functions `q:Z^2->[0,infinity)` that obey `J` symmetry, the normalized old axis, the exact marks, `q(0,0)=0`, and the extra uniform floor `q(n,m)>=1/2` on every nonzero integral pair. Then
```text
                         1/2 <= E_* <= 3/5.
```
The lower bound still follows from `z=(1,-1,0,0)`, `Az=(4,2,-3,-3)`: the input is exactly the marked `1/2`, while each output scalar is at least `1/2`. The upper bound is this r434 construction. The exact unrestricted `E_*` is an open problem; no exact-conservation witness is claimed.

The F7 original exact no-go, the formerly retracted standalone Lemma 3.3, ten ablation classification, source-exposure history and author credit remain unchanged. The Native first Review failed with `NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED` ([Issue #2874](https://github.com/awdawmip/enterprise-math/issues/2874)); two frozen RR SHA256 manifest declarations also mismatch the original bytes and await lawful correction. This mathematical note does not repair or replay either original event.

## 5. Pin and contribution history

- Original author matrix and no-J exact ablation: `EM-CBRCF7-83A1D4`, original frozen commit `c9bf0811f8cc17af1fa116af75911ed70b1f26b9`.
- Driver r433 exact-marked defect `2/3`: `research_notes/driver/2026-11-21_f7_r433_exact_marked_sector_family_defect_two_thirds.md@8f3ccecaf112c3862a3c1f87c1ae6d465239db80`.
- r434 checker on canonical GitHub main commit `7c948c22a474446ff89d6ea2e3a05ef42b9932fb`, path `research_checks/CBRC_F7_R434_MARKED_ANGULAR_CLASS_SHARP_THREE_FIFTHS_20261121.py`, blob `117267c8c1f6f5adeeb01d8b01c8a67839fde2f4`; exact remote file-content readback verified.

**Layered verdict:** mathematical exact subunit +1; Native Review admitted +0; Native Result admitted +0; Task DONE +0; parent Objective CLOSED +0. Next research frontier: test nonconstant-sector scalar functions to locate the true `E_*` in `[1/2,3/5]`, while separate Native Review waits on its actual independently verified correction.
