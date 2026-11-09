# R5 — Generic physical 15-edge necessity, with an explicit lawful witness

Date: 2026-11-10 (Asia/Shanghai). Research status: AUTHOR_DERIVATION / EXACT_INTEGER_ENUMERATION_EXECUTED / INDEPENDENT_REVIEW_PENDING.

## Frozen inputs and question

Continue the exact seven-likelihood-ratio P/Q–BRC observation model in R5 PRs [#1894](https://github.com/awdawmip/enterprise-math/pull/1894), [#1905](https://github.com/awdawmip/enterprise-math/pull/1905) and [#1913](https://github.com/awdawmip/enterprise-math/pull/1913). Preserve scientific pins GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and EM `86149263e38c22292c9def1e0f69092efa1be77e`. This is an auxiliary statistical observer; P000 native X6/heartbeat ontology is not changed.

Let `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)` and the allowed support be the 30 edges

`D={(0,0),(6,6)} ∪ {(i,j): 0<=i<=6, j∈{1,2,3,5}}`.

A nonnegative matrix `E` obeys `sum_j E_ij=mu_i`, `sum_i E_ij=nu_j`, and `sum_i r_i E_ij=r_j nu_j`, totaling 21 affine Blackwell equations. Denote by `C` the resulting 21×30 rational column matrix and by `b=(mu,nu,(r_j nu_j)_j)` their right side. These equations, rather than a bare graph-flow model, are the support definition.

The physical source `X` has `X_g=X_b`; the seedless-F target `Y` satisfies `Y_g=1, Y_z=Y_a/10`; the two stopping times satisfy `T1(X)=T1(Y)`, `T2(X)=T2(Y)`. Use the frozen physical affine mass map and time functionals exactly as in PR #1913 `VERIFY.py`. The resulting physical equality space has 9 dimensions, and its marginal observer affine hull has 8 dimensions (PR #1913's exact rank-8 certificate).

**New results.** (i) The **original exact rational**, lawful, matched-time `g=b` physical point `p0` from PR #1894/#1913 itself has minimum positive transport support **exactly 15**. (ii) A nonempty relatively open eight-dimensional lawful physical Blackwell-feasible marginal chamber has minimum support 15 almost everywhere. Both results refute the proposed universal <=14-edge bound for the frozen real-valued physical family; the rational witness makes the counterexample fully finite and explicit.

## Certificate reduction: six-dimensional quotient

Choose the strictly feasible rational physical pair `p0=(X,Y)` from PR #1913 (listed explicitly below), with `b0=b(p0)`. Let `Jc` be the 5×14 Jacobian of the five physical equalities and `N=(n0,...,n8)` its rational RREF free-variable nullspace basis. In order, free variables are `(Xu,Xv,Xw,Xz,Yb,Yu,Yv,Yw,Yz)`. Let `Jb` be the 21×14 Jacobian of the Blackwell right side. Define the eight rational physical directions `P=(n0,n1,n2,n4,n5,n6,n7,n8)`. The prior 8×8 nonzero minor `-19799371/47239200` verifies that `Jb P` has rank 8. Hence

`W=span_Q{ b0, Jb n0, Jb n1, Jb n2, Jb n4, Jb n5, Jb n6, Jb n7, Jb n8 }`

is a **nine-dimensional rational linear space**, containing the affine eight-dimensional physical right-side hull.

The 30-column `C` has rank 15. Use the fifteen independent columns from PR #1913

`SB=((0,0),(0,1),(2,1),(0,2),(2,2),(4,2),(0,3),(1,3),(3,3),(4,3),(5,3),(4,5),(5,5),(6,5),(6,6))`

and the fifteen pivot rows `PIV=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)`. Their 15×15 determinant is `-299/1600`. Transform the 21-vector columns into 15 basis coordinates using this invertible submatrix. Taking the exact left nullspace of transformed `W` gives a six-dimensional quotient map

`Q: span_Q(C) → Q^6`, with `ker Q=W`.

The integer-scaled images of the 30 columns, in the standard ordering `D`, are recorded in `QUOTIENT_MATRIX.txt` (six rows, thirty columns). Every matrix entry is a small integer; the underlying rational derivation is reproduced by `VERIFY_PHYSICAL.py`. Thus the finite flat enumeration below is an **exact integer computation**, not floating-point rank inference.

For any edge set `S` with `|S|<=14`, if its linear span contains `W`, then

`rank(Q(C_S))=rank(C_S)-9<=5.`

Every subset with quotient rank at most 5 lies in a quotient hyperplane spanned by five independent projected columns, because the entire quotient has rank 6. Enumerating the `binom(30,5)=142506` five-subsets therefore checks all possibilities. `VERIFY_FLATS.cpp` uses signed 128-bit integer intermediates, exact 5×5 cofactors, primitive integer normal vectors and exact zero dot products.

Executed flat counts:

```text
all five-subsets 142506; quotient-rank-five five-subsets 67728
distinct rank-five flats 2986
support-size histogram:
7:1944, 8:372, 9:24, 10:264, 11:192, 12:147, 13:36,
14:3, 24:4.
```

**Only seven quotient hyperplanes contain at least fourteen projected columns.** Four have exactly 24 columns; three have exactly 14. Their complete index sets and primitive normals are in `EXACT_OUTPUT.txt`.

The four 24-column flats each omit every off-diagonal edge from one of the four internal source columns `j∈{1,2,3,5}`. Whenever `nu_j>mu_j`, that column must have a positive off-diagonal edge (otherwise its diagonal mass alone forces `mu_j>=nu_j`). Thus no valid transport in the open strict-deficit chamber can have its support entirely in any of those four flats.

For the other three 14-column flats, exact rational ranks are

```text
(rank(C_F), rank(Q(C_F)), dim(span(C_F)∩W))
(13, 5, 8), (12, 5, 7), (12, 5, 7).
```

Each intersection dimension is strictly less than 9, so **none** of these flats has `W` in its column span.

Consequently, for every support `S` with at most 14 positive edges that could realize a point with the four strict deficits, the affine physical hull `b0+Jb P·R^8` is not contained in `span(C_S)`. Its intersection with that span is a **proper rational affine subspace** of physical marginal dimension at most 7. Since there are finitely many supports, the union of their images is 8D measure zero.

For every feasible point the full Blackwell matrix has a vertex coupling using at most `rank C=15` edges (compact nonnegative fiber). At the strictly feasible `p0` of PR #1913, all 30 edge weights are positive, so a relatively open physical eight-dimensional neighborhood is Blackwell feasible. The four strict deficits hold throughout a smaller such neighborhood. Therefore **the exact generic minimum is 15 throughout this neighborhood outside a finite union of proper affine subspaces**.

## Explicit lawful 15-needed physical pair (rational and transcendental versions)

Set `H=17774559/17507527960` and the rational seven-component inputs

```text
X0=(999/1000, 1/6, 999/1000, 1/20, 29/240, 11/160, 1/120)
Y0=(1, 2002911/10904720, 26095487/40892700,
    442758619/6542832000, 11037627/68154500,
    394502727/2180944000, 2002911/109047200)
DY=(0,1,0,-1/4,-1/4,0,1/10)
X=(X0[0],...,X0[5],X0[6]+H/2)
Y=Y0+(1/100000)*DY
p0=(X,Y).
```

These are PR #1913's exact lawful physical point. Its 30-edge strictly positive coupling `E0` is reproduced by assigning `tau=1/10^7` to every edge, then using the `SB`/ `PIV` invertible submatrix to correct the fifteen SB weights so that `C E0=b0`. Exact checks give `min E0=tau` and all 21 Blackwell equations.

### Stronger exact rational p0 certificate (no transcendence required)

The original *rational* `p0` itself is a 15-edge-necessary physical instance. The four 24-edge flats fail the strict deficit test. For the remaining three 14-edge quotient flats `F4,F5,F6`, the exact rational augmented rank tests give:

```text
flat F4: rank(C_F4)=13, rank([C_F4 | b0])=14
flat F5: rank(C_F5)=12, rank([C_F5 | b0])=13
flat F6: rank(C_F6)=12, rank([C_F6 | b0])=13
```

Hence the rational right-hand side `b0` lies in **none** of these three support spans. Every support with at most 14 edges must belong to some one of the seven enumerated flats. The four 24-edge cases contradict the four exact strict deficits; the other three miss `b0` by a nonzero rank increment. Therefore **no nonnegative coupling with at most 14 positive edges realizes `b0`**, and the 15-column vertex upper bound implies the exact rational physical conclusion:

```text
min_support(b(p0)) = 15.
```

The corresponding exact audit assertions are appended to `VERIFY_PHYSICAL.py`, with the three 15/14 augmented rank checks logged in `EXACT_OUTPUT.txt`. This is a finite rational counterexample to the universal 14-edge claim.



Let `t=e/10^100`, with `e` Euler's number. The known elementary bounds `2<e<3` and its transcendence are used only for a precise algebraic witness. Set

`p(t)=p0+sum_{k=1}^8 t^k n_{a_k}`, `(a1,...,a8)=(0,1,2,4,5,6,7,8)`.

All five physical equalities hold exactly for `p(t)`. Let `B=Jb P`; solve the 15×15 SB submatrix for each of the eight columns of `B` to obtain an exact 30×8 rational correction `Delta E` supported on SB. Then

`E(t)=E0+sum_{k=1}^8 t^k Delta E[:,k]`

satisfies `C E(t)=b(p(t))` exactly.

Executed rational bounds:

```text
min positive physical capacity slack at p0: 7/2000000
forced zero slack indices in 26-vector: (4,15,23), all tangent changes zero
min of the four strict deficits at p0: 654982477/81785400000
min E0: 1/10000000
max row sum of absolute correction coefficients, Delta E: 535/52
max row sum of absolute capacity-slack tangent coefficients: 27
max row sum of absolute deficit tangent coefficients: 17/2
```

Since `0<t<3/10^100<1`, each perturbation is bounded by `t` times the corresponding row sum. Every required transport weight and physical capacity slack remains strictly positive; all four deficits remain strict; the three forced zero slacks remain zero. Thus `p(t)` is a lawful physical Blackwell-feasible pair in the selected model.

Finally let `S` be any support of at most 14 edges. If `S` could realize `p(t)`, its span must meet the four-deficit chamber and, by the seven-flat argument, cannot contain all of `W`. There is therefore a rational linear functional `L_S` vanishing on `span(C_S)` but not identically on `W`. The scalar

`L_S(b(p(t)))=L_S(b0)+sum_{k=1}^8 t^k L_S(Jb n_{a_k})`

is a **nonzero rational-coefficient polynomial evaluated at a transcendental number**. It cannot vanish. Therefore `b(p(t))` has no 14-or-fewer-edge coupling. The universal 15-edge vertex upper bound yields

`min_support(b(p(t)))=15`.

The transcendental expression is an alternative uniform-algebraic witness; the original **rational p0** is already certified above and is the simpler exact counterexample inside the lawful physical g=b family.

## Executed verification, scope and next question

Local checks: exact `Fraction`/SymPy linear algebra of physical equalities, eight-direction rank, the 15-column coupling basis, quotient rows, three exceptional ranks, positive witness envelope; independently an all-integer C++ exhaustive 5-column hyperplane enumeration (142506 candidate subsets). See `EXACT_OUTPUT.txt`, `QUOTIENT_MATRIX.txt`, `VERIFY_PHYSICAL.py`, and `VERIFY_FLATS.cpp`. SymPy is used solely for rational matrix operations; the exhaustive count is performed in integer arithmetic. These are author-side mathematical certificates pending independent audit.

**Result for the mother question:** the universal <=14-edge proposition fails for the frozen lawful physical family, with an **exact rational lawful p0 requiring 15 edges**, plus a relatively open eight-dimensional chamber where minimum support is 15 almost everywhere. The remaining classification question is to describe the lower-dimensional exceptional physical configurations admitting <=14 edges and their precise BRC observer-fiber structure. Formal mathematical admission and independent checker replication remain to be completed.

**Actual control:** Researcher-ID `EM-DIRECT-1D756F / TASK_RESEARCH`, Activity-ID `RA-502640168EFB6EAF60E28451` (native activity registration). The dispatch available to this session points to an X6 task, not an authorized R5 claim. This report is independently published author-side evidence; it does not mutate an active R5 claim, Result, Review, Working Truth or P000.
