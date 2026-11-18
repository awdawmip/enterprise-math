# R284W — Exact common-kernel certificate beyond Hall deficiency for Port numerator degree

Date: 2026-11-19. Status: **AUTHOR_PROVED / LOCAL_EXACT_FRACTION_CHECK_PASSED / NOT_REVIEWED**.

Scientific input remains frozen at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Immediate mathematical source: R284V, `research_notes/portable_direct/R284V_OFFDIAGONAL_COFACTOR_HALL_CERTIFICATE_20261118.md` at immutable commit `851060e73f9915e78e463f738c1c144962752c49`. Also uses R281 relevance reduction, R284R finite product grids, R284S quadratic obstruction, R284T bordered-determinant comparison and R284U diagonal SCC criterion. This is **auxiliary named nonnegative-rational BRC Port linear algebra**, with no claimed native-X6 source or dynamic correspondence.

## 1. A rank certificate for a matching-present numerator

Let `V={0,...,n-1}`, `W(x,z)=W_0+x E_{uv}+sum_{j=1}^m z_j E_{u_jv_j}` with a fixed rational baseline and separately named rank-one edits. Write `M(x,z)=I-W(x,z)` and the ordered observation `F_ab=(M^-1)_{ab}=N_ab/D`, with `N_ab=(-1)^{a+b}det M[rows != b, cols != a]`, `D=det M`. The rational readout is interpreted wherever `D != 0`; the algebraic identities below are global polynomial identities.

If `u=b` or `v=a`, the `x` edit does not occur in `N_ab`. Otherwise let `R=V\{b,u}`, `C=V\{a,v}`, and define the `(n-2)x(n-2)` *complementary pencil*

`A(z)=M(0,z)[R,C]=A_0+sum_j z_j A_j`.

Here each `A_j` is either zero or one negative matrix unit. The cofactor expansion of R284V gives the precise sign
```
[x] N_ab(x,z) = (-1)^(a+b+r+c+1) det A(z),
```
where `r`, `c` are the zero-based positions of `u`, `v` in the original cofactor after deleting row `b`, column `a`.

**Theorem W1 (uniform fixed-kernel zero certificate).** If there is a nonzero rational column `q` satisfying `A_j q=0` for every `j=0,...,m`, or a nonzero rational row `p^T` satisfying `p^T A_j=0` for every `j=0,...,m`, then `[x]N_ab(x,z) == 0` as a polynomial in all other named edits `z`.

*Proof.* The same vector annihilates `A(z)` on the indicated side for all `z`. Consequently `det A(z)\equiv0`; the exact complementary-cofactor identity gives the coefficient assertion. The argument is valid over any characteristic-zero field. QED.

**Theorem W2 (single-unit-edit fast criterion).** Let `T_C` be the set of columns in `C` hit by at least one *other* named edit `(u_j,v_j)` with both endpoints surviving in `R,C`; define `U_C=C\T_C`. A common right kernel in W1 exists **if and only if**
```
rank_Q(A_0[:,U_C]) < |U_C|.
```
Likewise, if `T_R` is the set of surviving edited rows and `U_R=R\T_R`, a common left kernel exists **if and only if**
```
rank_Q(A_0[U_R,:]) < |U_R|.
```
Empty restricted-column/row sets do not provide nonzero witnesses.

*Proof.* For a nonzero single matrix unit `A_j=-e_{r_j}e_{c_j}^T`, its right kernel consists exactly of vectors with coordinate `q_{c_j}=0`. Intersecting these elementary kernels enforces `q` supported on `U_C`. The remaining equation is `A_0[:,U_C]q_{U_C}=0`, equivalent to deficient column rank. Transposition proves the left statement. QED.

The certificate needs one scan of named edges and rational rank elimination on a matrix of order at most `n-2` for each tested edit/output. It can also be checked from an **explicit nonzero vector** by exact matrix-vector products, bypassing determinant expansion and all tensor-grid observations. Arithmetic-operation cost is `O(m+n^3)` per local certificate with naive elimination; exact bit complexity additionally depends on coefficient bit heights and intermediate fractions. Both Hall deficiency (R284V) and fixed-kernel rank deficiency are independent *sufficient* routes; a matching-present matrix can still have a common kernel.

