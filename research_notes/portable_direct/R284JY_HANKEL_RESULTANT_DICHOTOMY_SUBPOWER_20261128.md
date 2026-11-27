# R284JY — Hankel–resultant dichotomy and subpower sparsity of integer budgets

2026-11-28. Author proof; NOT_REVIEWED. Own recovered metadata EM-DIRECT-0C386E / TASK_RESEARCH, MCP-8cd6c4fa26b9459d923ff73ba0082220, Activity RA-B82240E8488EF5A1DA5186C4. Recovery r1-20261128-0256-own-recovery returned own registration and no own RUN; it grants no execution authority. Current owner inventory r1-20261128-0256-leased was RUNNING at last read before this write; no new claim or shared Task mutation. Independent continuation of own portable research. External auxiliary arithmetic observer, not native spatial attribution.

Current account normative snapshot b21e854cbabe95f89fc35d0fdd5ef4c2038645de (canonical entries matched immutable blob metadata), P000 V4/V5, ACTIVE worldview, TASK/informed entry, portable/continuation, joint and residual contracts consumed. Frozen scientific input: 3144172dd7a914ff9ea11e79c54ef3e653e7c9f6:research_notes/portable_direct/R284JX_HANKEL_DETERMINANTS_AND_POWER_SAVING_20261128.md (full text, blob 2047c300ef0a4e7391d27f6dd09ad77857bda9f0). Reuse JX's all-fixed-order expansion, c1 != 0 (certified positive there), integer determinant theorem and shrinking-target theorem, and inherited eventual unique legal real root of complete C. No change to scientific pins, no independent re-review of JX/JV coefficients or JS uniqueness.

## 1. Main theorem

Let a real sequence y_d on all sufficiently large positive integers have, for every fixed M>=1,
  y_d=P_2(d)+sum_{k=1}^M c_k d^(-k)+O_M(d^(-M-1)),
where P_2 is a fixed real polynomial of degree at most 2 and c1 != 0. Define
  E(X)=#{d<=X:y_d is an integer},
  E_A(X)=#{d<=X:dist(y_d,Z)<=d^(-A)}.
Then for every epsilon>0,
  E(X)=O_epsilon(X^epsilon).
More strongly, for every epsilon>0 there is a finite A>0 such that
  E_A(X)=O_epsilon(X^epsilon),
where the implied constants may depend on the fixed sequence and chosen A. In the finite Hankel case below a single A works for every epsilon. No assumption of irrationality, transcendence, infinite Hankel nonvanishing or actual analyticity in 1/d is needed. This is a theorem about asymptotic expansions along integer arguments, not a claim of rationality of the actual sequence.

The proof uses both possible outcomes of the joint Hankel observer. If nonzero principal minors have unbounded order, use JX directly. Otherwise the full reciprocal sequence has an exact finite recurrence, and its information is retained as a polynomial denominator relation. Integer-valued or extremely near-integer observations force exact integer interpolation relations, whose nonconstant denominators divide a nonzero integer resultant.

## 2. Finite principal Hankel nonvanishing implies a full recurrence

Set H_m=det(c_{i+j-1})_{1<=i,j<=m}. Since H_1=c1 !=0, if the set of nonzero principal minors is bounded, it has a largest index r>=1. Solve uniquely for a_0,...,a_{r-1} in
  e_i := c_{i+r}+sum_{j=0}^{r-1} a_j c_{i+j}=0, 1<=i<=r,
using H_r !=0.

Suppose an e_i is nonzero, and let r+t be its first nonzero index (t>=1). In H_{r+t}, simultaneously replace each column r+u (1<=u<=t) by its ORIGINAL column plus sum_{j=0}^{r-1} a_j times ORIGINAL column u+j. This triangular change has determinant 1. The new entries in column r+u are e_{i+u-1}. The top r rows in these t columns vanish. The bottom t by t block has entries e_{r+v+u-1}, zero when v+u<=t and equal to e_{r+t} on its anti-diagonal v+u=t+1. Consequently
  H_{r+t}=H_r (-1)^(t(t-1)/2) e_{r+t}^t !=0,
contradicting maximality. Thus e_i=0 for every i>=1.

