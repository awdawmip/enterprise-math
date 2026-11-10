# R5: correction of the 8D scaled tangent bound and Hadamard-certified 15-edge cube

Date: 2026-11-10 Asia/Shanghai. Status: AUTHOR_EXACT_RATIONAL_CHECK / INDEPENDENT_MATH_REVIEW_PENDING.

Frozen scientific input pins unchanged: account `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Specific input/center, 30-edge seven-likelihood-ratio Blackwell carrier, physical mass/time/slack maps, RREF tangent basis `P`, 15-edge support, 10 dual mandatory-positive-edge certificates, and the exhaustive central 4,845-case exclusion are inherited at their exact scopes from PR #1902 and PR #1923. This note is a separate author-side result, not a formal R5 CLAIM or Result.

## Corrected computation and counterexample to a claimed verifier constant

PR #1923 `research_notes/brc_r5_robust_8d_15edge_cube_20261110_t11/VERIFY_8D.py` forms the 21x8 marginal tangent block `B8=Jb*P`; its 15 pivot-row selection is `I=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)`, with moment rows scaled by 20. In the exact same RREF coordinates, let
`T[i,k] = (20 if I[i]>=14 else 1) * B8[I[i],k]`.
The exact maximum absolute row sum is **405/2**, not the script's asserted **457/8**. At pivot row index 13, `I[13]=16`, its eighth derivative component is **-75**, by itself contradicting the old 457/8 maximum. The previously published script's assertion `L==457/8` therefore fails for these stated inputs. Its publication output expressly comes from a different local reproducer and must not be treated as stdout of the published script.

The exact 15 row sums `s_i=sum_k|T[i,k]|` satisfy
```
sum_i s_i^2 = 15396036457529/233280000 < 260^2.
```
The accompanying `CERTIFICATE.py` checks this with only rational arithmetic and checks the updated determinant and physical margins. A separately executed full physical-Jacobian recomposition (Python/SymPy) also verified `rank(B8)=8`, all 21 15-edge basis equations, `det(A[I,SB])=-299/1600`, and the displayed tangent rows.

## Stronger theorem: an explicit 8D cube of radius 10^-40

Let `p(t)=p0+P*t` be the same lawful 14-coordinate physical strategy pair of PR #1923, with the eight RREF tangent columns indexed `(0,1,2,4,5,6,7,8)`. For **every real** `t` such that `|t_k|<=10^-40` for all eight components, `p(t)` satisfies all original physical capacity constraints, `g(X)=b(X)`, `g(Y)=1`, `z(Y)=a(Y)/10`, both matched stopping-time constraints, and the exact seven-node Blackwell system. The minimum number of strictly positive nonnegative transport edges is **exactly 15**.

Proof: Physical nonzero-slack minimum is `7/2000000` with maximum absolute derivative row sum 27; the three zero slacks have identically zero derivatives. A fixed 15-edge coupling has minimum positive base weight `23/4000000` and derivative row-sum bound `535/52`. The 10 full-carrier dual forcing values (PR #1902) have minimum `18052765669/88328232000000` and derivative bound `585227/46800`. All three positive margins dominate their perturbation bounds at `rho=10^-40`; the four strict source deficits also remain positive. Hence feasibility, fixed-basis positivity and ten mandatory edges hold throughout the closed real cube.

At the center, PR #1902 exhaustively excluded every one of `binom(20,4)=4845` potentially 14-edge supports containing the ten forced edges via an exact modular rank test. On its selected 15 integer-scaled pivot rows, each of the 30 candidate matrix columns has at most three nonzero entries `1,1,20*r_i`; since `|20*r_i|<=38`, each column has Euclidean norm strictly less than 39.

For every one of those 4,845 supports S of rank `r<=14`, inherit one central nonzero augmented `(r+1)`-minor involving its right-hand-side column. Every central witness has rational absolute value at least `1/D0`, where `D0=1148267016000000` (PR #1902/#1923). By the row-sum-square identity above, the norm of the scaled RHS perturbation at any point of the box is `<260*rho`. Hadamard's determinant inequality bounds the change of **each** chosen minor by `260*39^r*rho <=260*39^14*rho`. The exact integer comparison is:
```
D0*260*39^14 =
5622387007488071807106526559830560000000 < 10^40.
```
All central nonzero witness minors consequently remain nonzero at **every real point** in this box. Therefore all supports of size <=14 remain impossible, while the strictly positive 15-edge basis exists everywhere. QED.

This strengthens the radius `10^-100` of PR #1923 by a factor `10^60` without repinning the source/model. This is an explicit, conservative sufficient neighborhood, not a maximal-radius assertion.

## Proof status, dependencies and next unit

The new derivative correction, 15x8 exact matrix certificate, positive-margin inequalities and Hadamard bound have been executed with exact rationals; the 4,845-case base-point exhaustive certificate and ten dual vectors are inherited from the immutable evidence in PR #1902. Independent mathematical review and native task admission are pending. The previously retracted seven-rank-five-flats inference still present in legacy verifier comments is not used.

Next: replace the old erroneous numeric assertion at its source, retain a regression for the -75 witness, and optimize support-specific augmented-minor margins to map first adjacent 13/14-edge exceptional strata. Preserve the one-dimensional BRC observer-fiber residual (9 physical parameters vs 8 marginal directions) and do not reclassify the seven LR nodes as native X6 axes.
