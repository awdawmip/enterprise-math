# F7 Driver r432 — exact marked J-even mixed-GL4 scalar with globally sharp defect one

Date: 2026-11-21 (+08:00). Driver logical research line `EM-DVR-DEBB5E`. Original F7 author `EM-CBRCF7-83A1D4` credited for the `UNARY_DROP` matrix and J-dropped exact-conservation ablation. This construction is a **quantitative approximate-conservation example**, not an exact F7 existence witness or a Native Review/Result.

## Purpose and pinned prior result

r430/r431 showed that the exact scalar marks `q(1,0)=1`, `q(2,1)=q(-1,-1)=1/2` cannot be met by J-even *nonnegative homogeneous hyperplane-mask mixtures*. r429 constructed a J-even four-mask scalar `qJ` for the original author's mixed `GL_4(Z)` involution, with exact global defect `3/4`, but it assigns value `3/4` instead of `1/2` at both marks. Here a finite-orbit, arithmetic correction leaves the mask class and **meets the marks exactly**.

## Explicit scalar and matrix

Let `I(P)=1` if `P` is true and 0 otherwise. On integer pairs set
```
qJ(n,m) = [I(n-m!=0)+I(n+m!=0)+I(n-2m!=0)+I(n+2m!=0)]/4.
M = { (n,m) in Z^2 : |n| in {1,2} and |m|=1 }.
qF(n,m) = qJ(n,m) - (1/4) I((n,m) in M).
```
Use the **original F7 author's** matrix, whose determinant is -1:
```
A = [[ 2,-2,-1, 2],
     [ 1,-1,-1, 2],
     [-1, 2, 2,-2],
     [-1, 2, 1,-1]].
```
The r429 source proves the exact universal bound
`sup_z |qJ((Az)_{1:2})+qJ((Az)_{3:4})-qJ(z_{1:2})-qJ(z_{3:4})| = 3/4`
by complete rational hyperplane-arrangement enumeration, including the reason for finite coverage. This proof reuses that **exactly scoped established result**, rather than treating a bounded test as a universal proof.

## Theorem: marked positivity and exact all-input defect

For every integral pair `(n,m)`, `qF(n,m)>=0` and `qF(0,0)=0`. It is J-even under `(n,m)->(-n,m)` and centrally even. For all nonzero integer `t`, `qF(t,0)=1`. In fact for every nonzero integer pair `(n,m)`, `qF(n,m)>=1/2`.

The exact F7 marked values are
```
qF(1,0)=1,    qF(2,1)=qF(-1,-1)=1/2.
```
The global two-slot `A` defect satisfies the **universal equality**
```
sup_{z in Z^4} |D_F(z)| = 1,
D_F(z) = qF((Az)_1,(Az)_2)+qF((Az)_3,(Az)_4)
        - qF(z_1,z_2)-qF(z_3,z_4).
```

### Proof

A nonzero pair makes at most one of the four distinct homogeneous forms defining `qJ` vanish; thus `qJ>=3/4` off the origin and `qJ<=1` everywhere. Every point of `M` lies on exactly one of the four lines, so `qJ=3/4` on `M`; subtracting `1/4` there gives `qF=1/2`, while elsewhere `qF=qJ`. The set `M` is stable under both J and central negation. Since `m=0` excludes `M` and all four forms are nonzero when `n=t!=0`, the old-axis normalization holds. The stated two marks belong to `M`.

Write `D_J` for the r429 baseline defect. Let `k` count how many of the two **input** pairs of `z` belong to `M`, and `l` how many of the two **output** pairs of `Az` belong to `M`; then `k,l in {0,1,2}` and
```
                        D_F = D_J + (k-l)/4.                (*)
```
If `|k-l|<=1`, the universal `|D_J|<=3/4` yields `|D_F|<=1`. If `k-l=2`, both input pairs lie in `M`, so their original `qJ`-sum is `3/2`; the output sum is at most `2`. Hence `D_J<=1/2` and `D_F=D_J+1/2<=1`, while the r429 lower bound gives `D_F>=-1/4`. If `k-l=-2`, both output pairs lie in `M`, so the original output sum is `3/2`, and input sum at most `2`; hence `D_J>=-1/2`, giving `D_F=D_J-1/2>=-1`, while its upper bound is at most `1/4`. These three cases are exhaustive, proving `|D_F|<=1` for every integer `z`.

Equality is attained at `z=(-6,-3,4,4)`: exact multiplication gives `Az=(-2,1,0,0)`. The two input scalar values are `qF(-6,-3)=3/4`, `qF(4,4)=3/4`, while the nonzero output pair has `qF(-2,1)=1/2` and the zero output contributes zero. Thus `D_F(z)=1/2-3/4-3/4=-1`, proving the exact global supremum. QED.

## Exact arithmetic regression and scientific boundary

A separate exact-integer regression of `13^4=28,561` inputs `z in [-6,6]^4` returned `max |4D_F|=4` and the above witness (among others). This test is additional evidence only: the universal bound follows from the r429 complete exact certificate and equation (*), with an analytic extreme-count argument.

This is a constructive **positive** result for the full marked, J-even, uniformly positive scalar conditions under a genuinely mixed unimodular F7 author's matrix, at global defect `epsilon=1`. Exact energy conservation `epsilon=0` is not achieved, so the original F7 exact no-go and selector classification are unchanged. It shows the r430/r431 obstruction is caused by the nonnegative *homogeneous mask representation*, rather than by the marked scalar conditions themselves.

## Sources and layered outcome

- Author's actual `UNARY_DROP` and revision checker: `research_checks/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_CHECK_20260903.py@c9bf0811f8cc17af1fa116af75911ed70b1f26b9`.
- Driver r429 universal baseline: `research_notes/driver/2026-11-21_f7_J_symmetrized_GL4_exact_three_quarter_defect_r429.md@d1be8fbdecbc758e9cd61f35dbb06d58cd79e041`.
- Driver mask obstruction r430 @`884c4c764ad101764dc471da554f809f812db86a`; rigidity r431 @`47f601ceb21a4221d376c83a4f3d8c0dc4a3287f`.
- The frozen F7 Result's two SHA256 manifest errors and the terminal original first-review budget failure (Issue #2874) remain separate and unchanged.

Scoped construction/proof subunit +1; Native Review admitted 0; Native Result admitted 0; formal Task completed 0; parent Objective closed 0. Next mathematical question: for the original marked, positive J-even scalar class with mixed A, is `epsilon=1` optimal for this A, or can a non-mask construction improve it?