Let G(z)=sum_{k>=1} c_k z^k be a formal power series. Multiplying by
  b(z)=1+a_{r-1}z+...+a_0 z^r
annihilates every coefficient of degree >=r+1, so b(z)G(z)=g(z), with deg g<=r. In the integer coordinate d put
  B0(d)=d^r b(1/d), A0(d)=B0(d)P_2(d)+d^r g(1/d).
Then B0 is monic of degree r, A0 has degree <=r+2, and for every fixed N
  B0(d)y_d-A0(d)=O_N(d^(-N)).
This conclusion follows from the all-order asymptotic expansion by taking sufficiently many terms, not from convergence of G or equality of y_d to a rational function. The reciprocal coefficient c1 !=0 is retained.

## 3. Unbounded Hankel case

If H_m !=0 for arbitrarily large m, the frozen JX determinant theorem gives E(X)=O_m(X^(1/(2m+1))). For any epsilon>0 choose one such fixed m with 1/(2m+1)<=epsilon. JX's shrinking-target theorem also gives E_A(X)=O_m(X^(1/(2m+1))) for A>=4m. This proves the assertions in this branch without asserting which branch the R284 sequence belongs to.

## 4. Finite Hankel case: exact dyadic interpolation from asymptotic relations

Fix r from section 2 and set n=2r+4, k=r+3. Work on [D,2D], D a sufficiently large integer. Choose a fixed real A satisfying
  A>max(r+(r+2)(n-1),r+4).
For each d in the shrinking target set choose a nearest integer z_d, so |z_d-y_d|<=d^(-A). For exact integer observations take z_d=y_d. All |z_d|=O(D^2).

Use the full n-column integer observer
  (1,d,...,d^(r+2), z_d,d z_d,...,d^r z_d).
For any n different target arguments, form its square integer matrix. Replace its last column by the linear combination B0(d) z_d-A0(d) of the original columns. This preserves the determinant because B0 is monic of degree r. Its new last column is O(D^(r-A)) uniformly: apply the arbitrary-order residual bound in section 2 with N>A. All other entries are O(D^(r+2)). Expansion along the new last column gives
  |det|=O(D^[r-A+(r+2)(n-1)])=o(1).
Since the original determinant is integral, it is exactly zero for every n-tuple, uniformly. Thus the matrix of ALL targets in the dyadic interval has rank t<n (if fewer than n points, their count is already bounded).

Choose t independent rows and t pivot columns, and one nonpivot column. By Cramer's rule, setting that free coordinate to the nonzero pivot determinant and solving the t pivot coordinates by signed minors gives a nonzero integer null vector for every row; other free coordinates are zero. Its entries are O(D^[(r+2)t]). This yields polynomials A_D,B_D in Z[x], degrees <=r+2,r, polynomial height in D, with
  B_D(d) z_d=A_D(d)
for every target d in [D,2D]. If at least n points exist, B_D cannot be zero: otherwise the nonzero A_D has too many roots. This is a newly constructed dyadic exact relation; its coefficients need not approximate or equal A0,B0. In particular no unproved arithmetic property of the real formal coefficients is needed.

## 5. A nonzero reciprocal tail excludes polynomial degeneration

For any k+1 distinct integer nodes in [D,2D], let [d_0,...,d_k] denote the ordinary divided difference of order k=r+3. P_2 has zero divided difference of this order. The exact divided difference of 1/x is (-1)^k/prod_i d_i, by the standard recursive formula (induction). For each fixed j>=2, the order-k divided difference of x^(-j) is O(D^(-j-k)) by the derivative mean-value formula. Expand y_d to M>=k+1. The discrete remainder's divided difference is O(D^(-M-1)) because the explicit sum has k+1 terms and every product of distinct integer differences has absolute value >=1. The rounded perturbation contributes O(D^-A). Since A>k+1, uniformly
  [d_0,...,d_k] z = (-1)^k c1/prod_i d_i + o(D^(-k-1)).
The leading term has magnitude >=|c1|(2D)^(-k-1); thus this divided difference never vanishes for sufficiently large D. Therefore z_d cannot coincide with ANY real polynomial of degree <=r+2 at r+4 target arguments, regardless of the polynomial's height.

