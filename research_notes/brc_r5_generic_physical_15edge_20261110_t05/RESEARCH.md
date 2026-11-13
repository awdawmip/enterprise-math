# R5 — Generic 15-edge necessity for lawful 8D physical Blackwell pairs

Date: 2026-11-10 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING. This extends physical 8D lower-bound PR #1913 and statistical 15-edge result PR #1905. Scientific inputs remain frozen at account `a01383f825ef9d43b4b754254303298c64041568` and Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`, as recorded in PR #1913; original physical formulas from PR #1894. Statistical LR carrier is not native P000 X6 space.

## Theorem

In the frozen seven-likelihood-ratio model, there is a nonempty relatively open eight-dimensional set U of lawful matched-stopping-time, `X_g=X_b` FULL_HIST source / seedless-F target pairs with `nu_j > mu_j` for each `j=1,2,3,5`, all Blackwell feasible. **For almost every marginal pair in U, every nonnegative Blackwell realization needs at least 15 positive edges; a 15-edge realization exists.** Consequently the generic minimum on U is exactly 15, and lawful physical instances requiring 15 edges exist. The exceptional ≤14-edge set is contained in finitely many proper affine subspaces of the physical 8D hull. This proof does not identify the precise minimum for the original rational PR #1894 pair.

The 30 allowed edges are `D={(0,0),(6,6)} union {(i,j): i=0..6, j in (1,2,3,5)}`. With `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`, write `C_(i,j)` for the 21-vector containing 1 at row-margin i and source-column margin 7+j, and r_i at conditional-moment 14+j. `E>=0` must have row marginal mu, column marginal nu and `sum_i r_i E_ij=r_j nu_j`. The full C matrix has rational rank 15, hence every feasible normalized pair has a vertex coupling of support ≤15.

## Proof: physical hull and annihilator

The frozen physical family has 14 raw parameters with five independent equations: `X_g=X_b; Y_g=1; Y_z=Y_a/10; T1(X)=T1(Y); T2(X)=T2(Y)`. Its affine statistical margin image has dimension 8 (PR #1913). Let W be the nine-dimensional linear span of the 21-coordinate RHS vectors `(mu,nu,(r_j nu_j)_j)` of the physical family. The exact program independently reconstructs this span and checks `rank(W)=9`, `rank(full C)=15`.

Inside the strict-deficit chamber, any realizing support S contains an off-diagonal edge in every source column j=1,2,3,5; otherwise `mu_j>=nu_j`. Thus the four columnwise martingale defects `H_j(i,k)=(r_i-r_j) 1_(k=j)` are linearly independent on S. The annihilator of W inside the full 15D C-column image has dimension 6. It is spanned by H1,H2,H3,H5 and two additional rational physical invariant functionals:

`A(i,j)=a_i-18`, `a=(36,28,23,18,13,8,0)`;

`B(i,j)=b_i+c_j`, `b=(-36,-36,-31,-18,-5,0,0)`, `c=(36,36,31,18,0,0,0)`.

On normalized margins they express `36mu0+28mu1+23mu2+18mu3+13mu4+8mu5=18` and `-36mu0-36mu1-31mu2-18mu3-5mu4+36nu0+36nu1+31nu2+18nu3=0`. Their augmented edge-evaluation rank with the H_j is exactly six.

Suppose a feasible support S with |S|≤14 spans W. Since the full transport column space has rank 15, there exists a nonzero annihilating linear functional on that space vanishing on S and W. It must have the form `L=lambda A + mu B + sum_j t_j H_j`, with `(lambda,mu)!=(0,0)` because the four H_j are independent on every feasible S.

For each internal source column j and target index i≠j, L(i,j)=0 forces

`t_j= -(lambda*(a_i-18)+mu*(b_i+c_j))/(r_i-r_j)`.

The diagonal (j,j) vanishes only when its numerator is zero. Endpoint edges (0,0), (6,6) vanish only when `lambda A+mu B=0`. For a fixed projective ratio (lambda:mu), the four t_j can be optimized independently to maximize the total zero edges. As (lambda:mu) varies, the count changes only at pairwise slope coincidences in a single column, diagonal-zero equations, or endpoint-zero equations. Pairwise coincidences are exactly

`lambda*((a_i-18)*(r_k-r_j)-(a_k-18)*(r_i-r_j)) + mu*((b_i+c_j)*(r_k-r_j)-(b_k+c_j)*(r_i-r_j))=0`.

These provide a finite **exhaustive**, not sampled, rational projective check. Exact enumeration produces 20 exceptional projective ratios. Every nonexceptional ratio admits at most 6 zero edges. Among all exceptional ratios, only (lambda:mu)=(0:1) admits 14 zeros; the next best has 12. The three maximal 14-zero sets all include endpoints (0,0),(6,6), and the target-row triples in source columns 1,2,5 respectively {1,3,5}, {2,3,4}, {1,3,5}. Column 3 has exactly three alternative triples: {0,3,6}, {1,3,5}, {2,3,4}. The corresponding exact transport-column ranks are **13, 12, 12**. Adjoining the physical span W raises each rank to **14**. Therefore W is in the span of none of these sets, and hence in no realizing support of ≤14 edges.

Consequently for every S with ≤14 edges, `span(C_S) intersect W_aff` is a proper affine subspace of the physical 8D hull. A finite union of proper affine subspaces has measure zero there. The exact frozen rational physical basepoint has all nonmandatory capacity slacks positive, four strict deficits, and a 30-edge strictly positive rational coupling with smallest edge weight `1/10^7`. A linear right-inverse to the full rank-15 transport map and openness of physical capacities ensure a nonempty 8D relatively open feasible chamber U. For almost every point of U, support ≥15; the vertex bound proves support ≤15. This also implies **existence** of rational legal physical 15-needed pairs, since the excluded proper affine subspaces are rational and rational points of U are dense.

## Reproduction and frontier

`VERIFY.py` is a standard-library `fractions.Fraction` checker. It independently reconstructs the physical mass and matched-time equations and rank-9 RHS span, checks physical capacity slacks, four strict deficits, builds a strictly positive 30-edge exact coupling solving all 21 Blackwell equations, ranks 30 columns and six functionals, generates all 20 exceptional projective ratios, maximizes their zero-column counts, and ranks the three 14-zero sets relative to W. `EXACT_OUTPUT.txt` is actual executed output. Its finite certificates and the argument above establish the infinite generic result. Mathematical admission remains pending independent review.

Next discriminating question: select an **explicit small-denominator rational lawful physical pair** and produce a finite exact certificate excluding every ≤14-edge support. The original PR #1894 rational point remains a promising but not yet exact-certified candidate. Secondary direction: classify transitions between the 15-edge charts across lower-support exceptional strata.

Native research activity for this turn: Researcher-ID `EM-DIRECT-3EFF3E`, Activity-ID `RA-8078A08F5DE9D1D2A5C11545`. No formal R5 Owner/CLAIM, native scientific checkpoint, independent review or mathematical admission asserted.
