# R5: Exact 15-edge necessity for a lawful matched-time g=b Blackwell pair

Date: 2026-11-10 (Asia/Shanghai).
Evidence: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING.
Scientific pins (unchanged): global a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e.
Dependencies: PR #1894 (b4d0594d3f9705dbe403b607741871ec9ff97842), PR #1896 (1ad4649af24cbd5c3a4527ecdd226b721c49aac9), PR #1899 (dd91fa668d0d48ee6926c02e5e44051c7133a1f6).

## Theorem

For the specific physically lawful FULL_HIST source X with g=b and seedless-F target Y with matched stopping-time coordinates of PR #1894, the minimum number of positive entries in any nonnegative Blackwell transport is **exactly 15**. This is an explicit physically lawful counterexample to the proposed uniform-14 upper bound over all admissible matched-time g=b / seedless-F pairs in the frozen seven-likelihood-ratio model. The previously verified universal 15-edge vertex upper bound on the nu_4=0 statistical face remains valid.

The seven indices used here are labelled likelihood-ratio branches, not the six P000 native spatial axes. No native Heartbeat dynamics or physical calibration is asserted.

## Exact input

Set likelihood ratios r=(1/10,1/2,3/4,1,5/4,3/2,19/10), and physical coordinates (g,a,b,u,v,w,z). Define:

X0=(999/1000,1/6,999/1000,1/20,29/240,11/160,1/120)
Y0=(1,2002911/10904720,26095487/40892700,442758619/6542832000,11037627/68154500,394502727/2180944000,2002911/109047200)
H=17774559/17507527960
X=X0+(H/2)*(0,0,0,0,0,0,1)
Y=Y0+(1/100000)*(0,1,0,-1/4,-1/4,0,1/10).

With the exact mass map M, stopping-time map and 13 physical slacks of PR #1894 (all formulas reproduced in VERIFY.py), nu=M(X), mu=M(Y). Direct exact checking yields X lawful with g=b, Y lawful with g=1, z=a/10, mu_1=23/4000000, nu_4=0, sum mu=sum nu=1 and T(X)=T(Y)=(17609/6000,33857/12000).

The complete allowed nonnegative coupling carrier D has 30 edges:
D={(0,0),(6,6)} union {(i,j):0<=i<=6, j in {1,2,3,5}}.

For each edge e=(i,j), its 21-coordinate augmented column A_e has 1 at target row i, 1 at source row 7+j, r_i at moment row 14+j. The required right-hand side h is (mu,nu,(r_j nu_j)_j). A transport E>=0 must solve AE=h.

## Certificate 1: fifteen strictly positive weights

Take ordered support
B=((0,0),(0,1),(2,1),(0,2),(2,2),(4,2),(0,3),(1,3),(3,3),(4,3),(5,3),(4,5),(5,5),(6,5),(6,6)).
The 15x15 submatrix on augmented row indices
I=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
has determinant -299/1600. The exact rational linear solve A[I,B] E_B=h[I] produces 15 strictly positive weights (minimum 23/4000000). VERIFY.py checks *all 21 original equations*. EXACT_OUTPUT.txt prints the 15 exact weights. Hence the minimum is at most 15.

## Certificate 2: ten mandatory positive entries

For each edge e in
F={(0,0),(0,1),(0,2),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6)}
VERIFY.py contains a sparse rational vector y_e in dimension 21 satisfying all 30 exact dual inequalities
  <y_e,A_f> <= 1 if f=e, otherwise <=0
and <y_e,h> >0. For every feasible nonnegative E, summing yields E_e >= <y_e,h> >0, so F is contained in every feasible support. A useful explicit strict bound is
E_(4,3) >= 64190522124239/2296534032000000 > 2mu_1.
All 300 rational dual inequalities and strict values are checked, without numerical tolerances.

## Certificate 3: complete modular exclusion of supports with <=14 edges

If a feasible E had <=14 positive edges, by Certificate 2 its support would contain F and be contained in F∪T for some four-element T from the 20 edges D\F. There are exactly binomial(20,4)=4845 such sets.

Restrict AE=h to the 15 independent coordinates I listed above, and scale moment rows by 20 to obtain an *integer* 15x30 matrix C with every entry of modulus <=38. Use prime p=2^127-1. It satisfies
  p > 14! * 38^14 = 1141244518792022784022839872716800.
Therefore every nonzero determinant of any square submatrix on <=14 columns has absolute value <p (Leibniz bound). Its rational column rank equals its rank modulo p. The rational h denominators are coprime to p, as the code verifies.

The ten forced C-columns are linearly independent modulo p. Eliminate them by exact modular Gaussian elimination. The quotient of the 15-row space by their column span has dimension five. For each of the 20 other edges, project its column to this 5D quotient, and project h as well. For each of the 4845 four-element subsets T, VERIFY.py checks
  rank_Fp([projected(C_T) | projected(h)]) > rank_Fp(projected(C_T)).
The *complete* resulting distribution is:
  (rank columns, rank with h)=(4,5) in 3669 cases,
  (3,4) in 1143 cases,
  (2,3) in 33 cases.
Total: 3669+1143+33=4845. Every possible <=14 support is inconsistent modulo p. Because its rational rank is preserved under this reduction, the system is inconsistent over Q as well: if a rational solution existed, an invertible pivot minor would make a solution with denominators coprime to p, giving a modular solution. This contradicts the checked rank gap. Thus **no** nonnegative <=14-edge transport exists, while Certificate 1 attains 15.

The dual comparison on E_(4,3) alone is *not* used as the full lower-bound proof: a possible fourteenth edge can modify column 3's moment equation. The exhaustive modular certificate correctly covers all such cases.

## Verification, interpretation, next unit

Run the standard-library-only Python 3 program VERIFY.py. It performs all 13 source and target slacks, two stopping times, 21 equalities, exact determinant and positivity, ten full-carrier dual certificates (300 inequalities), exhaustive 4845 reduced supports modulo p, and strict 15-edge conclusion. EXACT_OUTPUT.txt is the actual execution stdout. The finite exhaustive check plus the rank-lifting argument is the mathematical proof; the code does not call MILP, floating-point approximations or any external solver.

The source-side research result is author-verified and awaits independent mathematical review and task admission. This note does not modify P000, frozen scientific pins, Owner/CLAIM, or formally create a Result.

Next: find a positive-width neighborhood of lawful matched-time physical strategy pairs whose transport support minimum remains 15. Analyze the legal physical tangent constraints and strict dual/matroid inequalities. Precisely identify which perturbation directions preserve the forcing certificate, and construct a 15-edge positive basis throughout a rational box or interval.