Cancel the primitive polynomial gcd of A_D,B_D over Q[x] to obtain integer polynomials A',B' coprime over Q, using Gauss's lemma (if A_D=0 the relation is the zero polynomial on nonzero denominator nodes, covered by the same nonfit argument). The original B_D has at most r integer zeros. At least n-r=r+4 targets remain if there were n or more. If B' is constant, A'/B' is a polynomial of degree <=r+2 agreeing with all these remaining z_d, contradicting the divided-difference result. Thus B' has degree at least 1; A' is nonzero. This step uses c1 !=0 even in the finite-rank branch.

The reduced polynomials still have height polynomial in D. Indeed primitive common factors divide the original integer polynomials in Z[x]. Each quotient has leading coefficient bounded by the original height and its complex roots belong to the original polynomial; the elementary Cauchy root bound bounds those roots by 1+original height. With fixed degree, elementary symmetric coefficient formulas give polynomial height for the quotient. No effectiveness or denominator bound on the formal real recurrence was used.

## 6. Resultant and divisor count

The integer R_D=Res(A',B') is nonzero by coprimality over Q. Its Sylvester determinant has fixed size and polynomial-height entries, so 1<=|R_D|=O(D^K) for a fixed K depending on r and the height bounds. The Sylvester adjugate (or integer Bezout resultant identity) gives integer polynomials U,V with U A'+V B'=R_D. Thus at every target with B_D(d)!=0, B'(d) is a nonzero integer divisor of R_D: the interpolation equation gives A'(d)=z_d B'(d). For each signed divisor v, the equation B'(d)=v has at most deg B'<=r integer roots. Hence the number of targets in the block is at most
  r+2r tau(|R_D|).
For every eta>0, tau(N)=O_eta(N^eta): for sufficiently large primes p use e+1<=2^e<=p^(eta e), and for the finite small primes absorb max_{e>=0}(e+1)/p^(eta e) into a constant. Choosing eta small enough in terms of K and epsilon proves O_epsilon(D^epsilon). Dyadic summation is geometric for epsilon>0, with finitely many initial arguments absorbed. This proves the main theorem also in the finite-Hankel case, and the fixed A of section 4 works for every epsilon in this branch.

## 7. R284 consequences and verification scope

Apply the theorem to y_d=q_d, the eventually unique legal real root of the complete frozen C(q,d), using JX's arbitrary fixed-order expansion and c1 approx 10.255919898762528 >0. We obtain, with no remaining Hankel nonvanishing hypothesis,
  for every epsilon>0,
  #{d<=X: there exists a legal integer q with C(q,d)=0}=O_epsilon(X^epsilon).
In particular the same count bound holds for the target equality q K(q,d)=32/3, by the frozen necessary cross-residual equation. Moreover for every epsilon>0 there exists A with E_A(X)=O_epsilon(X^epsilon); the frozen global minimum residual-distance comparison transfers this to g_d<=d^(-A-1), absorbing a fixed multiplicative constant for sufficiently large d.

This is a proof by exhaustive structural dichotomy, not a computation of further H_m or an assertion that R284's formal residual series is rational. The load-bearing nonzero c1 and all-order expansion are from frozen JX/JW/JV; their inherited evidence status is unchanged. The proof in sections 2–6 is self-contained except for elementary determinant/divided-difference/resultant facts proved or identified there and the frozen JX theorem used in the unbounded branch. No new numerical or code execution is needed or claimed. Neither effective onset nor effective A(epsilon) is obtained without further information on the actual branch, recurrence or Hankel nonvanishing. The result does not prove finitely many exceptions or exclude each individual integer root. NOT_REVIEWED.

## 8. Next question

The conditional target from JX is now discharged without deciding infinitely many nonzero Hankel minors. Prioritize an effective finite candidate filter and a pointwise obstruction, using exact integer polynomial C and the existing p-adic certification windows; study whether the all-order expansion admits quantitative remainder bounds or whether the recurrence branch itself can be excluded. Retain the exact resultant and denominator coordinates if the finite-rank branch can be identified; they are integer witnesses, not a factor-only projection. No shared Task/Result/Review authority asserted.