**Corollary W3 (paired observer degree drop).** Apply R281 observer relevance reduction separately in the two compared models and fix any matched scalar output. Suppose each reduced model containing edit `x` either excludes the edit from its cofactor or passes W1/W2. Then `N_h` is independent of `x` and each `D_h` is affine in `x`. Hence `P=N_1D_2-N_2D_1` is affine in `x` globally in the other edit variables. If this is certified for every declared output, replace the three-node `x` grid of R284R/R284T by two nodes, subject to the same joint-stability/precision hypotheses. An edit relevant in only one model retains the one-sided R284R degree handling.

## 2. Strict witness: perfect matching exists but both exact cofactor slopes vanish

Four named Ports `0,1,2,3`, ordered output `F_01=(I-W)^-1_{01}`, two declared additive edits `x:2->3` and `y:1->0`, and baseline
```
W_0(t,c) = [[0,t,t,0], [0,0,0,0], [0,0,0,0], [0,c,c,0]].
```
Set model 1 `(t_1,c_1)=(1/8,1/7)`, model 2 `(t_2,c_2)=(1/10,1/9)`. All nonzero weights are nonnegative. For `0<=x,y<=1/4` every row sum is strictly below one.

For `a=0,b=1,u=2,v=3` the complementary pencil, with rows `0,3` and columns `1,2`, is
```
A = [[-t,-t], [-c,-c]].
```
All four support positions are nonzero: the bipartite support graph **has a perfect matching**. Nevertheless `A (1,-1)^T=0`, and the other edit `y:1->0` is excluded from this pencil. W1/W2 therefore certify `[x]N_01\equiv0`, where R284V's pure Hall test is inconclusive.

Direct exact determinant expansion yields
```
N_1=1/8,       D_1=1-x/7-y/8,
N_2=1/10,      D_2=1-x/9-y/10,
P=N_1 D_2-N_2 D_1 = 1/40+x/2520.
```
The graph-only rule may initially allocate a three-node `x` coordinate; W1 reduces it to two. Both `x` and `y` are globally linear in the comparison polynomial after the certificates, allowing a `2x2=4` equality grid. The extra exact pair-specific identity `[y]P=0` allows a two-point grid in `x` alone.

### Negative control: break one of the twin columns

Change only model 2's baseline edge `0->2` from `t_2=1/10` to `1/8=t_2+delta`, where `delta=1/40`. Model 2's complementary matrix is `[[-1/10,-1/8],[-1/9,-1/9]]`, with determinant `-1/360`; the shared-kernel certificate now fails. Exact formulas are
```
N_2=1/10+x/360,
D_2=1-x/9-y/10-xy/360,
P=1/40-x/420+x^2/2520.
```
The nonzero `x^2` coefficient `1/2520` is a real two-model quadratic obstruction. Thus the W1 certificate makes a distinguishing, falsifiable prediction on a nearby stable nonnegative example.

## 3. Exact checks and their limits

Executed the accompanying Python standard-library `Fraction` checker and persisted machine-readable JSON results. **PASS** for both four-Port pairs at all nine `(x,y)` values from `{0,1/8,1/4}^2`, independently computing the 4x4 determinants and 3x3 observer cofactors: **36 exact per-model cofactor/determinant node checks** across the two pairs. Stable denominators verified at every node; formulas above checked exactly.

A deterministic seeded finite test (seed 28423) examined **480 randomly generated** instances with `n=4,5,6`, two other named edits, nonnegative small rational baselines and fixed rational evaluations. The implemented W2 criterion held in **199** instances. For those, **796** exact comparisons of `N_ab` at `x=0` and `x=1/16` over all four `z\in\{0,1/16\}^2` agreed. **3** of these certified cases had an existing perfect matching, independently confirming Hall-present rank certificates in the finite test. These samples corroborate the theorem; the algebraic proof establishes the universal implication.

Files: `R284W_common_kernel_certificate.py` and `R284W_common_kernel_verification.json` in this same `research_notes/portable_direct/` directory. Reproduce with `python research_notes/portable_direct/R284W_common_kernel_certificate.py`. No native X6 computation or independent mathematical review performed.

## 4. Next independently useful question

Find *variable-dependent* rational polynomial kernel certificates for complementary pencils which are singular for all edits yet admit no constant left/right common annihilator; test attainable cases within the nonnegative stable BRC Port constraint. Separate truly structural matching deficits, baseline-induced exact cancellations and paired-model cross-polynomial cancellations. For an eventual algorithmic speed claim, benchmark graph matching, rational rank checks, coefficient height and reduced-grid exact evaluations on the same specified family.
